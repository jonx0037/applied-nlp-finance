# Chapter 10 — Market Regime Detection

This chapter presents the author's primary research contribution — deep treatment of sentiment-based market regime detection. It builds on the data pipelines from Chapters 6-9 to construct a cross-asset sentiment regime detector, combining text-derived features with price/volume data. The chapter includes real-world case studies from COVID, the 2022 rate hiking cycle, and crypto contagion events.

## What Is a Market Regime?

Define and classify regimes — trend, volatility, correlation, and narrative regimes — establishing a taxonomy for the chapter. A market regime is a persistent statistical state of the market characterized by stable distributional properties, and recognizing when regimes shift is one of the most valuable capabilities in systematic trading.

## Existing Quantitative Regime Detection Methods

Survey HMMs, Markov Switching models, and clustering approaches as the quantitative baseline. These price/volume-based methods detect regimes from return distributions, but they are inherently reactive — they can only identify a regime after observing enough data from within it.

## Why Sentiment-Based Regime Detection Is Complementary

Argue that text-derived regime features capture information not present in price/volume data, making them complementary rather than redundant. Narrative shifts often precede statistical regime changes, giving text-based detectors the potential for earlier identification of transitions.

## Cross-Asset Sentiment Regime Detector: Architecture

Present the full architecture of the sentiment-based regime detector, from raw text inputs to regime labels. The architecture integrates earnings call sentiment, central bank tone, social media volume, and entity graph topology into a unified regime classification framework.

## Implementation Walkthrough

Step through the implementation from raw text to regime label, referencing the earnings call, central bank, social media, and entity extraction pipelines from Chapters 6-9. Each pipeline contributes a distinct feature set, and the walkthrough shows how they are aligned temporally and combined for regime inference.

## Multi-Modal Regime Features

Combine text-derived sentiment with price/volume regime indicators and entity-graph topology shifts for richer regime characterization. Multi-modal features capture dimensions of market state that no single data modality can represent alone.

## Evaluating Regime Detectors

Assess stability, transition detection accuracy, and forward return predictiveness of regime labels. Regime detection evaluation requires specialized metrics because standard classification metrics ignore the temporal structure and transition dynamics that make regimes useful.

## Case Studies

Analyze real-world regime transitions: COVID market crash, 2022 rate hiking cycle, and crypto contagion events. Each case study illustrates how text-derived features signaled regime changes and whether the sentiment regime detector identified transitions earlier than price-based methods alone.
