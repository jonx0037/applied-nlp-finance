# Chapter 1 — Why Text Moves Markets — Annotated Bibliography

**Purpose:** This chapter makes the conceptual case for financial NLP before any code is written. It argues that financial markets are narrative-driven systems, that language encodes unique signal about participant beliefs, and that NLP has matured enough to extract that signal at scale.

**What this chapter needs from its sources:**
- Theoretical grounding for how information enters prices (and why language is underweighted)
- The paradox of efficiency and the role of costly information acquisition
- Narrative economics as a formal framework for text-as-signal
- Empirical evidence that text moves markets (historical case studies)
- Evidence for why NLP lagged price/volume quant strategies
- A basis for taxonomizing financial text data

**Citation format:** Chicago (Notes and Bibliography), 17th edition.

**Verification workflow:** Each entry includes a `Status` field. Mark `[x] Verified via SMU Library` after confirming the source is accessible and the citation details are accurate.

---

## 1. The Efficient Market Hypothesis and Information

These sources establish the theoretical baseline your chapter opens with — and the cracks in it that make financial NLP necessary.

### 1.1 Foundational: EMH and Information Theory

**Fama, Eugene F. "Efficient Capital Markets: A Review of Theory and Empirical Work." *Journal of Finance* 25, no. 2 (May 1970): 383–417.**

- DOI: `10.1111/j.1540-6261.1970.tb00518.x`
- **Summary:** Defines three forms of market efficiency (weak, semi-strong, strong) and establishes that an informationally efficient market is one where prices "at each moment incorporate all available information about future values." Presented at the Twenty-Eighth Annual Meeting of the American Finance Association, December 1969.
- **Relevance:** *Section 1 (EMH and Information).* The semi-strong form assumes all *public* information is reflected in prices — but the paper says nothing about the speed or mechanism by which *linguistic* information is processed. This gap is the opening wedge for the entire book.
- **How to use:** Cite the three-form taxonomy, then immediately problematize the implicit assumption that "information" is numeric. The semi-strong form's silence on text is your chapter's entry point.
- Status: `[ ] Unverified`

---

**Fama, Eugene F. "Efficient Capital Markets: II." *Journal of Finance* 46, no. 5 (December 1991): 1575–1617.**

- DOI: `10.1111/j.1540-6261.1991.tb04636.x`
- **Summary:** Twenty-year update to the 1970 paper. Acknowledges that returns are predictable from past returns, dividend yields, and term-structure variables — rejecting the older market efficiency-constant expected returns model. Argues market efficiency is a continuum, not a binary: "the lower the transaction costs in a market, including the costs of obtaining information and trading, the more efficient the market."
- **Relevance:** *Section 1.* The "efficiency as continuum" framing is critical — it opens space for text-based information that is costly to process (and therefore not instantly reflected in prices).
- **How to use:** Pair with the 1970 paper to show how Fama himself softened the strong-form claims. The "costs of obtaining information" clause is where NLP enters.
- Status: `[ ] Unverified`

---

**Grossman, Sanford J., and Joseph E. Stiglitz. "On the Impossibility of Informationally Efficient Markets." *American Economic Review* 70, no. 3 (June 1980): 393–408.**

- URL: `https://www.aeaweb.org/aer/top20/70.3.393-408.pdf`
- **Summary:** Proves that perfectly informationally efficient markets are impossible: if prices fully reflected all information, there would be no incentive to spend resources acquiring it, and markets would collapse. Proposes an "equilibrium degree of disequilibrium" where prices *partially* reflect informed traders' information, compensating them for acquisition costs.
- **Relevance:** *Section 1.* The Grossman-Stiglitz paradox is the strongest theoretical justification for financial NLP: text-based information is costly to acquire and process, so it is *exactly* the kind of information that creates exploitable inefficiency.
- **How to use:** This is the theoretical hinge between "markets are efficient" and "there's alpha in text." Frame NLP as reducing the cost of processing linguistic information — shifting the equilibrium.
- Status: `[ ] Unverified`

---

**Hayek, Friedrich A. "The Use of Knowledge in Society." *American Economic Review* 35, no. 4 (September 1945): 519–530.**

- URL: `https://www.econlib.org/library/Essays/hykKnw.html`
- **Summary:** Argues that knowledge is dispersed across society and that prices serve as a mechanism for aggregating this distributed information. No single agent possesses all relevant knowledge; the price system communicates information without any participant needing to understand the whole.
- **Relevance:** *Section 1–2.* Hayek's dispersed-knowledge framework is the philosophical precursor to EMH. But his argument is actually *stronger* for text than for prices: much of what market participants "know" is encoded in language (analyst reports, earnings calls, news), not in the prices themselves. NLP is a mechanism for aggregating the linguistic knowledge that prices only partially reflect.
- **How to use:** Use as the opening intellectual frame — Hayek → Fama → Grossman-Stiglitz as a progression from "prices aggregate knowledge" to "but not perfectly, especially for costly-to-process linguistic knowledge."
- Status: `[ ] Unverified`

---

### 1.2 Foundational: Information Asymmetry

**Akerlof, George A. "The Market for 'Lemons': Quality Uncertainty and the Market Mechanism." *Quarterly Journal of Economics* 84, no. 3 (August 1970): 488–500.**

- DOI: `10.2307/1879431`
- **Summary:** Demonstrates how information asymmetry between buyers and sellers can lead to market collapse (adverse selection). When quality is unobservable, bad goods drive out good ones. Won Akerlof the 2001 Nobel Prize and launched the field of information economics.
- **Relevance:** *Section 2 (What "Information" Means).* Corporate disclosure language is a mechanism for reducing information asymmetry. Firms use earnings calls, risk factors, and MD&A sections to signal quality — but the *way* they use language (hedging, obfuscation, specificity) carries signal beyond the literal content.
- **How to use:** Brief reference to establish that information asymmetry is the core market failure NLP helps address. Language is how firms bridge the information gap — or strategically maintain it.
- Status: `[ ] Unverified`

---

## 2. What "Information" Means When It Arrives as Language

These sources establish why linguistic data is fundamentally different from numeric data and why it carries unique signal.

### 2.1 Foundational: Narrative Economics

**Shiller, Robert J. "Narrative Economics." *American Economic Review* 107, no. 4 (April 2017): 967–1004.**

- DOI: `10.1257/aer.107.4.967`
- **Summary:** AEA Presidential Address. Argues that popular narratives "go viral" and drive economic behavior — spending, investing, hiring. Proposes "narrative economics" as a formal research program studying how contagious stories shape economic events. Uses the 1920–21 Depression, the Great Depression, and the Great Recession as case studies of narrative-driven economic behavior.
- **Relevance:** *Section 2.* This is the single most important theoretical source for the chapter. Shiller provides the framework for treating narratives as causal economic forces, not just reflections of fundamentals. This directly supports the book's core thesis that text captures *why* markets move.
- **How to use:** Central to Section 2. Shiller's epidemiological model of narrative contagion provides the conceptual bridge between "text exists" and "text drives markets."
- Status: `[ ] Unverified`

---

**Shiller, Robert J. *Narrative Economics: How Stories Go Viral and Drive Major Economic Events*. Princeton, NJ: Princeton University Press, 2019.**

- ISBN: `978-0-691-18229-2`
- **Summary:** Expands the 2017 AEA address into a full treatment. Defines an economic narrative as "a contagious story that has the potential to change how people make economic decisions." Traces narrative contagion across multiple historical episodes. Winner of the PROSE Award in Economics.
- **Relevance:** *Section 2.* The book-length treatment gives depth to the argument. Particularly useful for the "contagion" framing — narratives spread like epidemics, and NLP can track that spread in real time.
- **How to use:** Cite alongside the 2017 article for readers who want the full argument. The "contagious story" definition is quotable and precise.
- Status: `[ ] Unverified`

---

### 2.2 Foundational: Language, Framing, and Decision-Making

**Tversky, Amos, and Daniel Kahneman. "The Framing of Decisions and the Psychology of Choice." *Science* 211, no. 4481 (January 1981): 453–458.**

- DOI: `10.1126/science.7455683`
- **Summary:** Demonstrates that logically identical outcomes produce different decisions depending on how they are framed linguistically. Establishes framing effects as a robust cognitive bias — the *way* information is presented matters as much as the information itself.
- **Relevance:** *Section 2.* Framing effects are the behavioral-economics justification for why *language* carries unique signal. If the same earnings result framed as "beat expectations by 2 cents" vs. "revenue growth decelerated" produces different market reactions, then the linguistic framing *is* the information.
- **How to use:** Brief citation to ground the argument that language is not a transparent container for facts — it actively shapes how recipients process information.
- Status: `[ ] Unverified`

---

**Kahneman, Daniel, and Amos Tversky. "Prospect Theory: An Analysis of Decision under Risk." *Econometrica* 47, no. 2 (March 1979): 263–292.**

- DOI: `10.2307/1914185`
- **Summary:** Proposes prospect theory as an alternative to expected utility theory. People evaluate outcomes relative to a reference point and are loss-averse. Won Kahneman the 2002 Nobel Prize. The theory implies that how outcomes are described (gains vs. losses framing) affects economic decisions.
- **Relevance:** *Section 2.* Loss aversion and reference-dependent preferences explain why negative language in financial text has disproportionate impact on markets — a finding confirmed empirically by Tetlock (2007) and Loughran-McDonald (2011).
- **How to use:** Pairs with Tversky-Kahneman (1981) to establish the behavioral foundation. Brief reference — the detailed empirical evidence comes from the NLP papers below.
- Status: `[ ] Unverified`

---

## 3. Historical Examples: Text Moving Markets

These sources provide the concrete evidence that text drives measurable market outcomes.

### 3.1 Foundational: Media and Market Sentiment

**Tetlock, Paul C. "Giving Content to Investor Sentiment: The Role of Media in the Stock Market." *Journal of Finance* 62, no. 3 (June 2007): 1139–1168.**

- DOI: `10.1111/j.1540-6261.2007.01232.x`
- **Summary:** Quantifies the relationship between media pessimism and stock market behavior using daily content from the Wall Street Journal's "Abreast of the Market" column. Finds that (1) high media pessimism predicts downward pressure on prices followed by reversion to fundamentals, and (2) unusually high or low pessimism predicts high trading volume. Won the 2007 Smith-Breeden Prize.
- **Relevance:** *Section 3 (Historical Examples).* This is the landmark empirical paper proving that media text carries tradeable signal. It's the bridge between the theoretical arguments (Sections 1–2) and the practical NLP pipeline the rest of the book builds.
- **How to use:** Central to Section 3. The WSJ column analysis is a concrete, accessible example of text moving markets. Emphasize the reversion finding — it suggests noise trading driven by sentiment, not new fundamental information.
- Status: `[ ] Unverified`

---

**Tetlock, Paul C., Maytal Saar-Tsechansky, and Sofus Macskassy. "More Than Words: Quantifying Language to Measure Firms' Fundamentals." *Journal of Finance* 63, no. 3 (June 2008): 1437–1467.**

- DOI: `10.1111/j.1540-6261.2008.01362.x`
- **Summary:** Extends Tetlock (2007) from market-level to firm-level analysis. Finds that (1) the fraction of negative words in firm-specific news stories forecasts low firm earnings, (2) stock prices briefly underreact to the information embedded in negative words, and (3) earnings and return predictability from negative words is largest for stories that focus on fundamentals. Analyzes all WSJ and Dow Jones News Service stories about S&P 500 firms, 1980–2004.
- **Relevance:** *Section 3.* Demonstrates that text-based signals predict *fundamentals* (earnings), not just sentiment-driven price moves. This is stronger evidence for financial NLP than pure sentiment correlation.
- **How to use:** Pair with Tetlock (2007) to show the progression from market-level to firm-level prediction. The "underreaction" finding supports the EMH challenge from Section 1.
- Status: `[ ] Unverified`

---

### 3.2 Methodological: Earnings Call Tone and Post-Earnings Drift

**Price, S. McKay, James S. Doran, David R. Peterson, and Barbara A. Bliss. "Earnings Conference Calls and Stock Returns: The Incremental Informativeness of Textual Tone." *Journal of Banking & Finance* 36, no. 4 (April 2012): 992–1011.**

- DOI: `10.1016/j.jbankfin.2011.10.013`
- **Summary:** Demonstrates that the linguistic tone of earnings conference calls is a significant predictor of abnormal returns and trading volume. Conference call tone dominates earnings surprises in explaining post-earnings-announcement drift (PEAD) over the 60 trading days following the call. The Q&A portion has incremental explanatory power, concentrated in firms with higher cash flow uncertainty.
- **Relevance:** *Section 3 (Earnings Call Tone).* Concrete evidence that earnings call language predicts stock drift — one of the three historical examples outlined in the chapter plan.
- **How to use:** Use as the primary citation for the earnings call tone example. The finding that tone *dominates* earnings surprises is striking and highly quotable.
- Status: `[ ] Unverified`

---

**Meursault, Vitaly, Pierre Liang, Bryan Routledge, and Madeline Marco Scanlon. "PEAD.txt: Post-Earnings-Announcement Drift Using Text." *Journal of Financial and Quantitative Analysis* 58, no. 6 (September 2023): 2409–2439.**

- DOI: `10.1017/S0022109022001181`
- **Summary:** Constructs a text-only model for predicting post-earnings announcement drift. The text-based PEAD (PEAD.txt) produces a drift of 8.01% from one day after the earnings call to the calendar year mark — the largest purely machine learning model-based drift documented. Uses computational linguistics techniques and large language models.
- **Relevance:** *Section 3.* Demonstrates the state of the art in text-based earnings signal construction. The 8.01% drift figure is a powerful "text works" datapoint.
- **How to use:** Cite as evidence of how far earnings-text analysis has progressed since Tetlock (2007). The magnitude of the drift makes the case that NLP is not marginal — it's economically significant.
- Status: `[ ] Unverified`

---

### 3.3 Empirical: Social Media and Market Behavior

**Bollen, Johan, Huina Mao, and Xiaojun Zeng. "Twitter Mood Predicts the Stock Market." *Journal of Computational Science* 2, no. 1 (March 2011): 1–8.**

- DOI: `10.1016/j.jocs.2010.12.007`
- **Summary:** Analyzes Twitter feeds using OpinionFinder and Google-Profile of Mood States (GPOMS) to predict DJIA movements. Achieves 86.7% accuracy in predicting daily up/down changes in DJIA closing values. Finds that specific mood dimensions (especially "Calm") are predictive, but not all. Over 2,500 Google Scholar citations.
- **Relevance:** *Section 3 (Twitter Sentiment Preceding Price Moves).* The canonical early paper on social media sentiment predicting markets. High-profile and widely cited — readers will expect to see it.
- **How to use:** Cite as the landmark social media-to-market paper, but note its limitations (short sample period, specific mood dimensions, replication concerns raised by Lachanski and Pav 2017).
- Status: `[ ] Unverified`

---

**Costola, Michele, Marco Nofer, Oliver Hinz, and Loriana Pelizzon. "Self-Induced Consensus of Reddit Users to Characterise the GameStop Short Squeeze." *Scientific Reports* 12, article 13263 (August 2022).**

- DOI: `10.1038/s41598-022-17925-2`
- **Summary:** Analyzes the GameStop short squeeze (January 2021) through r/wallstreetbets Reddit data. Finds that the occurrence and sentiment of GME-related comments increased significantly *before* the short squeeze. A small minority of 462 influential subredditors disproportionately impacted GME stock returns and volatility.
- **Relevance:** *Section 3.* The GameStop saga is the most vivid recent example of social media text moving markets. This peer-reviewed paper provides rigorous analysis for what was widely covered in popular press.
- **How to use:** Use as the GameStop case study citation. The "462 influential subredditors" finding illustrates information asymmetry *within* social media, which connects back to Section 1's efficiency discussion.
- Status: `[ ] Unverified`

---

**Long, Wenjie, Brian Lucey, Aleksandar Šević, and Lamia Nouri. "'I Just Like the Stock': The Role of Reddit Sentiment in the GameStop Share Rally." *Financial Review* 58, no. 1 (February 2023): 19–37.**

- DOI: `10.1111/fire.12328`
- **Summary:** Examines the role of Reddit sentiment in the GameStop rally. Finds that the tone of discussions on r/wallstreetbets displayed significant predictive associations with intraday GameStop returns, volatility, bid-ask spreads, and volumes.
- **Relevance:** *Section 3.* A complementary GameStop study focusing on intraday dynamics. Useful for showing that text signal operates at multiple time scales.
- **How to use:** Pair with Costola et al. (2022) for a complete GameStop case study.
- Status: `[ ] Unverified`

---

**Antweiler, Werner, and Murray Z. Frank. "Is All That Talk Just Noise? The Information Content of Internet Stock Message Boards." *Journal of Finance* 59, no. 3 (June 2004): 1259–1294.**

- DOI: `10.1111/j.1540-6261.2004.00662.x`
- **Summary:** Analyzes over 1.5 million messages on Yahoo Finance and Raging Bull about Dow Jones companies. Finds that stock messages help predict market volatility (statistically significant, economically small effect on returns) and that disagreement among posted messages is associated with increased trading volume. Over 2,400 citations.
- **Relevance:** *Section 3.* The earliest rigorous study of online text and markets — a historical predecessor to the social media studies. Establishes that even noisy online discussion carries some information content.
- **How to use:** Cite as the historical starting point for the social media → markets literature. The "not just noise" framing is useful for Chapter 1's argument.
- Status: `[ ] Unverified`

---

**Das, Sanjiv R., and Mike Y. Chen. "Yahoo! for Amazon: Sentiment Extraction from Small Talk on the Web." *Management Science* 53, no. 9 (September 2007): 1375–1388.**

- DOI: `10.1287/mnsc.1070.0704`
- **Summary:** Develops a methodology for extracting investor sentiment from stock message boards using an ensemble of classifiers. Finds that aggregate tech-sector sentiment predicts stock index levels, but not individual stock returns. Time series and cross-sectional aggregation improves sentiment index quality.
- **Relevance:** *Section 3.* Early work on sentiment extraction methodology. The aggregation finding (sector-level prediction works better than stock-level) is a useful caveat about the granularity of text-based signals.
- **How to use:** Cite alongside Antweiler and Frank (2004) as foundational message-board studies. The aggregation insight connects to Chapter 5's signal construction discussion.
- Status: `[ ] Unverified`

---

### 3.4 Empirical: Central Bank Language

**Rosa, Carlo. "The Financial Market Effect of FOMC Minutes." *Federal Reserve Bank of New York Economic Policy Review* 19, no. 2 (December 2013): 67–81.**

- URL: `https://www.newyorkfed.org/medialibrary/media/research/epr/2013/0913rosa.pdf`
- **Summary:** Finds that the release of FOMC minutes induces "higher than normal" volatility across asset classes. Volatility of two-year Treasury yields is roughly three times larger on event days than during non-event periods.
- **Relevance:** *Section 3 (Fed Minutes Moving Bond Markets).* Direct evidence that Fed text releases cause measurable market impact.
- **How to use:** Use for the Fed minutes historical example. The "3x volatility" figure is concrete and compelling.
- Status: `[ ] Unverified`

---

**Doh, Taeyoung, Dongho Song, and Shu-Kuei X. Yang. "Deciphering Federal Reserve Communication via Text Analysis." Federal Reserve Bank of Kansas City Research Working Paper no. 20-14 (2020).**

- URL: `https://www.kansascityfed.org/documents/5642/rwp20-14dohsongyang.pdf`
- **Summary:** Applies text analysis methods (including the Universal Sentence Encoder and FinBERT) to FOMC statements to quantify sentiment. Finds that sentiment scores are among the most important predictors of financial market reactions in the first minute after FOMC announcements.
- **Relevance:** *Section 3.* Demonstrates state-of-the-art NLP applied to central bank communication. The "first minute" finding illustrates how quickly text-based information is processed by markets.
- **How to use:** Cite as a modern NLP application to Fed communication. Bridges Chapter 1's historical examples to the technical methods developed in later chapters (especially Chapter 7).
- Status: `[ ] Unverified`

---

### 3.5 Empirical: Social Media and Individual Market Events

**Dam, Jauron Gunther. "CEO's Tweets and Firm Stock Returns: A Case Study of Elon Musk and Tesla." Honors thesis, Georgia Southern University, 2021.**

- URL: `https://digitalcommons.georgiasouthern.edu/honors-theses/850/`
- **Summary:** Event study analysis of Elon Musk's tweets and Tesla stock returns. Documents specific instances of dramatic market movements, including the May 2020 "stock price too high" tweet causing an immediate 10% drop, and the SEC $40M settlement following the 2018 "funding secured" tweet.
- **Relevance:** *Section 3 (Musk Tweets Example).* A concrete, well-documented case study of social media language moving stock prices — and the regulatory response.
- **How to use:** Use as a vivid case study alongside more rigorous aggregate studies. The SEC settlement adds a regulatory dimension.
- **Note:** This is an honors thesis, not a peer-reviewed journal article. Consider pairing with a more authoritative source if available.
- Status: `[ ] Unverified`

---

**Manela, Asaf, and Alan Moreira. "News Implied Volatility and Disaster Concerns." *Journal of Financial Economics* 123, no. 1 (January 2017): 137–162.**

- DOI: `10.1016/j.jfineco.2016.01.032`
- **Summary:** Constructs NVIX, a text-based measure of uncertainty using front-page WSJ articles dating back to 1890. NVIX peaks during crashes, policy uncertainty, world wars, and financial crises. High NVIX periods are followed by above-average stock returns, even after controlling for VIX and other volatility measures.
- **Relevance:** *Section 3.* Demonstrates that text-based risk measures capture information not contained in traditional volatility metrics. The 130-year time span makes the argument that text signal is not a recent artifact — it has been present throughout modern financial history.
- **How to use:** Powerful evidence for the longevity and robustness of text-based signals. The "1890 to present" construction is striking for a Chapter 1 argument about why text *has always* mattered.
- Status: `[ ] Unverified`

---

## 4. Why NLP Has Lagged Price/Volume Quant Strategies

### 4.1 Methodological: The State of Financial Text Analysis

**Loughran, Tim, and Bill McDonald. "When Is a Liability Not a Liability? Textual Analysis, Dictionaries, and 10-Ks." *Journal of Finance* 66, no. 1 (February 2011): 35–65.**

- DOI: `10.1111/j.1540-6261.2010.01625.x`
- **Summary:** Shows that word lists developed for other disciplines (notably the Harvard General Inquirer) misclassify nearly three-fourths of "negative" words in financial contexts — "liability," "tax," "cost" are not negative in 10-K filings. Develops an alternative set of six financial sentiment word lists (negative, positive, litigious, uncertainty, constraining, superfluous) containing 2,337 negative words specifically calibrated for financial text.
- **Relevance:** *Section 4 (Why NLP Lagged) and Section 5 (Taxonomy).* This paper simultaneously explains a key barrier (generic NLP tools failed on financial text) and provides a solution. It's foundational for Chapters 3 and 5 as well.
- **How to use:** Central to the "why NLP lagged" argument. The "three-fourths misclassification" finding vividly illustrates that financial text requires domain-specific methods — which weren't available until recently.
- **Cross-reference:** Also relevant to Chapter 3 (NLP Foundations) and Chapter 5 (Sentiment Analysis).
- Status: `[ ] Unverified`

---

**Loughran, Tim, and Bill McDonald. "Textual Analysis in Accounting and Finance: A Survey." *Journal of Accounting Research* 54, no. 4 (September 2016): 1187–1230.**

- DOI: `10.1111/1475-679X.12123`
- **Summary:** Comprehensive survey of textual analysis methods in accounting and finance. Covers bag-of-words, readability, word lists, Zipf's law, cosine similarity, and Naive Bayes. Describes nuances and implementation challenges while reviewing contemporary literature and highlighting areas for future research.
- **Relevance:** *Section 4.* The definitive survey of the field as of 2016. Useful for contextualizing where financial NLP stood before the transformer revolution.
- **How to use:** Cite as the field's self-assessment just before transformers changed everything. The gap between this survey and current capabilities illustrates why NLP has accelerated.
- **Cross-reference:** Also relevant to Chapter 3 (NLP Foundations).
- Status: `[ ] Unverified`

---

**Kearney, Colm, and Sha Liu. "Textual Sentiment in Finance: A Survey of Methods and Models." *International Review of Financial Analysis* 33 (May 2014): 171–185.**

- DOI: `10.1016/j.irfa.2014.02.006`
- **Summary:** Surveys information sources, content analysis methods, and empirical models used in financial textual sentiment analysis. Summarizes findings on how textual sentiment impacts individual, firm-level, and market-level behavior and performance.
- **Relevance:** *Section 4.* An earlier survey that captures the state of the field in the pre-deep-learning era. Useful for showing how limited the toolkit was before BERT/transformers.
- **How to use:** Pair with Loughran-McDonald (2016) to establish the "before" picture.
- Status: `[ ] Unverified`

---

**Gentzkow, Matthew, Bryan Kelly, and Matt Taddy. "Text as Data." *Journal of Economic Literature* 57, no. 3 (September 2019): 535–574.**

- DOI: `10.1257/jel.20181020`
- **Summary:** Introduces text-as-data methods to the economics profession. Discusses features that make text different from other data, provides a practical overview of statistical methods (bag-of-words, embeddings, topic models, supervised learning), and surveys applications across economics. Originally circulated as NBER Working Paper no. 23276 (2017).
- **Relevance:** *Section 4 and Chapter 3.* The canonical methodological reference for economists approaching text data. Useful for readers coming from quantitative finance backgrounds who need the bridge from "traditional data" to "text data."
- **How to use:** Cite as the methodological foundation. The paper's framing of text's unique properties (high dimensionality, context dependence, ambiguity) explains why quant strategies were slow to adopt it.
- **Cross-reference:** Also relevant to Chapter 3 (NLP Foundations).
- Status: `[ ] Unverified`

---

### 4.2 Contextual: Why the Barriers Are Falling

**Xing, Frank Zheng, Erik Cambria, and Roy E. Welsch. "Natural Language Based Financial Forecasting: A Survey." *Artificial Intelligence Review* 50, no. 1 (June 2018): 49–73.**

- DOI: `10.1007/s10462-017-9588-9`
- **Summary:** Surveys NLP-based financial forecasting methods, covering sentiment analysis, event extraction, and time series prediction from text. Documents the progression from dictionary-based to machine learning to deep learning approaches.
- **Relevance:** *Section 4.* Documents the technical progression that enabled modern financial NLP. Useful for the "why now" argument — the convergence of transformer models, accessible APIs, and cloud compute.
- Status: `[ ] Unverified`

---

**Li, Qing, Chao Wang, and Jiawei Han. "Natural Language Processing in Finance: A Survey." *Information Fusion* 114 (February 2025): 102755.**

- DOI: `10.1016/j.inffus.2024.102755`
- **Summary:** Comprehensive 2024/2025 survey covering ten major financial NLP applications: sentiment analysis, narrative processing, forecasting, portfolio management, question answering, risk management, regulatory compliance, ESG, explainable AI, and digital assets. The most current survey of the field available.
- **Relevance:** *Section 4 (and cross-chapter).* Captures the current state of the art, including LLM-era advances. Useful for showing how far the field has come since the Loughran-McDonald and Kearney-Liu surveys.
- **How to use:** Cite as the most current panoramic view of the field.
- **Cross-reference:** Useful across multiple chapters as a general reference.
- Status: `[ ] Unverified`

---

## 5. A Taxonomy of Financial Text Data

### 5.1 Methodological: Readability and Disclosure Quality

**Li, Feng. "Annual Report Readability, Current Earnings, and Earnings Persistence." *Journal of Accounting and Economics* 45, no. 2–3 (August 2008): 221–247.**

- DOI: `10.1016/j.jacceco.2008.02.003`
- **Summary:** Measures readability of public company annual reports using the Fog index and document length. Finds that (1) annual reports of firms with lower earnings are harder to read, and (2) firms with easier-to-read reports have more persistent positive earnings. In profitable firms, causation words ("because") associate with less persistent earnings, positive emotion words with more persistent earnings.
- **Relevance:** *Section 5 (Taxonomy).* Demonstrates that even the *readability* of financial text carries signal — establishing that multiple linguistic dimensions beyond sentiment are informative. This is a key example under "structured, scheduled" text (10-K annual reports).
- **How to use:** Cite to show that financial text carries signal at multiple levels (sentiment, readability, specificity). The "harder to read = lower earnings" finding is counterintuitive and memorable.
- **Cross-reference:** Also relevant to Chapter 6 (Corporate Disclosure).
- Status: `[ ] Unverified`

---

### 5.2 Methodological: Word-Level Financial Analysis

**Jegadeesh, Narasimhan, and Di Wu. "Word Power: A New Approach for Content Analysis." *Journal of Financial Economics* 110, no. 3 (December 2013): 712–729.**

- DOI: `10.1016/j.jfineco.2013.08.012`
- **Summary:** Develops a data-driven approach to weighting words based on their stock market reaction, rather than using pre-defined sentiment dictionaries. Finds that the appropriate choice of term weighting is at least as important as accurate word list compilation. Significant relation between document tone (using this method) and market reaction to 10-K filings.
- **Relevance:** *Section 5 (Taxonomy).* Illustrates the evolution from manually constructed dictionaries to data-driven approaches. This methodological progression is part of the "why NLP lagged" story — earlier methods required expensive human curation.
- **How to use:** Cite to show that the field has moved beyond hand-curated word lists toward more sophisticated approaches.
- **Cross-reference:** Also relevant to Chapter 3 (NLP Foundations) and Chapter 5 (Signal Construction).
- Status: `[ ] Unverified`

---

## 6. NLP Adoption in Industry

### 6.1 Contextual: Hedge Fund and Asset Manager Adoption

**Alternative Investment Management Association (AIMA). "Getting in Pole Position: How Hedge Funds Are Leveraging Gen AI to Get Ahead." London: AIMA, 2024.**

- URL: `https://www.aima.org/static/a4f9bc40-8c32-42e6-87f52bd89f6e1a82/How-hedge-funds-are-leveraging-Gen-AI-to-get-ahead.pdf`
- **Summary:** Industry survey finding that 86% of hedge fund managers permit staff to use generative AI tools. Documents use cases including document analysis, summarization, and content generation. Notes that AI-led hedge funds generated cumulative returns roughly 3x the broader hedge fund universe (33.9% vs. 12.1%, per Cerulli Associates analysis).
- **Relevance:** *Section 4 (Why NLP Lagged — and Why That's Changing).* Industry adoption data grounds the "barriers are falling" argument in current practice, not just academic research.
- **How to use:** Cite the 86% adoption and 3x return figures as evidence that the industry has moved past skepticism. Note that this is an industry report, not peer-reviewed research — use for context, not as proof of alpha.
- **Note:** Industry report, not peer-reviewed. Verify currency of statistics.
- Status: `[ ] Unverified`

---

## Cross-Chapter References

The following sources cited above are also relevant to subsequent chapters. This tracking prevents redundant research in later passes.

| Source | Ch 1 Section | Also Relevant To |
|--------|-------------|------------------|
| Loughran & McDonald (2011) | Sec 4 (Why NLP Lagged) | Ch 3 (Lexicons), Ch 5 (Sentiment) |
| Loughran & McDonald (2016) | Sec 4 (Survey) | Ch 3 (Methods Survey) |
| Gentzkow, Kelly & Taddy (2019) | Sec 4 (Text as Data) | Ch 3 (Methodology) |
| Price et al. (2012) | Sec 3 (Earnings Calls) | Ch 6 (Earnings Calls) |
| Meursault et al. (2023) | Sec 3 (PEAD) | Ch 6 (Earnings Calls), Ch 11 (Evaluation) |
| Rosa (2013) | Sec 3 (Fed Minutes) | Ch 7 (Central Bank Language) |
| Doh, Song & Yang (2020) | Sec 3 (Fed NLP) | Ch 7 (Central Bank Language) |
| Costola et al. (2022) | Sec 3 (GameStop) | Ch 8 (Social Media) |
| Long et al. (2023) | Sec 3 (GameStop) | Ch 8 (Social Media) |
| Antweiler & Frank (2004) | Sec 3 (Message Boards) | Ch 8 (Social Media) |
| Das & Chen (2007) | Sec 3 (Message Boards) | Ch 8 (Social Media) |
| Li (2008) | Sec 5 (Readability) | Ch 6 (Corporate Disclosure) |
| Li et al. (2025) | Sec 4 (Survey) | All chapters (general reference) |

---

## Research Gaps

The following areas need additional sourcing:

- [ ] **Quantitative statistics on volume of financial text data generated daily** — SEC filing counts, financial news article volume, social media post volume. Check SEC EDGAR statistics page and GDELT documentation for aggregate counts.
- [ ] **Musk tweets — peer-reviewed source:** The current Musk citation is an honors thesis (Dam 2021). Search for a peer-reviewed event study or law review article analyzing the SEC enforcement action and market impact.
- [ ] **Taper tantrum 2013 — NLP-specific analysis:** The 2013 taper tantrum is well-documented as a market event, but a specific paper applying NLP to Bernanke's testimony/communication would strengthen the Fed example. Eichengreen et al. (2014, NBER) or Feroli et al. (2014) may address this.
- [ ] **History of quant text strategies at specific funds:** Two Sigma, Renaissance Technologies, or Bridgewater references to text-based strategies would ground the industry adoption narrative. Likely found in industry press (Institutional Investor, Risk.net) rather than academic journals.
- [ ] **Additional behavioral finance sources:** Consider Thaler (2015) *Misbehaving*, De Bondt and Thaler (1985) on overreaction, or Barberis and Thaler (2003) "A Survey of Behavioral Finance" for a stronger behavioral bridge.
- [ ] **Malkiel "A Random Walk Down Wall Street"** as a popular counterpoint to Shiller's narrative economics — useful for framing the intellectual debate.

---

## Verification Priority

Start SMU Library verification with these sources first (highest impact on chapter quality):

1. **Shiller (2017)** — AEA Presidential Address (anchors the entire chapter)
2. **Fama (1970)** — EMH foundation
3. **Grossman & Stiglitz (1980)** — The paradox that justifies financial NLP
4. **Tetlock (2007)** — Landmark empirical proof
5. **Loughran & McDonald (2011)** — Domain-specific NLP breakthrough
6. **Manela & Moreira (2017)** — 130 years of text-based signal
7. **Tetlock, Saar-Tsechansky & Macskassy (2008)** — Firm-level text prediction
8. **Shiller (2019)** — Book-length treatment of narrative economics
9. **Gentzkow, Kelly & Taddy (2019)** — Text-as-data methodology
10. **Bollen, Mao & Zeng (2011)** — Social media prediction (high-profile, some controversy)

---

*Research compiled April 2026. All citations require manual verification through SMU Library before inclusion in final manuscript.*
