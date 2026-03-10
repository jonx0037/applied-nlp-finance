# Chapter 9 — Entity Extraction and Financial Knowledge Graphs

This chapter moves beyond bag-of-sentiment to structured relational understanding of financial text. It covers financial NER, relation extraction, knowledge graph construction from SEC filings and earnings calls, and temporal knowledge graphs that track evolving relationships. The chapter bridges text analysis with graph-based analytics.

## Named Entity Recognition for Financial Entities

Adapt NER for companies, executives, instruments, and regulatory bodies, addressing domain-specific challenges like ticker disambiguation. Financial NER requires recognizing entities that general-purpose models miss — ticker symbols, CUSIP identifiers, regulatory filing codes, and financial instrument names.

## Domain-Specific NER Challenges

Handle ticker symbols as common words, subsidiary disambiguation, and cross-referencing to identifiers (CUSIPs, LEIs). "APPLE" might be a fruit or a company, "GS" might be Goldman Sachs or a generic abbreviation, and resolving these ambiguities requires financial context.

## Relation Extraction from Financial Text

Extract who-owns-whom, supply chain dependencies, and executive-to-company mappings from filings and news. Relation extraction transforms flat text into structured knowledge, enabling graph-based analysis of corporate ecosystems.

## Building Knowledge Graphs from Financial Sources

Construct knowledge graphs from SEC filings, earnings calls, and news articles using extracted entities and relations. The knowledge graph becomes a queryable representation of the financial world as described in text, enabling questions that no single document can answer.

## Temporal Knowledge Graphs

Track how relationships evolve over time — board changes, M&A activity, supply chain shifts — and use temporal dynamics as features. Financial relationships are not static, and the rate and direction of change in graph topology carries signal about corporate strategy and risk.

## Use Cases: Supply Chain Risk, Contagion, Activism

Apply knowledge graphs to practical financial problems: supply chain risk propagation, contagion modeling, activism detection, and competitive landscape mapping. Each use case demonstrates how relational structure extracted from text enables analysis impossible with sentiment alone.

## Graph-Based Features for Downstream Models

Extract centrality metrics, community detection results, and path-based signals from financial knowledge graphs for use in predictive models. Graph topology features — degree centrality, betweenness, clustering coefficients — complement text-derived sentiment features in downstream models.

## Multi-Modal Graph Enrichment

Link text-extracted relationships with structured financial data — ownership percentages, revenue exposure, geographic footprint. The richest knowledge graphs combine what text says about relationships with what structured data quantifies about them.
