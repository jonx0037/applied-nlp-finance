# Chapter 9 — Entity Extraction and Knowledge Graphs: Foundations Exercises

## Exercise 9.1: Financial NER Pipeline
Build a Named Entity Recognition pipeline that extracts company names, person names, monetary amounts, and dates from SEC filings. Evaluate precision and recall against a manually annotated set of 20 paragraphs.

## Exercise 9.2: Knowledge Graph Construction
Using entities extracted from a set of 10-K filings, construct a knowledge graph with company, person, and product nodes. Add edges for relationships such as "supplies_to", "competes_with", and "has_executive".

## Exercise 9.3: Supply Chain Tracing
Starting from a single company node in your knowledge graph, implement a breadth-first traversal to identify its supply chain network up to depth 3. Visualize the resulting subgraph.
