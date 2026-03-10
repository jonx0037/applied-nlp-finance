# Chapter 4 — Transformers, LLMs, and Financial Language Models

This chapter provides deep treatment of transformer architecture and modern LLM workflows in the financial domain. It covers domain-adapted models like FinBERT and BloombergGPT, fine-tuning strategies, and the expanding role of LLM-based workflows including zero-shot classification, structured extraction, and agentic pipelines. The chapter equips readers to choose the right model for each task.

## BERT Architecture Review

Brief review of the BERT architecture, assuming ML literacy, focused on aspects most relevant to financial fine-tuning. The attention mechanism, positional encoding, and masked language modeling objective are covered with emphasis on what they imply for financial text understanding.

## Why General-Purpose BERT Underperforms on Financial Text

Analyze the vocabulary mismatch, distributional differences, and domain-specific semantics that degrade general BERT performance on financial tasks. Financial language uses common English words with specialized meanings, creating a systematic bias in models trained on general corpora.

## FinBERT and Domain-Adapted Models

Deep dive into FinBERT's architecture, training corpus, and fine-tuning strategy, alongside BloombergGPT, FinGPT, and Llama-finance variants. Each model represents a different approach to domain adaptation, from continued pretraining to instruction tuning.

## Fine-Tuning on Custom Financial Corpora

Cover data requirements, training recipes, hyperparameter selection, and evaluation methodology for domain-specific fine-tuning. Practical guidance on dataset size thresholds, learning rate schedules, and early stopping criteria specific to financial text tasks.

## LLM-Based Financial Workflows

Explore zero-shot and few-shot prompting, structured extraction via JSON-mode and function calling, prompt engineering for financial tasks, LLM-as-judge labeling, and agentic multi-step analysis pipelines. The LLM workflow paradigm has expanded the scope of financial NLP far beyond classification.

## Cost/Latency/Accuracy Tradeoff Matrix

Compare fine-tuned FinBERT, prompted GPT-4/Claude, and distilled models across the dimensions that matter for production deployment. Include concrete cost estimates for processing typical financial document volumes at each quality tier.

## Choosing the Right Model for the Task

Framework for deciding when to fine-tune, when to prompt, and when to chain models based on task requirements and constraints. The decision tree accounts for latency tolerance, accuracy requirements, data availability, and budget.
