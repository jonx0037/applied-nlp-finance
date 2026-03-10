# Chapter 5 — Sentiment Analysis and Signal Construction

This chapter bridges the gap between model output and tradeable signal. It covers temporal aggregation, signal normalization, cross-asset sentiment effects, and multi-modal feature fusion. The focus is on production-grade signal engineering that avoids common pitfalls like look-ahead bias.

## Raw Sentiment Scores vs. Aggregated Indices

Distinguish between point-in-time model outputs and the aggregated sentiment indices that trading systems actually consume. A single document's sentiment score is rarely useful in isolation; the value lies in how scores are combined across documents, sources, and time.

## Temporal Aggregation Strategies

Compare rolling windows, exponential weighting, and event-time vs. calendar-time aggregation approaches. The choice of aggregation method can dramatically affect signal behavior, from smoothness to responsiveness to regime changes.

## Cross-Asset Sentiment Effects

Examine how equity sentiment bleeds into credit, volatility, and commodity markets, creating cross-asset trading opportunities. Sentiment contagion follows economic linkages, and mapping these linkages is essential for portfolio-level signal construction.

## Signal Normalization and Regime Conditioning

Cover z-scoring, percentile ranking, and regime-conditional normalization to ensure signals remain comparable across market environments. A sentiment signal that is "bullish" in a crisis has a very different meaning than the same score in a bull market.

## Multi-Modal Feature Fusion

Combine text-derived features with tabular data from the same source — sentiment alongside financial ratios, language tone with earnings surprise magnitude. The most powerful signals emerge from combining what is said with what the numbers show.

## Avoiding Look-Ahead Bias

Detail the specific mechanisms by which look-ahead bias enters text-based feature construction and how to prevent them. Publication timestamps, processing delays, and revision schedules all create opportunities for bias to contaminate signals.
