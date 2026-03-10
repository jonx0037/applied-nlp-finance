# Chapter 11 — Backtesting and Evaluation

This chapter teaches rigorous evaluation methodology specific to NLP-based trading strategies. It addresses the backtest overfitting problem, validation approaches suited to time-series data, financial performance metrics, and common failure modes. The chapter is unapologetically honest about where NLP-driven strategies can go wrong.

## The Backtest Overfitting Problem

Explain why NLP-based strategies are especially susceptible to overfitting and how the proliferation of text features amplifies multiple testing concerns. The combinatorial explosion of possible text features — different tokenizations, aggregation windows, sentiment models, and normalization schemes — creates a massive multiple testing problem.

## Validation Approaches for Time-Series

Compare walk-forward validation, expanding window, and purged cross-validation methods for text-based strategy evaluation. Standard k-fold cross-validation is inappropriate for time-series data, and purged cross-validation addresses the autocorrelation that makes naive splits leak information.

## Financial Performance Metrics

Cover Sharpe ratio, Calmar ratio, information ratio, and maximum drawdown in the context of NLP signal evaluation. Each metric captures a different dimension of strategy quality, and no single metric tells the full story of a text-driven strategy's viability.

## NLP-Specific Evaluation

Develop evaluation frameworks for assessing whether a model genuinely "understands" financial language or is exploiting spurious correlations. Ablation studies, feature importance analysis, and out-of-domain testing help distinguish genuine linguistic signal from statistical artifacts.

## Benchmark Construction

Design fair baselines for NLP strategies, including text-agnostic benchmarks and dictionary-based sentiment benchmarks. A text-based strategy must demonstrably outperform sensible baselines — including a simple Loughran-McDonald dictionary approach — to justify its complexity.

## Transaction Costs, Slippage, and Market Impact

Model realistic execution costs for text-driven strategies, including the unique timing challenges of event-driven signals. Text signals often cluster around events when liquidity conditions are worst, making execution cost modeling especially important for realistic evaluation.

## Common Failure Modes

Catalog stale data, survivorship bias, data snooping, and other pitfalls with concrete examples of how they manifest in NLP pipelines. Each failure mode is illustrated with a specific example of how it can corrupt backtest results in text-based strategies.
