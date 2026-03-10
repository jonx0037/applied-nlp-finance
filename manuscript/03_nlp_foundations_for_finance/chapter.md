# Chapter 3 — NLP Foundations for Finance

This chapter establishes the NLP baseline so readers understand what transformers improved upon. It covers classical text processing methods — tokenization, bag-of-words, TF-IDF, word embeddings — and their specific applications and limitations in financial contexts. The chapter makes the case for when classical NLP remains the right choice.

## Tokenization for Financial Text

Examine why tokenization decisions matter more in financial text — ticker symbols, camelCase terms, numerical expressions, and domain-specific abbreviations require special handling. A tokenizer that splits "10-K" into three tokens or fails to recognize "AAPL" as a named entity will degrade every downstream task.

## Bag-of-Words, TF-IDF, and Financial Lexicons

Cover traditional document representations and introduce the Loughran-McDonald dictionary as the foundational financial sentiment lexicon. The Loughran-McDonald dictionary corrected Harvard General Inquirer's misclassification of common financial terms, and understanding this correction is essential context for financial sentiment work.

## Word Embeddings in Financial Context

Evaluate Word2Vec, GloVe, and fastText on financial corpora, highlighting where general-purpose embeddings diverge from financial meaning. Words like "liability," "capital," and "default" have domain-specific meanings that general embeddings fail to capture.

## Classical Sentiment Approaches

Survey VADER, TextBlob, and rule-based sentiment systems, benchmarking them against labeled financial datasets (FiQA, SEntFiN). These baselines establish the performance floor that transformer-based approaches must demonstrably exceed to justify their additional complexity.

## When Classical NLP Is Still the Right Choice

Make the pragmatic case for classical methods when latency, interpretability, or cost constraints outweigh the accuracy gains of transformer-based approaches. In many production settings, a well-tuned TF-IDF model with domain-specific features outperforms a poorly prompted LLM.
