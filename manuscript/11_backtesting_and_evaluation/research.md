# Chapter 11 — Backtesting and Evaluation — Annotated Bibliography

**Purpose:** This chapter teaches rigorous evaluation methodology specific to NLP-based trading strategies. It addresses backtest overfitting, time-series validation, financial performance metrics, NLP-specific evaluation (ablation, feature importance), benchmark design, transaction costs, and common failure modes. The chapter is the book's methodological conscience.

**What this chapter needs from its sources:**
- Backtest overfitting theory and the multiple testing problem
- Time-series validation methods (walk-forward, purged CV, CPCV)
- Financial performance metrics with proper statistical inference (Sharpe, Calmar, IR)
- Feature importance and explainability methods (SHAP, ablation)
- Transaction cost modeling for event-driven strategies
- Survivorship bias, look-ahead bias, and data snooping in NLP contexts
- Post-publication alpha decay evidence
- Fair benchmark construction for text-based strategies

**Citation format:** Chicago (Notes and Bibliography), 17th edition.

**Note on chapter tone:** This chapter is deliberately cautionary. The preceding chapters show what NLP *can* do; this chapter shows how to rigorously verify that it actually *did*. The sources are drawn from the "skeptical" wing of quantitative finance — researchers who study why backtests lie and how multiple testing inflates apparent performance.

---

## 1. The Backtest Overfitting Problem

### 1.1 Foundational: Probability of Backtest Overfitting

**Bailey, David H., Jonathan M. Borwein, Marcos López de Prado, and Qiji Jim Zhu. "The Probability of Backtest Overfitting." *Journal of Computational Finance* 20, no. 4 (2017): 39–69.**

- DOI: `10.21314/JCF.2016.322`
- **Type:** Peer-reviewed journal article.
- **Summary:** Develops a formal framework for quantifying the probability that a backtest is overfit (PBO). As the number of strategy variants tested increases, the probability of selecting a strategy that performs well in-sample but poorly out-of-sample rises rapidly. Provides a computable PBO metric.
- **Relevance:** *Section 1 (Backtest Overfitting).* The foundational reference for the chapter's core warning. NLP makes the overfitting problem *worse* because the researcher has enormous degrees of freedom: choice of sentiment model (VADER, L-M, FinBERT, GPT-4), aggregation window (1 day, 5 days, 20 days), normalization method (z-score, percentile), and signal threshold. Each combination is an implicit strategy variant.
- **How to use:** Open the chapter with the PBO framework. Calculate how many implicit strategy variants a typical NLP pipeline generates. For example: 4 sentiment models × 5 aggregation windows × 3 normalizations × 3 thresholds = 180 variants — enough for high PBO even with moderate Sharpe ratios.
- **Cross-reference:** Already cited in Chapters 5 and 10 research.
- Status: `[ ] Unverified`

---

### 1.2 Foundational: Multiple Testing in Financial Research

**Harvey, Campbell R., Yan Liu, and Heqing Zhu. "… and the Cross-Section of Expected Returns." *Review of Financial Studies* 29, no. 1 (January 2016): 5–68.**

- DOI: `10.1093/rfs/hhv059`
- **Type:** Peer-reviewed journal article (top-3 finance journal).
- **Summary:** Addresses the "factor zoo" problem: hundreds of papers claim to find factors that predict stock returns, but given extensive data mining, the usual significance criteria (t > 2.0) are insufficient. Introduces a multiple testing framework with time-varying significance cutoffs. A newly discovered factor needs t > 3.0 to be credible. Argues that most claimed research findings in financial economics are likely false.
- **Relevance:** *Section 1 (Backtest Overfitting).* The most influential paper on multiple testing in finance. Text-based signals are subject to the same critique: if hundreds of researchers have tried different text features, tokenizations, and aggregations to predict returns, the bar for statistical significance must be raised. The t > 3.0 threshold directly applies to evaluating NLP-based strategies.
- **How to use:** Central to Section 1. Present the Harvey-Liu-Zhu threshold as the standard NLP-based strategies must meet. The "most claimed findings are likely false" conclusion is provocative but essential for honest evaluation.
- Status: `[ ] Unverified`

---

### 1.3 Foundational: Data Snooping Bootstrap Test

**White, Halbert. "A Reality Check for Data Snooping." *Econometrica* 68, no. 5 (September 2000): 1097–1126.**

- DOI: `10.1111/1468-0262.00152`
- **Type:** Peer-reviewed journal article.
- **Summary:** Provides a bootstrap-based procedure for testing whether the best model from a specification search has genuine predictive superiority over a benchmark. Constructs p-values that account for the full set of models tested, not just the selected winner. Addresses the fundamental problem that the "best" model from a large search will appear to outperform even when no model genuinely does.
- **Relevance:** *Section 1 (Data Snooping) and Section 5 (Benchmark Construction).* White's Reality Check is the formal statistical solution to data snooping. For NLP strategies, it provides a test of whether the "best" combination of text features, model, and parameters actually outperforms a benchmark after accounting for the full search over alternatives.
- **How to use:** Cite as the formal test for data snooping. Pair with Harvey-Liu-Zhu (2016) — Harvey addresses the t-statistic threshold, White provides the bootstrap test.
- Status: `[ ] Unverified`

---

## 2. Validation Approaches for Time-Series

### 2.1 Foundational: Purged Cross-Validation

**López de Prado, Marcos. *Advances in Financial Machine Learning*. Hoboken, NJ: Wiley, 2018.**

- ISBN: `978-1-119-48208-6`
- **Type:** Book.
- **Summary:** Introduces purged k-fold cross-validation (removing training observations whose labels overlap with test labels), embargo periods to prevent information leakage, and Combinatorial Purged Cross-Validation (CPCV) for generating multiple backtest paths from a single dataset. Also covers meta-labeling, fractional differentiation, and structural breaks.
- **Relevance:** *Section 2 (Validation).* The primary reference for time-series-appropriate validation methods. Standard k-fold CV is inappropriate for financial time series because it leaks future information into the training set. Purged CV and CPCV solve this for NLP features where label overlap (e.g., sentiment computed over a window that straddles train/test boundaries) is a specific concern.
- **How to use:** Central to Section 2. Walk through why standard CV fails for NLP features (temporal autocorrelation in text sentiment, overlapping windows), then present purged CV and CPCV as the solutions. Provide implementation guidance in the companion code.
- **Cross-reference:** Already cited in Chapters 5 and 10 research.
- Status: `[ ] Unverified`

---

## 3. Financial Performance Metrics

### 3.1 Foundational: Sharpe Ratio Statistics

**Lo, Andrew W. "The Statistics of Sharpe Ratios." *Financial Analysts Journal* 58, no. 4 (July–August 2002): 36–52.**

- DOI: `10.2469/faj.v58.n4.2453`
- **Type:** Peer-reviewed journal article.
- **Summary:** Derives the statistical distribution of the Sharpe ratio under multiple assumptions: IID returns, stationary returns, and with time aggregation. Shows that the common practice of annualizing monthly Sharpe ratios by multiplying by √12 is only valid under IID assumptions. With serial correlation (common in NLP-based strategies that hold positions over multiple days), annual Sharpe ratios can be overstated by up to 65%. Once serial correlation is properly accounted for, hedge fund rankings change dramatically.
- **Relevance:** *Section 3 (Performance Metrics).* The definitive reference for proper Sharpe ratio inference. NLP-based strategies are particularly susceptible to Sharpe inflation because (1) sentiment signals are autocorrelated, and (2) event-driven strategies generate clustered returns. Lo's correction is essential for honest evaluation.
- **How to use:** Central to Section 3. Present Lo's correction alongside the standard Sharpe formula. The 65% overstatement finding is a concrete, memorable number. Show readers how to compute the corrected Sharpe ratio accounting for serial correlation.
- Status: `[ ] Unverified`

---

## 4. NLP-Specific Evaluation

### 4.1 Foundational: Feature Importance and Explainability

**Lundberg, Scott M., and Su-In Lee. "A Unified Approach to Interpreting Model Predictions." In *Advances in Neural Information Processing Systems 30 (NeurIPS 2017)*, 4765–4774. Long Beach, CA, 2017.**

- URL: `https://arxiv.org/abs/1705.07874`
- **Type:** Peer-reviewed conference paper (NeurIPS).
- **Summary:** Introduces SHAP (SHapley Additive exPlanations), a unified framework assigning each feature an importance value for individual predictions. Based on Shapley values from game theory, SHAP provides theoretically grounded, consistent feature attributions. Unifies six existing explanation methods and shows improved computational performance and human-intuition consistency.
- **Relevance:** *Section 4 (NLP-Specific Evaluation).* SHAP values provide the tool for answering "which text features actually drove this prediction?" For NLP-based strategies, SHAP can decompose a regime label or return prediction into contributions from individual text features (earnings call tone, FOMC hawk/dove score, social media volume, etc.), enabling ablation studies that verify genuine signal.
- **How to use:** Cite as the feature importance methodology. Show how SHAP values answer the critical question: "Is this model working because of genuine linguistic signal, or because of spurious correlations?" A model where SHAP attributes most importance to a single text feature (e.g., earnings call word count) rather than linguistically meaningful features is suspicious.
- Status: `[ ] Unverified`

---

## 5. Benchmark Construction

### 5.1 Foundational: Fair Baselines for Text Strategies

**Loughran, Tim, and Bill McDonald. "When Is a Liability Not a Liability? Textual Analysis, Dictionaries, and 10-Ks." *Journal of Finance* 66, no. 1 (February 2011): 35–65.**

- DOI: `10.1111/j.1540-6261.2010.01625.x`
- **Summary:** Loughran-McDonald dictionary with six financial sentiment word lists.
- **Relevance:** *Section 5 (Benchmark Construction).* The L-M dictionary provides the simplest credible text-based benchmark. Any sophisticated NLP strategy must demonstrably outperform an L-M dictionary baseline to justify its additional complexity. If FinBERT can't beat a word-counting approach using L-M, the transformer overhead isn't warranted.
- **How to use:** Present the L-M dictionary as Benchmark Tier 2 (above buy-and-hold but below the NLP strategy being tested). The benchmark ladder: (1) buy-and-hold, (2) L-M dictionary sentiment, (3) VADER/TextBlob, (4) the proposed NLP strategy.
- **Cross-reference:** Already cited in Chapters 1, 3, and 4 research.
- Status: `[ ] Unverified`

---

## 6. Transaction Costs, Slippage, and Market Impact

### 6.1 Empirical: Real-World Trading Costs

**Frazzini, Andrea, Ronen Israel, and Tobias J. Moskowitz. "Trading Costs." Working paper, AQR Capital Management, 2018.**

- URL: `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3229719`
- **Type:** Working paper (industry research).
- **Summary:** Uses $1.7 trillion of live trade execution data from a large institutional money manager across 21 developed equity markets over 19 years to measure real-world trading costs and price impact. Finds actual trading costs to be an order of magnitude smaller than previous academic studies suggest. Provides a novel description of how costs vary across trade type, stock characteristics, trade size, time, and exchanges.
- **Relevance:** *Section 6 (Transaction Costs).* The most comprehensive empirical study of real-world trading costs. Provides the cost estimates readers should use when evaluating NLP-based strategies. The "order of magnitude smaller than academic estimates" finding means that many NLP strategies that appear unprofitable under pessimistic cost assumptions may actually be viable.
- **How to use:** Cite for realistic cost estimates. Note the caveat: Frazzini et al. measure costs for a large institutional trader with sophisticated execution — a retail trader or smaller fund would face higher costs. Present a cost sensitivity analysis showing how strategy profitability changes across cost assumptions.
- Status: `[ ] Unverified`

---

## 7. Common Failure Modes

### 7.1 Foundational: Post-Publication Alpha Decay

**McLean, R. David, and Jeffrey Pontiff. "Does Academic Research Destroy Stock Return Predictability?" *Journal of Finance* 71, no. 1 (February 2016): 5–32.**

- DOI: `10.1111/jofi.12365`
- **Type:** Peer-reviewed journal article (top-3 finance journal).
- **Summary:** Reconstructs 82–97 published cross-sectional return predictors. Portfolio returns are 26% lower out-of-sample and 58% lower post-publication. The 32% difference (58% − 26%) is attributable to publication-informed trading. Post-publication, characteristic portfolios experience higher volume, variance, and short interest — evidence of arbitrage activity degrading the signal.
- **Relevance:** *Section 7 (Failure Modes — Alpha Decay).* The most rigorous study of post-publication alpha decay. Directly relevant to NLP-based strategies: if a text feature's predictive power is documented in an academic paper, that power will degrade as other traders implement it. The 58% post-publication decay is a sobering number.
- **How to use:** Central to the alpha decay discussion. Frame it as a warning: the NLP strategies this book teaches will face the same competitive decay once they become widely known. This motivates continuous innovation and proprietary feature engineering rather than relying on published recipes.
- Status: `[ ] Unverified`

---

### 7.2 Empirical: Look-Ahead Bias in LLM Backtests

**Glasserman, Paul, and Caden Lin. "Assessing Look-Ahead Bias in Stock Return Predictions Generated by GPT Sentiment Analysis." arXiv preprint, arXiv:2309.17322, September 2023.**

- URL: `https://arxiv.org/abs/2309.17322`
- **Type:** Preprint (Columbia University).
- **Summary:** Identifies two forms of LLM-specific look-ahead bias: (1) the model may "know" returns that followed historical news articles from its training data, and (2) general knowledge of named companies distorts sentiment measurement. Tests by comparing performance on original vs. de-biased headlines.
- **Relevance:** *Section 7 (Failure Modes — Look-Ahead Bias).* A new failure mode unique to the LLM era. If readers use GPT-4 or Claude to score sentiment on historical news for backtesting, the model's training data may include both the news *and* the subsequent returns, creating a direct information leak.
- **How to use:** Cite alongside traditional look-ahead bias sources. The de-biasing methodology (removing company identifiers) provides a practical mitigation. Recommend using models with known training cutoff dates and testing on post-cutoff data.
- **Cross-reference:** Already cited in Chapter 5 research.
- Status: `[ ] Unverified`

---

### 7.3 Contextual: Survivorship Bias in NLP

**Survivorship bias in NLP financial data** is addressed through the general observation that only 1.2% of studies (out of 164 reviewed from 2023–2025 across ML, NLP, and financial AI venues) acknowledged survivorship bias in their text datasets. Specific concerns include:

- Delisted companies disappearing from text corpora (news stops covering failed firms)
- Removed social media posts (deleted tweets, removed Reddit posts) creating a positivity bias
- LLM training data over-representing surviving firms due to corpus construction choices
- CRSP data showing 1.6% annualized return overstatement in survivorship-biased datasets (1926–2001)

*Dedicated paper reference needed — see Research Gaps.*

---

## 8. Cross-Cutting Survey References

**López de Prado, Marcos. *Advances in Financial Machine Learning*. Hoboken, NJ: Wiley, 2018.**

- *(See Section 2.1 above)*
- **Relevance for entire chapter:** Covers validation, overfitting, and evaluation in a unified framework.
- Status: `[ ] Unverified`

---

**Gentzkow, Matthew, Bryan Kelly, and Matt Taddy. "Text as Data." *Journal of Economic Literature* 57, no. 3 (September 2019): 535–574.**

- DOI: `10.1257/jel.20181020`
- **Summary:** Discusses evaluation and validation considerations specific to text-as-data methods in economics.
- **Cross-reference:** Already cited in Chapters 1–3 research.
- Status: `[ ] Unverified`

---

## Cross-Chapter References

| Source | Ch 11 Section | Also Relevant To |
|--------|-------------|------------------|
| Bailey et al. (2017) | Sec 1 (PBO) | Ch 5, Ch 10 |
| Harvey et al. (2016) | Sec 1 (Multiple Testing) | Foundational methodology |
| White (2000) | Sec 1 (Data Snooping) | Foundational methodology |
| López de Prado (2018) | Sec 2 (Purged CV) | Ch 5, Ch 10 |
| Lo (2002) | Sec 3 (Sharpe Ratio) | Ch 10 (Evaluation) |
| Lundberg & Lee (2017) | Sec 4 (SHAP) | Ch 4 (Model Explainability) |
| Loughran & McDonald (2011) | Sec 5 (Benchmark) | Ch 1, Ch 3 |
| Frazzini et al. (2018) | Sec 6 (Transaction Costs) | Ch 12 (Deployment) |
| McLean & Pontiff (2016) | Sec 7 (Alpha Decay) | Ch 5 (Signal Decay), Ch 8 (WSB alpha decay) |
| Glasserman & Lin (2023) | Sec 7 (LLM Bias) | Ch 4, Ch 5 |

---

## Research Gaps

The following areas need additional sourcing:

- [ ] **Survivorship bias in NLP text datasets** — Need a dedicated paper documenting survivorship bias mechanisms specific to financial text data (disappearing coverage of delisted firms, deleted social media posts, corpus construction choices). The 1.2% acknowledgment rate statistic comes from a 2025 arXiv survey — verify and cite properly.
- [ ] **Calmar ratio and maximum drawdown inference** — Need references on statistical properties and confidence intervals for the Calmar ratio and maximum drawdown, analogous to Lo (2002) for the Sharpe ratio. These metrics are mentioned in the chapter plan but lack dedicated methodology references.
- [ ] **Information ratio and benchmark selection** — Need a paper specifically addressing information ratio computation and benchmark selection for text-driven strategies. How to choose the right benchmark (market, sector, L-M dictionary strategy) is a design decision with major evaluation implications.
- [ ] **Ablation study methodology for NLP features** — Need references on structured ablation studies (removing one feature at a time, removing feature groups) specifically for financial NLP models. General ML ablation methodology may suffice, but financial-specific examples would strengthen the section.
- [ ] **Market impact around earnings announcements** — Need specific studies measuring bid-ask spread widening, depth reduction, and price impact during earnings call windows (typically 4:00–4:30 PM ET). Text-driven strategies that trade on earnings call sentiment face worst-case execution conditions.
- [ ] **Data snooping in NLP specifically** — Need a paper documenting how NLP researchers' degrees of freedom (model choice, tokenization, feature selection, window length, aggregation method) inflate apparent backtest performance. A financial NLP-specific version of Harvey-Liu-Zhu would be ideal.
- [ ] **Walk-forward validation with sentiment features** — Need a reference specifically implementing walk-forward validation for text-based financial features, addressing the temporal alignment challenge (how to handle sentiment features computed over rolling windows that straddle walk-forward boundaries).
- [ ] **Diebold-Mariano test for NLP forecast comparison** — Need the Diebold-Mariano (1995) forecast comparison test reference for comparing NLP-based forecasts against baseline forecasts. This is the appropriate statistical test for the benchmark comparison section.

---

## Verification Priority

Start SMU Library verification with these sources first:

1. **Harvey, Liu & Zhu (2016)** — Multiple testing framework (RFS — foundational)
2. **Lo (2002)** — Sharpe ratio statistics (FAJ — essential metrics reference)
3. **McLean & Pontiff (2016)** — Post-publication alpha decay (JF — key cautionary finding)
4. **Bailey et al. (2017)** — PBO (if not already verified from Ch 5/10)
5. **White (2000)** — Reality Check for data snooping (Econometrica)
6. **López de Prado (2018)** — AFML book (if not already verified)
7. **Lundberg & Lee (2017)** — SHAP framework (NeurIPS)
8. **Frazzini et al. (2018)** — Trading costs data
9. **Glasserman & Lin (2023)** — LLM look-ahead bias (if not already verified from Ch 5)
10. **Loughran & McDonald (2011)** — Benchmark baseline (if not already verified)

---

*Research compiled April 2026. All citations require manual verification through SMU Library before inclusion in final manuscript.*
