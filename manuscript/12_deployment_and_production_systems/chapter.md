# Chapter 12 — Deployment and Production Systems

This chapter closes the gap between research notebook and production pipeline. It covers architecture patterns for batch and streaming NLP, model serving with FastAPI, vector databases for semantic search, RAG patterns, and infrastructure concerns including monitoring and drift detection. The Docker setup from the companion repo is extended into a full production architecture.

## Architecture Patterns: Batch vs. Streaming

Compare batch and streaming NLP pipeline architectures, with guidance on when each is appropriate for financial applications. Batch processing suits scheduled filings and end-of-day analysis, while streaming is necessary for real-time news and social media sentiment.

## Model Serving with FastAPI

Build a FastAPI service for NLP model inference, addressing latency, concurrency, and model versioning in production. The service exposes sentiment scoring, entity extraction, and classification endpoints with proper request validation, error handling, and response schemas.

## Vector Databases for Financial Document Search

Deploy pgvector, Pinecone, or Weaviate for semantic search over financial documents, with indexing and query optimization strategies. Semantic search enables analysts to find conceptually similar documents across large corpora, going beyond keyword matching to meaning-based retrieval.

## RAG Patterns for Financial Q&A

Implement Retrieval-Augmented Generation patterns for financial question answering, combining document retrieval with language model generation. RAG architectures ground LLM responses in actual financial documents, reducing hallucination and providing verifiable source attribution.

## Model Drift Detection and Retraining

Monitor model performance over time and build automated triggers for retraining when financial language distributions shift. Financial language evolves — new terminology emerges, sentiment calibration drifts, and market regimes change the meaning of familiar phrases.

## Infrastructure: Docker and Cloud Deployment

Extend the companion repo's Docker setup to cloud deployment on AWS SageMaker and GCP Vertex AI. Production deployment requires container orchestration, autoscaling, and integration with cloud-native monitoring and logging services.

## Monitoring and Alerting

Build model performance dashboards and data quality alerts to maintain production NLP systems. Monitoring covers input data quality, model prediction distributions, latency metrics, and downstream signal quality — any of which can degrade silently without proper alerting.
