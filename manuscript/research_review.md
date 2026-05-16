# Research Pass Review — Applied NLP for Finance

**Date:** April 2026
**Scope:** Chapters 1–13 annotated bibliography compilation
**Total sources identified:** ~231 across 13 chapters
**Citation format:** Chicago (Notes and Bibliography), 17th edition
**Next step:** Manual verification through SMU Library

---

## 1. Executive Summary

This document summarizes the findings, patterns, and strategic insights from the first comprehensive research pass across all 13 chapters of *Applied NLP for Finance*. The research compilation produced 13 annotated `research.md` files, one per chapter, containing full Chicago citations, summaries, relevance notes, cross-chapter reference tracking, research gaps, and verification priority lists.

The research reveals that the book sits at a unique intersection of three mature but previously disconnected literatures: (1) quantitative finance and market microstructure, (2) natural language processing and computational linguistics, and (3) behavioral economics and narrative theory. No existing book synthesizes all three at the depth this manuscript targets.

---

## 2. Cross-Cutting Intellectual Themes

### 2.1 The Hayek–Fama–Grossman-Stiglitz–Shiller Arc

The book's theoretical backbone runs through four papers that each build on and challenge the last:

- **Hayek (1945)** — Knowledge is dispersed; prices aggregate it
- **Fama (1970)** — Markets are informationally efficient; prices reflect all public information
- **Grossman & Stiglitz (1980)** — Perfect efficiency is paradoxical; costly information creates exploitable inefficiency
- **Shiller (2017, 2019)** — Narratives *are* the information that prices struggle to incorporate

This arc provides the philosophical justification for the entire book: text is the medium through which dispersed, costly-to-process knowledge enters prices — imperfectly and with exploitable delays. Every chapter draws energy from this progression, even when it isn't explicitly cited.

### 2.2 The Domain Specificity Principle

A recurring finding across multiple chapters is that *generic NLP tools systematically fail on financial text*:

- **Loughran & McDonald (2011)** — Three-fourths of Harvard GI "negative" words are misclassified in financial contexts (Ch 1, 3)
- **Loukas et al. (2021)** — EDGAR-trained word embeddings outperform generic GloVe on financial tasks (Ch 2, 3)
- **Araci (2019)** — FinBERT improves over general BERT by 14 percentage points on financial sentiment (Ch 4)
- **Tang & Yang (2025)** — General MTEB embedding rankings are *uncorrelated* with financial retrieval performance on FinMTEB (Ch 12)

This principle — that financial text requires domain-specific models, lexicons, embeddings, and benchmarks — is the book's most practically important finding. It should be made explicit as a recurring theme.

### 2.3 The Signal-Then-Decay Pattern

Multiple chapters document the same pattern: text-based signals are discovered, exploited, and then degrade:

- **Tetlock (2007)** — Media pessimism predicts market pressure, then *reverts* (Ch 1, 5)
- **Bradley et al. (2024)** — WSB due diligence posts produced 5% quarterly alpha pre-GameStop; predictability *vanished* post-GameStop (Ch 8)
- **McLean & Pontiff (2016)** — Published return predictors decline 58% post-publication (Ch 11, 13)
- **Di Mascio et al. (2016)** — Alpha is strongest immediately after signal construction and decays with age (Ch 5)

This pattern implies that the book should teach *methodology* (how to discover and evaluate signals) rather than *recipes* (specific signals to trade). Recipes decay; methodology endures.

### 2.4 The Reflexivity Challenge

The book's deepest intellectual tension emerges in Chapter 13 but is foreshadowed throughout:

- **Chapter 1** argues: "Narratives move markets → NLP can extract signal"
- **Chapter 13** argues: "Narratives move markets → NLP can *amplify* manipulation and create feedback loops"

Soros's reflexivity (1987) and Stein's crowding externalities (2009) formalize the concern: when NLP models participate in the market, they change the system they're trying to predict. The same mechanism that makes text informative (narratives drive behavior) also makes it dangerous (narratives can be false, manipulated, or self-reinforcing).

This tension should not be resolved — it should be held openly as the book's central intellectual challenge.

---

## 3. Source Profile Analysis

### 3.1 Source Types by Chapter

| Chapter | Journal Articles | Books | Preprints/WP | Documentation/Reports | Legal/Regulatory |
|---------|-----------------|-------|-------------|----------------------|-----------------|
| Ch 1 | 18 | 2 | 0 | 0 | 0 |
| Ch 2 | 9 | 0 | 2 | 6 | 3 |
| Ch 3 | 14 | 3 | 1 | 0 | 0 |
| Ch 4 | 8 | 0 | 5 | 0 | 0 |
| Ch 5 | 10 | 1 | 2 | 0 | 0 |
| Ch 6 | 14 | 0 | 0 | 0 | 0 |
| Ch 7 | 10 | 0 | 3 | 3 | 0 |
| Ch 8 | 12 | 0 | 1 | 1 | 0 |
| Ch 9 | 9 | 0 | 2 | 0 | 0 |
| Ch 10 | 11 | 1 | 1 | 0 | 0 |
| Ch 11 | 7 | 1 | 1 | 0 | 0 |
| Ch 12 | 5 | 0 | 1 | 0 | 0 |
| Ch 13 | 7 | 3 | 0 | 2 | 3 |

**Key observations:**
- Chapters 1, 3, and 6 are most heavily grounded in peer-reviewed literature
- Chapter 4 has the highest proportion of preprints, reflecting the fast-moving LLM landscape
- Chapter 2 is the most source-type diverse (academic + documentation + legal)
- Chapter 12 has the fewest academic sources (engineering-focused chapter)
- Chapter 13 is the only chapter citing books as primary sources (Taleb, Kahneman, Soros)

### 3.2 Most-Cited Sources Across Chapters

These sources appear in three or more chapter research files, making them the book's intellectual anchors:

| Source | Chapters Cited |
|--------|---------------|
| Loughran & McDonald (2011) | Ch 1, 3, 4, 5, 11 |
| Li et al. (2025) NLP Finance Survey | Ch 1, 2, 3, 4, 5, 12, 13 |
| Gentzkow, Kelly & Taddy (2019) | Ch 1, 2, 3, 5, 11 |
| Tetlock (2007) | Ch 1, 5, 8 |
| Manela & Moreira (2017) NVIX | Ch 1, 2, 5, 10 |
| García (2013) | Ch 1, 5, 10 |
| López de Prado (2018) | Ch 5, 10, 11 |
| Baker & Wurgler (2006) | Ch 5, 10 |
| Billio et al. (2012) | Ch 9, 10, 13 |
| McLean & Pontiff (2016) | Ch 8, 11, 13 |
| Loukas et al. (2021) EDGAR-CORPUS | Ch 2, 3, 9 |

### 3.3 Publication Venue Distribution

The sources span a wide range of venues, reflecting the book's interdisciplinary nature:

**Top finance journals (JF, JFE, RFS, JFQA):** ~35 sources
- *Journal of Finance:* Fama, Tetlock, Loughran-McDonald, García, McLean-Pontiff, Stein, etc.
- *Journal of Financial Economics:* Calomiris-Mamaysky, Manela-Moreira, Pedersen, Brunnermeier-Pedersen
- *Review of Financial Studies:* Harvey-Liu-Zhu, Cookson et al. (Echo Chambers, Partisanship), Bradley et al.

**Top accounting journals (TAR, JAR, JAE, RAS):** ~12 sources
- Matsumoto et al., Larcker-Zakolyukina, Brown-Tucker, Campbell et al.

**Top economics journals (AER, QJE, JEL, Econometrica):** ~10 sources
- Shiller, Nakamura-Steinsson, Gorodnichenko et al., Hamilton, White, Blinder et al.

**NLP/ML venues (ACL, EMNLP, NeurIPS, ICML):** ~20 sources
- Devlin (BERT), Vaswani (Transformer), Loukas (FiNER), Lewis (RAG), Lundberg (SHAP)

**Interdisciplinary/applied journals:** ~15 sources
- *Crime Science:* Kamps-Kleinberg
- *CACM:* Cresci (bot detection)
- *Digital Finance:* Divernois-Filipović

---

## 4. Research Gaps Inventory

Across all 13 chapters, approximately 90 specific research gaps were identified. The most critical gaps — those that affect multiple chapters or the book's core arguments — are:

### 4.1 High-Priority Gaps (Affect Multiple Chapters)

1. **Prior work on sentiment-based regime detection** (Ch 10) — The book's primary novelty claim. Must be thoroughly verified before Chapter 10 can be written with confidence.

2. **NLP model performance degradation during 2008 crisis** (Ch 13, 1, 10) — COVID is well-documented; a 2008 case study would strengthen the historical argument.

3. **Distribution shift in financial language during crises** (Ch 13, 4, 10) — Quantitative measurement of how financial vocabulary, sentiment calibration, and terminology change during crises.

4. **Cross-platform sentiment aggregation** (Ch 8, 5) — No study systematically combines sentiment from Twitter + Reddit + StockTwits + news and tests multi-platform vs. single-platform signal quality.

5. **Latency benchmarks: classical vs. BERT vs. LLM** (Ch 3, 4, 12) — Specific timing data for financial document classification across model types on CPU and GPU.

### 4.2 Chapter-Specific Critical Gaps

- **Ch 2:** Bloomberg vs. Refinitiv vs. NewsAPI API comparison for NLP use cases
- **Ch 3:** Tokenizer comparison on financial text (spaCy vs. NLTK vs. HF)
- **Ch 5:** Exponential decay half-life calibration for different text sources
- **Ch 6:** CEO vs. CFO sentiment gap as a standalone predictive feature
- **Ch 7:** Structural break detection in FOMC communication regimes
- **Ch 9:** Ticker symbol disambiguation dedicated study
- **Ch 11:** Survivorship bias in NLP text datasets (dedicated paper)
- **Ch 12:** Financial RAG with interleaved text and tabular data

---

## 5. Methodological Progression Across Chapters

The sources reveal a clean methodological ladder that structures the book's technical arc:

```
Ch 3: Word counts → TF-IDF → Word embeddings → Domain lexicons
  ↓
Ch 4: BERT → FinBERT → BloombergGPT → LLM prompting → LoRA
  ↓
Ch 5: Raw scores → Temporal aggregation → Signal normalization → Multi-modal fusion
  ↓
Ch 6-8: Earnings calls → Central bank text → Social media (domain application)
  ↓
Ch 9: NER → Relation extraction → Knowledge graphs → Graph features
  ↓
Ch 10: HMM regimes → Sentiment regimes → Multi-modal regime detection
  ↓
Ch 11: Purged CV → PBO → Sharpe correction → Multiple testing
  ↓
Ch 12: Model serving → Vector DBs → RAG → Drift detection → Monitoring
```

Each step builds on the previous, and the sources document this progression. The book's companion code (`src/`) should mirror this ladder.

---

## 6. Three Research Eras

The sources cluster into three temporal eras, each with distinct characteristics:

### Era 1: Classical Financial Text Analysis (2004–2015)
**Defining papers:** Tetlock (2007), Loughran-McDonald (2011), Antweiler-Frank (2004)
**Methods:** Dictionaries, bag-of-words, word counts, classical ML
**Venues:** Primarily finance and accounting journals
**Character:** Careful empirical work establishing that text carries financial signal

### Era 2: Transformer Revolution (2017–2022)
**Defining papers:** Vaswani (2017), Devlin (2019), Araci (2019), Wu et al. (2023) BloombergGPT
**Methods:** BERT, FinBERT, domain-adapted transformers, fine-tuning
**Venues:** Mixed NLP/finance venues
**Character:** Dramatic accuracy improvements; domain adaptation becomes central

### Era 3: LLM Paradigm Shift (2023–present)
**Defining papers:** Yang et al. (2023) FinGPT, Zheng et al. (2023) LLM-as-Judge, Glasserman-Lin (2023)
**Methods:** Zero-shot/few-shot prompting, structured extraction, RAG, agentic pipelines
**Venues:** Preprints, workshops, rapid iteration
**Character:** Accessibility explosion; new failure modes (LLM look-ahead bias); methods evolving faster than publication cycles

The book must serve readers across all three eras — some will use L-M dictionaries in production, others will prompt Claude for sentiment labels. The research supports both approaches by documenting when each is appropriate.

---

## 7. Verification Strategy Recommendations

### 7.1 Priority Tiers for SMU Library Verification

**Tier 1 — Must-verify first (foundational, high-impact):** ~30 sources
These are papers the book cannot be published without citing correctly. All top-journal papers (JF, JFE, RFS, AER, QJE, Econometrica) and foundational NLP papers (BERT, Transformer, RAG).

**Tier 2 — Verify before chapter drafting:** ~50 sources
Domain-specific papers that anchor individual chapters. These can be verified as each chapter is drafted.

**Tier 3 — Verify during revision:** ~40 sources
Supporting citations, working papers, and contextual references that enrich but don't anchor arguments.

**Tier 4 — May not need verification:** ~20 sources
Official documentation (SEC EDGAR, FRASER, ECB datasets), regulatory documents, and technical standards (NIST) that are publicly accessible and don't require library access.

### 7.2 Verification Workflow

For each source at SMU Library:
1. **Confirm citation accuracy** — author names, title, journal, volume, pages, year, DOI
2. **Access full text** — download PDF for reference during chapter drafting
3. **Read abstract + introduction + conclusion** — capture the author's own summary
4. **Note 2–3 specific findings** — page numbers for direct quotes or key statistics
5. **Mark verified** in `research.md` — change `[ ] Unverified` to `[x] Verified via SMU Library`
6. **Update spreadsheet** — mark verification status in master spreadsheet

### 7.3 Sources Requiring Special Attention

Some sources need verification beyond standard library access:

- **Two FinBERTs** — Verify that Araci (2019) and Huang et al. (2023) are indeed distinct models with different architectures and training data. The naming collision must be documented accurately.
- **Preprints** — Check whether any cited preprints have since been published in peer-reviewed venues (especially Glasserman-Lin 2023, FinGPT, BloombergGPT).
- **Regulatory documents** — Confirm SEC 2025 examination priorities and FINRA guidance are current as of manuscript finalization.
- **FinMTEB** — Verify the uncorrelated MTEB/FinMTEB performance finding — it's a strong claim that anchors Chapter 12's embedding selection guidance.

---

## 8. Connections to Companion Code

The research directly informs the companion code architecture:

| Code Module | Primary Research Sources |
|-------------|------------------------|
| `src/data/scrapers.py` | Ch 2: EDGAR API docs, PRAW, GDELT |
| `src/data/preprocessing.py` | Ch 3: Sennrich (BPE), Loughran-McDonald dictionary |
| `src/models/finbert.py` | Ch 4: Araci (2019), Huang et al. (2023) |
| `src/models/llm_prompting.py` | Ch 4: Zheng et al. (2023) LLM-as-Judge |
| `src/models/signal_builder.py` | Ch 5: Baker-Wurgler (2006), García (2013), Lo (2002) |
| `src/models/regime_detector.py` | Ch 10: Hamilton (1989), Calomiris-Mamaysky (2019) |
| `src/knowledge/entity_extraction.py` | Ch 9: Loukas et al. (2022) FiNER |
| `src/knowledge/graph_builder.py` | Ch 9: Li et al. (2024) FinDKG, Billio et al. (2012) |
| `src/evaluation/backtest.py` | Ch 11: López de Prado (2018), Bailey et al. (2017) |
| `src/evaluation/metrics.py` | Ch 11: Lo (2002), Harvey et al. (2016) |

---

## 9. What This Book Contributes Beyond Existing Literature

The research pass reveals that no existing book or survey combines all of:

1. **Full NLP pipeline** from tokenization through LLMs (Chapters 3–4)
2. **Domain-specific financial text sources** treated individually (Chapters 6–8)
3. **Knowledge graph construction** from financial text (Chapter 9)
4. **Regime detection** using text features as a *novel research contribution* (Chapter 10)
5. **Rigorous evaluation methodology** with NLP-specific failure modes (Chapter 11)
6. **Production deployment** with financial-domain concerns (Chapter 12)
7. **Honest ethical and philosophical treatment** of limits (Chapter 13)

Existing books cover subsets: López de Prado covers ML for finance (but not NLP); Jurafsky-Martin covers NLP (but not finance); Loughran-McDonald surveys textual analysis in accounting (but not production systems or regime detection). This book's contribution is the synthesis — and Chapter 10's sentiment-based regime detection is the original research thread that no other source provides.

---

*Review compiled April 2026. This document should be updated as SMU Library verification progresses and as chapter drafting reveals additional research needs.*
