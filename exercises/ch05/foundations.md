# Chapter 5 — From Text to Trading Signal: Foundations Exercises

## Exercise 5.1: Sentiment Signal Construction
Build a daily sentiment signal from raw article-level sentiment scores. Implement temporal aggregation (equal-weighted and exponentially decayed) and align the signal to market trading days.

## Exercise 5.2: Signal Normalization
Implement rolling z-score normalization for a sentiment signal. Experiment with window lengths of 20, 60, and 120 days and visualize how each affects signal behavior during volatile periods.

## Exercise 5.3: Look-Ahead Bias Check
Write a function that detects potential look-ahead bias in a signal DataFrame by verifying that no future information is used at each timestamp. Test it on both a clean signal and one with an intentionally introduced bias.
