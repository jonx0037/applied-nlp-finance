# Chapter 8 — Social Media and Alternative Text Data

This chapter handles noisier, higher-frequency, and legally complex text sources. It uses Reddit's WallStreetBets as a case study in separating signal from noise, covers bot detection and data quality filtering, and explores social media's role in crypto markets. The chapter honestly addresses the challenges unique to alternative data.

## Reddit WallStreetBets: Signal vs. Noise

Use WSB as a case study for extracting tradeable signal from high-noise environments, including manipulation detection. The GameStop saga demonstrated that retail social media can drive real market impact, but also that distinguishing organic sentiment from coordinated campaigns is extremely difficult.

## StockTwits and Microblogging Sentiment

Analyze high-frequency social sentiment from microblogging platforms, covering sampling strategies and aggregation methods. StockTwits provides self-labeled bullish/bearish tags that simplify sentiment extraction but introduce self-selection bias.

## News Momentum vs. Social Media Momentum

Compare and contrast traditional news sentiment with social media sentiment, examining correlation structure and divergence events. When news and social sentiment diverge, the divergence itself can be a powerful signal about information asymmetry or speculative excess.

## Bot Detection and Data Quality

Build filtering pipelines to detect bot activity, spam, and coordinated inauthentic behavior that corrupts sentiment signals. Account age, posting frequency, linguistic patterns, and network analysis all contribute to bot detection, and failing to filter bots can completely corrupt sentiment signals.

## Short Squeeze Detection

Identify unusual language patterns and activity spikes that may signal coordinated trading activity or short squeeze setups. Volume anomalies in text data — unusual mention frequency, new account participation, and specific linguistic patterns — often precede short squeeze events.

## Crypto Social Media Channels

Cover Discord, Telegram, and X as primary communication channels for crypto markets, with their unique data access challenges. Crypto markets are social-media-native in a way that traditional equity markets are not, making social text analysis both more impactful and more noisy.
