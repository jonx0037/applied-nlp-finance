# Preface

## Why This Book

Financial markets are fundamentally narrative-driven systems. Price and volume data capture *what happened*; text data captures *why*. This book teaches you how to build, evaluate, and deploy NLP systems that systematically extract signal from financial language at scale.

The author came to NLP through financial markets and humanities — not the other way around. That perspective shapes every chapter: we treat language not as a data type to be processed, but as the primary medium through which market participants form and communicate beliefs.

## How to Read This Book

This book serves four distinct audiences, each with a recommended reading path:

### Quantitative Researchers and Data Scientists
Start at Chapter 1 and read linearly. The book builds concepts progressively, with each chapter assuming knowledge from prior ones.

### ML Engineers at Hedge Funds, Fintechs, or Trading Desks
You likely have strong ML foundations. Skim Chapters 1–3 for domain context, then dive deep starting at Chapter 4. The production-oriented material in Chapters 11–12 will be particularly relevant.

### Sophisticated Independent Traders
Focus on Chapters 1, 5, 6, 10, and 11 as a targeted track. These chapters cover the conceptual foundation, signal construction, earnings analysis, regime detection, and backtesting — the core loop for building a text-driven trading system.

### Graduate Students
Start at Chapter 1 and read linearly. The tiered exercise system provides scaffolding: begin with Foundations exercises to build implementation confidence, then progress to Intermediate and Advanced as your skills develop.

## The Companion Repository

Every chapter has a corresponding Jupyter notebook in the companion GitHub repository at `github.com/jonx0037/applied-nlp-finance`. The repository contains all source code, utility modules, and sample datasets needed to reproduce the examples in this book.

Setup is straightforward:
```bash
git clone https://github.com/jonx0037/applied-nlp-finance.git
cd applied-nlp-finance
pip install -e ".[notebooks]"
```

## Tiered Exercise System

Each chapter includes exercises at three levels:

- **Foundations:** Core implementation tasks that reinforce the chapter's key concepts. Every reader should complete these.
- **Intermediate:** Extensions and variations that deepen understanding and encourage experimentation.
- **Advanced:** Open-ended research problems suitable for capstone projects, independent study, or production prototyping.

Exercises are located in the `exercises/` directory, organized by chapter.

## Acknowledgments

*[TBD]*
