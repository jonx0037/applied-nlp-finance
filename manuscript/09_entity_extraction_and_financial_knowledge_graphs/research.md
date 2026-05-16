# Chapter 9 — Entity Extraction and Financial Knowledge Graphs — Annotated Bibliography

**Purpose:** This chapter moves beyond bag-of-sentiment to structured relational understanding of financial text. It covers financial NER, relation extraction, knowledge graph construction from SEC filings and earnings calls, temporal knowledge graphs, and graph-based features for downstream models. The chapter bridges NLP with graph analytics.

**What this chapter needs from its sources:**
- Financial NER benchmarks and domain-specific challenges (ticker disambiguation, XBRL)
- Relation extraction models for financial text (ownership, supply chain, executive-company)
- Knowledge graph construction methodology and tools
- Temporal knowledge graphs for tracking evolving financial relationships
- Graph-based features (centrality, community detection) as financial signals
- Supply chain risk, contagion modeling, and activism detection use cases
- Multi-modal graph enrichment (text + structured data)

**Citation format:** Chicago (Notes and Bibliography), 17th edition.

**Note on chapter positioning:** This is a v2 addition filling the gap between sentiment analysis (Chapter 5) and regime detection (Chapter 10). It represents an increasingly important but less mature area of financial NLP — the literature is thinner than for sentiment analysis but growing rapidly, especially with LLM-based knowledge graph construction.

---

## 1. Named Entity Recognition for Financial Entities

### 1.1 Foundational: Financial NER Benchmarks

**Loukas, Lefteris, Manos Fergadiotis, Ilias Chalkidis, Eirini Spyropoulou, Prodromos Malakasiotis, Ion Androutsopoulos, and Georgios Paliouras. "FiNER: Financial Numeric Entity Recognition for XBRL Tagging." In *Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, 4419–4431. Dublin: Association for Computational Linguistics, May 2022.**

- DOI: `10.18653/v1/2022.acl-long.303`
- **Type:** Peer-reviewed conference paper (ACL — top NLP venue).
- **Summary:** Introduces XBRL tagging as a new entity extraction task and releases FiNER-139, a dataset of 1.1 million sentences with gold XBRL tags from annual and quarterly SEC reports. Uses 139 entity types — far larger than typical NER label sets. Most annotated tokens are numeric, where the correct tag depends heavily on context. Proposes solutions including pseudo-token replacement for numeric expressions and releases SEC-BERT, a BERT model pre-trained on financial filings.
- **Relevance:** *Section 1 (Financial NER).* The most comprehensive financial NER dataset available. FiNER-139's 1.1M sentences and 139 entity types make it the go-to benchmark for financial entity extraction. The focus on *numeric* entities (revenue figures, share counts, dollar amounts) fills a gap that standard NER misses.
- **How to use:** Central to Section 1. The XBRL tagging formulation is a key insight — it frames NER not as finding company names but as linking numeric values to their semantic meaning in financial statements. SEC-BERT provides a practical model readers can use.
- **Cross-reference:** Related to Loukas et al. (2021) EDGAR-CORPUS in Chapter 2.
- Status: `[ ] Unverified`

---

**Alvarado, Julio Cesar Salinas, Karin Verspoor, and Timothy Baldwin. "Domain Adaption of Named Entity Recognition to Support Credit Risk Assessment." In *Proceedings of the 2015 Australasian Language Technology Association Workshop*, 84–90. Parramatta, Australia: ALTA, December 2015.**

- URL: `https://aclanthology.org/U15-1010/`
- **Type:** Peer-reviewed workshop paper.
- **Summary:** Early work on adapting NER for financial domain. Addresses the challenge that financial text contains entity types (financial instruments, regulatory bodies, contractual terms) absent from standard NER training data. Uses the FIN5 dataset of SEC financial agreements (54,256 words, 5 training documents).
- **Relevance:** *Section 1 (NER Benchmarks).* Provides the FIN5 benchmark reference and documents the domain-adaptation challenge for financial NER — general NER models miss financial-specific entity types.
- **How to use:** Cite as an early benchmark, then show progression to FiNER-139's scale.
- Status: `[ ] Unverified`

---

### 1.2 Methodological: LLMs for Financial NER

**Zhou, Yilun, Yulin Chen, and Lei Wang. "Financial Named Entity Recognition: How Far Can LLM Go?" In *Proceedings of the Joint Workshop of the 8th Financial Technology and Natural Language Processing and the 1st Agent AI for Scenario Planning (FinNLP-AgentScen)*, 115–122. Albuquerque, NM: Association for Computational Linguistics, 2025.**

- URL: `https://aclanthology.org/2025.finnlp-1.15/`
- **Type:** Peer-reviewed workshop paper.
- **Summary:** Evaluates nine LLMs across five financial NER benchmark datasets, examining the impact of prompt formats and prompting techniques (zero-shot, few-shot, CoT) on accuracy. Finds that LLMs show strong zero- and few-shot reasoning without task-specific supervision, though their application to financial entity extraction still lags behind fine-tuned models on some benchmarks.
- **Relevance:** *Section 1 and Section 2 (NER Challenges).* The most current assessment of LLM capabilities for financial NER. Connects the NER discussion to Chapter 4's LLM workflow paradigm.
- **How to use:** Cite for the current state of LLM-based NER. The prompt engineering findings (which formats work best for financial entities) provide practical guidance.
- Status: `[ ] Unverified`

---

## 2. Domain-Specific NER Challenges

### 2.1 Contextual: Ticker Symbol Disambiguation

The notes identify ticker disambiguation (e.g., "COST" = Costco or the word "cost," "CAT" = Caterpillar or a feline) as a key challenge. This is addressed as a sub-problem within the broader financial NER literature:

**Loukas et al. (2022)** (see above) addresses numeric entity disambiguation through context-dependent XBRL tagging.

*Additional source needed — see Research Gaps.*

---

## 3. Relation Extraction from Financial Text

### 3.1 Foundational: Financial Relation Extraction Dataset

**Sharma, Sahil, Surgan Jandial, Shuaib Ahmed, Sukhdeep Kharbanda, Tejas Vaidhya, and Balaji Krishnamurthy. "FIRE: A Dataset for Financial Relation Extraction." In *Findings of the Association for Computational Linguistics: NAACL 2024*, 3637–3652. Mexico City: Association for Computational Linguistics, June 2024.**

- URL: `https://aclanthology.org/2024.findings-naacl.230/`
- **Type:** Peer-reviewed conference paper (NAACL Findings).
- **Summary:** Introduces FIRE, a hand-annotated dataset for financial relation extraction that is larger and more comprehensive than prior datasets (FinRED) in covering diverse relations and financial aspects of businesses. Evaluates SpERT (span-based entity and relation extraction) with curriculum learning approaches for the financial domain.
- **Relevance:** *Section 3 (Relation Extraction).* The primary benchmark dataset for financial relation extraction. SpERT evaluation provides a concrete model baseline for readers.
- **How to use:** Cite as the benchmark for relation extraction. Walk through the relation types covered (ownership, supply chain, executive-company) and the SpERT model architecture.
- Status: `[ ] Unverified`

---

### 3.2 Methodological: LLM-Based Knowledge Graph Construction

**Li, Xiaohui Victor, Saizhuo Wang, Yinda Du, and Jimin Huang. "FinDKG: Dynamic Knowledge Graphs with Large Language Models for Detecting Global Trends in Financial Markets." In *Proceedings of the 5th ACM International Conference on AI in Finance (ICAIF '24)*. Brooklyn, NY: ACM, November 2024.**

- DOI: `10.1145/3677052.3698603`
- **Type:** Peer-reviewed conference paper.
- **Summary:** Introduces FinDKG, an open-source Financial Dynamic Knowledge Graph constructed from financial news articles using a fine-tuned LLM (ICKG — Integrated Contextual Knowledge Graph Generator). Features a well-defined schema with 15 predefined relationships and 12 entity types. Models causal effects between financial markets and tracks influential persons and impactful events. Demonstrates KG-based trend detection outperforming text-only approaches.
- **Relevance:** *Section 4 (Building Knowledge Graphs).* The most comprehensive open-source financial KG construction pipeline. The LLM-based extraction approach represents the current state of the art, replacing hand-crafted rules with prompted/fine-tuned language models.
- **How to use:** Central to Section 4. Present the ICKG pipeline as the recommended approach for readers: LLM extracts (entity, relation, entity) triples → schema validates → temporal index stores. The 15 relation types and 12 entity types provide a concrete schema readers can adopt.
- Status: `[ ] Unverified`

---

## 4. Building Knowledge Graphs from Financial Sources

### 4.1 Methodological: SEC Filing KG Construction

**FinReflectKG. "FinReflectKG: Agentic Construction and Evaluation of Financial Knowledge Graphs." In *Proceedings of the 6th ACM International Conference on AI in Finance (ICAIF '25)*. 2025.**

- DOI: `10.1145/3768292.3770363`
- **Type:** Peer-reviewed conference paper.
- **Summary:** Constructs a comprehensive financial knowledge graph from SEC 10-K filings of all S&P 100 companies. Supports three extraction modes: single-pass, multi-pass, and reflection-agent-based, with dynamic schema configuration using both LLMs and domain experts. Also introduces FinReflectKG-EvalBench for standardized KG evaluation.
- **Relevance:** *Section 4.* Demonstrates end-to-end KG construction from SEC filings at scale. The multi-pass and agent-based extraction modes represent the cutting edge. The evaluation benchmark (EvalBench) addresses a critical gap — how to measure KG quality.
- **How to use:** Cite alongside FinDKG as a complementary approach: FinDKG builds from news articles, FinReflectKG from SEC filings. Together they show that financial KGs can be constructed from multiple source types.
- Status: `[ ] Unverified`

---

## 5. Temporal Knowledge Graphs

### 5.1 Survey: Temporal KG Methods

**Cai, Binglin, Yonggang Xiang, Liyan Gao, He Zhang, Yue Li, and Jiaqi Li. "A Survey on Temporal Knowledge Graph: Representation Learning and Applications." arXiv preprint, arXiv:2403.04782, March 2024.**

- URL: `https://arxiv.org/abs/2403.04782`
- **Type:** Preprint (survey).
- **Summary:** Comprehensively reviews temporal knowledge graph embedding methods, categorizing them into seven classes. Covers TComplEx (tensor decomposition in complex vector space with temporal embeddings), DE-SimplE (diachronic embeddings with static and time-varying segments), and T-SimplE (order-4 tensor decomposition). Also covers evaluation schemes, datasets, and applications.
- **Relevance:** *Section 5 (Temporal Knowledge Graphs).* The most current survey of temporal KG methods. Provides the theoretical and methodological foundation for tracking evolving financial relationships (board changes, M&A, supply chain shifts).
- **How to use:** Cite as the survey reference. Focus on TComplEx and DE-SimplE as the most applicable methods for financial temporal KGs, where entities (companies, executives) have both stable attributes and time-varying relationships.
- Status: `[ ] Unverified`

---

## 6. Use Cases: Supply Chain Risk, Contagion, Activism

### 6.1 Empirical: Supply Chain Knowledge Graphs

**Brintrup, Alexandra, Nikolaos Kosasih, Yangbang Zhang, and Edward Sheridan. "Towards Knowledge Graph Reasoning for Supply Chain Risk Management Using Graph Neural Networks." *International Journal of Production Research* 62, nos. 1–2 (2024): 601–620.**

- DOI: `10.1080/00207543.2022.2100841`
- **Type:** Peer-reviewed journal article.
- **Summary:** Develops neurosymbolic models using GNNs to extract information from supply chain data as embeddings and uses symbolic logic to infer new supply chain knowledge. Combines NLP-extracted supply chain relations with link prediction to identify hidden supply chain connections. First GNN-based approach to model uncertainty in supply chain knowledge graph reasoning.
- **Relevance:** *Section 6 (Supply Chain Risk).* Demonstrates how knowledge graphs enable supply chain risk analysis that text alone cannot support. The link prediction component (inferring unobserved supply chain links from graph structure) is a concrete financial application of graph reasoning.
- **How to use:** Cite as the primary supply chain KG reference. The link prediction application — discovering hidden supply chain dependencies not mentioned in any single document — illustrates why KGs are more powerful than document-level NLP.
- Status: `[ ] Unverified`

---

### 6.2 Empirical: Knowledge-Driven Stock Prediction

**Deng, Shumin, Ningyu Zhang, Wen Zhang, Jiaoyan Chen, Jeff Z. Pan, and Huajun Chen. "Knowledge-Driven Stock Trend Prediction and Explanation via Temporal Convolutional Network." In *Companion Proceedings of the 2019 World Wide Web Conference*, 678–685. San Francisco, CA: ACM, May 2019.**

- DOI: `10.1145/3308560.3317701`
- **Type:** Peer-reviewed conference paper (WWW).
- **Summary:** Proposes KDTCN (Knowledge-Driven Temporal Convolutional Network), which extracts structured events from financial news and uses external knowledge from knowledge graphs to obtain event embeddings for stock prediction. The model reacts to abrupt changes faster and outperforms state-of-the-art methods. Importantly, it also facilitates *explanation* of predictions, particularly around abrupt market changes.
- **Relevance:** *Section 6 (Use Cases) and Section 7 (Graph-Based Features).* Demonstrates that knowledge graph embeddings improve stock prediction beyond text-only approaches. The explainability angle is valuable — KG-based features can explain *why* a prediction was made (via the relational path), unlike opaque sentiment scores.
- **How to use:** Cite to connect KG construction to downstream financial prediction. The explainability benefit is a key differentiator from sentiment-based approaches.
- Status: `[ ] Unverified`

---

## 7. Graph-Based Features for Downstream Models

### 7.1 Empirical: Network Centrality and Stock Returns

**Ahern, Kenneth R. "Network Centrality and the Cross Section of Stock Returns." Working paper, University of Southern California, 2013.**

- URL: `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2197370`
- **Type:** Working paper.
- **Summary:** Analyzes a correlation network of residual stock returns for 5,000+ US firms using principal components to compute network centrality. Finds that firms more central in the network earn higher returns than peripheral firms. Network centrality has substantial predictive power in out-of-sample tests, particularly during financial crises.
- **Relevance:** *Section 7 (Graph-Based Features).* The primary reference for using graph centrality as a stock return predictor. Validates that graph topology features (degree, betweenness, eigenvector centrality) carry financial signal beyond what individual firm characteristics capture.
- **How to use:** Cite to justify extracting centrality metrics from knowledge graphs as features for downstream models. The crisis-period predictive power connects to Chapter 10's regime detection.
- Status: `[ ] Unverified`

---

### 7.2 Methodological: Systemic Risk from Network Structure

**Billio, Monica, Mila Getmansky, Andrew W. Lo, and Loriana Pelizzon. "Econometric Measures of Connectedness and Systemic Risk in the Finance and Insurance Sectors." *Journal of Financial Economics* 104, no. 3 (June 2012): 535–559.**

- DOI: `10.1016/j.jfineco.2011.12.010`
- **Type:** Peer-reviewed journal article.
- **Summary:** Proposes econometric measures of connectedness based on Granger-causality networks. Applies network analysis to measure systemic risk in financial institutions. Six centrality measures (degree, closeness, betweenness, Katz, eccentricity, information centrality) quantify systemic importance. Betweenness centrality identifies key nodes controlling systemic risk propagation.
- **Relevance:** *Section 7 (Graph Features) and Section 6 (Contagion Modeling).* Provides the formal framework for using graph centrality metrics as systemic risk features. The six centrality measures constitute a concrete feature engineering blueprint.
- **How to use:** Cite for the centrality-as-risk-feature framework. The six measures provide a checklist for feature extraction from financial knowledge graphs: degree (how connected?), betweenness (how important for information flow?), closeness (how quickly can shocks propagate?).
- Status: `[ ] Unverified`

---

## 8. Multi-Modal Graph Enrichment

### 8.1 Contextual: Combining Text and Structured Data

**Zha, Daochen, Zaid Pervaiz Bhat, and Xia Hu. "Financial Forecasting from Textual and Tabular Time Series." In *Findings of the Association for Computational Linguistics: EMNLP 2024*. Miami, FL: Association for Computational Linguistics, November 2024.**

- URL: `https://aclanthology.org/2024.findings-emnlp.486/`
- **Type:** Peer-reviewed conference paper.
- **Summary:** Multi-modal method combining text features with tabular financial variables through cross-modality fusion.
- **Relevance:** *Section 8 (Multi-Modal Enrichment).* The multi-modal fusion architecture (text + tabular) extends naturally to knowledge graph enrichment: link text-extracted relationships (ownership, supply chain) with structured financial data (ownership percentages, revenue exposure).
- **Cross-reference:** Already cited in Chapter 5 research.
- Status: `[ ] Unverified`

---

## Cross-Chapter References

| Source | Ch 9 Section | Also Relevant To |
|--------|-------------|------------------|
| Loukas et al. (2022) FiNER | Sec 1 (NER) | Ch 2 (EDGAR), Ch 4 (SEC-BERT) |
| Sharma et al. (2024) FIRE | Sec 3 (Relation Extraction) | Ch 4 (NLP Methods) |
| Li et al. (2024) FinDKG | Sec 4 (KG Construction) | Ch 10 (Regime — graph features) |
| FinReflectKG (2025) | Sec 4 (SEC Filing KG) | Ch 2 (EDGAR parsing) |
| Cai et al. (2024) TKG Survey | Sec 5 (Temporal KG) | Ch 10 (Regime — temporal dynamics) |
| Brintrup et al. (2024) | Sec 6 (Supply Chain) | Ch 10 (Regime — contagion) |
| Deng et al. (2019) KDTCN | Sec 6, 7 (KG → Prediction) | Ch 5 (Signal Construction) |
| Ahern (2013) | Sec 7 (Centrality Features) | Ch 10 (Regime Detection) |
| Billio et al. (2012) | Sec 7 (Systemic Risk) | Ch 10 (Regime), Ch 13 (Systemic Risk) |
| Zha et al. (2024) | Sec 8 (Multi-Modal) | Ch 5 (Feature Fusion) |

---

## Research Gaps

The following areas need additional sourcing:

- [ ] **Ticker symbol disambiguation** — Need a dedicated paper on context-based disambiguation of ticker symbols that are common English words (COST, CAT, FORD, ALL, KEY). This is a practical NER challenge that general NER papers don't address.
- [ ] **CUSIP, LEI, ISIN cross-referencing** — Need references on identifier systems and cross-referencing databases for financial entity resolution. OpenFIGI, GLEIF, or similar identifier databases should be documented as resources for entity linking.
- [ ] **Neo4j and graph database tools for financial KGs** — Need practical references on graph database implementation (Neo4j, Amazon Neptune, RDF/OWL) for financial knowledge graphs. Neo4j's documentation and case studies may provide examples.
- [ ] **Community detection algorithms for financial networks** — Need papers applying community detection (Louvain, Girvan-Newman, spectral clustering) to financial knowledge graphs for sector/cluster identification. These algorithms can discover latent industry groupings from relationship graphs.
- [ ] **Activist investor detection from filing language** — Need a paper specifically detecting activist investor campaigns from changes in 13D filing language, ownership graph topology changes, or unusual board composition shifts. The SEC's 2023 rule shortening the 13D disclosure window may be relevant context.
- [ ] **REBEL model for financial relation extraction** — Need a paper evaluating the REBEL (Relation Extraction By End-to-end Language generation) model on financial text specifically. REBEL's sequence-to-sequence approach may be compared with SpERT's span-based approach.
- [ ] **Knowledge graph completion for financial data** — Need papers on inferring missing links in financial knowledge graphs (e.g., predicting undisclosed supply chain relationships from partial graph structure).

---

## Verification Priority

Start SMU Library verification with these sources first:

1. **Loukas et al. (2022)** — FiNER benchmark (ACL — foundational NER)
2. **Sharma et al. (2024)** — FIRE relation extraction dataset (NAACL)
3. **Li et al. (2024)** — FinDKG dynamic knowledge graph (ICAIF)
4. **Billio et al. (2012)** — Systemic risk network measures (JFE)
5. **Deng et al. (2019)** — Knowledge-driven stock prediction (WWW)
6. **Brintrup et al. (2024)** — Supply chain KG with GNNs
7. **Cai et al. (2024)** — Temporal KG survey
8. **FinReflectKG (2025)** — SEC filing KG construction (ICAIF)
9. **Ahern (2013)** — Network centrality and returns
10. **Zhou et al. (2025)** — LLMs for financial NER

---

*Research compiled April 2026. All citations require manual verification through SMU Library before inclusion in final manuscript.*
