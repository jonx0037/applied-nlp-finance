# Chapter 2 — Text Data Acquisition

This chapter provides a comprehensive, honest guide to sourcing financial text data. It covers the major sources — SEC EDGAR, financial news APIs, earnings call transcripts, central bank communications, and social media — with practical details on access methods, rate limits, and legal considerations. The chapter concludes with building a reliable data pipeline with deduplication and provenance tracking.

## SEC EDGAR: Structured Corporate Filings

Cover 8-K, 10-K, 10-Q, and proxy filing access — structure, full-text search, rate limits, and the EDGAR API. EDGAR is the single most important free source of structured financial text, and understanding its filing hierarchy is essential for any financial NLP pipeline.

## Financial News APIs

Survey Bloomberg, Refinitiv, NewsAPI, GDELT, and Alpaca News — comparing coverage, latency, cost, and data quality. Each API occupies a different point in the cost-coverage tradeoff, and the right choice depends on research budget and latency requirements.

## Earnings Call Transcripts

Evaluate Seeking Alpha, Motley Fool, and vendor APIs as sources for earnings call text, including structured vs. unstructured transcript formats. Transcript quality varies significantly across providers, and the choice of source affects downstream NLP accuracy.

## Central Bank Communications

Map official sources and structured archives for Fed, ECB, BoJ, and BoE communications, including FOMC statements, minutes, and press conference transcripts. Central bank text is among the most market-moving language in finance, and reliable sourcing is non-negotiable.

## Social Media Sources

Cover Reddit (PRAW), Twitter/X API tiers, and StockTwits — including API limitations, data quality concerns, and high-frequency sampling strategies. Social media is the noisiest but highest-frequency financial text source, requiring careful filtering before analysis.

## Web Scraping Ethics and Legal Considerations

Address `robots.txt` compliance, Terms of Service considerations, and data licensing frameworks relevant to financial text data. Responsible data acquisition is both an ethical obligation and a legal necessity for any production system.

## Building a Reliable Data Pipeline

Design a pipeline with deduplication, provenance tracking, and timestamp normalization to ensure data integrity across sources. A data pipeline is only as good as its weakest quality control mechanism.

## Data Versioning Strategy

Evaluate DVC and git-lfs for dataset snapshots, and establish `data/README.md` as a provenance guide for reproducibility. Versioned datasets are essential for reproducing experiments and tracking the lineage of text-derived features.
