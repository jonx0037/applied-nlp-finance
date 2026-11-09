"""Generate ``manuscript/references_master_index.md`` from ``references.bib``.

The index gives the author a per-chapter scan view of the bibliography
(complementing the flat-alphabetical biber-native ``.bib`` file). It cross-references
which chapters cite which entry, and surfaces verification status from the
``research.md`` files.

CLI: ``uv run python -m tools.build_master_index``
"""

from __future__ import annotations

import argparse
import logging
import re
import sys
from collections import defaultdict
from pathlib import Path

import bibtexparser

logger = logging.getLogger("build_master_index")

REPO_ROOT = Path(__file__).resolve().parent.parent
BIB_PATH = REPO_ROOT / "manuscript" / "99_bibliography" / "references.bib"
INDEX_PATH = REPO_ROOT / "manuscript" / "references_master_index.md"
MANUSCRIPT_DIR = REPO_ROOT / "manuscript"

CHAPTER_TITLES: dict[str, str] = {
    "ch00": "Preface",
    "ch01": "Why Text Moves Markets",
    "ch02": "Text Data Acquisition",
    "ch03": "NLP Foundations for Finance",
    "ch04": "Transformers, LLMs, and Financial Language Models",
    "ch05": "Sentiment Analysis and Signal Construction",
    "ch06": "Earnings Calls and Corporate Disclosure",
    "ch07": "Central Bank Language and Macro Signals",
    "ch08": "Social Media and Alternative Data",
    "ch09": "Entity Extraction and Financial Knowledge Graphs",
    "ch10": "Market Regime Detection",
    "ch11": "Backtesting and Evaluation",
    "ch12": "Deployment and Production Systems",
    "ch13": "Risk, Ethics, and the Limits of Financial NLP",
}


def _read_entries() -> list[dict]:
    """Load all entries (including @online which bibtexparser v1 drops)."""
    text = BIB_PATH.read_text(encoding="utf-8")
    # Pre-pass: rewrite @online to @misc with a marker, so bibtexparser keeps them.
    rewritten = re.sub(r"^@online\{", "@misc{__ONLINE__", text, flags=re.MULTILINE)
    db = bibtexparser.loads(rewritten)
    for e in db.entries:
        if e["ID"].startswith("__ONLINE__"):
            e["ENTRYTYPE"] = "online"
            e["ID"] = e["ID"][len("__ONLINE__") :]
    return db.entries


def _verification_status_index() -> dict[tuple[str, int], bool]:
    """Build an index of (first_surname, year) -> verified-flag from research.md files.

    This is used to surface verification status in the master index. Best-effort —
    if the parser's fingerprint differs from this lookup's key, we just mark
    "Unverified" (a safe default).
    """
    status: dict[tuple[str, int], bool] = {}
    for md_path in sorted(MANUSCRIPT_DIR.glob("[0-9][0-9]_*/research.md")):
        text = md_path.read_text(encoding="utf-8")
        # Walk entry chunks (between --- separators)
        for chunk in text.split("\n---\n"):
            bold_match = re.search(r"\*\*([^*]+?\.\s*\d{4}.*?)\*\*", chunk, re.DOTALL)
            if not bold_match:
                continue
            verified = bool(
                re.search(r"^\s*-\s*Status:\s*`?\[x\]\s*Verified", chunk, re.MULTILINE | re.IGNORECASE)
            )
            # Crude key: first word of bold (likely surname) + last 4-digit year
            body = bold_match.group(1)
            surname = re.match(r"([A-Za-z\-]+)", body)
            year_match = re.search(r"\b(19\d{2}|20\d{2}|21\d{2})\b", body[-200:])
            if surname and year_match:
                key = (surname.group(1).lower(), int(year_match.group(1)))
                status[key] = status.get(key, False) or verified
    return status


def _format_short_citation(entry: dict) -> str:
    """A one-line short form for the by-chapter listing."""
    author_field = entry.get("author", "")
    # First author surname + "et al." if more than 2
    parts = author_field.split(" and ")
    first_surname = parts[0].split(",", 1)[0].strip()
    if len(parts) == 1:
        author_short = first_surname
    elif len(parts) == 2:
        second_surname = parts[1].split(",", 1)[0].strip() if "," in parts[1] else parts[1].split()[-1]
        author_short = f"{first_surname} & {second_surname}"
    else:
        author_short = f"{first_surname} et al."

    title = entry.get("title", "").strip()
    if len(title) > 80:
        title = title[:77] + "..."

    venue_field = (
        entry.get("journaltitle")
        or entry.get("booktitle")
        or entry.get("publisher")
        or entry.get("howpublished")
        or ""
    )
    venue = venue_field.strip()
    if venue and len(venue) > 50:
        venue = venue[:47] + "..."

    year = entry.get("year", "?")
    return f"{author_short} ({year}) — *{title}*" + (f" — {venue}" if venue else "")


def _format_full_entry(entry: dict, verified: bool) -> str:
    """Full markdown block for the by-key listing."""
    key = entry["ID"]
    etype = entry["ENTRYTYPE"]
    parts = [f"### `{key}`", "", f"**Type:** `@{etype}`", ""]

    author_field = entry.get("author", "")
    if author_field:
        # Author list is biblatex-style; re-flow for readability
        names = [a.strip() for a in author_field.split(" and ")]
        parts.append(f"**Authors:** {', '.join(names)}")
    parts.append(f"**Title:** {entry.get('title', '?')}")
    parts.append(f"**Year:** {entry.get('year', '?')}")

    for field_name, label in [
        ("journaltitle", "Journal"),
        ("booktitle", "Book/Proceedings"),
        ("publisher", "Publisher"),
        ("institution", "Institution"),
        ("school", "School"),
        ("howpublished", "Published as"),
    ]:
        value = entry.get(field_name)
        if value:
            parts.append(f"**{label}:** {value}")
            break  # Only one venue field per entry

    vol = entry.get("volume")
    num = entry.get("number")
    pages = entry.get("pages")
    if vol or pages:
        bits = []
        if vol:
            bits.append(f"vol. {vol}")
        if num:
            bits.append(f"no. {num}")
        if pages:
            bits.append(f"pp. {pages}")
        parts.append(f"**Citation detail:** {', '.join(bits)}")

    if entry.get("doi"):
        parts.append(f"**DOI:** [{entry['doi']}](https://doi.org/{entry['doi']})")
    if entry.get("url"):
        parts.append(f"**URL:** {entry['url']}")
    if entry.get("isbn"):
        parts.append(f"**ISBN:** {entry['isbn']}")

    chapters = entry.get("keywords", "").split(",")
    chapters = [c.strip() for c in chapters if c.strip()]
    if chapters:
        parts.append(f"**Cited in:** {', '.join(chapters)}")
    parts.append(f"**Verification:** {'✓ Verified via SMU Library' if verified else 'Unverified'}")
    parts.append("")
    return "\n".join(parts)


def build_index() -> int:
    """Generate the index Markdown file. Returns the entry count."""
    entries = _read_entries()
    if not entries:
        logger.error("No entries loaded from %s", BIB_PATH)
        return 0

    # Surface verification status (best-effort)
    status_idx = _verification_status_index()

    def _is_verified(entry: dict) -> bool:
        author_field = entry.get("author", "")
        surname = author_field.split(",", 1)[0].strip().lower() if "," in author_field else ""
        try:
            year = int(entry.get("year", 0))
        except (ValueError, TypeError):
            year = 0
        return status_idx.get((surname, year), False)

    # Group entries by chapter
    by_chapter: dict[str, list[dict]] = defaultdict(list)
    for entry in entries:
        chapters = [c.strip() for c in entry.get("keywords", "").split(",") if c.strip()]
        for ch in chapters:
            by_chapter[ch].append(entry)
        if not chapters:
            by_chapter["unassigned"].append(entry)

    # Build markdown
    output: list[str] = []
    output.append("# References Master Index")
    output.append("")
    output.append("Generated from [references.bib](99_bibliography/references.bib) by")
    output.append("`tools/build_master_index.py`. Do not hand-edit — regenerate from the source.")
    output.append("")

    # Summary
    type_counts: dict[str, int] = defaultdict(int)
    for e in entries:
        type_counts[e["ENTRYTYPE"]] += 1
    verified_count = sum(1 for e in entries if _is_verified(e))
    output.append(f"**Total entries:** {len(entries)}  ")
    output.append(f"**Verified via SMU Library:** {verified_count} ({verified_count * 100 // len(entries)}%)")
    output.append("")
    output.append("**Entry types:** " + ", ".join(
        f"`@{t}` ({c})" for t, c in sorted(type_counts.items(), key=lambda x: -x[1])
    ))
    output.append("")

    # By-chapter section
    output.append("## By Chapter")
    output.append("")
    for ch in sorted(by_chapter.keys()):
        if ch == "unassigned":
            continue
        ch_title = CHAPTER_TITLES.get(ch, ch)
        ch_num = ch.replace("ch", "Chapter ").lstrip("0") or "Preface"
        output.append(f"### {ch_num} — {ch_title}")
        output.append("")
        entries_for_chapter = sorted(by_chapter[ch], key=lambda e: e["ID"])
        for e in entries_for_chapter:
            verified_mark = "✓" if _is_verified(e) else " "
            output.append(f"- `[{verified_mark}]` `{e['ID']}` — {_format_short_citation(e)}")
        output.append("")

    if "unassigned" in by_chapter:
        output.append("### Unassigned (no chapter affiliation)")
        output.append("")
        for e in sorted(by_chapter["unassigned"], key=lambda x: x["ID"]):
            output.append(f"- `{e['ID']}` — {_format_short_citation(e)}")
        output.append("")

    # By-key section
    output.append("## By Citation Key (alphabetical)")
    output.append("")
    for entry in sorted(entries, key=lambda x: x["ID"]):
        output.append(_format_full_entry(entry, _is_verified(entry)))

    INDEX_PATH.write_text("\n".join(output), encoding="utf-8")
    return len(entries)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )

    count = build_index()
    print(f"Wrote {count} entries to {INDEX_PATH.relative_to(REPO_ROOT)}")
    return 0 if count > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
