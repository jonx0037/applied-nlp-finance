# Bibliography Tooling

Scripts that generate and validate `manuscript/99_bibliography/references.bib`
from the per-chapter `research.md` files. The bib file is **never** hand-edited;
the source of truth lives in `research.md`.

## Scripts

| Script | Purpose |
|---|---|
| `citation_keys.py` | Pure-function key generator (`lastname_year[_keyword]`). Unit-tested in `tests/test_tools/test_citation_keys.py`. |
| `research_to_bibtex.py` | Parses `manuscript/*/research.md` → emits unified `references.bib` with anchor-source dedup. |
| `verify_doi.py` | Cross-checks DOIs against CrossRef. Produces `verification_report.txt`. |
| `build_master_index.py` | Generates `manuscript/references_master_index.md` (per-chapter scan view). |
| `tier1_worklist.py` | Generates `tools/tier1_worklist.md` (SMU Library verification checklist). |

## Quick reference

```bash
cd applied-nlp-finance
source .venv/bin/activate

# After editing research.md:
uv run python -m tools.research_to_bibtex --write
uv run python -m tools.build_master_index

# Cross-check DOIs (slow — ~90s for ~100 DOIs):
uv run python -m tools.verify_doi --all

# Re-generate the Tier-1 worklist if entries change:
uv run python -m tools.tier1_worklist

# Validate the bib (system biber, optional):
biber --tool --validate-config --output-file=/tmp/refs-validated.bib manuscript/99_bibliography/references.bib

# Run unit tests for citation_keys:
pytest tests/test_tools/
```

## Conventions

See [`manuscript/99_bibliography/CITATIONS.md`](../manuscript/99_bibliography/CITATIONS.md) for:

- Citation key format (`lastname_year[_keyword]`) and disambiguation rules.
- Required vs. recommended fields per entry type.
- Special cases (two FinBERTs, regulatory docs, legal cases, non-English authors).
- Workflow for SMU Library verification.

## Outputs

These files are generated and **should not be hand-edited**:

- `manuscript/99_bibliography/references.bib`
- `manuscript/references_master_index.md`
- `tools/verification_report.txt`
- `tools/tier1_worklist.md`
