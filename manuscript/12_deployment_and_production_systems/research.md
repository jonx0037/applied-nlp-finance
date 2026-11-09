# Chapter 12 — Deployment and Production Systems — Annotated Bibliography

**Purpose:** This chapter closes the gap between research notebook and production pipeline. It covers architecture patterns (batch vs. streaming), model serving with FastAPI, vector databases for semantic search, RAG patterns for financial Q&A, model drift detection, cloud deployment, and monitoring. The Docker setup from the companion repo is extended into a full production architecture.

**What this chapter needs from its sources:**
- RAG architecture (original paper + comprehensive survey + financial application)
- Model drift detection methodology (concept drift, distribution shift, NLP-specific)
- Technical debt and MLOps frameworks for production ML
- Vector database selection and embedding model benchmarking
- Batch vs. streaming architecture patterns for financial NLP
- Financial-specific RAG evaluation and hallucination reduction

**Citation format:** Chicago (Notes and Bibliography), 17th edition.

**Note on source types:** This chapter draws more heavily from engineering documentation, industry research, and systems papers than from traditional finance journals. The sources are a mix of peer-reviewed ML papers (NeurIPS, EMNLP), engineering working papers, and technical benchmarks. This reflects the chapter's practitioner-engineering orientation.

---

## 1. Architecture Patterns: Batch vs. Streaming

### 1.1 Contextual: Technical Debt in ML Systems

**Sculley, D., Gary Holt, Daniel Golovin, Eugene Davydov, Todd Phillips, Dietmar Ebner, Vinay Chaudhary, Michael Young, Jean-François Crespo, and Dan Dennison. "Hidden Technical Debt in Machine Learning Systems." In *Advances in Neural Information Processing Systems 28 (NeurIPS 2015)*, 2503–2511. Montreal, QC, 2015.**

- URL: `https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems`
- **Type:** Peer-reviewed conference paper (NeurIPS). Google Research.
- **Summary:** Argues that ML systems accumulate massive ongoing maintenance costs beyond the initial model development. Identifies ML-specific risk factors: boundary erosion, entanglement, hidden feedback loops, undeclared consumers, data dependencies, configuration debt, changes in the external world, and system-level anti-patterns. The famous "only a small fraction of real-world ML systems is composed of the ML code" finding — the surrounding infrastructure (data collection, verification, feature extraction, monitoring, serving) dominates.
- **Relevance:** *Section 1 (Architecture) and entire chapter.* The foundational reference for why production NLP is *primarily an engineering problem*, not a modeling problem. Every architectural choice in this chapter (batch vs. streaming, model versioning, monitoring, drift detection) addresses a form of technical debt identified by Sculley et al.
- **How to use:** Open the chapter with Sculley's framework. The "ML code is a tiny fraction" diagram is iconic and immediately communicates the chapter's message: building a good sentiment model (Chapters 3–4) is necessary but not sufficient for production value.
- Status: `[ ] Unverified`

---

## 2. Model Serving with FastAPI

*FastAPI model serving is primarily documented through technical documentation rather than academic papers. The companion code (`src/`) provides the reference implementation.*

*See Research Gaps for potential academic references on NLP model serving architectures.*

---

## 3. Vector Databases for Financial Document Search

### 3.1 Foundational: Financial Embedding Benchmark

**Tang, Yixuan, and Yi Yang. "FinMTEB: Finance Massive Text Embedding Benchmark." In *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, 3143–3164. 2025.**

- URL: `https://arxiv.org/abs/2502.10990`
- **Type:** Peer-reviewed conference paper (EMNLP).
- **Summary:** Introduces FinMTEB, a financial counterpart to the general-purpose MTEB benchmark, comprising 64 datasets across seven tasks (classification, clustering, retrieval, pair-classification, reranking, STS). Key finding: *performance of general-purpose embedding models on MTEB is not correlated with their performance on FinMTEB*, demonstrating that general models don't translate well to finance. Domain characteristics significantly impact performance (domain effect = 56.82 vs. model effect = 4.17 in classification tasks).
- **Relevance:** *Section 3 (Vector Databases — Embedding Selection).* The single most important finding for readers choosing embedding models: general-purpose MTEB rankings are *misleading* for financial retrieval. Readers must evaluate on FinMTEB or create their own financial retrieval benchmarks. This directly affects vector database performance because the embedding model determines retrieval quality.
- **How to use:** Central to the embedding model selection discussion. The uncorrelated general vs. financial performance finding is the chapter's strongest argument for domain-specific evaluation. Present FinMTEB as the benchmark readers should use, not general MTEB leaderboards.
- Status: `[ ] Unverified`

---

## 4. RAG Patterns for Financial Q&A

### 4.1 Foundational: RAG Original Paper

**Lewis, Patrick, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, et al. "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." In *Advances in Neural Information Processing Systems 33 (NeurIPS 2020)*, 9459–9474. Virtual, 2020.**

- URL: `https://arxiv.org/abs/2005.11401`
- **Type:** Peer-reviewed conference paper (NeurIPS).
- **Summary:** Introduces RAG — models combining pre-trained parametric memory (LLM) with non-parametric memory (document retrieval) for language generation. RAG models generate more specific, diverse, and factual language than parametric-only baselines. Provides the foundational architecture: query → retrieve relevant documents → generate answer conditioned on retrieved context.
- **Relevance:** *Section 4 (RAG Patterns).* The foundational reference for RAG architecture. Every financial RAG system the chapter discusses builds on this architecture.
- **How to use:** Cite as the origin of RAG. Present the core architecture (retriever + generator), then show how financial RAG adapts it: the retriever searches over 10-K filings, earnings transcripts, and analyst reports; the generator answers financial questions grounded in retrieved documents.
- Status: `[ ] Unverified`

---

### 4.2 Survey: RAG Architectures (Naive, Advanced, Modular)

**Gao, Yunfan, Yun Xiong, Xinyu Gao, Kangxiang Jia, Jinliu Pan, Yuxi Bi, Yi Dai, Jiawei Sun, Meng Wang, and Haofen Wang. "Retrieval-Augmented Generation for Large Language Models: A Survey." arXiv preprint, arXiv:2312.10997, March 2024.**

- URL: `https://arxiv.org/abs/2312.10997`
- **Type:** Preprint (comprehensive survey).
- **Summary:** Surveys the progression from Naive RAG (simple retrieve-then-generate) through Advanced RAG (pre-retrieval optimization, post-retrieval reranking, iterative retrieval) to Modular RAG (composable retrieval/generation/augmentation modules). Covers evaluation frameworks (context relevance, answer faithfulness, answer relevance) and benchmarks.
- **Relevance:** *Section 4 (RAG Patterns).* The most comprehensive RAG survey available. Provides the Naive → Advanced → Modular taxonomy the chapter can adopt. The evaluation framework (faithfulness, relevance, context precision) is directly applicable to financial RAG evaluation.
- **How to use:** Use the three-tier taxonomy to structure Section 4. Naive RAG suffices for simple document Q&A; Advanced RAG (with reranking and iterative retrieval) is needed for complex financial questions spanning multiple documents; Modular RAG enables specialized financial pipelines (e.g., separate retrievers for filings vs. news vs. transcripts).
- Status: `[ ] Unverified`

---

### 4.3 Empirical: Financial RAG Evaluation

**Gupta, Sanjay, Asif Ekbal, and Pushpak Bhattacharyya. "Evaluating Retrieval-Augmented Generation Models for Financial Report Question and Answering." *Applied Sciences* 14, no. 20 (October 2024): 9318.**

- DOI: `10.3390/app14209318`
- **Type:** Peer-reviewed journal article.
- **Summary:** Evaluates RAG applied to financial annual reports, testing retrieval quality and answer accuracy for financial question answering. Addresses domain-specific challenges: long documents, tabular data embedded in text, numerical reasoning requirements, and the need for verifiable source attribution.
- **Relevance:** *Section 4 (Financial RAG).* The primary reference for RAG applied specifically to financial documents. The domain-specific challenges (long filings, tables, numerical reasoning) are exactly what readers will encounter.
- **How to use:** Cite to ground the RAG discussion in financial reality. The challenges documented (table extraction, numerical reasoning, cross-document synthesis) inform the architectural choices readers must make.
- Status: `[ ] Unverified`

---

## 5. Model Drift Detection and Retraining

### 5.1 Contextual: NLP-Specific Drift Detection

**Lu, Jie, Anjin Liu, Fan Dong, Feng Gu, Joao Gama, and Guangquan Zhang. "Learning under Concept Drift: A Review." *IEEE Transactions on Knowledge and Data Engineering* 31, no. 12 (December 2019): 2346–2363.**

- DOI: `10.1109/TKDE.2018.2876857`
- **Type:** Peer-reviewed journal article (IEEE TKDE).
- **Summary:** Comprehensive review of concept drift in machine learning. Covers drift types (sudden, gradual, incremental, recurring), detection methods (statistical tests, window-based, ensemble-based), and adaptation strategies (retrain from scratch, incremental learning, ensemble rotation). Provides a taxonomy of drift handling approaches.
- **Relevance:** *Section 5 (Drift Detection).* The theoretical foundation for model drift detection. Financial language drift manifests as: (1) vocabulary evolution (new terms like "DeFi," "SPACs"), (2) sentiment recalibration (words change valence during crises), and (3) regime-dependent meaning shifts (same words carry different signal in different market environments). Each drift type requires different detection and adaptation strategies.
- **How to use:** Cite as the drift detection framework. Map their taxonomy to financial NLP: sudden drift = market crash language shift; gradual drift = evolving financial terminology; recurring drift = cyclical sentiment patterns tied to earnings seasons or FOMC cycles.
- Status: `[ ] Unverified`

---

## 6. Infrastructure: Docker and Cloud Deployment

### 6.1 Foundational: Production ML Systems

**Sculley, D., et al. "Hidden Technical Debt in Machine Learning Systems." NeurIPS 2015.**

- *(See citation above in Section 1.1)*
- **Relevance for Section 6:** The infrastructure concerns (containerization, autoscaling, cloud deployment) are all forms of the "surrounding infrastructure" that Sculley identifies as dominating real-world ML systems.
- Status: `[ ] Unverified`

---

## 7. Monitoring and Alerting

### 7.1 Methodological: ML Monitoring Framework

**Breck, Eric, Shanqing Cai, Eric Nielsen, Michael Salib, and D. Sculley. "The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction." In *Proceedings of IEEE BigData 2017*, 1123–1132. Boston, MA: IEEE, December 2017.**

- DOI: `10.1109/BigData.2017.8258038`
- **Type:** Peer-reviewed conference paper (IEEE BigData). Google Research.
- **Summary:** Proposes a rubric of 28 tests for evaluating ML system production readiness across four categories: (1) data tests (feature expectations, data pipeline integrity), (2) model tests (model staleness, numerical stability), (3) ML infrastructure tests (training reproducibility, model specification), and (4) monitoring tests (prediction quality, staleness detection). Assigns points for each test, producing an "ML Test Score."
- **Relevance:** *Section 7 (Monitoring and Alerting).* Provides a concrete, checklist-based framework for evaluating whether an NLP system is production-ready. The 28-test rubric can be adapted to financial NLP: data tests → text input quality (missing fields, encoding errors, timestamp validity); model tests → sentiment score distribution stability; monitoring tests → prediction quality alerts.
- **How to use:** Cite as the production readiness framework. Adapt the 28-test rubric for financial NLP pipelines. This gives readers a concrete "are we ready?" checklist before deploying sentiment models.
- Status: `[ ] Unverified`

---

## Cross-Chapter References

| Source | Ch 12 Section | Also Relevant To |
|--------|-------------|------------------|
| Sculley et al. (2015) | Sec 1, 6 (Technical Debt) | General ML engineering |
| Lewis et al. (2020) RAG | Sec 4 (RAG Foundation) | Ch 4 (LLM Workflows) |
| Gao et al. (2024) RAG Survey | Sec 4 (RAG Taxonomy) | Ch 4 (LLM Workflows) |
| Tang & Yang (2025) FinMTEB | Sec 3 (Embedding Benchmark) | Ch 4 (Model Selection) |
| Gupta et al. (2024) | Sec 4 (Financial RAG) | Ch 6 (Document Analysis) |
| Lu et al. (2019) | Sec 5 (Drift Detection) | Ch 11 (Evaluation) |
| Breck et al. (2017) | Sec 7 (Monitoring Rubric) | Ch 11 (Evaluation) |

---

## Research Gaps

The following areas need additional sourcing:

- [ ] **FastAPI NLP model serving architecture** — Need references on FastAPI-specific patterns for serving NLP models in production: async inference, model loading strategies, request batching, and model versioning. FastAPI documentation provides technical guidance, but an academic or industry paper comparing serving frameworks (FastAPI vs. TorchServe vs. Triton) for NLP workloads would strengthen the section.
- [ ] **pgvector vs. Pinecone vs. Weaviate vs. Qdrant comparison** — Need a formal benchmark (not just blog posts) comparing vector database performance for financial document retrieval. VectorDBBench provides open benchmarks but may not include financial-domain evaluation. Consider citing alongside FinMTEB for a complete retrieval stack assessment.
- [ ] **AWS SageMaker and GCP Vertex AI for NLP deployment** — Need references documenting best practices for deploying transformer-based NLP models on these cloud platforms. AWS and GCP documentation provides technical detail, but academic case studies or industry reports would be more citable.
- [ ] **Docker multi-stage builds for NLP models** — Need references on container optimization for NLP workloads (GPU support, model weight caching, image size reduction). This is an engineering best practice that lacks dedicated academic treatment.
- [ ] **Population Stability Index (PSI) for NLP drift** — Need a reference specifically applying PSI to NLP feature distributions (e.g., monitoring sentiment score distributions over time). PSI is well-documented for tabular features but less so for text-derived features.
- [ ] **Financial RAG with tabular data** — Need a paper addressing the specific challenge of RAG over financial documents that contain both text and tables (10-K filings, earnings reports). Standard RAG chunking strategies fail on documents with interleaved text and tables.
- [ ] **Prometheus/Grafana monitoring for ML pipelines** — Need references on monitoring stack design for production ML/NLP systems. The combination of prediction quality metrics, data quality alerts, and infrastructure metrics is well-practiced but under-documented in academic literature.
- [ ] **Batch vs. streaming NLP for finance specifically** — Need an academic or industry paper documenting the architectural decision between batch and streaming NLP pipelines for financial text, with specific latency and throughput benchmarks. The conceptual guidance is available but financial-specific benchmarks are scarce.

---

## Verification Priority

Start SMU Library verification with these sources first:

1. **Sculley et al. (2015)** — Hidden technical debt (NeurIPS — foundational)
2. **Lewis et al. (2020)** — RAG original paper (NeurIPS — foundational)
3. **Gao et al. (2024)** — RAG survey (comprehensive reference)
4. **Tang & Yang (2025)** — FinMTEB embedding benchmark (EMNLP)
5. **Breck et al. (2017)** — ML Test Score (IEEE BigData)
6. **Lu et al. (2019)** — Concept drift review (IEEE TKDE)
7. **Gupta et al. (2024)** — Financial RAG evaluation

---

*Research compiled April 2026. All citations require manual verification through SMU Library before inclusion in final manuscript.*
