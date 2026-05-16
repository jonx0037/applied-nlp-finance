# Chapter 5 — Sentiment Analysis and Signal Construction — Annotated Bibliography

**Purpose:** This chapter bridges the gap between model output and tradeable signal. It covers temporal aggregation, signal normalization, cross-asset sentiment effects, multi-modal feature fusion, and the critical topic of avoiding look-ahead bias. The focus is on production-grade signal engineering.

**What this chapter needs from its sources:**
- Sentiment index construction methodology (from raw scores to aggregated indices)
- Temporal aggregation methods (rolling windows, exponential decay, event-time vs. calendar-time)
- Cross-asset sentiment spillover evidence
- Signal normalization and regime-conditioning techniques
- Multi-modal fusion of text and tabular features
- Look-ahead bias mechanisms specific to NLP pipelines
- Alpha decay analysis for text-based signals

**Citation format:** Chicago (Notes and Bibliography), 17th edition.

**Note on chapter positioning:** This is where the book pivots from NLP methodology to quantitative finance. Sources span both communities — NLP researchers publishing in ACL/EMNLP and finance researchers publishing in JF/JFE/RFS. The chapter must bridge both.

---

## 1. Raw Sentiment Scores vs. Aggregated Indices

### 1.1 Foundational: Sentiment Index Construction

**Baker, Malcolm, and Jeffrey Wurgler. "Investor Sentiment and the Cross-Section of Stock Returns." *Journal of Finance* 61, no. 4 (August 2006): 1645–1680.**

- DOI: `10.1111/j.1540-6261.2006.00885.x`
- **Type:** Peer-reviewed journal article.
- **Summary:** Constructs a composite investor sentiment index from six market-based proxies (NYSE turnover, dividend premium, closed-end fund discount, IPO volume, IPO first-day returns, equity share in new issues) via principal component analysis. Shows that when sentiment is high, speculative stocks (small, young, volatile, unprofitable, non-dividend-paying) earn relatively low subsequent returns, and vice versa.
- **Relevance:** *Section 1 (Aggregated Indices).* The canonical paper on sentiment index construction. While Baker-Wurgler use market-based proxies rather than text, their PCA-based aggregation methodology is directly applicable to combining multiple text-based sentiment measures into a composite index.
- **How to use:** Cite as the foundational framework for sentiment index construction. Then show how text-based measures (Tetlock, Garcia, etc.) can be incorporated into or compared against the Baker-Wurgler framework.
- Status: `[ ] Unverified`

---

**Baker, Malcolm, and Jeffrey Wurgler. "Investor Sentiment in the Stock Market." *Journal of Economic Perspectives* 21, no. 2 (Spring 2007): 129–152.**

- DOI: `10.1257/jep.21.2.129`
- **Type:** Peer-reviewed journal article (survey/overview).
- **Summary:** Accessible overview of the sentiment literature. Defines investor sentiment as "a belief about future cash flows and investment risks that is not justified by the facts at hand." Surveys measurement approaches and argues that "the question is no longer whether investor sentiment affects stock prices, but how to measure investor sentiment and quantify its effects."
- **Relevance:** *Section 1.* The accessible companion to Baker-Wurgler (2006). The definition of sentiment and the survey of measurement approaches provides the conceptual framework for the chapter.
- **How to use:** Use the sentiment definition early in the chapter. The survey of measurement approaches contextualizes where text-based measures fit in the broader sentiment measurement landscape.
- Status: `[ ] Unverified`

---

### 1.2 Empirical: Text-Based Sentiment Indices

**García, Diego. "Sentiment during Recessions." *Journal of Finance* 68, no. 3 (June 2013): 1267–1300.**

- DOI: `10.1111/jofi.12027`
- **Type:** Peer-reviewed journal article.
- **Summary:** Constructs a daily text-based sentiment proxy from the fraction of positive and negative words in New York Times financial news columns (1905–2005). Key finding: the predictability of stock returns using news content is *concentrated in recessions*. A one standard deviation sentiment shock during recessions predicts a 12 basis points change in DJIA conditional returns over one day.
- **Relevance:** *Section 1 (From Scores to Indices) and Section 4 (Regime Conditioning).* Demonstrates a century-long text-based sentiment index and — critically — shows that sentiment signal strength is regime-dependent. This is the empirical foundation for the regime-conditioning argument in Section 4.
- **How to use:** Central to two sections. In Section 1: how to construct a daily text-based index from word counts. In Section 4: the regime-dependence finding motivates conditional normalization — sentiment predicts returns in recessions but not in expansions.
- Status: `[ ] Unverified`

---

**Ke, Zheng Tracy, Bryan T. Kelly, and Dacheng Xiu. "Predicting Returns with Text Data." NBER Working Paper no. 26186, August 2019.**

- URL: `https://www.nber.org/papers/w26186`
- **Type:** Working paper (NBER).
- **Summary:** Develops a supervised learning framework for constructing sentiment scores optimized for return prediction, analyzing 22+ million Dow Jones Newswires articles (1989–2017). Three-step method: (1) predictive screening to isolate sentiment terms, (2) topic modeling for sentiment weights, (3) penalized likelihood for article-level scores. Shows text data forecasts intraday returns.
- **Relevance:** *Section 1 (Sentiment Scores) and Section 2 (Temporal Aggregation).* The most sophisticated text-to-signal methodology in the literature. The supervised approach (optimizing word weights for return prediction) is a major advance over unsupervised sentiment dictionaries. The intraday signal finding is relevant to temporal aggregation.
- **How to use:** Cite as the state-of-the-art in text-based return prediction. The three-step methodology provides a concrete recipe readers can implement. Contrast with dictionary-based approaches (L-M, VADER) to show the evolution from unsupervised to supervised signal construction.
- Status: `[ ] Unverified`

---

## 2. Temporal Aggregation Strategies

### 2.1 Empirical: Intraday Sentiment Dynamics

**Renault, Thomas. "Intraday Online Investor Sentiment and Return Patterns in the U.S. Stock Market." *Journal of Banking & Finance* 84 (November 2017): 25–40.**

- DOI: `10.1016/j.jbankfin.2017.07.002`
- **Type:** Peer-reviewed journal article.
- **Summary:** Constructs a lexicon from StockTwits messages and aggregates individual message sentiment at half-hour intervals. Finds that the first half-hour change in investor sentiment predicts the last half-hour S&P 500 ETF return. The intraday effect is driven by shifts in novice trader sentiment.
- **Relevance:** *Section 2 (Temporal Aggregation).* Demonstrates half-hour aggregation windows for social media sentiment. The finding that novice trader sentiment drives the signal has implications for signal quality filtering.
- **How to use:** Cite as the primary reference for intraday temporal aggregation. The half-hour window provides a concrete aggregation choice readers can benchmark against. The novice-vs-expert distinction informs the filtering discussion.
- Status: `[ ] Unverified`

---

### 2.2 Methodological: Exponential Decay and Signal Processing

**Tetlock, Paul C. "Giving Content to Investor Sentiment: The Role of Media in the Stock Market." *Journal of Finance* 62, no. 3 (June 2007): 1139–1168.**

- DOI: `10.1111/j.1540-6261.2007.01232.x`
- **Type:** Peer-reviewed journal article.
- **Summary:** Uses daily WSJ column content to predict market sentiment. Media pessimism predicts downward pressure on prices followed by reversion; unusually high/low pessimism predicts high trading volume. The temporal dynamics (prediction → reversion) demonstrate signal decay.
- **Relevance:** *Section 2 (Temporal Aggregation).* The prediction-then-reversion pattern reveals how sentiment signal decays over time — pessimism predicts short-term pressure but reverts, implying an optimal holding period for sentiment-based strategies.
- **How to use:** Use the reversion finding to motivate the signal decay analysis. Connect to exponential decay weighting — the decay parameter should reflect the empirical half-life of sentiment signal.
- **Cross-reference:** Already cited in Chapter 1 research.
- Status: `[ ] Unverified`

---

## 3. Cross-Asset Sentiment Effects

### 3.1 Empirical: Sentiment Spillover

**Baker, Malcolm, and Jeffrey Wurgler. "Investor Sentiment and the Cross-Section of Stock Returns." *Journal of Finance* 61, no. 4 (August 2006): 1645–1680.**

- *(See citation above in Section 1.1)*
- **Relevance for Section 3:** Baker-Wurgler show sentiment has differential effects across stock categories. This within-equity cross-section finding extends naturally to cross-asset questions: if sentiment affects speculative stocks differently than safe stocks, does it also affect equities vs. credit vs. volatility differently?
- Status: `[ ] Unverified`

---

**Manela, Asaf, and Alan Moreira. "News Implied Volatility and Disaster Concerns." *Journal of Financial Economics* 123, no. 1 (January 2017): 137–162.**

- DOI: `10.1016/j.jfineco.2016.01.032`
- **Type:** Peer-reviewed journal article.
- **Summary:** NVIX — text-based uncertainty measure from WSJ front pages (1890–present). High NVIX predicts above-average stock returns, even after controlling for VIX. Demonstrates that text-based risk measures capture cross-asset information (equity returns, volatility dynamics) not contained in price-based measures.
- **Relevance:** *Section 3 (Cross-Asset).* NVIX is a text-based measure that predicts equity returns *after controlling for* the options-derived VIX — demonstrating cross-asset information content. Text sentiment bleeds from news → equity expectations → volatility.
- **Cross-reference:** Already cited in Chapters 1 and 2 research.
- Status: `[ ] Unverified`

---

## 4. Signal Normalization and Regime Conditioning

### 4.1 Foundational: Regime-Dependent Signal Behavior

**García, Diego. "Sentiment during Recessions." *Journal of Finance* 68, no. 3 (June 2013): 1267–1300.**

- *(See citation above in Section 1.2)*
- **Relevance for Section 4:** The core finding — that sentiment predictability concentrates in recessions — is the empirical foundation for regime-conditional normalization. A sentiment z-score of +1.5 means something completely different in a recession vs. an expansion.
- **How to use:** Use as the primary motivating evidence for why normalization must be regime-conditional. The 12bp daily return prediction in recessions vs. no prediction in expansions quantifies the regime difference.
- Status: `[ ] Unverified`

---

### 4.2 Methodological: Financial Machine Learning Framework

**López de Prado, Marcos. *Advances in Financial Machine Learning*. Hoboken, NJ: Wiley, 2018.**

- ISBN: `978-1-119-48208-6`
- **Type:** Book.
- **Summary:** Comprehensive treatment of ML for finance, including purged k-fold cross-validation (solving look-ahead bias in time-series data), combinatorial purged cross-validation (CPCV), meta-labeling, fractional differentiation, and the Probability of Backtest Overfitting (PBO). Introduces the concept of information-driven bars and structural breaks.
- **Relevance:** *Section 4 (Normalization) and Section 6 (Look-Ahead Bias).* The purged CV methodology is essential for properly evaluating sentiment signals. The structural break detection is relevant to regime identification. The meta-labeling framework provides a principled way to combine sentiment signals with other features.
- **How to use:** Cite for purged CV and the backtest overfitting framework. These are the evaluation methods the companion code should implement for sentiment signal validation.
- **Cross-reference:** Also relevant to Chapter 11 (Backtesting and Evaluation).
- Status: `[ ] Unverified`

---

## 5. Multi-Modal Feature Fusion

### 5.1 Methodological: Text + Tabular Fusion

**Zha, Daochen, Zaid Pervaiz Bhat, and Xia Hu. "Financial Forecasting from Textual and Tabular Time Series." In *Findings of the Association for Computational Linguistics: EMNLP 2024*. Miami, FL: Association for Computational Linguistics, November 2024.**

- URL: `https://aclanthology.org/2024.findings-emnlp.486/`
- **Type:** Peer-reviewed conference paper.
- **Summary:** Proposes a multimodal method for combining textual features (earnings call transcripts) and tabular financial variables (financial ratios, macroeconomic indicators). Uses modality-specific encoders, a text feature extraction module (MTFE), and cross-modality fusion (CMF) to mix modalities. Addresses early vs. late fusion strategies.
- **Relevance:** *Section 5 (Multi-Modal Feature Fusion).* Directly addresses the chapter's topic of combining text-derived features with tabular data. The architecture comparison (early vs. late fusion, cross-modal attention) provides concrete design choices.
- **How to use:** Cite as the primary reference for text + tabular fusion architecture. The earnings call + financial ratios example maps directly to the chapter's motivating scenario (sentiment + earnings surprise magnitude).
- Status: `[ ] Unverified`

---

### 5.2 Empirical: Multi-Modal Credit Risk

**Li, Yupeng, Haipeng Chen, and Xin Liu. "Multi-Modal Deep Learning for Credit Rating Prediction Using Text and Numerical Data Streams." arXiv preprint, arXiv:2304.10740, April 2023.**

- URL: `https://arxiv.org/abs/2304.10740`
- **Type:** Preprint.
- **Summary:** Investigates deep learning models and fusion strategies (concatenation, cross-attention) at different levels (early, intermediate, late, hybrid) for credit rating prediction. Combines textual data (10-K filings, analyst reports) with numerical financial data. Determines which model combinations and integration stages yield optimal results.
- **Relevance:** *Section 5.* Provides empirical comparison of fusion strategies in a financial application. The credit rating domain is distinct from equity returns, demonstrating that multi-modal fusion is broadly applicable across financial tasks.
- **How to use:** Cite alongside Zha et al. (2024) for a second application domain. The systematic comparison of fusion strategies at different levels provides practical guidance.
- Status: `[ ] Unverified`

---

## 6. Avoiding Look-Ahead Bias

### 6.1 Foundational: LLM-Specific Look-Ahead Bias

**Glasserman, Paul, and Caden Lin. "Assessing Look-Ahead Bias in Stock Return Predictions Generated by GPT Sentiment Analysis." arXiv preprint, arXiv:2309.17322, September 2023.**

- URL: `https://arxiv.org/abs/2309.17322`
- **Type:** Preprint (Columbia University).
- **Summary:** Identifies two forms of look-ahead bias in LLM-based financial NLP: (1) *look-ahead bias* — the LLM may have specific knowledge of stock returns that followed a news article, since its training data includes both the article and subsequent returns; (2) *distraction effect* — general knowledge of named companies interferes with sentiment measurement. Tests by comparing performance on original headlines vs. de-biased headlines with company identifiers removed.
- **Relevance:** *Section 6 (Look-Ahead Bias).* The most important source for this section. Identifies a form of look-ahead bias *unique to LLMs* that didn't exist with classical NLP methods — the model's training data may include both the news and the subsequent returns, creating a direct information leak.
- **How to use:** Central to Section 6. This is a new category of bias that the book's audience needs to understand. The de-biasing methodology (removing company identifiers) provides a practical mitigation strategy. Connect to the LLM workflow discussion in Chapter 4.
- Status: `[ ] Unverified`

---

### 6.2 Methodological: Point-in-Time Data Design

**López de Prado, Marcos. *Advances in Financial Machine Learning*. Hoboken, NJ: Wiley, 2018.**

- *(See citation above in Section 4.2)*
- **Relevance for Section 6:** The purged cross-validation methodology directly addresses look-ahead bias in time-series ML. The concept of "information leakage" through overlapping labels applies to text-based features where the publication timestamp may not match the information availability timestamp.
- Status: `[ ] Unverified`

---

### 6.3 Contextual: Backtest Overfitting

**Bailey, David H., Jonathan M. Borwein, Marcos López de Prado, and Qiji Jim Zhu. "The Probability of Backtest Overfitting." *Journal of Computational Finance* 20, no. 4 (2017): 39–69.**

- DOI: `10.21314/JCF.2016.322`
- **Type:** Peer-reviewed journal article.
- **Summary:** Develops a formal framework for quantifying the probability that a backtest is overfit (PBO). Shows that as the number of strategy variants tested increases, the probability of selecting a strategy that performs well in-sample but poorly out-of-sample rises rapidly.
- **Relevance:** *Section 6.* Text-based NLP makes backtest overfitting worse because the researcher has many degrees of freedom: choice of sentiment model, aggregation window, normalization method, threshold for signal generation. Each choice is effectively a strategy variant, inflating PBO.
- **How to use:** Cite to formalize the overfitting risk specific to NLP-based signal construction. The "many degrees of freedom" argument is particularly salient for text features.
- **Cross-reference:** Also relevant to Chapter 11 (Backtesting and Evaluation).
- Status: `[ ] Unverified`

---

## 7. Signal Decay and Alpha Persistence

### 7.1 Empirical: Alpha Decay

**Di Mascio, Rick, Anton Lines, and Narayan Y. Naik. "Alpha Decay." Working paper, Columbia University and Inalytics, 2016.**

- URL: `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2580551`
- **Type:** Working paper.
- **Summary:** Studies how alpha decays after portfolio construction. Shows that alpha is strongest shortly after the signals used to construct portfolios are first available and decays as the information ages. Relevant to understanding the half-life of text-based trading signals.
- **Relevance:** *Section 2 (Temporal Aggregation) and Section 7 (Signal Decay).* Alpha decay determines the optimal holding period and rebalancing frequency for sentiment-based strategies. A signal with a 3-day half-life should drive different trading rules than one with a 30-day half-life.
- **How to use:** Cite to frame the signal decay question. Connect to temporal aggregation: the exponential decay parameter in signal construction should approximately match the empirical alpha decay rate.
- Status: `[ ] Unverified`

---

## 8. Cross-Cutting Survey References

**Kearney, Colm, and Sha Liu. "Textual Sentiment in Finance: A Survey of Methods and Models." *International Review of Financial Analysis* 33 (May 2014): 171–185.**

- DOI: `10.1016/j.irfa.2014.02.006`
- **Summary:** Surveys methods and models for financial textual sentiment, covering signal construction approaches.
- **Relevance:** General survey context for the chapter.
- **Cross-reference:** Already cited in Chapters 1 and 3 research.
- Status: `[ ] Unverified`

---

**Gentzkow, Matthew, Bryan Kelly, and Matt Taddy. "Text as Data." *Journal of Economic Literature* 57, no. 3 (September 2019): 535–574.**

- DOI: `10.1257/jel.20181020`
- **Summary:** Canonical text-as-data survey, including discussion of how text features are constructed for economic prediction.
- **Relevance:** Methodological foundation for text-to-signal pipeline.
- **Cross-reference:** Already cited in Chapters 1–3 research.
- Status: `[ ] Unverified`

---

## Cross-Chapter References

| Source | Ch 5 Section | Also Relevant To |
|--------|-------------|------------------|
| Baker & Wurgler (2006) | Sec 1, 3 (Sentiment Index) | Ch 10 (Regime Detection) |
| Baker & Wurgler (2007) | Sec 1 (Survey) | Ch 1 (Background) |
| García (2013) | Sec 1, 4 (Regime-Dependent) | Ch 7 (Central Bank — recessions), Ch 10 (Regime) |
| Ke, Kelly & Xiu (2019) | Sec 1, 2 (Supervised Sentiment) | Ch 4 (ML Methods) |
| Renault (2017) | Sec 2 (Intraday) | Ch 8 (Social Media) |
| Tetlock (2007) | Sec 2 (Signal Decay) | Ch 1 (Foundational) |
| Manela & Moreira (2017) | Sec 3 (Cross-Asset) | Ch 1, Ch 2 |
| López de Prado (2018) | Sec 4, 6 (Normalization, Bias) | Ch 11 (Backtesting) |
| Bailey et al. (2017) | Sec 6 (Overfitting) | Ch 11 (Backtesting) |
| Glasserman & Lin (2023) | Sec 6 (LLM Bias) | Ch 4 (LLM Workflows), Ch 13 (Limits) |
| Zha et al. (2024) | Sec 5 (Multi-Modal Fusion) | Ch 9 (Knowledge Graphs — graph + text) |
| Li et al. (2023) | Sec 5 (Multi-Modal Credit) | Ch 6 (Corporate Disclosure) |
| Di Mascio et al. (2016) | Sec 7 (Alpha Decay) | Ch 11 (Evaluation) |

---

## Research Gaps

The following areas need additional sourcing:

- [ ] **Exponential decay parameter selection** — Need a study that empirically calibrates exponential decay half-lives for different financial text sources (news articles vs. earnings calls vs. social media). The optimal half-life likely differs by source: social media sentiment may decay in hours, earnings call tone in days, 10-K risk factors in quarters.
- [ ] **Z-score vs. percentile ranking for sentiment** — Need an empirical comparison of z-score normalization vs. percentile ranking for sentiment signals across different market regimes. This is a practical question with real P&L implications.
- [ ] **Event-time vs. calendar-time aggregation** — Need a paper that directly compares event-time aggregation (aligned to earnings dates, FOMC meetings) vs. calendar-time (daily/weekly rolling) for sentiment signals. The choice affects signal characteristics (smoothness, responsiveness, trading frequency).
- [ ] **Bali, Engle, Murray on conditional risk measures** — The notes mention this reference for regime-conditional normalization. Search for Bali, Engle, and Murray's work on time-varying risk measures and conditional normalization.
- [ ] **Point-in-time database design for text features** — Need references on database architecture for storing text features with strict point-in-time semantics (avoiding survivorship bias from deleted social media posts, revised filings, etc.).
- [ ] **Cross-asset sentiment: equity → credit and equity → commodities** — Need specific papers showing text-based sentiment spillover from equity markets to credit spreads, commodity prices, and implied volatility surfaces. The theoretical mechanism is clear but empirical evidence may be sparse.
- [ ] **Production sentiment index examples from quant firms** — Industry papers or working papers from AQR, Two Sigma, or Man Group documenting their sentiment index construction methodology.

---

## Verification Priority

Start SMU Library verification with these sources first:

1. **Baker & Wurgler (2006)** — Sentiment index construction (foundational)
2. **García (2013)** — Text-based sentiment, regime-dependence (central to chapter)
3. **Ke, Kelly & Xiu (2019)** — Supervised text-to-signal methodology
4. **Glasserman & Lin (2023)** — LLM-specific look-ahead bias (novel, critical)
5. **López de Prado (2018)** — Purged CV, backtest overfitting (methodology)
6. **Baker & Wurgler (2007)** — Sentiment survey (JEP)
7. **Renault (2017)** — Intraday sentiment aggregation
8. **Bailey et al. (2017)** — Probability of Backtest Overfitting
9. **Di Mascio et al. (2016)** — Alpha decay
10. **Zha et al. (2024)** — Multi-modal fusion (EMNLP)

---

*Research compiled April 2026. All citations require manual verification through SMU Library before inclusion in final manuscript.*
