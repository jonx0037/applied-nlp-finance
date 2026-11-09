# Chapter 10 — Market Regime Detection — Annotated Bibliography

**Purpose:** This chapter presents the author's primary research contribution — sentiment-based market regime detection. It builds on the data pipelines from Chapters 6–9, surveys existing quantitative regime detection methods, argues that text-derived features are complementary, presents a cross-asset sentiment regime detector architecture, and includes case studies from COVID, the 2022 rate hiking cycle, and crypto contagion events.

**What this chapter needs from its sources:**
- Foundational regime switching models (Hamilton, Ang-Bekaert)
- HMM and clustering approaches for financial regime detection
- Evidence that text/sentiment features add value beyond price/volume for regime identification
- Multi-modal regime feature construction (text + price + graph topology)
- Regime detection evaluation methodology
- Case study data: COVID crash, 2022 rate cycle, Terra/Luna, FTX
- News-to-risk-and-return prediction at the country/market level

**Citation format:** Chicago (Notes and Bibliography), 17th edition.

**Note on chapter positioning:** This chapter draws from the author's SMU MSDS capstone project and represents the book's primary original research contribution. The argument — that narrative shifts precede statistical regime changes — is a testable, novel claim. The chapter integrates virtually all prior chapters: sentiment models (Ch 4–5), earnings call features (Ch 6), central bank tone (Ch 7), social media signals (Ch 8), and graph topology (Ch 9).

---

## 1. What Is a Market Regime?

### 1.1 Foundational: Regime Switching Models

**Hamilton, James D. "A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle." *Econometrica* 57, no. 2 (March 1989): 357–384.**

- DOI: `10.2307/1912559`
- **Type:** Peer-reviewed journal article. Over 10,000 citations.
- **Summary:** Proposes modeling changes in regime as a discrete-state Markov process governing the parameters of an autoregression. Develops algorithms for inferring unobserved regime shifts and estimating parameters by maximum likelihood. The foundational paper for all Markov regime-switching models in economics and finance.
- **Relevance:** *Section 1 (What Is a Regime?) and Section 2 (Existing Methods).* The starting point for the entire chapter. Hamilton's definition of a regime — a persistent state with distinct statistical properties — is the definition the chapter uses. The Markov switching framework is the baseline against which the sentiment-based approach is compared.
- **How to use:** Open the chapter with Hamilton's framework. Define regimes as persistent states with stable distributional properties. Then explain why price-based regime detection is *inherently reactive* — it requires observing enough data *from within* a regime to identify it, creating a detection lag.
- Status: `[ ] Unverified`

---

### 1.2 Foundational: Regime Switching in Financial Markets

**Ang, Andrew, and Geert Bekaert. "Regime Switches in Interest Rates." *Journal of Business & Economic Statistics* 20, no. 2 (April 2002): 163–182.**

- DOI: `10.1198/073500102317351930`
- **Type:** Peer-reviewed journal article.
- **Summary:** Examines regime-switching models for interest rates in the US, Germany, and UK. Finds that regime-switching models forecast better out-of-sample than single-regime models. Regimes correspond reasonably well with business cycles. International information (cross-country short rates and term spreads) improves regime classification.
- **Relevance:** *Section 2 (Existing Methods).* Establishes that regime-switching works for fixed income and that cross-asset information improves detection — a finding that directly supports the chapter's cross-asset sentiment approach.
- **How to use:** Cite alongside Hamilton (1989) as the key financial application. The cross-asset improvement finding foreshadows the chapter's argument that cross-asset *text* features improve regime detection even further.
- Status: `[ ] Unverified`

---

**Guidolin, Massimo, and Allan Timmermann. "Asset Allocation under Multivariate Regime Switching." *Journal of Economic Dynamics and Control* 31, no. 11 (November 2007): 3503–3544.**

- DOI: `10.1016/j.jedc.2006.12.004`
- **Type:** Peer-reviewed journal article.
- **Summary:** Identifies four distinct regimes in joint stock-bond return distributions — crash, slow growth, bull, and recovery — using multivariate regime-switching models. Optimal asset allocations vary considerably across regimes. In crash states, longer-horizon investors allocate more to stocks; in bull markets, the opposite. Out-of-sample tests confirm economic importance.
- **Relevance:** *Section 1 (Regime Taxonomy).* The four-regime taxonomy (crash, slow growth, bull, recovery) provides a concrete framework the chapter can adopt or adapt. The asset allocation implications demonstrate *why* regime detection matters economically.
- **How to use:** Cite for the four-regime taxonomy. Each regime has distinct characteristics that text features can help identify: crash regimes coincide with extreme negative sentiment; bull regimes with consensus optimism; recovery regimes with cautious but improving narrative tone.
- Status: `[ ] Unverified`

---

## 2. Existing Quantitative Regime Detection Methods

### 2.1 Methodological: HMM for Market Regimes

**Nystrup, Peter, Bo William Hansen, Henrik Madsen, and Erik Lindström. "Regime-Based Versus Static Asset Allocation: Letting the Data Speak." *Journal of Portfolio Management* 42, no. 1 (Fall 2015): 103–109.**

- DOI: `10.3905/jpm.2015.42.1.103`
- **Type:** Peer-reviewed journal article.
- **Summary:** Investigates whether HMM-based regime detection can improve asset allocation over a static 60/40 benchmark. Uses a two-state HMM to detect high-volatility and low-volatility regimes. Finds regime-based allocation outperforms static allocation, particularly during crisis periods.
- **Relevance:** *Section 2 (Existing Methods — HMM).* The primary practical reference for HMM-based regime detection in portfolio management. Establishes the performance baseline the sentiment-based approach must beat or complement.
- **How to use:** Cite as the HMM baseline. The two-state (high-vol / low-vol) model is the simplest regime detector — the chapter's multi-modal approach adds text features to detect regimes that pure volatility clustering misses (e.g., a regime where volatility is low but narrative tone has shifted hawkish).
- Status: `[ ] Unverified`

---

## 3. Why Sentiment-Based Regime Detection Is Complementary

### 3.1 Foundational: Sentiment Predicts Returns Conditionally

**García, Diego. "Sentiment during Recessions." *Journal of Finance* 68, no. 3 (June 2013): 1267–1300.**

- DOI: `10.1111/jofi.12027`
- **Type:** Peer-reviewed journal article.
- **Summary:** Text-based sentiment predicts stock returns in recessions but not in expansions. One standard deviation sentiment shock in recessions predicts 12bp daily return change.
- **Relevance:** *Section 3 (Why Sentiment Is Complementary).* The core empirical justification for combining sentiment with regime models. If sentiment's predictive power is regime-dependent, then jointly modeling sentiment and regimes should outperform either alone — sentiment helps identify regimes, and regime context helps interpret sentiment.
- **How to use:** Present as the key motivating evidence. The regime-conditional predictability creates a natural synergy between sentiment and regime detection: you need regimes to interpret sentiment, and you need sentiment to detect regimes. This virtuous circle is the chapter's central argument.
- **Cross-reference:** Already cited in Chapters 1 and 5 research.
- Status: `[ ] Unverified`

---

### 3.2 Empirical: News Drives Risk and Returns Globally

**Calomiris, Charles W., and Harry Mamaysky. "How News and Its Context Drive Risk and Returns around the World." *Journal of Financial Economics* 133, no. 2 (August 2019): 299–336.**

- DOI: `10.1016/j.jfineco.2018.11.009`
- **Type:** Peer-reviewed journal article.
- **Summary:** Develops classification methodology for news article content and context to predict risk and return across 51 countries. A parsimonious summary of news — topic-specific sentiment, frequency, and unusualness (entropy) of word flow — predicts future country-level returns, volatilities, and drawdowns. Economic significance is high and *larger for year-ahead than monthly predictions*. News about emerging markets contains more incremental information.
- **Relevance:** *Section 3 (Why Sentiment Is Complementary) and Section 4 (Architecture).* The strongest evidence that text-derived features predict market risk states (volatility, drawdowns) at the country level. The "entropy" feature — unusualness of word flow — is a particularly creative text feature that captures narrative regime shifts. The longer-horizon predictability (year-ahead > monthly) suggests that text captures slow-moving regime information.
- **How to use:** Central to the "complementary" argument. The entropy feature (measuring how unusual the current news flow is relative to history) is directly applicable as a regime transition indicator — highly unusual news flow signals a regime change.
- Status: `[ ] Unverified`

---

### 3.3 Empirical: Narrative-Driven Risk Assessment

**Manela, Asaf, and Alan Moreira. "News Implied Volatility and Disaster Concerns." *Journal of Financial Economics* 123, no. 1 (January 2017): 137–162.**

- DOI: `10.1016/j.jfineco.2016.01.032`
- **Type:** Peer-reviewed journal article.
- **Summary:** NVIX peaks during crashes, wars, and crises. High NVIX predicts above-average returns after controlling for VIX. 130-year time span demonstrates text signal persistence.
- **Relevance:** *Section 3.* NVIX is effectively a text-based regime indicator — it spikes during disaster/crisis regimes and subsides during calm regimes. The finding that it predicts returns *beyond* VIX means text captures regime information not in price-based volatility measures.
- **Cross-reference:** Already cited in Chapters 1, 2, and 5 research.
- Status: `[ ] Unverified`

---

## 4. Cross-Asset Sentiment Regime Detector: Architecture

### 4.1 Methodological: Multi-Modal Feature Fusion

**Zha, Daochen, Zaid Pervaiz Bhat, and Xia Hu. "Financial Forecasting from Textual and Tabular Time Series." In *Findings of the Association for Computational Linguistics: EMNLP 2024*. Miami, FL: Association for Computational Linguistics, November 2024.**

- URL: `https://aclanthology.org/2024.findings-emnlp.486/`
- **Type:** Peer-reviewed conference paper.
- **Summary:** Multi-modal method combining text features with tabular financial variables through cross-modality fusion.
- **Relevance:** *Section 4 and Section 6 (Multi-Modal Features).* The architectural foundation for combining text-derived sentiment features with price/volume features and graph topology features in the regime detector.
- **Cross-reference:** Already cited in Chapters 5 and 9 research.
- Status: `[ ] Unverified`

---

### 4.2 Methodological: Graph Topology as Regime Feature

**Billio, Monica, Mila Getmansky, Andrew W. Lo, and Loriana Pelizzon. "Econometric Measures of Connectedness and Systemic Risk in the Finance and Insurance Sectors." *Journal of Financial Economics* 104, no. 3 (June 2012): 535–559.**

- DOI: `10.1016/j.jfineco.2011.12.010`
- **Type:** Peer-reviewed journal article.
- **Summary:** Six centrality measures quantify systemic connectedness. Betweenness centrality identifies nodes controlling systemic risk propagation. Network topology changes signal regime shifts.
- **Relevance:** *Section 4 (Architecture) and Section 6 (Multi-Modal Features).* Graph centrality metrics from financial knowledge graphs (Chapter 9) serve as regime features. Rapid changes in betweenness centrality — when the "importance" of a node in the financial network shifts suddenly — signal structural regime transitions.
- **Cross-reference:** Already cited in Chapter 9 research.
- Status: `[ ] Unverified`

---

## 5. Case Studies

### 5.1 COVID Market Crash (February–March 2020)

**Baker, Scott R., Nicholas Bloom, Steven J. Davis, Kyle Kost, Marco Sammon, and Tasaneeya Viratyosin. "The Unprecedented Stock Market Reaction to COVID-19." *Review of Asset Pricing Studies* 10, no. 4 (December 2020): 742–758.**

- DOI: `10.1093/rapstu/raaa008`
- **Type:** Peer-reviewed journal article.
- **Summary:** Documents that no previous infectious disease outbreak (including the Spanish Flu) affected the stock market as forcefully as COVID-19. The paper uses text-based methods to decompose the drivers: government-imposed restrictions and the voluntary social distancing response (not the disease itself) drove the crash. Text analysis of news and policy documents identifies the causal mechanism.
- **Relevance:** *Section 8 (Case Studies — COVID).* The primary academic reference for the COVID market crash. The text-based decomposition methodology (what drove the crash?) is directly applicable to the regime detection framework — sentiment features can distinguish between disease-fear sentiment and policy-response sentiment.
- **How to use:** Central to the COVID case study. Show how sentiment shifted rapidly from "disease risk" to "lockdown impact" to "stimulus optimism" — each representing a distinct narrative sub-regime within the broader crisis.
- Status: `[ ] Unverified`

---

### 5.2 Crypto Contagion (Terra/Luna, FTX)

**Conlon, Thomas, Shaen Corbet, and Yang Hu. "Understanding the Contagion Effects of the FTX Exchange Collapse." Working paper, SSRN, 2023.**

- URL: `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4640797`
- **Type:** Working paper.
- **Summary:** Analyzes contagion effects from the FTX collapse. Finds that the FTX signature differed from Terra/Luna — FTX produced a more modest change in total cross-market connectedness but the most significant increase in *internal* (within-crypto) spillovers.
- **Relevance:** *Section 8 (Case Studies — Crypto Contagion).* Provides quantitative contagion analysis for the FTX case study. The contrast between Terra/Luna (broad cross-market contagion) and FTX (concentrated internal contagion) illustrates how different crisis types produce different regime characteristics.
- **How to use:** Pair Terra/Luna and FTX as contrasting contagion case studies. Show how social media text signals preceded price-based contagion detection in both cases but with different sentiment dynamics.
- Status: `[ ] Unverified`

---

### 5.3 2022 Rate Hiking Cycle

**Gorodnichenko, Yuriy, Tho Pham, and Oleksandr Talavera. "The Voice of Monetary Policy." *American Economic Review* 113, no. 2 (February 2023): 548–584.**

- DOI: `10.1257/aer.20220129`
- **Summary:** Fed chair vocal tone moves markets beyond text content. Demonstrates that communication style (not just content) carries regime-relevant information.
- **Relevance:** *Section 8 (Case Studies — 2022 Rate Cycle).* The 2022 hiking cycle was characterized by a dramatic shift in Fed communication tone — from "transitory inflation" to aggressive tightening rhetoric. This paper's methodology (text + audio analysis) applies directly to tracking the communication regime transition.
- **Cross-reference:** Already cited in Chapter 7 research.
- Status: `[ ] Unverified`

---

## 6. Multi-Modal Regime Features

### 6.1 Empirical: Sentiment and Volatility Regimes

**Baker, Malcolm, and Jeffrey Wurgler. "Investor Sentiment and the Cross-Section of Stock Returns." *Journal of Finance* 61, no. 4 (August 2006): 1645–1680.**

- DOI: `10.1111/j.1540-6261.2006.00885.x`
- **Summary:** Sentiment index from market-based proxies predicts cross-sectional returns differently in high-sentiment vs. low-sentiment periods.
- **Relevance:** *Section 6 (Multi-Modal Features).* Baker-Wurgler's sentiment index is itself a regime indicator. High-sentiment and low-sentiment periods are effectively regimes with different return dynamics. Adding text-based sentiment to their market-based proxies creates a richer multi-modal regime characterization.
- **Cross-reference:** Already cited in Chapter 5 research.
- Status: `[ ] Unverified`

---

## 7. Evaluating Regime Detectors

### 7.1 Methodological: Backtest Rigor

**López de Prado, Marcos. *Advances in Financial Machine Learning*. Hoboken, NJ: Wiley, 2018.**

- ISBN: `978-1-119-48208-6`
- **Summary:** Purged cross-validation, CPCV, and Probability of Backtest Overfitting frameworks.
- **Relevance:** *Section 7 (Evaluation).* Regime detection evaluation requires specialized methods because standard train/test splits violate temporal structure. López de Prado's purged CV prevents information leakage across regime boundaries. The PBO framework quantifies overfitting risk when testing multiple regime definitions.
- **Cross-reference:** Already cited in Chapter 5 research.
- Status: `[ ] Unverified`

---

**Bailey, David H., Jonathan M. Borwein, Marcos López de Prado, and Qiji Jim Zhu. "The Probability of Backtest Overfitting." *Journal of Computational Finance* 20, no. 4 (2017): 39–69.**

- DOI: `10.21314/JCF.2016.322`
- **Summary:** Formal framework for quantifying probability of backtest overfitting.
- **Relevance:** *Section 7.* Regime detectors are particularly susceptible to overfitting because the researcher has many degrees of freedom: number of regimes, feature selection, transition probability specification, and evaluation window.
- **Cross-reference:** Already cited in Chapter 5 research.
- Status: `[ ] Unverified`

---

## Cross-Chapter References

| Source | Ch 10 Section | Also Relevant To |
|--------|-------------|------------------|
| Hamilton (1989) | Sec 1, 2 (Regime Foundation) | Foundational |
| Ang & Bekaert (2002) | Sec 2 (Interest Rate Regimes) | Ch 7 (Central Bank) |
| Guidolin & Timmermann (2007) | Sec 1 (Regime Taxonomy) | Ch 11 (Portfolio Evaluation) |
| Nystrup et al. (2015) | Sec 2 (HMM Baseline) | Ch 11 (Backtesting) |
| García (2013) | Sec 3 (Regime-Conditional Sentiment) | Ch 1, Ch 5 |
| Calomiris & Mamaysky (2019) | Sec 3, 4 (News → Risk/Returns) | Ch 5 (Signal Construction) |
| Manela & Moreira (2017) | Sec 3 (NVIX as Regime Indicator) | Ch 1, Ch 2, Ch 5 |
| Billio et al. (2012) | Sec 4, 6 (Graph Topology) | Ch 9 (Knowledge Graphs) |
| Baker et al. (2020) | Sec 8 (COVID Case Study) | Ch 13 (Tail Events) |
| Conlon et al. (2023) | Sec 8 (Crypto Contagion) | Ch 8 (Social Media) |
| Gorodnichenko et al. (2023) | Sec 8 (Rate Cycle) | Ch 7 (Central Bank) |
| Baker & Wurgler (2006) | Sec 6 (Sentiment Regimes) | Ch 5 |
| López de Prado (2018) | Sec 7 (Evaluation) | Ch 5, Ch 11 |
| Bailey et al. (2017) | Sec 7 (PBO) | Ch 5, Ch 11 |
| Zha et al. (2024) | Sec 4, 6 (Multi-Modal Fusion) | Ch 5, Ch 9 |

---

## Research Gaps

The following areas need additional sourcing:

- [ ] **Prior work on sentiment-based regime detection specifically** — Need to thoroughly search for any existing papers that explicitly combine text-derived sentiment features with regime-switching models (HMM, Markov Switching, or clustering). This is the core novelty claim — need to verify what has been done vs. what is genuinely new.
- [ ] **Gaussian Mixture Model clustering for regime detection** — Need references on GMM-based regime detection as an alternative to HMM. GMMs are simpler and don't assume Markov transition dynamics, making them useful baselines.
- [ ] **COVID crash timeline with key dates and sentiment markers** — Need a detailed timeline: WHO pandemic declaration (March 11, 2020), US travel ban (March 11), market circuit breakers (March 9, 12, 16, 18), Fed emergency rate cut (March 15), fiscal stimulus (March 27). Map these to sentiment regime transitions.
- [ ] **2022 rate hiking cycle communication timeline** — Need FOMC-by-FOMC timeline of the communication regime shift: "transitory" language (2021), first hawkish pivot (November 2021 minutes), first rate hike (March 2022), "front-loading" language (May-June 2022), "higher for longer" (late 2022).
- [ ] **Terra/Luna crash: NLP-specific analysis** — Need a paper applying NLP to social media text preceding the Terra/Luna depegging (May 2022). Social media signals (Telegram, Twitter) reportedly preceded the on-chain depegging.
- [ ] **Regime detection stability metrics** — Need formal metrics for regime stability: average regime duration, transition frequency, regime "flip-flopping" rate. Standard classification metrics (accuracy, F1) don't capture these temporal dynamics.
- [ ] **Forward return predictiveness testing** — Need statistical testing methodology (e.g., Diebold-Mariano test for forecast comparison) appropriate for comparing regime-conditional return predictions against unconditional predictions.
- [ ] **Cross-asset sentiment feature alignment** — Need references on temporal alignment of features from different text sources (earnings calls on different dates, FOMC meetings every 6 weeks, social media continuous). Temporal alignment is a practical engineering challenge.

---

## Verification Priority

Start SMU Library verification with these sources first:

1. **Hamilton (1989)** — Regime switching foundation (Econometrica — must-cite)
2. **Calomiris & Mamaysky (2019)** — News drives risk globally (JFE — strongest evidence)
3. **Guidolin & Timmermann (2007)** — Four-regime taxonomy (JEDC)
4. **Ang & Bekaert (2002)** — Interest rate regime switching (JBES)
5. **García (2013)** — Regime-conditional sentiment (if not already verified from Ch 1/5)
6. **Baker et al. (2020)** — COVID market crash (RAPS)
7. **Nystrup et al. (2015)** — HMM baseline (JPM)
8. **Manela & Moreira (2017)** — NVIX as regime indicator (if not already verified)
9. **Billio et al. (2012)** — Network connectedness (if not already verified from Ch 9)
10. **Conlon et al. (2023)** — FTX contagion analysis

---

*Research compiled April 2026. All citations require manual verification through SMU Library before inclusion in final manuscript.*
