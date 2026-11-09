# Chapter 7 — Central Bank Language and Macro Signals — Annotated Bibliography

**Purpose:** This chapter tackles the most market-moving scheduled text events in finance — central bank communications. It covers FOMC statement analysis, the evolution from Greenspan's opacity to forward guidance, hawkish/dovish language models, cross-central bank comparative analysis (ECB, BoJ, BoE), nowcasting from central bank language, and the "Fed whisperer" problem.

**What this chapter needs from its sources:**
- FOMC communication structure and information content hierarchy
- Evolution of central bank communication transparency
- Hawkish/dovish scoring methodologies (dictionaries, topic models, deep learning)
- Cross-central bank comparative analysis (ECB, BoJ, BoE)
- Nowcasting economic indicators from central bank text
- Market microstructure around central bank announcements
- The "information effect" and what markets learn from Fed text

**Citation format:** Chicago (Notes and Bibliography), 17th edition.

**Note on research community:** This chapter draws heavily from monetary economics and central banking research — working papers from the Fed, ECB, BIS, and Riksbank, plus papers in *Journal of Monetary Economics*, *Journal of International Economics*, *QJE*, and *AER*. Several key papers are authored by central bank staff, who have unique insight into both sides of the communication equation.

---

## 1. FOMC Statements, Minutes, and Press Conferences

### 1.1 Foundational: Communication and Market Impact

**Rosa, Carlo. "The Financial Market Effect of FOMC Minutes." *Federal Reserve Bank of New York Economic Policy Review* 19, no. 2 (December 2013): 67–81.**

- URL: `https://www.newyorkfed.org/medialibrary/media/research/epr/2013/0913rosa.pdf`
- **Type:** Fed working paper / policy review.
- **Summary:** FOMC minutes release induces "higher than normal" volatility across asset classes. Volatility of two-year Treasury yields is roughly three times larger on event days than during non-event periods.
- **Relevance:** *Section 1 (FOMC Structure).* Quantifies the market impact of Fed minutes specifically, establishing them as a high-signal text source worthy of NLP analysis.
- **Cross-reference:** Already cited in Chapter 1 research.
- Status: `[ ] Unverified`

---

**Nakamura, Emi, and Jón Steinsson. "High-Frequency Identification of Monetary Non-Neutrality: The Information Effect." *Quarterly Journal of Economics* 133, no. 3 (August 2018): 1283–1330.**

- DOI: `10.1093/qje/qjy004`
- **Type:** Peer-reviewed journal article.
- **Summary:** Using 30-minute windows around FOMC announcements, shows that interest rate surprises simultaneously raise both nominal/real rates *and* growth forecasts — the opposite of standard theory. Explains this via an "information effect": markets interpret rate hikes as the Fed revealing positive private information about the economy, not just tightening policy.
- **Relevance:** *Section 1 and Section 6 (Fed Whisperer Problem).* The information effect is fundamental to understanding what NLP is actually extracting from FOMC text. When a sentiment model detects "hawkish" language, the market may react positively (information effect) rather than negatively (tightening shock). This dual interpretation complicates naive sentiment-to-signal pipelines.
- **How to use:** Central to both the FOMC structure discussion and the "Fed whisperer" section. The information effect means NLP systems must distinguish between *what the Fed is doing* (policy action) and *what the Fed is revealing* (economic outlook). Pure hawk/dove scoring conflates these channels.
- Status: `[ ] Unverified`

---

### 1.2 Reference: FOMC Archives

**Federal Reserve Bank of St. Louis. "Federal Open Market Committee Meeting Minutes, Transcripts, and Other Documents, 1933–2026." FRASER Digital Library, accessed April 2026.**

- URL: `https://fraser.stlouisfed.org/title/federal-open-market-committee-meeting-minutes-transcripts-documents-677`
- **Type:** Official archive.
- **Summary:** Comprehensive FOMC archive: Greenbooks (1964–2010), minutes (1993–present), full transcripts (5-year lag), Beige Books, FOMC Speak database (2010–2023).
- **Relevance:** *Section 1.* Primary data source reference for Fed text.
- **Cross-reference:** Already cited in Chapter 2 research.
- Status: `[ ] Unverified`

---

## 2. The Evolution of Fed Communication

### 2.1 Foundational: Communication and Monetary Policy Survey

**Blinder, Alan S., Michael Ehrmann, Marcel Fratzscher, Jakob De Haan, and David-Jan Jansen. "Central Bank Communication and Monetary Policy: A Survey of Theory and Evidence." *Journal of Economic Literature* 46, no. 4 (December 2008): 910–945.**

- DOI: `10.1257/jel.46.4.910`
- **Type:** Peer-reviewed survey article.
- **Summary:** The definitive survey of central bank communication theory and evidence. Documents how communication has become an increasingly important monetary policy tool over the preceding two decades. Shows that communication can move financial markets, enhance the predictability of monetary policy decisions, and help achieve macroeconomic objectives.
- **Relevance:** *Section 2 (Evolution of Communication).* The canonical survey for the entire chapter. Provides the theoretical framework for why central bank communication matters and documents the historical evolution from opacity to transparency.
- **How to use:** Cite early in Section 2 as the comprehensive reference. The historical evolution narrative (from minimal disclosure to forward guidance) structures the section. Readers need this context to understand why NLP approaches must account for communication regime changes.
- Status: `[ ] Unverified`

---

### 2.2 Contextual: Forward Guidance Theory

**Eggertsson, Gauti B., and Michael Woodford. "The Zero Bound on Interest Rates and Optimal Monetary Policy." *Brookings Papers on Economic Activity* 2003, no. 1 (2003): 139–235.**

- URL: `https://www.brookings.edu/articles/the-zero-bound-on-interest-rates-and-optimal-monetary-policy/`
- **Type:** Peer-reviewed conference paper.
- **Summary:** Shows that a central bank at the zero lower bound can achieve additional stimulus by credibly committing to keep rates low into the future — formalized forward guidance as a monetary policy tool. This paper catalyzed the Fed's adoption of explicit forward guidance, fundamentally changing the nature of FOMC communication.
- **Relevance:** *Section 2 (Evolution — Forward Guidance).* The theoretical paper that legitimized forward guidance, which transformed FOMC communication from "what did the Fed decide?" to "what is the Fed promising about the future?" This shift has massive implications for NLP: post-2003 FOMC statements contain fundamentally different information content than pre-2003 statements.
- **How to use:** Cite as the intellectual origin of forward guidance. The pre/post shift is a structural break in the text data that NLP models must account for.
- Status: `[ ] Unverified`

---

## 3. Hawkish/Dovish Language Models

### 3.1 Foundational: Automated Semantic Scoring

**Lucca, David O., and Francesco Trebbi. "Measuring Central Bank Communication: An Automated Approach with Application to FOMC Statements." NBER Working Paper no. 15367, September 2009.**

- URL: `https://www.nber.org/papers/w15367`
- **Type:** Working paper (NBER).
- **Summary:** Proposes an automated, objective scoring technique for FOMC statements along a hawkish-dovish metric using Internet search engines (Google, Factiva) to determine semantic orientation. Finds that short-term Treasury yields respond to policy rate changes, while longer-dated Treasuries mainly react to communication content. Communication changes lead policy rate decisions by more than a year.
- **Relevance:** *Section 3 (Hawk/Dove Models).* One of the earliest automated hawkish/dovish scoring approaches. The search-engine-based semantic orientation method is creative but pre-transformer. The finding that communication *leads* rate decisions by a year is striking evidence for NLP's predictive value.
- **How to use:** Cite as an early automated approach, then show how subsequent methods (dictionary-based, topic models, deep learning) improved on it. The "communication leads rates by a year" finding motivates the entire chapter.
- Status: `[ ] Unverified`

---

### 3.2 Methodological: Dictionary-Based Central Bank Scoring

**Apel, Mikael, and Marianna Blix Grimaldi. "How Informative Are Central Bank Minutes?" *Review of Economics* 65, no. 1 (2014): 53–76.**

- DOI: `10.1515/roe-2014-0103`
- **Type:** Peer-reviewed journal article. (Earlier version: Riksbank Working Paper no. 261, 2012.)
- **Summary:** Develops a domain-specific dictionary for central bank sentiment (hawkish/dovish) and applies it to Swedish Riksbank minutes. The "net hawkishness" measure derived from the dictionary predicts interest rate decisions. The dictionary was subsequently adopted by Hubert and Labondance (2021) for FOMC and ECB analysis.
- **Relevance:** *Section 3 (Hawk/Dove Models).* The primary reference for dictionary-based central bank sentiment scoring. The Apel-Grimaldi dictionary is the central banking equivalent of the Loughran-McDonald dictionary for corporate text — a domain-specific lexicon that corrects for general-purpose misclassification.
- **How to use:** Present as the dictionary approach to hawk/dove scoring. Contrast with Lucca-Trebbi's search-engine approach and Hansen-McMahon's topic model approach to show the methodological evolution.
- Status: `[ ] Unverified`

---

### 3.3 Methodological: Topic Model Approach

**Hansen, Stephen, and Michael McMahon. "Shocking Language: Understanding the Macroeconomic Effects of Central Bank Communication." *Journal of International Economics* 99, Supplement 1 (March 2016): S114–S133.**

- DOI: `10.1016/j.jinteco.2015.12.008`
- **Type:** Peer-reviewed journal article.
- **Summary:** Uses computational linguistics tools (LDA topic models) to decompose FOMC communication into two dimensions: information about current economic conditions and forward guidance about future policy. Within a FAVAR framework, finds that forward guidance shocks are more important than current-conditions communication for market and real variables.
- **Relevance:** *Section 3 (Hawk/Dove Models).* Advances beyond one-dimensional hawk/dove scoring to a multi-dimensional decomposition of central bank communication. The distinction between "current conditions" and "forward guidance" is conceptually more nuanced than a single hawk/dove axis.
- **How to use:** Cite as the topic-model approach. The two-dimensional decomposition (conditions vs. guidance) directly addresses a limitation of the dictionary-based hawk/dove scoring — a statement can be hawkish about the economy *and* dovish about future rates, and these carry different market implications.
- Status: `[ ] Unverified`

---

### 3.4 Methodological: Deep Learning / Audio Analysis

**Gorodnichenko, Yuriy, Tho Pham, and Oleksandr Talavera. "The Voice of Monetary Policy." *American Economic Review* 113, no. 2 (February 2023): 548–584.**

- DOI: `10.1257/aer.20220129`
- **Type:** Peer-reviewed journal article (top-5 economics journal).
- **Summary:** Develops a deep learning model to detect emotions from *audio* of Fed chair press conferences (not just text). After controlling for policy actions and text sentiment, a positive vocal tone leads to significant increases in share prices. Financial variables respond to vocal cues beyond the textual content.
- **Relevance:** *Section 3 (Hawk/Dove Models) and Section 6 (Fed Whisperer Problem).* Demonstrates that central bank communication carries signal *beyond text* — in the prosody, tone, and emotional delivery. This is the cutting edge of central bank NLP, extending from text analysis to multi-modal (text + audio) analysis.
- **How to use:** Cite as the frontier of central bank communication analysis. The finding that vocal tone moves markets *after controlling for text sentiment* has direct implications for multi-modal approaches. Connects to the book's multi-modal theme (Chapters 5, 9, 10).
- Status: `[ ] Unverified`

---

### 3.5 Methodological: Sentiment and Policy Expectations

**Hubert, Paul, and Fabien Labondance. "The Signaling Effects of Central Bank Tone." *European Economic Review* 133 (April 2021): 103684.**

- DOI: `10.1016/j.euroecorev.2021.103684`
- **Type:** Peer-reviewed journal article.
- **Summary:** Investigates whether sentiment conveyed by ECB and FOMC policymakers affects the term structure of private short-term interest rate expectations. Uses the Apel-Grimaldi dictionary adapted for Fed and ECB communication. Identifies sentiment as exogenous shocks using an augmented narrative approach.
- **Relevance:** *Section 3 (Hawk/Dove Scoring) and Section 4 (Cross-Central Bank).* Bridges the dictionary approach to both the Fed and ECB, demonstrating cross-institution applicability. The policy expectations channel connects sentiment scoring to the macro signals in Section 5.
- **How to use:** Cite as the study that applies the same dictionary methodology across both the Fed and ECB, enabling cross-institution comparison.
- Status: `[ ] Unverified`

---

## 4. Cross-Central Bank Language Analysis

### 4.1 Empirical: ECB Communication and Asset Prices

**Schmeling, Maik, and Christian Wagner. "Does Central Bank Tone Move Asset Prices?" *Journal of Financial and Quantitative Analysis* 59, no. 5 (August 2024): 2093–2130.**

- DOI: `10.1017/S0022109024000073`
- **Type:** Peer-reviewed journal article. (Earlier CEPR DP 13490, 2019.)
- **Summary:** Measures ECB press conference tone using the Loughran-McDonald dictionary. Finds that positive tone changes are associated with equity return differentials of ~60bp on press conference days (growing to 100bp+ by the next meeting), increasing government bond yields, lower implied volatility, lower variance risk premia, and tighter credit spreads. Communication tone is a monetary policy tool that affects risk appetite and risk premia.
- **Relevance:** *Section 4 (Cross-Central Bank — ECB).* The primary ECB-specific paper demonstrating that central bank tone moves asset prices through a risk-based channel. The use of the Loughran-McDonald dictionary for ECB text shows cross-domain applicability of financial NLP tools.
- **How to use:** Central to the ECB subsection. The 60bp return differential and multi-asset impact (equities, bonds, vol, credit) make a powerful quantitative argument. Contrast with Fed studies to highlight cross-institutional similarities and differences.
- Status: `[ ] Unverified`

---

### 4.2 Reference: ECB Communication Data

**European Central Bank. "Speeches Dataset." ECB.europa.eu, accessed April 2026.**

- URL: `https://www.ecb.europa.eu/press/key/html/downloads.en.html`
- **Type:** Official dataset.
- **Summary:** Precompiled dataset of all ECB speeches with metadata, updated monthly. Released explicitly for NLP research.
- **Relevance:** *Section 4 (ECB).* Official data source.
- **Cross-reference:** Already cited in Chapter 2 research.
- Status: `[ ] Unverified`

---

### 4.3 Empirical: Bank of Japan Communication

**Oshima, Yuri, and Yoichi Matsubayashi. "Monetary Policy Communication of the Bank of Japan: Computational Text Analysis." Discussion Paper no. 1816, Kobe University, 2018.**

- URL: `https://ideas.repec.org/p/koe/wpaper/1816.html`
- **Type:** Working paper.
- **Summary:** Applies computational text analysis to Bank of Japan press conferences. Reveals significant differences in communication strategies across BoJ governors. Addresses challenges of analyzing Japanese central bank text, including translation issues and cultural communication norms.
- **Relevance:** *Section 4 (Cross-Central Bank — BoJ).* The primary BoJ reference. The cross-governor variation and translation challenges are important practical issues for readers building cross-central-bank NLP systems.
- **How to use:** Cite to address the BoJ-specific challenges: Japanese-to-English translation introduces noise, cultural norms favor indirect communication, and governor-level variation is large.
- Status: `[ ] Unverified`

---

### 4.4 Contextual: Central Bank Text Mining Guide

**Bholat, David, Stephen Hansen, Pedro Santos, and Cheryl Schonhardt-Bailey. "Text Mining for Central Banks." *Centre for Central Banking Studies Handbook* no. 33. London: Bank of England, 2015.**

- URL: `https://www.bankofengland.co.uk/ccbs/text-mining-for-central-banks`
- **Type:** Central bank handbook.
- **Summary:** Practical guide to text mining methods for central bank applications from BoE researchers. Covers preprocessing, sentiment analysis, topic modeling, and text classification.
- **Relevance:** *Section 4 (Cross-Central Bank — BoE).* The BoE's own guide to text mining central bank communication. Useful for the BoE subsection and as a practical reference for readers.
- **Cross-reference:** Already cited in Chapter 2 research.
- Status: `[ ] Unverified`

---

## 5. Nowcasting Macro Indicators from Language

### 5.1 Foundational: Estimating Central Bank Objectives from Text

**Shapiro, Adam Hale, and Daniel J. Wilson. "Taking the Fed at Its Word: A New Approach to Estimating Central Bank Objectives Using Text Analysis." *Review of Economic Studies* 89, no. 5 (October 2022): 2768–2805.**

- DOI: `10.1093/restud/rdac004`
- **Type:** Peer-reviewed journal article.
- **Summary:** Estimates the Fed's objective function directly from sentiment expressed in FOMC transcripts, minutes, and speeches. Finds that the FOMC's implicit inflation target was approximately 1.5% (below the commonly assumed 2%), and that the FOMC's loss function depends strongly on output growth and stock market performance, less on perceived economic slack.
- **Relevance:** *Section 5 (Nowcasting).* Demonstrates that NLP applied to Fed text can reveal not just what the Fed *thinks* about the economy, but what the Fed *cares about* — its objective function. This is a deeper form of nowcasting: inferring central bank preferences, not just economic conditions.
- **How to use:** Central to Section 5. The finding that the implicit inflation target was 1.5% (not 2%) from text analysis alone is a powerful demonstration of what NLP can extract from central bank communication. The methodology (sentiment → objective function estimation) is technically sophisticated.
- Status: `[ ] Unverified`

---

### 5.2 Empirical: Communication and Market Microstructure

**Doh, Taeyoung, Dongho Song, and Shu-Kuei X. Yang. "Deciphering Federal Reserve Communication via Text Analysis." Federal Reserve Bank of Kansas City Research Working Paper no. 20-14, 2020.**

- URL: `https://www.kansascityfed.org/documents/5642/rwp20-14dohsongyang.pdf`
- **Type:** Fed working paper.
- **Summary:** Applies FinBERT and Universal Sentence Encoder to FOMC statements. Sentiment score is among the most important predictors of financial market reaction in the first minute after FOMC announcements.
- **Relevance:** *Section 5 (Nowcasting) and market microstructure.* Demonstrates state-of-the-art NLP (FinBERT) applied to Fed communication with market microstructure-level timing.
- **Cross-reference:** Already cited in Chapter 1 research.
- Status: `[ ] Unverified`

---

## 6. The "Fed Whisperer" Problem

### 6.1 Foundational: Information Effect

**Nakamura, Emi, and Jón Steinsson. "High-Frequency Identification of Monetary Non-Neutrality: The Information Effect." *Quarterly Journal of Economics* 133, no. 3 (August 2018): 1283–1330.**

- *(See citation above in Section 1.1)*
- **Relevance for Section 6:** The information effect is the core theoretical challenge for the "Fed whisperer" section. When the Fed raises rates and markets rally, it's because markets are reading between the lines — the rate hike reveals the Fed's positive private assessment of the economy. NLP systems that simply score hawk/dove will miss this second channel.
- **How to use:** Frame the "Fed whisperer" problem as the dual-channel interpretation challenge: every FOMC communication simultaneously reveals (1) a policy intention and (2) private economic information. The NLP challenge is separating these channels.
- Status: `[ ] Unverified`

---

### 6.2 Empirical: Voice Beyond Text

**Gorodnichenko, Yuriy, Tho Pham, and Oleksandr Talavera. "The Voice of Monetary Policy." *American Economic Review* 113, no. 2 (February 2023): 548–584.**

- *(See citation above in Section 3.4)*
- **Relevance for Section 6:** The finding that *vocal tone* moves markets after controlling for text content is the ultimate "Fed whisperer" evidence — there is information in *how* things are said, not just *what* is said. This is what market participants mean when they talk about "reading between the lines."
- Status: `[ ] Unverified`

---

## Cross-Chapter References

| Source | Ch 7 Section | Also Relevant To |
|--------|-------------|------------------|
| Blinder et al. (2008) | Sec 2 (Communication Survey) | General background |
| Nakamura & Steinsson (2018) | Sec 1, 6 (Information Effect) | Ch 10 (Regime Detection — Fed signals) |
| Hansen & McMahon (2016) | Sec 3 (Topic Models) | Ch 4 (NLP Methods) |
| Gorodnichenko et al. (2023) | Sec 3, 6 (Voice/Audio) | Ch 5 (Multi-Modal Fusion) |
| Schmeling & Wagner (2024) | Sec 4 (ECB Tone) | Ch 5 (Cross-Asset Effects) |
| Shapiro & Wilson (2022) | Sec 5 (Nowcasting) | Ch 10 (Regime Detection) |
| Rosa (2013) | Sec 1 (FOMC Minutes) | Ch 1 (Historical Examples) |
| Doh et al. (2020) | Sec 5 (FinBERT + FOMC) | Ch 1, Ch 4 (FinBERT) |
| Lucca & Trebbi (2009) | Sec 3 (Automated Scoring) | Ch 4 (NLP Methods) |
| Hubert & Labondance (2021) | Sec 3, 4 (Dictionary Scoring) | Ch 3 (Lexicons) |
| FRASER Archive | Sec 1 (Data Source) | Ch 2 (Data Acquisition) |
| ECB Speeches Dataset | Sec 4 (ECB Data) | Ch 2 (Data Acquisition) |
| Bholat et al. (2015) | Sec 4 (BoE) | Ch 2 (Central Bank Data) |
| Eggertsson & Woodford (2003) | Sec 2 (Forward Guidance) | Theoretical background |
| Apel & Blix Grimaldi (2014) | Sec 3 (Dictionary) | Ch 3 (Domain Lexicons) |

---

## Research Gaps

The following areas need additional sourcing:

- [ ] **"Fedspeak" dictionary construction** — Need a specific published "Fedspeak" dictionary/lexicon beyond the Apel-Grimaldi adaptation. The Kansas City Fed or other regional Feds may have published domain-specific word lists for central bank communication analysis.
- [ ] **Structural break detection in communication regimes** — Need a paper that formally tests for structural breaks in FOMC communication (e.g., pre/post-Greenspan, pre/post-forward guidance, pre/post-press conferences). The communication regime changes affect NLP model validity across time periods.
- [ ] **BoE Monetary Policy Committee communication patterns** — Need a dedicated study of BoE MPC communication, comparable to the FOMC and ECB studies. The Bholat et al. (2015) handbook is useful but not an empirical study of BoE text and market impact.
- [ ] **Cross-central bank language model transfer** — Need a study testing whether NLP models trained on Fed text transfer to ECB or BoJ text. CentralBankRoBERTa (Pfeifer et al. 2023, *Journal of Finance and Data Science*) may address this — search for it.
- [ ] **Nowcasting CPI/GDP from central bank language** — Need a paper that specifically uses central bank text to nowcast inflation or GDP *before official data releases*. Shapiro-Wilson (2022) estimates objectives, not forecasts. The St. Louis Fed's nowcasting work may combine text with traditional indicators.
- [ ] **Market microstructure around FOMC: NLP signal window** — Need precise timing data on how quickly NLP-derived signals become stale after FOMC releases. The Doh et al. (2020) "first minute" finding needs to be complemented with longer-horizon signal decay analysis.
- [ ] **BIS CB-LMs language model** — The BIS working paper (no. 1215, 2024) on central bank language models should be verified and potentially cited in this chapter for the cross-central bank section.

---

## Verification Priority

Start SMU Library verification with these sources first:

1. **Blinder et al. (2008)** — Central bank communication survey (foundational)
2. **Nakamura & Steinsson (2018)** — Information effect (QJE — central to chapter)
3. **Gorodnichenko et al. (2023)** — Voice of monetary policy (AER — cutting edge)
4. **Hansen & McMahon (2016)** — Topic model decomposition
5. **Schmeling & Wagner (2024)** — ECB tone and asset prices
6. **Shapiro & Wilson (2022)** — Fed objectives from text (RES)
7. **Lucca & Trebbi (2009)** — Automated FOMC scoring
8. **Apel & Blix Grimaldi (2014)** — Hawk/dove dictionary
9. **Hubert & Labondance (2021)** — Cross-institution sentiment
10. **Eggertsson & Woodford (2003)** — Forward guidance theory

---

*Research compiled April 2026. All citations require manual verification through SMU Library before inclusion in final manuscript.*
