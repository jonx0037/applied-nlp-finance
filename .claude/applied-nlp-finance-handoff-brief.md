# Claude Code Handoff Brief: *Applied NLP for Finance* (v2)
**Author:** Jonathan Rocha  
**Date:** March 2026  
**Revision:** v2 — structural, content, and reproducibility improvements  
**Purpose:** Scaffold the full file and directory structure for the book manuscript and its companion GitHub repository.

---

## 1. Project Overview

**Book Title (working):** *Applied NLP for Finance: Building Market Intelligence Systems with Language Models*

**Core Thesis:** Financial markets are fundamentally narrative-driven systems. Price and volume data capture *what happened*; text data captures *why*. NLP — particularly transformer-based models — is now mature enough to systematically extract signal from financial language at scale. This book teaches readers how to build, evaluate, and deploy those systems end to end.

**Target Audience:**
- Quantitative researchers and data scientists transitioning into financial NLP
- ML engineers at hedge funds, fintechs, or trading desks
- Sophisticated independent traders building their own signal pipelines
- Graduate students in finance, data science, or computational linguistics

**Audience Skill Variance:** The reader base spans from grad students to production ML engineers. The preface includes a "How to Read This Book" section that maps entry points by background. Chapters use **Prerequisite** callout boxes where advanced material builds on earlier content. Each chapter's companion notebook includes tiered exercises: *Foundations* (core implementation), *Intermediate* (extensions and variations), and *Advanced* (open-ended research problems). The `exercises/` directory organizes these by chapter.

**Tone:** Technically rigorous but practitioner-first. Every concept is grounded in real implementation decisions. Code is production-oriented, not toy-level. Narrative context and conceptual framing are given serious weight — this is not a cookbook.

**Companion GitHub Repo:** `github.com/jonx0037/applied-nlp-finance`  
Every chapter has a corresponding Jupyter notebook in the repo. All datasets, model checkpoints (where licensing permits), and utility modules are version-controlled. The repo is designed to evolve beyond publication.

---

## 2. Directory Structure to Scaffold

### Book Manuscript Repo

```
applied-nlp-finance/
├── README.md
├── LICENSE
├── .gitignore
├── .python-version                  # Pin Python version (e.g., 3.11.x)
├── .claude/
│   └── applied-nlp-finance-handoff-brief.md   ← copy of this file
│
├── manuscript/
│   ├── 00_preface/
│   │   └── preface.md
│   ├── 01_why_text_moves_markets/
│   │   ├── chapter.md
│   │   └── notes.md
│   ├── 02_text_data_acquisition/
│   │   ├── chapter.md
│   │   └── notes.md
│   ├── 03_nlp_foundations_for_finance/
│   │   ├── chapter.md
│   │   └── notes.md
│   ├── 04_transformers_llms_and_financial_language/
│   │   ├── chapter.md
│   │   └── notes.md
│   ├── 05_sentiment_analysis_and_signal_construction/
│   │   ├── chapter.md
│   │   └── notes.md
│   ├── 06_earnings_calls_and_corporate_disclosure/
│   │   ├── chapter.md
│   │   └── notes.md
│   ├── 07_central_bank_language_and_macro_signals/
│   │   ├── chapter.md
│   │   └── notes.md
│   ├── 08_social_media_and_alternative_data/
│   │   ├── chapter.md
│   │   └── notes.md
│   ├── 09_entity_extraction_and_financial_knowledge_graphs/
│   │   ├── chapter.md
│   │   └── notes.md
│   ├── 10_market_regime_detection/
│   │   ├── chapter.md
│   │   └── notes.md
│   ├── 11_backtesting_and_evaluation/
│   │   ├── chapter.md
│   │   └── notes.md
│   ├── 12_deployment_and_production_systems/
│   │   ├── chapter.md
│   │   └── notes.md
│   ├── 13_risk_ethics_and_limits/
│   │   ├── chapter.md
│   │   └── notes.md
│   └── 99_bibliography/
│       └── references.bib
│
├── notebooks/
│   ├── ch01_why_text_moves_markets.ipynb
│   ├── ch02_text_data_acquisition.ipynb
│   ├── ch03_nlp_foundations.ipynb
│   ├── ch04_transformers_llms_financial.ipynb
│   ├── ch05_sentiment_signal.ipynb
│   ├── ch06_earnings_calls.ipynb
│   ├── ch07_central_bank_language.ipynb
│   ├── ch08_social_media_alt_data.ipynb
│   ├── ch09_entity_extraction_kg.ipynb
│   ├── ch10_regime_detection.ipynb
│   ├── ch11_backtesting_evaluation.ipynb
│   ├── ch12_deployment.ipynb
│   └── ch13_risk_ethics.ipynb
│
├── exercises/
│   ├── README.md                    # Explains tiered structure
│   ├── ch01/
│   │   ├── foundations.md
│   │   ├── intermediate.md
│   │   └── advanced.md
│   ├── ch02/
│   │   └── ...                      # Same structure per chapter
│   └── ...
│
├── src/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── scrapers.py              # SEC EDGAR, news API wrappers
│   │   ├── loaders.py               # Standardized data loading utilities
│   │   └── preprocessing.py         # Text cleaning, normalization
│   ├── models/
│   │   ├── __init__.py
│   │   ├── finbert.py               # FinBERT wrapper and fine-tuning helpers
│   │   ├── llm_prompting.py         # LLM-based classification and extraction
│   │   ├── regime_detector.py       # Sentiment regime detection pipeline
│   │   └── signal_builder.py        # Signal construction from model outputs
│   ├── knowledge/
│   │   ├── __init__.py
│   │   ├── entity_extraction.py     # NER for financial entities
│   │   └── graph_builder.py         # Knowledge graph construction utilities
│   ├── evaluation/
│   │   ├── __init__.py
│   │   ├── backtest.py              # Backtesting framework utilities
│   │   └── metrics.py               # NLP + financial evaluation metrics
│   └── utils/
│       ├── __init__.py
│       ├── config.py
│       └── logging.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py                  # Shared fixtures (sample data, model stubs)
│   ├── test_data/
│   │   ├── test_scrapers.py
│   │   ├── test_loaders.py
│   │   └── test_preprocessing.py
│   ├── test_models/
│   │   ├── test_finbert.py
│   │   ├── test_llm_prompting.py
│   │   ├── test_regime_detector.py
│   │   └── test_signal_builder.py
│   ├── test_knowledge/
│   │   ├── test_entity_extraction.py
│   │   └── test_graph_builder.py
│   └── test_evaluation/
│       ├── test_backtest.py
│       └── test_metrics.py
│
├── data/
│   ├── README.md                    # Per-chapter data provenance and acquisition guide
│   ├── raw/
│   │   └── .gitkeep
│   ├── processed/
│   │   └── .gitkeep
│   └── sample/                      # Small, redistributable sample datasets
│       └── .gitkeep
│
├── figures/
│   ├── ch01/
│   │   └── .gitkeep
│   ├── ch02/
│   │   └── .gitkeep
│   ├── ch03/
│   │   └── .gitkeep
│   ├── ch04/
│   │   └── .gitkeep
│   ├── ch05/
│   │   └── .gitkeep
│   ├── ch06/
│   │   └── .gitkeep
│   ├── ch07/
│   │   └── .gitkeep
│   ├── ch08/
│   │   └── .gitkeep
│   ├── ch09/
│   │   └── .gitkeep
│   ├── ch10/
│   │   └── .gitkeep
│   ├── ch11/
│   │   └── .gitkeep
│   ├── ch12/
│   │   └── .gitkeep
│   └── ch13/
│       └── .gitkeep
│
├── docker/
│   ├── Dockerfile                   # Full environment for running all notebooks
│   └── docker-compose.yml           # Multi-service setup (app + pgvector)
│
├── pyproject.toml                   # Single source of truth for deps and packaging
├── CONTRIBUTING.md
└── CHANGELOG.md
```

### Removed from v1
- `requirements.txt` — replaced by `pyproject.toml` as the single dependency source. A `pip install -e .` workflow means notebooks can `from src.models import finbert` without `sys.path` hacks.

---

## 3. Chapter Briefs

### Preface
Establish the author's position: a practitioner who came to NLP through financial markets and humanities, not the other way around. Frame the book's argument about narrative and markets. Acknowledge the fast-moving nature of the field and explain how to use the book alongside the companion repo.

**New in v2 — "How to Read This Book" section:** Map the four audience personas to recommended reading paths. Grad students start at Chapter 1 and read linearly. Experienced ML engineers may skip Chapters 1–3. Quant researchers with NLP exposure can jump directly to Chapter 5. Independent traders are directed to Chapters 1, 5, 6, 10–11 as a focused track. Explain the tiered exercise system (Foundations / Intermediate / Advanced) and how the companion repo mirrors the manuscript.

---

### Chapter 1 — Why Text Moves Markets
**Goal:** Make the conceptual case for financial NLP before a single line of code is written.

**Key topics:**
- The efficient market hypothesis and its assumption about information
- What "information" actually means when it arrives as language
- Historical examples: Fed minutes moving bond markets, earnings call tone predicting stock drift, Twitter sentiment preceding price moves
- Why NLP has lagged price/volume quant strategies — and why that's changing
- A taxonomy of financial text data (structured vs. unstructured, scheduled vs. unscheduled)

**Tone note:** This is the author's most humanistic chapter. Lean into the historical and narrative framing. This is where the English background earns its place.

---

### Chapter 2 — Text Data Acquisition
**Goal:** Give readers a comprehensive, honest guide to sourcing financial text data.

**Key topics:**
- SEC EDGAR: 8-K, 10-K, 10-Q, proxy filings — structure, access, rate limits
- Financial news APIs: Bloomberg, Refinitiv, NewsAPI, GDELT, Alpaca News
- Earnings call transcripts: Seeking Alpha, Motley Fool, vendor APIs
- Central bank communications: Fed, ECB, BoJ — official sources and structured archives
- Social media: Reddit (PRAW), Twitter/X API tiers, StockTwits
- Web scraping ethics, `robots.txt`, ToS considerations, data licensing
- Building a reliable data pipeline with deduplication and provenance tracking
- **Data versioning strategy:** Using DVC or git-lfs for dataset snapshots, plus `data/README.md` as a provenance guide so readers can reproduce exact datasets

**Code:** Scrapers and API wrappers in `src/data/scrapers.py`. Companion notebook demonstrates full pipeline for each source.

---

### Chapter 3 — NLP Foundations for Finance
**Goal:** Establish the NLP baseline so readers understand what transformers improved upon.

**Key topics:**
- Tokenization approaches and why they matter for financial text
- Bag-of-words, TF-IDF, and their use in financial lexicons (Loughran-McDonald dictionary)
- Word embeddings: Word2Vec, GloVe, fastText — strengths and limits in financial context
- Classical sentiment approaches: VADER, TextBlob, rule-based systems
- Benchmarking classical methods against labeled financial datasets (FiQA, SEntFiN)
- When classical NLP is still the right choice (latency, interpretability, cost)

**Code:** Preprocessing utilities in `src/data/preprocessing.py`.

---

### Chapter 4 — Transformers, LLMs, and Financial Language Models
**Goal:** Deep treatment of transformer architecture and modern LLM workflows in the financial domain.

**Key topics:**
- BERT architecture review (brief, assumes ML literacy)
- Why general-purpose BERT underperforms on financial text
- FinBERT: architecture, training corpus, fine-tuning strategy
- Other domain-adapted models: BloombergGPT, FinGPT, Llama-finance variants
- Fine-tuning on custom financial corpora: data requirements, training recipes, evaluation
- **LLM-based financial workflows (expanded):**
  - Zero-shot and few-shot prompting for financial classification tasks
  - Structured extraction from SEC filings via LLMs (JSON-mode, function calling)
  - Prompt engineering for financial summarization and sentiment labeling
  - LLM-as-judge: using frontier models to label training data for smaller classifiers
  - Agentic pipelines: multi-step financial analysis with tool-using LLMs
  - Cost/latency/accuracy tradeoff matrix: fine-tuned FinBERT vs. prompted GPT-4/Claude vs. distilled models
- Choosing the right model for the task: when to fine-tune, when to prompt, when to chain

**Code:** `src/models/finbert.py` — wrapper class with fine-tuning and inference utilities. `src/models/llm_prompting.py` — LLM classification, extraction, and labeling utilities.

---

### Chapter 5 — Sentiment Analysis and Signal Construction
**Goal:** Bridge the gap between model output and tradeable signal.

**Key topics:**
- Raw sentiment scores vs. aggregated sentiment indices
- Temporal aggregation: rolling windows, exponential weighting, event-time vs. calendar-time
- Cross-asset sentiment: how equity sentiment bleeds into credit, volatility, and commodities
- Signal normalization, z-scoring, and regime-conditioning
- Combining sentiment with price/volume features: feature engineering best practices
- **Multi-modal feature fusion:** combining text-derived features with tabular data from the same source (e.g., sentiment + financial ratios from the same 10-K, language tone + earnings surprise magnitude)
- Avoiding look-ahead bias in feature construction

**Code:** `src/models/signal_builder.py`.

---

### Chapter 6 — Earnings Calls and Corporate Disclosure
**Goal:** Systematic analysis of scheduled, high-signal financial language events.

> **Note (v2 reorder):** Chapters 6–8 now cover domain-specific text sources *before* the regime detection chapter, so that regime detection can reference concrete examples and data pipelines from these domains.

**Key topics:**
- Structure of earnings calls: prepared remarks vs. Q&A dynamics
- Linguistic features predictive of post-earnings drift: uncertainty language, hedging, specificity
- Tone analysis: CEO vs. CFO language differences, analyst question tone
- 10-K and 10-Q risk factor analysis: changes in language year-over-year as signal
- MD&A (Management Discussion and Analysis) as a structured NLP target
- Event study methodology for text-based signals

---

### Chapter 7 — Central Bank Language and Macro Signals
**Goal:** Parse the most market-moving scheduled text events in finance.

**Key topics:**
- FOMC statements, minutes, and press conference transcripts
- The evolution of Fed communication: from opacity to forward guidance
- Hawkish/dovish language models: building a continuous policy tone index
- ECB, BoJ, BoE — cross-central bank language analysis
- Nowcasting macro indicators from central bank language
- The "Fed whisperer" problem: when markets read between the lines

---

### Chapter 8 — Social Media and Alternative Text Data
**Goal:** Handle noisier, higher-frequency, and legally complex text sources.

**Key topics:**
- Reddit WallStreetBets as a case study: signal vs. noise, manipulation detection
- StockTwits and microblogging sentiment at high frequency
- News momentum vs. social media momentum: correlation and divergence
- Bot detection and data quality filtering
- Short squeeze detection from unusual language spikes
- Crypto social media: Discord, Telegram, and X as primary communication channels

---

### Chapter 9 — Entity Extraction and Financial Knowledge Graphs *(New)*
**Goal:** Move beyond bag-of-sentiment to structured relational understanding of financial text.

**Key topics:**
- Named Entity Recognition (NER) for financial entities: companies, executives, instruments, regulatory bodies
- Domain-specific NER challenges: ticker symbols as common words, subsidiary disambiguation, cross-reference to identifiers (CUSIPs, LEIs)
- Relation extraction: who-owns-whom, supply chain dependencies, executive-to-company mappings from filings
- Building knowledge graphs from SEC filings, earnings calls, and news articles
- Temporal knowledge graphs: tracking how relationships evolve (board changes, M&A, supply chain shifts)
- Use cases: supply chain risk propagation, contagion modeling, activism detection, competitive landscape mapping
- Graph-based features for downstream models: centrality metrics, community detection, path-based signals
- **Multi-modal graph enrichment:** linking text-extracted relationships with structured financial data (ownership percentages, revenue exposure, geographic footprint)

**Code:** `src/knowledge/entity_extraction.py` and `src/knowledge/graph_builder.py`.

---

### Chapter 10 — Market Regime Detection
**Goal:** The author's primary research contribution — deep treatment of sentiment-based regime detection.

> **Note (v2 reorder):** Now positioned after Chapters 6–9, this chapter can draw directly on the earnings call, central bank, social media, and entity extraction pipelines developed in preceding chapters. The regime detector consumes these as input features rather than introducing them in the abstract.

**Key topics:**
- What is a market regime? A taxonomy: trend, volatility, correlation, and narrative regimes
- Existing quantitative regime detection methods: HMMs, Markov Switching, clustering approaches
- Why sentiment-based regime detection is complementary, not redundant
- Cross-asset sentiment regime detector: architecture and methodology
- Implementation walkthrough: from raw text to regime label (referencing Ch6–9 pipelines as concrete inputs)
- **Multi-modal regime features:** combining text-derived sentiment with price/volume regimes and entity-graph topology shifts
- Evaluating regime detectors: stability, transition detection accuracy, forward return predictiveness
- Real-world case studies: COVID crash, 2022 rate hiking cycle, crypto contagion

**Code:** `src/models/regime_detector.py` — the core contribution of the companion repo.

**Note:** This chapter draws directly from the SMU MSDS capstone project. Cite accordingly.

---

### Chapter 11 — Backtesting and Evaluation
**Goal:** Teach rigorous evaluation methodology specific to NLP-based strategies.

**Key topics:**
- The backtest overfitting problem — and why NLP makes it worse
- Walk-forward validation vs. expanding window vs. purged cross-validation
- Sharpe ratio, Calmar ratio, and information ratio for NLP signal evaluation
- NLP-specific evaluation: how to assess whether the model "understands" finance
- Benchmark construction: what does a fair baseline look like?
- Transaction costs, slippage, and market impact for text-driven strategies
- Common failure modes: stale data, survivorship bias, data snooping

**Code:** `src/evaluation/backtest.py` and `src/evaluation/metrics.py`.

---

### Chapter 12 — Deployment and Production Systems
**Goal:** Close the gap between research notebook and production pipeline.

**Key topics:**
- Architecture patterns: batch vs. streaming NLP pipelines
- FastAPI for serving NLP models — latency, concurrency, versioning
- Vector databases for semantic search over financial documents (pgvector, Pinecone, Weaviate)
- RAG (Retrieval-Augmented Generation) patterns for financial Q&A
- Model drift detection and automated retraining triggers
- Infrastructure: Docker, cloud deployment (AWS SageMaker, GCP Vertex AI)
- Monitoring: model performance dashboards, data quality alerts

**Note:** The `docker/` directory at the repo root provides a working Dockerfile and docker-compose.yml so readers can reproduce the full environment from Chapter 1 onward, not just at the deployment stage.

---

### Chapter 13 — Risk, Ethics, and the Limits of Financial NLP
**Goal:** Honest, intellectually serious treatment of what NLP cannot do and what it shouldn't do.

**Key topics:**
- Model fragility: when language models fail at tail events
- The narrative fallacy: how models can overfit to story patterns
- Market manipulation via language: pump-and-dump, coordinated social media campaigns
- Regulatory landscape: SEC, FINRA, and MiCA considerations for algorithmic text-driven trading
- Systemic risk: what happens when every hedge fund uses the same NLP models
- The ethics of alternative data: privacy, consent, and insider information boundaries
- A practitioner's honest assessment of the state of the field

---

## 4. Companion GitHub Repo Instructions

**Repo name:** `applied-nlp-finance`  
**Visibility:** Public  
**License:** MIT (code), CC BY-NC 4.0 (manuscript drafts in `/manuscript`)

### `pyproject.toml` should include:

```toml
[build-system]
requires = ["setuptools>=68.0", "wheel"]
build-backend = "setuptools.backends._legacy:_Backend"

[project]
name = "applied-nlp-finance"
version = "0.1.0"
description = "Companion code for Applied NLP for Finance"
requires-python = ">=3.11"
license = {text = "MIT"}
authors = [{name = "Jonathan Rocha"}]

dependencies = [
    "transformers>=4.40",
    "torch>=2.2",
    "datasets>=2.18",
    "pandas>=2.2",
    "numpy>=1.26",
    "scikit-learn>=1.4",
    "matplotlib>=3.8",
    "seaborn>=0.13",
    "plotly>=5.20",
    "fastapi>=0.110",
    "uvicorn>=0.28",
    "praw>=7.7",
    "requests>=2.31",
    "beautifulsoup4>=4.12",
    "sec-edgar-downloader>=5.0",
    "pgvector>=0.2",
    "sqlalchemy>=2.0",
    "spacy>=3.7",
    "networkx>=3.2",
    "neo4j>=5.17",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "pytest-cov>=4.1",
    "ruff>=0.3",
    "mypy>=1.8",
    "pre-commit>=3.6",
]
notebooks = [
    "jupyter>=1.0",
    "ipykernel>=6.29",
]

[tool.setuptools.packages.find]
include = ["src*"]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-v --tb=short"

[tool.ruff]
line-length = 100
target-version = "py311"
```

### README.md should include:
- One-paragraph book description and author bio
- Table of contents linking to notebook files
- Setup instructions (`pip install -e ".[dev,notebooks]"`)
- Docker quickstart (`docker compose up`)
- Data acquisition guide (what's included vs. what requires an API key), referencing `data/README.md`
- Link to book purchase page (placeholder)
- Contributing guidelines reference

### `data/README.md` should include:
- Per-chapter table listing: data source, access method (API, scraper, manual), license/ToS, estimated size
- Step-by-step acquisition instructions for each source
- Notes on which datasets are included in `data/sample/` for immediate use
- Guidance on DVC or manual snapshot approach for exact reproducibility

### `.gitignore` should exclude:
- `data/raw/` (too large, often licensed)
- `.env` (API keys)
- `__pycache__/`, `.ipynb_checkpoints/`
- Model checkpoints > 100MB
- `.mypy_cache/`, `.ruff_cache/`
- `dist/`, `*.egg-info/`

### Each notebook should open with:
- Chapter title and number
- 2–3 sentence chapter summary
- `pip install -e ".[notebooks]"` reminder (one-time setup)
- Section headers matching the chapter structure
- Tiered exercise pointers: link to corresponding `exercises/chXX/` files

---

## 5. Scaffold Instructions for Claude Code

1. Create the full directory tree above under a root folder named `applied-nlp-finance/`
2. Initialize `.python-version` with `3.11`
3. Initialize each `chapter.md` file with: title, 3-sentence description, and placeholder section headers matching the chapter brief above
4. Initialize each `notes.md` file with: a `## Research Needed` section and a `## Key Citations (TBD)` section
5. Initialize each notebook (`.ipynb`) with: title cell, chapter summary markdown cell, imports cell (standard libraries only), one placeholder section cell, and a final cell linking to `exercises/chXX/`
6. Populate `src/` Python files with module docstrings, class/function stubs, and inline `# TODO` comments matching the functionality described in the chapter briefs — including the new `src/models/llm_prompting.py` and `src/knowledge/` modules
7. Populate `tests/` with stub test files — one test file per `src/` module, each containing at least one placeholder test function (`def test_placeholder(): pass`) and a docstring referencing what it will test
8. Write `exercises/README.md` explaining the three-tier system, then create per-chapter exercise files with placeholder headers for each tier
9. Write a complete `README.md` at the root level per the spec above
10. Write `pyproject.toml` per the spec above (do **not** create a separate `requirements.txt`)
11. Write `data/README.md` with the per-chapter data provenance table (placeholder entries)
12. Write `docker/Dockerfile` (Python 3.11-slim base, `pip install -e ".[notebooks]"`, expose Jupyter port)
13. Write `docker/docker-compose.yml` (app service + pgvector service)
14. Write `CONTRIBUTING.md` with standard PR workflow, code style (ruff), and test expectations
15. Write `CHANGELOG.md` with initial `## [0.1.0] — Unreleased` entry
16. Copy this brief to `.claude/applied-nlp-finance-handoff-brief.md`

---

## 6. Structural Decisions Log (v2)

This section documents the reasoning behind structural changes from v1 so future iterations maintain coherence.

| Change | Rationale |
|--------|-----------|
| Chapter reorder: domain sources (Ch 6–8) before regime detection (Ch 10) | Regime detection chapter now references concrete pipelines instead of forward-declaring them. Readers encounter the data sources that feed the regime detector before seeing the detector itself. |
| New chapter: Entity Extraction and Financial Knowledge Graphs (Ch 9) | Fills a meaningful gap — structured relational understanding of financial text is a distinct capability from sentiment analysis and is increasingly used in practice. Positions naturally between domain data chapters and the regime detector. |
| Expanded Ch 4: LLM workflows | The original brief under-represented LLM-based approaches (prompting, structured extraction, agentic pipelines) relative to their current practitioner relevance. These now get dedicated treatment alongside fine-tuned models. |
| Multi-modal integration (Ch 5, 9, 10) | Threaded across relevant chapters rather than a standalone chapter. Combining text with tabular/graph data is a technique, not a topic — it belongs where it's applied. |
| `pyproject.toml` replaces `requirements.txt` | Installable package (`pip install -e .`) eliminates `sys.path` hacks in notebooks. Single source of truth for dependencies with optional groups (dev, notebooks). |
| `tests/` directory added | A production-oriented book without tests contradicts its own premise. Even stubs set the expectation for readers contributing to the repo. |
| `docker/` directory added | Chapter 12 covers Docker deployment, but environment reproducibility should start at Chapter 1. Readers can `docker compose up` from day one. |
| Per-chapter `figures/` subdirectories | Flat `figures/` directory becomes unmanageable at 13 chapters. Mirrors `manuscript/` structure. |
| `exercises/` directory with tiered structure | Addresses audience skill variance without cluttering notebooks. Each chapter has three tiers: Foundations, Intermediate, Advanced. |
| `.python-version` and pinned deps | ML reproducibility is fragile. Pinned lower bounds in `pyproject.toml` plus `.python-version` reduce environment drift across readers. |
| `data/README.md` provenance guide | `data/raw/` is gitignored — readers need explicit instructions to reproduce datasets. Per-chapter provenance table fills this gap. |

---

## 7. Future Work (Subsequent Claude Chats)

The following will be developed in dedicated follow-up sessions:

- **Deep research pass per chapter:** Sourcing peer-reviewed articles, landmark papers, and books for each chapter's `references.bib` and `notes.md`
- **Code implementation:** Filling in `src/` module implementations chapter by chapter, including the new `llm_prompting.py` and `knowledge/` modules
- **Test implementation:** Writing real tests alongside `src/` implementations
- **Notebook development:** Full working code for each companion notebook
- **Exercise development:** Writing tiered exercises per chapter with solution keys
- **Market-sentiment.io integration:** Chapter 10 will reference the live dashboard as a working implementation example
- **Publisher research:** Identifying target publishers (O'Reilly, Manning, Springer, CRC Press) and preparing a proposal
- **Data versioning decision:** Evaluate DVC vs. git-lfs vs. manual approach and implement chosen strategy

---

*Brief prepared by Jonathan Rocha with Claude (Anthropic), March 2026.*
