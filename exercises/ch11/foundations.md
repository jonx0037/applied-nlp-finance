# Chapter 11 — Backtesting NLP Strategies: Foundations Exercises

## Exercise 11.1: Walk-Forward Backtest
Implement a walk-forward backtesting framework with expanding or rolling training windows. Apply it to a sentiment-based signal and report out-of-sample performance across each fold.

## Exercise 11.2: Benchmark Construction
Construct three benchmark strategies for comparing against NLP signals: (a) buy-and-hold, (b) a momentum-based signal, and (c) a random signal with matched turnover. Compute Sharpe ratio, max drawdown, and turnover for each.

## Exercise 11.3: Look-Ahead Bias Audit
Write a systematic audit function that checks a backtest implementation for common biases: look-ahead bias in features, survivorship bias in the universe, and timestamp alignment errors. Apply it to a sample backtest.
