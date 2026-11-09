# CLAUDE.md — Applied NLP for Finance

## Project Identity

Book + companion code repo: **Applied NLP for Finance: Building Market Intelligence Systems with Language Models** by Jonathan Rocha. The repo serves dual purposes — a publishable manuscript (`manuscript/`) and production-quality Python companion code (`src/`).

**Core thesis:** Financial markets are narrative-driven. Text captures *why* markets move; NLP extracts that signal at scale.

**Audience:** Quant researchers, ML engineers at funds/fintechs, grad students in finance/DS, and sophisticated independent traders. The code targets practitioners, not toy examples.

## Architecture

```
src/                    # Installable Python package (pip install -e .)
  data/                 # Acquisition, loading, preprocessing (scrapers, loaders, cleaning)
  models/               # NLP models and signal pipelines (FinBERT, LLM prompting, regime detection)
  knowledge/            # Entity extraction and knowledge graphs (NER, graph builder)
  evaluation/           # Backtesting and metrics (walk-forward, Sharpe, directional accuracy)
  utils/                # Config and logging
tests/                  # pytest suite — mirrors src/ structure (test_data/, test_models/, etc.)
manuscript/             # 13 chapters + preface, each in numbered directories (chapter.md + notes.md)
notebooks/              # 13 Jupyter notebooks, one per chapter (ch01_ through ch13_)
exercises/              # Tiered exercises per chapter: foundations.md, intermediate.md, advanced.md
data/                   # raw/ (gitignored), processed/ (gitignored), sample/ (committed)
figures/                # Per-chapter subdirectories (ch01/ through ch13/)
docker/                 # Dockerfile + docker-compose.yml (app + pgvector)
```

Imports use `from src.models import finbert` etc. — the package is installed editable via `pip install -e .`, no `sys.path` hacks.

## Code Conventions

- **Python:** >= 3.11 (pinned in `.python-version`)
- **Linter/formatter:** Ruff — line length 100, target py311
- **Type checking:** mypy
- **Docstrings:** NumPy style (Parameters, Returns, Examples sections)
- **Type hints:** Full PEP 484 annotations on all public APIs
- **Tests:** pytest with shared fixtures in `tests/conftest.py`
- **Imports:** Standard library first, then third-party, then `src.*` — Ruff enforces this

## Commands

```bash
# Setup
pip install -e ".[dev,notebooks]"

# Linting and formatting
ruff check src/ tests/
ruff check --fix src/ tests/
ruff format src/ tests/

# Type checking
mypy src/

# Tests
pytest                        # all tests
pytest --cov=src tests/       # with coverage
pytest tests/test_models/     # specific module

# Docker (includes Jupyter + pgvector)
docker compose up

# Jupyter
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser
```

## Key Dependencies

Transformers ecosystem (`transformers`, `torch`, `datasets`), data science stack (`pandas`, `numpy`, `scikit-learn`), visualization (`matplotlib`, `seaborn`, `plotly`), NLP (`spacy`), graphs (`networkx`, `neo4j`), web/API (`fastapi`, `uvicorn`, `requests`, `beautifulsoup4`, `praw`, `sec-edgar-downloader`), vector DB (`pgvector`, `sqlalchemy`). Full list in `pyproject.toml`.

## Manuscript Conventions

- Each chapter lives in `manuscript/NN_chapter_name/chapter.md` with a companion `notes.md`
- Chapters are numbered 00-13 (00 = preface, 99 = bibliography)
- **Tone:** Technically rigorous but practitioner-first. Not a cookbook — narrative context and conceptual framing matter.
- The author has a humanities + finance background. Chapter 1 is deliberately the most humanistic chapter.
- **Language:** Always use American English spelling and conventions (e.g., "organize," "color," "analyze," "defense," "catalog") — never British English variants.
- Chapters 6-8 (domain sources) come *before* Chapter 10 (regime detection) intentionally — so the detector references concrete pipelines, not abstractions
- Chapter 9 (Knowledge Graphs) is a v2 addition, filling the gap between sentiment and regime detection
- Chapter 10 (Regime Detection) is the author's primary research contribution (SMU MSDS capstone)

## Licensing

- **Code** (`src/`, `tests/`, `notebooks/`, `docker/`): MIT
- **Manuscript** (`manuscript/`): CC BY-NC 4.0
- Respect this distinction when generating content.

## Design Decisions to Preserve

1. **`pyproject.toml` is the single source of truth** for dependencies — no `requirements.txt`
2. **Tiered exercises** (Foundations / Intermediate / Advanced) address audience skill variance — maintain this pattern for new chapters
3. **Multi-modal integration** is threaded across Chapters 5, 9, 10 — not a standalone chapter
4. **Docker from Chapter 1** — environment reproducibility starts immediately, not at the deployment chapter
5. **`data/raw/` is always gitignored** — users acquire their own data following `data/README.md`
6. **`data/sample/`** contains small redistributable datasets that *are* committed

## What NOT to Do

- Don't create `requirements.txt` — use `pyproject.toml`
- Don't put `sys.path` hacks in notebooks — the package is installed editable
- Don't commit to `data/raw/` or `data/processed/`
- Don't commit model checkpoints (`.pt`, `.bin`, `.safetensors` > 100MB)
- Don't commit `.env` files or API keys
- Don't modify the chapter numbering scheme without updating all cross-references
- Don't write manuscript content as a cookbook — maintain narrative framing and conceptual depth

## Current State

The project is scaffolded with a full directory structure, module stubs, and test stubs. Implementation is in progress. Key areas for development:

- `src/` modules contain class/function stubs with `# TODO` markers — fill these in chapter-by-chapter
- `tests/` contain placeholder tests — write real tests alongside implementations
- `notebooks/` have skeleton structure — develop with working code
- `manuscript/` chapters have placeholder section headers — write full prose
- `references.bib` needs deep research passes per chapter

## Bibliography Conventions

- **Citation style:** Chicago 17 (Notes and Bibliography), rendered via `biblatex-chicago`.
- **Source of truth:** Each chapter's `manuscript/NN_*/research.md` is the canonical annotated bibliography. `manuscript/99_bibliography/references.bib` is **generated** from these files — do not hand-edit individual entries.
- **Citation keys:** `lastname_year[_keyword]` lowercase. See [`manuscript/99_bibliography/CITATIONS.md`](manuscript/99_bibliography/CITATIONS.md) for the full convention and disambiguation algorithm.
- **Cross-chapter sources:** entries cited in multiple chapters have a single canonical BibTeX entry with `keywords = {ch01,ch05,...}` listing all citing chapters. Per-chapter scan view lives in the generated [`manuscript/references_master_index.md`](manuscript/references_master_index.md).
- **Two FinBERTs:** Araci 2019 and Huang et al. 2023 are distinct models; they have distinct keys (`araci_2019_finbert`, `huang_etal_2023_finbert`). Never collapse on title alone.
- **Verification status:** Each `research.md` entry has a `Status:` line. After SMU Library verification, flip `[ ] Unverified` → `[x] Verified via SMU Library YYYY-MM-DD` and append a `Verification notes:` block with 2-3 page-anchored findings.

### Tooling (under `tools/`)

```bash
source .venv/bin/activate

# Regenerate references.bib from research.md files
uv run python -m tools.research_to_bibtex --write

# Cross-check DOIs against CrossRef (produces tools/verification_report.txt)
uv run python -m tools.verify_doi --all

# Regenerate the per-chapter cross-reference index
uv run python -m tools.build_master_index

# Re-generate the Tier-1 SMU verification worklist
uv run python -m tools.tier1_worklist

# Run the citation-key generator unit tests
pytest tests/test_tools/
```

Install the tooling deps with `uv pip install -e ".[tools]"`. Conventions are tested in `tests/test_tools/test_citation_keys.py`.

## Companion Resources

- **Handoff brief:** `.claude/applied-nlp-finance-handoff-brief.md` — detailed chapter briefs, design rationale, and structural decisions log
- **Data guide:** `data/README.md` — per-chapter data sources, access methods, and licensing
- **Bibliography conventions:** [`manuscript/99_bibliography/CITATIONS.md`](manuscript/99_bibliography/CITATIONS.md) — citation key format, required fields per entry type, regeneration commands
- **Tier-1 verification worklist:** [`tools/tier1_worklist.md`](tools/tier1_worklist.md) — generated checklist for SMU Library verification of foundational sources
- **pgvector service:** `docker-compose.yml` provides PostgreSQL with pgvector (user: `nlpfinance`, db: `financial_docs`, port: 5432)
