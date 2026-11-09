"""Cross-check ``references.bib`` DOIs against CrossRef.

For every entry that has a DOI, hit ``https://api.crossref.org/works/{doi}`` and
fuzzy-match the returned ``title`` / first ``author surname`` / ``year`` against
the bib entry. Writes a triage report to ``tools/verification_report.txt``.

This is **automated cross-checking, not verification** — it catches typos and
wrong DOIs but doesn't substitute for reading the paper at SMU Library.

Polite client: 1.5 req/s, exponential backoff on 5xx, 30 s total per request.

CLI:
    ``--tier 1``        Restrict to entries whose key matches the Tier 1 list.
    ``--key KEY``       Verify a single entry by citation key.
    ``--all``           (default) Check all entries with DOIs.
"""

from __future__ import annotations

import argparse
import logging
import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

import bibtexparser
import httpx
from rapidfuzz import fuzz

logger = logging.getLogger("verify_doi")

REPO_ROOT = Path(__file__).resolve().parent.parent
BIB_PATH = REPO_ROOT / "manuscript" / "99_bibliography" / "references.bib"
REPORT_PATH = REPO_ROOT / "tools" / "verification_report.txt"

CROSSREF_BASE = "https://api.crossref.org/works"
USER_AGENT = "applied-nlp-finance/0.1 (mailto:jonx0037@gmail.com)"  # polite header per CrossRef etiquette
REQUEST_DELAY = 0.7  # ~1.5 req/s
FUZZ_TITLE_THRESHOLD = 88


@dataclass
class VerificationResult:
    key: str
    doi: str
    status: str  # "ok", "mismatch", "not_found", "error"
    bib_title: str = ""
    crossref_title: str = ""
    title_score: float = 0.0
    bib_first_author: str = ""
    crossref_first_author: str = ""
    bib_year: int | None = None
    crossref_year: int | None = None
    note: str = ""


def _normalize_for_match(s: str) -> str:
    """Lowercase, strip accents, collapse whitespace, drop punctuation."""
    import unicodedata
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    s = re.sub(r"[^a-z0-9 ]", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def _first_author_surname(author_field: str) -> str:
    """Extract first author's surname from ``Last, First and ...``."""
    if not author_field:
        return ""
    first = author_field.split(" and ")[0]
    surname = first.split(",", 1)[0].strip() if "," in first else first.split()[-1]
    return _normalize_for_match(surname).strip("{}")


def _read_entries() -> list[dict]:
    """Read references.bib including @online entries (workaround for bibtexparser v1)."""
    text = BIB_PATH.read_text(encoding="utf-8")
    rewritten = re.sub(r"^@online\{", "@misc{__ONLINE__", text, flags=re.MULTILINE)
    db = bibtexparser.loads(rewritten)
    return db.entries


def _fetch_crossref(client: httpx.Client, doi: str) -> dict | None:
    """Fetch a CrossRef work record by DOI. Returns None on 404."""
    url = f"{CROSSREF_BASE}/{doi}"
    for attempt in range(4):
        try:
            resp = client.get(url, timeout=30.0)
        except (httpx.RequestError, httpx.TimeoutException) as e:
            logger.warning("Request error for %s: %s; retrying...", doi, e)
            time.sleep(1.5 ** attempt)
            continue
        if resp.status_code == 404:
            return None
        if resp.status_code >= 500:
            logger.warning("Server error %s for %s; retrying...", resp.status_code, doi)
            time.sleep(1.5 ** attempt)
            continue
        if resp.status_code == 200:
            return resp.json().get("message")
        logger.warning("Unexpected status %s for %s", resp.status_code, doi)
        return None
    return None


def _verify_entry(client: httpx.Client, entry: dict) -> VerificationResult:
    """Cross-check a single entry against CrossRef."""
    key = entry["ID"]
    doi = entry.get("doi", "").strip()
    bib_title = entry.get("title", "").strip()
    bib_first_author = _first_author_surname(entry.get("author", ""))
    try:
        bib_year = int(entry.get("year", 0))
    except (ValueError, TypeError):
        bib_year = None

    result = VerificationResult(
        key=key,
        doi=doi,
        status="error",
        bib_title=bib_title,
        bib_first_author=bib_first_author,
        bib_year=bib_year,
    )

    if not doi:
        result.status = "no_doi"
        return result

    msg = _fetch_crossref(client, doi)
    if msg is None:
        result.status = "not_found"
        result.note = "DOI returned 404 or unresolvable"
        return result

    cr_titles = msg.get("title", [])
    cr_title = cr_titles[0] if cr_titles else ""
    cr_authors = msg.get("author", [])
    cr_first_surname = (
        _normalize_for_match(cr_authors[0].get("family", ""))
        if cr_authors
        else ""
    )

    issued = msg.get("issued", {}).get("date-parts", [[]])
    cr_year = issued[0][0] if issued and issued[0] else None

    result.crossref_title = cr_title
    result.crossref_first_author = cr_first_surname
    result.crossref_year = cr_year

    # Fuzzy title match
    bib_norm = _normalize_for_match(bib_title)
    cr_norm = _normalize_for_match(cr_title)
    title_score = fuzz.token_set_ratio(bib_norm, cr_norm) if cr_norm else 0
    result.title_score = title_score

    mismatches = []
    if title_score < FUZZ_TITLE_THRESHOLD:
        mismatches.append(f"title score {title_score:.0f} < {FUZZ_TITLE_THRESHOLD}")
    if cr_first_surname and bib_first_author and cr_first_surname != bib_first_author:
        mismatches.append(f"author: {bib_first_author!r} vs {cr_first_surname!r}")
    if cr_year and bib_year and cr_year != bib_year:
        mismatches.append(f"year: {bib_year} vs {cr_year}")

    if mismatches:
        result.status = "mismatch"
        result.note = "; ".join(mismatches)
    else:
        result.status = "ok"

    return result


def verify_all(entries: list[dict], filter_keys: set[str] | None = None) -> list[VerificationResult]:
    """Run verification across the given entries."""
    results: list[VerificationResult] = []
    headers = {"User-Agent": USER_AGENT}

    with httpx.Client(headers=headers) as client:
        for entry in entries:
            if filter_keys is not None and entry["ID"] not in filter_keys:
                continue
            doi = entry.get("doi", "").strip()
            if not doi:
                continue
            try:
                r = _verify_entry(client, entry)
            except Exception as e:
                r = VerificationResult(
                    key=entry["ID"],
                    doi=doi,
                    status="error",
                    note=f"exception: {e}",
                )
            results.append(r)
            logger.info("[%s] %s — %s", r.status, r.key, r.note or "")
            time.sleep(REQUEST_DELAY)

    return results


def write_report(results: list[VerificationResult], path: Path) -> None:
    """Emit a human-readable triage report."""
    lines: list[str] = []
    lines.append("CrossRef DOI Verification Report")
    lines.append("=" * 50)
    lines.append("")

    status_counts: dict[str, int] = {}
    for r in results:
        status_counts[r.status] = status_counts.get(r.status, 0) + 1
    lines.append(f"Total entries checked: {len(results)}")
    for status, count in sorted(status_counts.items()):
        lines.append(f"  {status}: {count}")
    lines.append("")

    # Mismatches first (most important)
    mismatches = [r for r in results if r.status == "mismatch"]
    not_found = [r for r in results if r.status == "not_found"]
    errors = [r for r in results if r.status == "error"]
    ok = [r for r in results if r.status == "ok"]

    if mismatches:
        lines.append("=" * 50)
        lines.append("MISMATCHES (review and fix in research.md)")
        lines.append("=" * 50)
        lines.append("")
        for r in mismatches:
            lines.append(f"[MISMATCH] {r.key}")
            lines.append(f"  DOI:           {r.doi}")
            lines.append(f"  Note:          {r.note}")
            lines.append(f"  bib title:     {r.bib_title}")
            lines.append(f"  CrossRef:      {r.crossref_title}")
            lines.append(f"  Title score:   {r.title_score:.0f}")
            if r.bib_year != r.crossref_year:
                lines.append(f"  bib year:      {r.bib_year}  CrossRef: {r.crossref_year}")
            if r.bib_first_author != r.crossref_first_author:
                lines.append(f"  bib author:    {r.bib_first_author}  CrossRef: {r.crossref_first_author}")
            lines.append("")

    if not_found:
        lines.append("=" * 50)
        lines.append("NOT FOUND (DOI did not resolve)")
        lines.append("=" * 50)
        lines.append("")
        for r in not_found:
            lines.append(f"[404] {r.key}  DOI: {r.doi}")
        lines.append("")

    if errors:
        lines.append("=" * 50)
        lines.append("ERRORS (network or unexpected)")
        lines.append("=" * 50)
        lines.append("")
        for r in errors:
            lines.append(f"[ERR] {r.key}  DOI: {r.doi}  Note: {r.note}")
        lines.append("")

    lines.append("=" * 50)
    lines.append(f"OK ({len(ok)} entries with matching CrossRef records)")
    lines.append("=" * 50)
    for r in sorted(ok, key=lambda r: r.key):
        lines.append(f"  ✓ {r.key}")

    path.write_text("\n".join(lines), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--all", action="store_true", help="Check all entries (default).")
    parser.add_argument("--tier", type=int, choices=[1], help="Restrict to Tier N.")
    parser.add_argument("--key", help="Verify a single citation key.")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )

    entries = _read_entries()
    if not entries:
        print("No entries loaded.", file=sys.stderr)
        return 2

    filter_keys: set[str] | None = None
    if args.key:
        filter_keys = {args.key}
    # Tier filtering is a placeholder; the Tier 1 list lives in
    # tools/tier1_keys.txt once `identify_tier1.py` (next step) produces it.

    results = verify_all(entries, filter_keys)
    write_report(results, REPORT_PATH)

    n_mismatch = sum(1 for r in results if r.status == "mismatch")
    n_not_found = sum(1 for r in results if r.status == "not_found")
    print(f"Verified {len(results)} entries. {n_mismatch} mismatches, {n_not_found} not found.")
    print(f"Report: {REPORT_PATH.relative_to(REPO_ROOT)}")

    return 0 if n_mismatch == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
