# CrossRef Verification Triage Notes

Generated from `verification_report.txt` after the first run on 2026-05-15.

## Summary

| Status | Count | Notes |
|---|---|---|
| ok | 72 | Title, author, and year match CrossRef cleanly. |
| mismatch | 25 | See categorization below. |
| not_found | 0 | All DOIs resolved. |
| no_doi | 69 | Entries without DOI (preprints, regulatory docs, books w/o DOI). |
| **total** | **166** | |

The 97 entries with DOIs split: **72 clean / 25 flagged**.

## Mismatch Categorization

### Category A — Off-by-one year (online-first vs print)

These have **title score 100** and matching authors, but the year differs by 1
because CrossRef returns the online-first publication year while the bib uses
the print issue year. The print year is the correct Chicago citation. **No fix needed.**

- `bailey_etal_2017` (bib 2017, CrossRef 2016) — JCF print 2017
- `bradley_etal_2024` (bib 2024, CrossRef 2023) — RFS print 2024
- `brunnermeier_pedersen_2009` (bib 2009, CrossRef 2008)
- `campbell_etal_2014` (bib 2014, CrossRef 2013)
- `cookson_etal_2023` (bib 2023, CrossRef 2022)
- `longpre_etal_2023` (bib 2023, CrossRef 2024)
- (approx. 10 more in the same pattern)

### Category B — Unicode / formatting differences

These have **title score 85–99** due to Unicode hyphens, curly quotes, or
HTML entities returned by CrossRef. The content matches exactly. **No fix needed.**

- `brown_tucker_2011` (`&amp;` HTML entity, ‐ vs -)
- `bradley_etal_2024` (' vs ')
- `costola_etal_2022` (mixed-case title)

### Category C — CrossRef first-author ordering quirk

CrossRef sometimes returns a different author as "first" — typically the
corresponding author rather than the byline-first author. The title still
matches. **Verify at SMU Library, then either fix research.md author order
or document the CrossRef discrepancy.**

- `brintrup_etal_2024` — bib first author Brintrup, CrossRef first author Kosasih.
  Title and year match. Likely a corresponding-author swap.
- `costola_etal_2022` — bib Costola, CrossRef Mancini.

### Category D — Real DOI errors (research.md fix needed)

These are entries where the DOI resolves to a different paper entirely.
**Must fix in research.md before publication.**

- **`apel_grimaldi_2014`** — DOI `10.1515/roe-2014-0103` resolves to
  *"Ranking Economics and Econometrics ISI Journals by Quality Weighted Citations"*
  by Chang, not Apel & Grimaldi's *"How Informative Are Central Bank Minutes?"*
  Action: find correct DOI for the Apel-Grimaldi paper in *Review of Economics*
  (Sveriges Riksbank, vol. 65 no. 1, 2014, pp. 53-76), or remove the DOI field
  if no DOI exists.

## Recommended Workflow

1. Tier-1 SMU Library verification (next step) should resolve Category C and D
   issues for the foundational sources.
2. Re-run `verify_doi.py` after any research.md edits to confirm fixes.
3. Categories A and B can be ignored — they are CrossRef-side artifacts.

## How to Re-run

```bash
cd applied-nlp-finance
source .venv/bin/activate

# After editing research.md to fix a DOI:
uv run python -m tools.research_to_bibtex --write
uv run python -m tools.verify_doi --all
```
