"""Identify and print the Tier-1 verification worklist for SMU Library.

Tier 1 criteria (per research_review.md §7.1):
  * Papers in top-five economics journals (JF, JFE, RFS, AER, QJE, Econometrica).
  * Foundational NLP papers (BERT, Transformer, RAG, Word2Vec, GloVe, BPE, FinBERT).
  * Plus Tversky-Kahneman 1981 (Science, framing effects — foundational behavioral).

Produces ``tools/tier1_worklist.md`` — the human-facing checklist for SMU Library.
"""

from __future__ import annotations

import argparse
import logging
import re
import sys
from pathlib import Path

import bibtexparser

logger = logging.getLogger("tier1_worklist")

REPO_ROOT = Path(__file__).resolve().parent.parent
BIB_PATH = REPO_ROOT / "manuscript" / "99_bibliography" / "references.bib"
WORKLIST_PATH = REPO_ROOT / "tools" / "tier1_worklist.md"

TIER1_JOURNALS: frozenset[str] = frozenset(
    {
        "Journal of Finance",
        "Journal of Financial Economics",
        "Review of Financial Studies",
        "American Economic Review",
        "Quarterly Journal of Economics",
        "Econometrica",
        "Science",  # Tversky-Kahneman 1981 framing — foundational behavioral
    }
)

FOUNDATIONAL_NLP_KEYS: frozenset[str] = frozenset(
    {
        "vaswani_etal_2017",  # Transformer
        "devlin_etal_2019",  # BERT
        "lewis_etal_2020",  # RAG
        "mikolov_etal_2013_distributed",  # Word2Vec
        "pennington_etal_2014",  # GloVe
        "sennrich_etal_2016",  # BPE
        "araci_2019_finbert",  # FinBERT (Araci)
        "huang_etal_2023_finbert",  # FinBERT (Huang) — in Contemporary Accounting Research
    }
)


def _read_entries() -> list[dict]:
    """Read references.bib with @online rewrite."""
    text = BIB_PATH.read_text(encoding="utf-8")
    rewritten = re.sub(r"^@online\{", "@misc{__ONLINE__", text, flags=re.MULTILINE)
    db = bibtexparser.loads(rewritten)
    for e in db.entries:
        if e["ID"].startswith("__ONLINE__"):
            e["ENTRYTYPE"] = "online"
            e["ID"] = e["ID"][len("__ONLINE__") :]
    return db.entries


def is_tier1(entry: dict) -> bool:
    """Tier-1 membership rule."""
    journal = entry.get("journaltitle", "").strip()
    return journal in TIER1_JOURNALS or entry["ID"] in FOUNDATIONAL_NLP_KEYS


def _format_entry_line(entry: dict, idx: int) -> list[str]:
    """Render one entry as a multi-line worklist block."""
    key = entry["ID"]
    title = entry.get("title", "?")
    authors = entry.get("author", "?").replace(" and ", "; ")
    year = entry.get("year", "?")
    venue = (
        entry.get("journaltitle")
        or entry.get("booktitle")
        or entry.get("howpublished")
        or "?"
    )
    doi = entry.get("doi", "")
    url = entry.get("url", "")
    chapters = entry.get("keywords", "")

    locator = f"DOI: {doi}" if doi else (f"URL: {url}" if url else "(no DOI/URL)")

    lines = [
        f"### {idx}. `{key}`  · _cited in {chapters}_",
        "",
        f"**{authors}.** *{title}.* {venue}, {year}.",
        f"`{locator}`",
        "",
        "- [ ] Located PDF at SMU Library",
        "- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)",
        "- [ ] Read abstract + introduction + conclusion",
        "- [ ] Captured 2-3 page-anchored findings",
        "- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`",
        "",
    ]
    return lines


def build_worklist() -> int:
    """Write the Tier-1 worklist Markdown. Returns the Tier-1 entry count."""
    entries = _read_entries()
    tier1 = [e for e in entries if is_tier1(e)]

    # Sort by chapter then key for ordered verification
    def sort_key(e: dict) -> tuple:
        chapters = sorted(c.strip() for c in e.get("keywords", "").split(",") if c.strip())
        return (chapters[0] if chapters else "ch99", e["ID"])

    tier1.sort(key=sort_key)

    output: list[str] = []
    output.append("# Tier-1 SMU Library Verification Worklist")
    output.append("")
    output.append(
        "Foundational sources that must be verified before publication. Per "
        "[research_review.md §7.1](../manuscript/research_review.md): top-five "
        "economics journals (JF, JFE, RFS, AER, QJE, Econometrica) plus "
        "foundational NLP papers (Transformer, BERT, RAG, Word2Vec, GloVe, BPE, "
        "the two FinBERTs)."
    )
    output.append("")
    output.append(f"**Total:** {len(tier1)} sources")
    output.append("")
    output.append("**Workflow per source:**")
    output.append("1. Locate the paper in SMU Library (digital archives, JSTOR, Wiley, etc.).")
    output.append("2. Download PDF and verify the citation details against what's in `research.md`.")
    output.append("3. Read the abstract + introduction + conclusion. Skim the methods.")
    output.append("4. Capture 2-3 specific findings with page numbers in the research.md entry as a")
    output.append("   `Verification notes:` block under the `Status:` line.")
    output.append("5. Flip the status: `[ ] Unverified` → `[x] Verified via SMU Library YYYY-MM-DD`.")
    output.append("6. Re-run `python -m tools.research_to_bibtex --write` to regenerate the bib")
    output.append("   if anything changed (DOI fix, author correction, etc.).")
    output.append("")
    output.append("**Time estimate:** 15-30 min per source (Tier 1 papers reward careful reading).")
    output.append("")
    output.append("---")
    output.append("")

    for idx, e in enumerate(tier1, start=1):
        output.extend(_format_entry_line(e, idx))

    WORKLIST_PATH.write_text("\n".join(output), encoding="utf-8")
    return len(tier1)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )

    count = build_worklist()
    print(f"Wrote {count}-entry Tier-1 worklist to {WORKLIST_PATH.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
