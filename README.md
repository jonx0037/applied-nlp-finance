# Applied NLP for Finance

**Building Market Intelligence Systems with Language Models**

*By Jonathan Rocha*

Financial markets are fundamentally narrative-driven systems. Price and volume data capture *what happened*; text data captures *why*. This book teaches you how to build, evaluate, and deploy NLP systems that systematically extract signal from financial language at scale — from SEC filings and earnings calls to central bank communications and social media.

## Table of Contents

| Chapter | Notebook | Topic |
|---------|----------|-------|
| Preface | — | How to read this book |
| 1 | [ch01_why_text_moves_markets.ipynb](notebooks/ch01_why_text_moves_markets.ipynb) | Why Text Moves Markets |
| 2 | [ch02_text_data_acquisition.ipynb](notebooks/ch02_text_data_acquisition.ipynb) | Text Data Acquisition |
| 3 | [ch03_nlp_foundations.ipynb](notebooks/ch03_nlp_foundations.ipynb) | NLP Foundations for Finance |
| 4 | [ch04_transformers_llms_financial.ipynb](notebooks/ch04_transformers_llms_financial.ipynb) | Transformers, LLMs, and Financial Language Models |
| 5 | [ch05_sentiment_signal.ipynb](notebooks/ch05_sentiment_signal.ipynb) | Sentiment Analysis and Signal Construction |
| 6 | [ch06_earnings_calls.ipynb](notebooks/ch06_earnings_calls.ipynb) | Earnings Calls and Corporate Disclosure |
| 7 | [ch07_central_bank_language.ipynb](notebooks/ch07_central_bank_language.ipynb) | Central Bank Language and Macro Signals |
| 8 | [ch08_social_media_alt_data.ipynb](notebooks/ch08_social_media_alt_data.ipynb) | Social Media and Alternative Text Data |
| 9 | [ch09_entity_extraction_kg.ipynb](notebooks/ch09_entity_extraction_kg.ipynb) | Entity Extraction and Financial Knowledge Graphs |
| 10 | [ch10_regime_detection.ipynb](notebooks/ch10_regime_detection.ipynb) | Market Regime Detection |
| 11 | [ch11_backtesting_evaluation.ipynb](notebooks/ch11_backtesting_evaluation.ipynb) | Backtesting and Evaluation |
| 12 | [ch12_deployment.ipynb](notebooks/ch12_deployment.ipynb) | Deployment and Production Systems |
| 13 | [ch13_risk_ethics.ipynb](notebooks/ch13_risk_ethics.ipynb) | Risk, Ethics, and the Limits of Financial NLP |

## Quick Start

### Local Setup

```bash
git clone https://github.com/jonx0037/applied-nlp-finance.git
cd applied-nlp-finance
pip install -e ".[dev,notebooks]"
```

### Docker Setup

```bash
git clone https://github.com/jonx0037/applied-nlp-finance.git
cd applied-nlp-finance
docker compose up
```

This starts a Jupyter notebook server and a PostgreSQL instance with pgvector. Access Jupyter at `http://localhost:8888`.

## Data

Some datasets are included in `data/sample/` for immediate use. Larger datasets require API keys or manual download. See [`data/README.md`](data/README.md) for per-chapter data acquisition instructions.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for guidelines on contributing to this repository.

## License

- **Code:** MIT License
- **Manuscript:** CC BY-NC 4.0

## Buy the Book

*[Link to publisher page — coming soon]*
