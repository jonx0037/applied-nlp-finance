# Chapter 6 — Earnings Calls and Corporate Disclosure — Annotated Bibliography

**Purpose:** This chapter systematically analyzes scheduled, high-signal financial language events — earnings calls, 10-K/10-Q filings, and MD&A sections. It covers the structure of earnings calls, linguistic features predictive of post-earnings drift, CEO vs. CFO language divergence, risk factor analysis, and event study methodology for text-based signals.

**What this chapter needs from its sources:**
- Earnings call structure and information content (prepared remarks vs. Q&A)
- Linguistic features that predict post-earnings announcement drift (PEAD)
- CEO vs. CFO language divergence and deception detection
- 10-K risk factor and MD&A textual analysis
- Event study methodology appropriate for text-based signals
- Analyst question tone and evasion/non-answer detection

**Citation format:** Chicago (Notes and Bibliography), 17th edition.

**Note on research tradition:** This chapter draws primarily from the accounting and finance research traditions (AAA, JAR, JAE, TAR, RAS) rather than the NLP/ML community. The papers are methodologically rigorous in the accounting sense — careful identification strategies, controls for confounders, and economic significance testing — which provides a strong foundation for the practitioner audience.

---

## 1. Structure of Earnings Calls

### 1.1 Foundational: Conference Call Information Content

**Matsumoto, Dawn, Maarten Pronk, and Erik Roelofsen. "What Makes Conference Calls Useful? The Information Content of Managers' Presentations and Analysts' Discussion Sessions." *Accounting Review* 86, no. 4 (July 2011): 1383–1414.**

- DOI: `10.2308/accr-10034`
- **Type:** Peer-reviewed journal article.
- **Summary:** Examines 10,000+ conference call transcripts and finds that both the presentation and discussion (Q&A) segments have incremental information content over the accompanying press release. Discussion periods are *relatively more informative* than presentation periods. Managers provide increased disclosures during presentations when firm performance is poor, but relatively more information is released during Q&A in these circumstances.
- **Relevance:** *Section 1 (Structure of Earnings Calls).* The primary reference for the prepared remarks vs. Q&A decomposition. The finding that Q&A is relatively more informative — especially during bad performance — directly motivates building separate NLP pipelines for each segment.
- **How to use:** Central to Section 1. Use to establish that parsing earnings calls into segments is not arbitrary — the segments carry empirically distinct signal. The "more informative Q&A during bad news" finding is a key practical insight.
- Status: `[ ] Unverified`

---

**Bushee, Brian J., Dawn A. Matsumoto, and Gregory S. Miller. "Open versus Closed Conference Calls: The Determinants and Effects of Broadening Access to Disclosure." *Journal of Accounting and Economics* 34, nos. 1–3 (January 2003): 149–180.**

- DOI: `10.1016/S0165-4101(02)00073-3`
- **Type:** Peer-reviewed journal article.
- **Summary:** Examines the transition from "closed" (institutional-only) to "open" (publicly accessible) conference calls. Open calls are associated with greater small-trade activity and higher price volatility during the call period, suggesting that individual investor access increases both informedness and consensus in the market.
- **Relevance:** *Section 1 (Context).* Provides the institutional context for why conference call transcripts became widely available as a data source. The open-access transition is a prerequisite for the NLP analysis the chapter teaches.
- **How to use:** Brief reference for historical context. The accessibility transition explains why this data source is now viable for systematic analysis.
- Status: `[ ] Unverified`

---

## 2. Linguistic Features Predictive of Post-Earnings Drift

### 2.1 Foundational: Earnings Call Tone and PEAD

**Price, S. McKay, James S. Doran, David R. Peterson, and Barbara A. Bliss. "Earnings Conference Calls and Stock Returns: The Incremental Informativeness of Textual Tone." *Journal of Banking & Finance* 36, no. 4 (April 2012): 992–1011.**

- DOI: `10.1016/j.jbankfin.2011.10.013`
- **Type:** Peer-reviewed journal article.
- **Summary:** Conference call linguistic tone significantly predicts abnormal returns and trading volume. Tone dominates earnings surprises in explaining PEAD over 60 trading days. Q&A portion has incremental explanatory power, concentrated in firms with higher cash flow uncertainty.
- **Relevance:** *Section 2 (Linguistic Features and PEAD).* The primary citation for tone-driven PEAD. The finding that tone *dominates* earnings surprises is the chapter's strongest quantitative argument for why linguistic analysis adds value beyond traditional financial metrics.
- **How to use:** Central to Section 2. The "tone dominates earnings surprise" finding is striking and should be presented with the specific return magnitudes.
- **Cross-reference:** Already cited in Chapters 1 and 2 research.
- Status: `[ ] Unverified`

---

**Meursault, Vitaly, Pierre Liang, Bryan Routledge, and Madeline Marco Scanlon. "PEAD.txt: Post-Earnings-Announcement Drift Using Text." *Journal of Financial and Quantitative Analysis* 58, no. 6 (September 2023): 2409–2439.**

- DOI: `10.1017/S0022109022001181`
- **Type:** Peer-reviewed journal article.
- **Summary:** Text-only model produces PEAD of 8.01% from one day after the earnings call to the calendar year mark — the largest purely ML-based drift documented. Uses computational linguistics and LLMs for feature construction.
- **Relevance:** *Section 2.* State-of-the-art text-based PEAD. The 8.01% annual drift from text alone is an economically significant finding that demonstrates NLP's value for earnings analysis.
- **Cross-reference:** Already cited in Chapter 1 research.
- Status: `[ ] Unverified`

---

## 3. Tone Analysis: CEO vs. CFO Language

### 3.1 Foundational: Deception Detection in Conference Calls

**Larcker, David F., and Anastasia A. Zakolyukina. "Detecting Deceptive Discussions in Conference Calls." *Journal of Accounting Research* 50, no. 2 (May 2012): 495–540.**

- DOI: `10.1111/j.1475-679X.2012.00450.x`
- **Type:** Peer-reviewed journal article.
- **Summary:** Develops linguistic-based classification models of deception during quarterly earnings calls. Uses subsequent financial restatements to label calls as "truthful" or "deceptive." Deceptive executives exhibit more references to general knowledge, fewer non-extreme positive emotions, and fewer references to shareholder value. Deceptive CEOs use significantly more extreme positive emotion and fewer anxiety words. Out-of-sample accuracy beats random by 6–16%. A portfolio short on high-deception-score CFO firms produces annualized alpha of −4% to −11%.
- **Relevance:** *Section 3 (CEO vs. CFO Language).* The most striking linguistic analysis of executive behavior during earnings calls. The deception-detection methodology is both academically rigorous (using restatements as ground truth) and economically significant (portfolio alpha).
- **How to use:** Central to Section 3. The specific linguistic markers of deception (extreme positive emotion, lack of anxiety words, general-knowledge references) provide concrete NLP features readers can extract. The portfolio alpha demonstrates economic significance.
- Status: `[ ] Unverified`

---

### 3.2 Empirical: Non-Answers and Evasion

**Hollander, Stephan, Maarten Pronk, and Erik Roelofsen. "Does Silence Speak? An Empirical Analysis of Disclosure Choices During Conference Calls." *Journal of Accounting Research* 48, no. 3 (June 2010): 531–563.**

- DOI: `10.1111/j.1475-679X.2010.00365.x`
- **Type:** Peer-reviewed journal article.
- **Summary:** Finds that managers regularly withhold information by not answering analyst questions during conference calls. Best predictors of evasion: firm size, CEO stock-price-based incentives, company age, firm performance, litigation risk, and whether analysts are actively involved. Investors interpret silence negatively.
- **Relevance:** *Section 3 (Tone Analysis — Analyst Questions).* Establishes that *what is not said* carries signal. Evasion is a linguistically detectable behavior with negative return implications. Builds the case for NLP systems that detect non-answers, not just sentiment.
- **How to use:** Cite alongside Larcker-Zakolyukina (2012) to show that both deception (what is said falsely) and evasion (what is not said) are extractable signals. The "silence speaks" framing is memorable and pedagogically effective.
- Status: `[ ] Unverified`

---

**Gow, Ian D., David F. Larcker, and Anastasia A. Zakolyukina. "Non-Answers During Conference Calls." *Journal of Accounting Research* 59, no. 4 (September 2021): 1349–1384.**

- DOI: `10.1111/1475-679X.12371`
- **Type:** Peer-reviewed journal article.
- **Summary:** Develops a linguistic measure of non-answers using NLP analysis of conference calls. Finds ~11% of analyst questions elicit non-answers. Negative-tone, uncertain, complex, or detail-seeking questions trigger more non-answers. Performance-related questions drive non-answers, and this association is weaker when news is favorable. Competitive intensity increases non-answers to proprietary questions.
- **Relevance:** *Section 3.* The most methodologically advanced treatment of evasion detection. The 11% baseline rate provides a concrete benchmark. The taxonomy of question types that trigger non-answers provides a feature engineering blueprint for NLP systems.
- **How to use:** Cite as the state-of-the-art for evasion detection. The question-type taxonomy (negative tone → non-answer, performance question → non-answer) directly informs NLP feature engineering.
- Status: `[ ] Unverified`

---

## 4. Risk Factor Analysis: 10-K and 10-Q

### 4.1 Foundational: Risk Factor Information Content

**Campbell, John L., Hsinchun Chen, Dan S. Dhaliwal, Hsin-min Lu, and Logan B. Steele. "The Information Content of Mandatory Risk Factor Disclosures in Corporate Filings." *Review of Accounting Studies* 19, no. 1 (March 2014): 396–455.**

- DOI: `10.1007/s11142-013-9258-3`
- **Type:** Peer-reviewed journal article.
- **Summary:** Examines the SEC-mandated risk factor section (Item 1A, required since 2005). Finds that firms facing greater risk disclose more risk factors, and the type of risk determines disclosure emphasis. Risk factor information is reflected in systematic risk, idiosyncratic risk, information asymmetry, and firm value. Supports the SEC's decision to mandate these disclosures.
- **Relevance:** *Section 4 (Risk Factor Analysis).* The primary validation that 10-K risk factor disclosures are informative (not just boilerplate). Provides the academic justification for building NLP systems that analyze risk factor text.
- **How to use:** Cite to establish that risk factor sections carry real information before showing how NLP can extract it at scale. The risk-type taxonomy (systematic vs. idiosyncratic) connects to the Bao-Datta (2014) topic modeling approach.
- Status: `[ ] Unverified`

---

### 4.2 Methodological: Financial Constraints from Text

**Bodnaruk, Andriy, Tim Loughran, and Bill McDonald. "Using 10-K Text to Gauge Financial Constraints." *Journal of Financial and Quantitative Analysis* 50, no. 4 (August 2015): 623–646.**

- DOI: `10.1017/S0022109015000411`
- **Type:** Peer-reviewed journal article.
- **Summary:** Parses 10-K disclosures using a unique lexicon based on constraining words to measure the degree of financial constraint. Shows that text-based constraint measures predict future financial outcomes, complementing traditional firm-characteristic-based measures (age, size).
- **Relevance:** *Section 4 (Risk Factor Analysis).* Demonstrates that domain-specific word lists (constraining words) applied to 10-K filings predict firm-level financial outcomes. This is the Loughran-McDonald dictionary methodology applied to a specific, economically meaningful task.
- **How to use:** Cite as an example of targeted lexicon application to 10-K text. The "constraining words" approach is a concrete NLP implementation readers can build.
- Status: `[ ] Unverified`

---

## 5. MD&A as a Structured NLP Target

### 5.1 Foundational: MD&A Modification Analysis

**Brown, Stephen V., and Jennifer Wu Tucker. "Large-Sample Evidence on Firms' Year-over-Year MD&A Modifications." *Journal of Accounting Research* 49, no. 2 (May 2011): 309–346.**

- DOI: `10.1111/j.1475-679X.2010.00396.x`
- **Type:** Peer-reviewed journal article.
- **Summary:** Introduces a measure for MD&A narrative disclosure: the degree to which the MD&A differs from the previous year's filing. Finds that firms with larger economic changes modify the MD&A more. Stock price responses to 10-K filings are positively associated with the MD&A modification score. However, MD&A modification scores have declined over time even as MD&A disclosures have become longer, and the price reaction has weakened.
- **Relevance:** *Section 5 (MD&A Analysis).* The foundational paper for year-over-year MD&A change detection. The modification score methodology (measuring textual similarity between consecutive filings) is directly implementable as an NLP pipeline using cosine similarity or diff-based approaches.
- **How to use:** Central to Section 5. Present the modification score as a concrete NLP feature: compute cosine similarity between consecutive MD&A sections, use the delta as a signal. The declining usefulness finding is a sobering counterpoint — readers should understand that signal decay affects entire categories of text features.
- Status: `[ ] Unverified`

---

### 5.2 Empirical: MD&A Readability and Earnings

**Li, Feng. "Annual Report Readability, Current Earnings, and Earnings Persistence." *Journal of Accounting and Economics* 45, no. 2–3 (August 2008): 221–247.**

- DOI: `10.1016/j.jacceco.2008.02.003`
- **Type:** Peer-reviewed journal article.
- **Summary:** Firms with lower earnings produce harder-to-read annual reports. Easier-to-read reports have more persistent positive earnings. In profitable firms, causation words ("because") associate with less persistent earnings, positive emotion words with more persistent earnings.
- **Relevance:** *Section 5 (MD&A).* Demonstrates that readability itself is a signal within MD&A sections. The specific word-category findings (causation words → less persistent earnings) provide concrete NLP features.
- **Cross-reference:** Already cited in Chapter 1 research.
- Status: `[ ] Unverified`

---

## 6. Event Study Methodology for Text-Based Signals

### 6.1 Foundational: Event Study Framework

**MacKinlay, A. Craig. "Event Studies in Economics and Finance." *Journal of Economic Literature* 35, no. 1 (March 1997): 13–39.**

- URL: `https://www.bu.edu/econ/files/2011/01/MacKinlay-1996-Event-Studies-in-Economics-and-Finance.pdf`
- **Type:** Peer-reviewed journal article.
- **Summary:** The canonical survey of event study methodology. Describes how to define events, estimate normal returns (market model, CAPM), compute abnormal returns, and test statistical significance. Covers estimation windows, event windows, and aggregation methods (CAR, BHAR). The paper that most finance PhD students read first on event studies.
- **Relevance:** *Section 6 (Event Study Methodology).* The foundational reference for the event study methodology the chapter teaches. Every text-based signal evaluation in the chapter should follow this framework.
- **How to use:** Cite as the methodological baseline. Walk readers through the MacKinlay framework, then adapt it for text-based signals — where the "event" is the publication of a text (earnings call transcript, 10-K filing) and the signal is a text-derived feature.
- Status: `[ ] Unverified`

---

### 6.2 Methodological: Cross-Sectional Correlation in Event Studies

**Kolari, James W., and Seppo Pynnönen. "Event Study Testing with Cross-Sectional Correlation of Abnormal Returns." *Review of Financial Studies* 23, no. 11 (November 2010): 3996–4025.**

- DOI: `10.1093/rfs/hhq072`
- **Type:** Peer-reviewed journal article.
- **Summary:** Addresses the problem of cross-sectional correlation in event studies when events cluster in calendar time. Even low cross-correlation causes over-rejection of the null hypothesis. Proposes a modified t-statistic (adjusting Boehmer-Musumeci-Poulsen 1991) that accounts for cross-correlation.
- **Relevance:** *Section 6 (Event Study Methodology).* Earnings announcements cluster in time (earnings season), creating exactly the cross-correlation problem this paper solves. Standard event study tests will produce false positives without this correction.
- **How to use:** Cite as the methodological refinement to MacKinlay (1997) required for earnings-date clustered events. This is a practical issue readers will encounter immediately when running event studies on quarterly earnings calls.
- Status: `[ ] Unverified`

---

## 7. Additional Supporting Sources

### 7.1 Empirical: Analyst Report Text

**Huang, Allen H., Amy Y. Zang, and Rong Zheng. "Evidence on the Information Content of Text in Analyst Reports." *Accounting Review* 89, no. 6 (November 2014): 2151–2180.**

- DOI: `10.2308/accr-50865`
- **Type:** Peer-reviewed journal article.
- **Summary:** Textual discussions in 363,952 analyst reports provide information beyond earnings forecasts, recommendations, and target prices. Investors react more strongly to negative text. Text is more useful when emphasizing nonfinancial topics and written assertively.
- **Relevance:** *Section 3 (Analyst Question Tone).* Validates that analyst-generated text carries incremental information. The "negative text > positive text" asymmetry connects to Tetlock (2007) and informs how to weight analyst question features.
- **Cross-reference:** Already cited in Chapter 2 research.
- Status: `[ ] Unverified`

---

### 7.2 Empirical: Risk Factor Topic Modeling

**Bao, Yang, and Anindya Datta. "Simultaneously Discovering and Quantifying Risk Types from Textual Risk Disclosures." *Management Science* 60, no. 6 (June 2014): 1371–1391.**

- DOI: `10.1287/mnsc.2014.1930`
- **Type:** Peer-reviewed journal article.
- **Summary:** Uses LDA topic modeling on 10-K risk factor sections. About two-thirds of discovered risk types lack informativeness. Three systematic/liquidity risk types increase investor risk perceptions; five unsystematic risk types decrease them.
- **Relevance:** *Section 4 (Risk Factor Analysis).* Demonstrates topic modeling as a method for decomposing risk factor text. The finding that most risk types are uninformative helps readers focus their NLP efforts on the risk categories that matter.
- **Cross-reference:** Already cited in Chapter 2 research.
- Status: `[ ] Unverified`

---

## Cross-Chapter References

| Source | Ch 6 Section | Also Relevant To |
|--------|-------------|------------------|
| Matsumoto et al. (2011) | Sec 1 (Call Structure) | Ch 2 (Transcript Sources) |
| Price et al. (2012) | Sec 2 (PEAD) | Ch 1, Ch 5 (Signal Construction) |
| Meursault et al. (2023) | Sec 2 (PEAD.txt) | Ch 1, Ch 11 (Evaluation) |
| Larcker & Zakolyukina (2012) | Sec 3 (Deception) | Ch 13 (Ethics/Limits) |
| Hollander et al. (2010) | Sec 3 (Evasion) | Ch 13 (Ethics — disclosure failure) |
| Gow et al. (2021) | Sec 3 (Non-Answers) | Ch 8 (Social Media — evasion in other contexts) |
| Campbell et al. (2014) | Sec 4 (Risk Factors) | Ch 2 (EDGAR data) |
| Bodnaruk et al. (2015) | Sec 4 (Constraints) | Ch 3 (Lexicons), Ch 5 (Signal) |
| Brown & Tucker (2011) | Sec 5 (MD&A) | Ch 2 (EDGAR parsing) |
| Li (2008) | Sec 5 (Readability) | Ch 1, Ch 3 |
| MacKinlay (1997) | Sec 6 (Event Study) | Ch 11 (Backtesting) |
| Kolari & Pynnönen (2010) | Sec 6 (Event Study) | Ch 11 (Backtesting) |
| Huang et al. (2014) | Sec 7 (Analyst Reports) | Ch 2 (Data Sources) |
| Bao & Datta (2014) | Sec 4 (Topic Modeling) | Ch 2 (EDGAR) |

---

## Research Gaps

The following areas need additional sourcing:

- [ ] **Forward-looking statement detection** — Need references on detecting SEC safe harbor language patterns in corporate filings. Look for papers on future-tense verb identification and cautionary language classification in 10-K filings.
- [ ] **Earnings call transcript timestamps and market microstructure alignment** — Need references on how transcript publication timing relates to actual market microstructure data (bid-ask spread changes, order flow). This is critical for avoid look-ahead bias in intraday analysis.
- [ ] **Hedging language taxonomy** — Need a structured taxonomy of hedging and uncertainty language specifically for corporate disclosure (e.g., "we believe," "may," "could," "subject to"). Loughran-McDonald's "uncertainty" word list is a starting point but may not capture syntactic hedging patterns.
- [ ] **Cosine similarity for year-over-year 10-K change detection** — Need a paper that specifically validates cosine similarity (or other NLP distance metrics) for tracking risk factor changes between consecutive filings. Brown & Tucker (2011) use a modification score for MD&A; a parallel approach for risk factors would be valuable.
- [ ] **CEO vs. CFO sentiment gap as a signal** — Need a paper that directly studies the divergence between CEO and CFO sentiment during the same earnings call as a predictive feature. The intuition (CEO optimistic, CFO measured, gap = signal) is referenced in several papers but may lack a dedicated study.
- [ ] **Bushee conference call Q&A dynamics** — Brian Bushee has additional work on conference call dynamics beyond the 2003 open/closed paper. Search for his recent work on Q&A interaction patterns.

---

## Verification Priority

Start SMU Library verification with these sources first:

1. **Matsumoto et al. (2011)** — Conference call structure (central to chapter)
2. **Price et al. (2012)** — Tone and PEAD (if not already verified from Ch 1)
3. **Larcker & Zakolyukina (2012)** — Deception detection (striking finding)
4. **MacKinlay (1997)** — Event study methodology (foundational)
5. **Campbell et al. (2014)** — Risk factor information content
6. **Brown & Tucker (2011)** — MD&A modification analysis
7. **Gow et al. (2021)** — Non-answers detection (state-of-the-art)
8. **Hollander et al. (2010)** — Silence/evasion analysis
9. **Kolari & Pynnönen (2010)** — Event study cross-correlation correction
10. **Bodnaruk et al. (2015)** — Financial constraints from 10-K text

---

*Research compiled April 2026. All citations require manual verification through SMU Library before inclusion in final manuscript.*
