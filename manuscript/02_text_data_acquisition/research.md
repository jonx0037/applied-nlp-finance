# Chapter 2 — Text Data Acquisition — Annotated Bibliography

**Purpose:** This chapter provides a comprehensive, honest guide to sourcing financial text data. It covers the major sources — SEC EDGAR, financial news APIs, earnings call transcripts, central bank communications, and social media — with practical details on access methods, rate limits, legal considerations, and data pipeline design.

**What this chapter needs from its sources:**
- Academic papers that validate each data source (proving researchers have successfully used it)
- Technical documentation for APIs and data access methods
- Legal references for web scraping and data licensing
- Methodology papers on data quality, provenance, and versioning
- Practical references for pipeline design and reproducibility

**Citation format:** Chicago (Notes and Bibliography), 17th edition.

**Note on source types:** Unlike Chapter 1 (primarily peer-reviewed theory/empirics), Chapter 2 draws from a mix of academic papers, technical documentation, legal rulings, and industry reports. Sources are annotated with their type to help calibrate how to cite them in the manuscript.

---

## 1. SEC EDGAR: Structured Corporate Filings

These sources establish EDGAR as a research-grade data source and address the technical challenges of parsing filings.

### 1.1 Reference: EDGAR Documentation and APIs

**U.S. Securities and Exchange Commission. "EDGAR Application Programming Interfaces." SEC.gov, accessed April 2026.**

- URL: `https://www.sec.gov/search-filings/edgar-application-programming-interfaces`
- **Type:** Official technical documentation.
- **Summary:** Documents the RESTful APIs at data.sec.gov for accessing EDGAR submissions and extracted XBRL data in JSON format. No authentication or API keys required. APIs cover submissions history by filer and XBRL data from 10-Q, 10-K, 8-K, 20-F, 40-F, 6-K forms. Rate limit: 10 requests per second; exceeding triggers a temporary IP block (~10 minutes). Full-text search available at efts.sec.gov, indexing the complete text of every filing.
- **Relevance:** *Section 1 (SEC EDGAR).* The primary technical reference for building an EDGAR data pipeline. Rate limits and API structure must be documented accurately since readers will build scrapers against this API.
- **How to use:** Cite as the authoritative technical source. Emphasize the 10 req/sec limit and the distinction between structured XBRL endpoints (data.sec.gov) and full-text search (efts.sec.gov).
- Status: `[ ] Unverified`

---

### 1.2 Methodological: EDGAR Corpus and Parsing Tools

**Loukas, Lefteris, Manos Fergadiotis, Ion Androutsopoulos, and Prodromos Malakasiotis. "EDGAR-CORPUS: Billions of Tokens Make the World Go Round." In *Proceedings of the Third Workshop on Economics and Natural Language Processing*, 13–18. Punta Cana, Dominican Republic: Association for Computational Linguistics, November 2021.**

- DOI: `10.18653/v1/2021.econlp-1.2`
- URL: `https://aclanthology.org/2021.econlp-1.2/`
- **Type:** Peer-reviewed workshop paper.
- **Summary:** Introduces EDGAR-CORPUS, the largest financial NLP corpus available, comprising annual reports from all publicly traded US companies spanning 25+ years. Reports are downloaded, split into their corresponding item sections, and provided in clean JSON format. The authors also release EDGAR-W2V word embeddings trained on this corpus, demonstrating superiority over generic GloVe embeddings on financial NLP tasks.
- **Relevance:** *Section 1 (EDGAR) and Section 7 (Pipeline Design).* Demonstrates how to systematically parse EDGAR filings at scale. The corpus itself is a resource readers can use directly.
- **How to use:** Cite as the canonical example of building a large-scale EDGAR NLP dataset. The section-splitting methodology is directly applicable to readers' own pipelines. Also reference the companion tool EDGAR-CRAWLER.
- **Cross-reference:** Also relevant to Chapter 3 (NLP Foundations — training data).
- Status: `[ ] Unverified`

---

**Loukas, Lefteris, Manos Fergadiotis, Ion Androutsopoulos, and Prodromos Malakasiotis. "EDGAR-CRAWLER: From Raw Web Documents to Structured Financial NLP Datasets." In *Companion Proceedings of the ACM Web Conference 2025*. Sydney, Australia: ACM, 2025.**

- DOI: `10.1145/3701716.3715289`
- **Type:** Peer-reviewed conference demo paper (WWW 2025).
- **Summary:** Open-source toolkit for downloading SEC EDGAR financial reports and extracting textual data from specific item sections into structured JSON files. The only open-source toolkit offering end-to-end EDGAR download-to-structured-data pipeline.
- **Relevance:** *Section 1 and Section 7.* Practical tool readers can use directly. Demonstrates the engineering challenges of parsing EDGAR HTML at scale.
- **How to use:** Cite alongside EDGAR-CORPUS as the tool companion. Direct readers to the GitHub repository for immediate use.
- Status: `[ ] Unverified`

---

**Bao, Yang, and Anindya Datta. "Simultaneously Discovering and Quantifying Risk Types from Textual Risk Disclosures." *Management Science* 60, no. 6 (June 2014): 1371–1391.**

- DOI: `10.1287/mnsc.2014.1930`
- **Type:** Peer-reviewed journal article.
- **Summary:** Develops a variation of LDA topic modeling for discovering and quantifying risk types from 10-K textual risk disclosures. Finds that around two-thirds of disclosed risk types lack informativeness. Three types of systematic and liquidity risks increase investor risk perceptions, while five types of unsystematic risks decrease them.
- **Relevance:** *Section 1 (EDGAR).* Validates 10-K risk factor sections as a structured NLP target. Demonstrates a specific, high-value use case for EDGAR text extraction.
- **How to use:** Cite as evidence that risk factor sections carry differentiated signal — motivating why readers should build parsers that extract these specific sections.
- **Cross-reference:** Also relevant to Chapter 6 (Corporate Disclosure).
- Status: `[ ] Unverified`

---

### 1.3 Methodological: Readability and Filing Quality

**Loughran, Tim, and Bill McDonald. "Measuring Readability in Financial Disclosures." *Journal of Finance* 69, no. 4 (August 2014): 1643–1671.**

- DOI: `10.1111/jofi.12162`
- **Type:** Peer-reviewed journal article.
- **Summary:** Shows that the Fog index — the most commonly applied readability measure — is poorly specified in financial applications. One of its two components is misspecified, the other is difficult to measure. Finds that 10-K file size provides a better proxy for readability. Recommends using the "complete submission text file" size from EDGAR.
- **Relevance:** *Section 1 (EDGAR) and Section 7 (Pipeline Design).* Directly relevant to data quality decisions: which metadata to capture from EDGAR filings (file size matters), and how to avoid misapplying standard NLP metrics to financial text.
- **How to use:** Cite as a cautionary tale about naively applying generic NLP tools to financial filings — and as a practical reason to capture file size metadata in the data pipeline.
- **Cross-reference:** Also relevant to Chapter 3 (NLP Foundations) and Chapter 6 (Corporate Disclosure).
- Status: `[ ] Unverified`

---

## 2. Financial News APIs

### 2.1 Reference: GDELT

**Leetaru, Kalev, and Philip Schrodt. "GDELT: Global Data on Events, Location and Tone, 1979–2012." Paper presented at the International Studies Association Annual Convention, San Francisco, CA, April 2013.**

- URL: `https://www.gdeltproject.org/about.html`
- **Type:** Conference paper / technical documentation.
- **Summary:** Introduces GDELT, a CAMEO-coded dataset containing 200+ million geolocated events with global coverage from 1979 to the present. Data are based on news reports from international sources, coded for events, location, and tone. Updated in near real-time. Free and open access.
- **Relevance:** *Section 2 (Financial News APIs).* GDELT is the most comprehensive free news event database. Its tone scoring and event coding are directly useful for financial NLP, though it requires filtering for financial relevance.
- **How to use:** Cite as the primary free alternative to commercial news APIs. Discuss its strengths (coverage, history, cost) and limitations (requires financial event filtering, not purpose-built for finance).
- Status: `[ ] Unverified`

---

### 2.2 Contextual: News Sentiment and Market Prediction

**Manela, Asaf, and Alan Moreira. "News Implied Volatility and Disaster Concerns." *Journal of Financial Economics* 123, no. 1 (January 2017): 137–162.**

- DOI: `10.1016/j.jfineco.2016.01.032`
- **Type:** Peer-reviewed journal article.
- **Summary:** Constructs NVIX, a text-based measure of uncertainty from front-page WSJ articles dating to 1890. Demonstrates that news text carries information about market risk not captured by VIX or other traditional volatility measures.
- **Relevance:** *Section 2.* Validates financial news as a data source with deep historical coverage and measurable market impact. The 130-year time span demonstrates the longevity of news-text signal.
- **How to use:** Cite as evidence that news APIs are worth the investment — the signal is real and persistent.
- **Cross-reference:** Already cited in Chapter 1 research.
- Status: `[ ] Unverified`

---

### 2.3 Contextual: Analyst Reports as Data Source

**Huang, Allen H., Amy Y. Zang, and Rong Zheng. "Evidence on the Information Content of Text in Analyst Reports." *Accounting Review* 89, no. 6 (November 2014): 2151–2180.**

- DOI: `10.2308/accr-50865`
- **Type:** Peer-reviewed journal article.
- **Summary:** Analyzes 363,952 analyst reports for S&P 500 firms (1995–2008) using Naive Bayes. Finds that textual discussions provide information to investors beyond earnings forecasts, stock recommendations, and target prices. Investors react more strongly to negative than positive text. Report text is more useful when it emphasizes nonfinancial topics, is written assertively and concisely, and when other signals in the report have low perceived validity.
- **Relevance:** *Section 2 (News APIs and Data Sources).* Validates analyst reports as a distinct, high-value financial text data source — separate from news and filings. Motivates including analyst report APIs in the data acquisition strategy.
- **How to use:** Cite to justify including analyst reports in the taxonomy of financial text sources. The "negative text > positive text" finding connects to Tetlock (2007) from Chapter 1.
- Status: `[ ] Unverified`

---

## 3. Earnings Call Transcripts

### 3.1 Methodological: Transcript Quality and NLP Performance

**Price, S. McKay, James S. Doran, David R. Peterson, and Barbara A. Bliss. "Earnings Conference Calls and Stock Returns: The Incremental Informativeness of Textual Tone." *Journal of Banking & Finance* 36, no. 4 (April 2012): 992–1011.**

- DOI: `10.1016/j.jbankfin.2011.10.013`
- **Type:** Peer-reviewed journal article.
- **Summary:** Conference call tone is a significant predictor of abnormal returns and trading volume. Tone dominates earnings surprises in explaining PEAD over 60 trading days. Q&A portion has incremental explanatory power concentrated in firms with higher cash flow uncertainty.
- **Relevance:** *Section 3 (Earnings Call Transcripts).* Validates earnings call transcripts as a high-value data source. The Q&A vs. prepared remarks distinction motivates building parsers that separate these sections.
- **How to use:** Cite as the canonical academic validation of earnings calls as NLP input. The section-specific findings (Q&A > prepared remarks for some signals) inform how to structure the data pipeline.
- **Cross-reference:** Already cited in Chapter 1 research.
- Status: `[ ] Unverified`

---

### 3.2 Methodological: NLP Approaches for Earnings Calls

**FactSet. "Comparing Natural Language Processing (NLP) Approaches for Earnings Calls." FactSet Insight, 2023.**

- URL: `https://insight.factset.com/comparing-natural-language-processing-nlp-approaches-for-earnings-calls`
- **Type:** Industry research report.
- **Summary:** Compares three NLP approaches on a dataset of 1.7 million corporate documents: FinBERT, Loughran-McDonald (LM), and Alexandria Technology. Finds large disagreement among the three, particularly at the topic and sentence level. Alexandria significantly outperforms FinBERT and LM in a simulation against the S&P 500 over a decade.
- **Relevance:** *Section 3.* Demonstrates that the choice of NLP method applied to earnings calls matters as much as the data source. Also illustrates the scale of data available from vendor APIs.
- **How to use:** Cite as an industry perspective on NLP model choice for earnings call analysis. The 1.7M document dataset figure contextualizes the scale of vendor data.
- **Note:** Industry report, not peer-reviewed. Use for practical context.
- Status: `[ ] Unverified`

---

### 3.3 Methodological: StockTwits as Labeled Data Source

**Divernois, Marc-Aurèle, and Damir Filipović. "StockTwits Classified Sentiment and Stock Returns." *Digital Finance* 5 (2023): 607–636.**

- DOI: `10.1007/s42521-023-00102-z`
- **Type:** Peer-reviewed journal article.
- **Summary:** Uses StockTwits self-labeled bullish/bearish sentiment data (January 2010 – March 2020) for all US and Canadian stocks. Machine learning classifiers trained on user sentiment-labeled messages achieve 85.9% out-of-sample accuracy, comparable to human annotator agreement (80–85%). Self-labeled sentiments are argued to be better measurements than algorithmically derived ones.
- **Relevance:** *Section 5 (Social Media Sources — StockTwits).* Validates StockTwits as a data source with unique self-labeling property. The 85.9% classification accuracy establishes a benchmark.
- **How to use:** Cite as the primary academic validation of StockTwits data quality. The self-labeling feature makes it unique among social media financial data sources.
- Status: `[ ] Unverified`

---

## 4. Central Bank Communications

### 4.1 Reference: FRASER and FOMC Archives

**Federal Reserve Bank of St. Louis. "Federal Open Market Committee Meeting Minutes, Transcripts, and Other Documents, 1933–2026." FRASER Digital Library, accessed April 2026.**

- URL: `https://fraser.stlouisfed.org/title/federal-open-market-committee-meeting-minutes-transcripts-documents-677`
- **Type:** Official archive / digital library.
- **Summary:** Comprehensive archive of FOMC materials dating to 1933, including: Greenbooks (1964–2010) with staff economic analysis, minutes (1993–present), full transcripts released with a five-year lag, agendas, Beige Books, and the FOMC Speak database (August 2010 – August 2023) of speeches, testimony, and interviews by FOMC participants.
- **Relevance:** *Section 4 (Central Bank Communications).* The primary data source reference for Fed text. FRASER is free, comprehensive, and the canonical source for Fed communication research.
- **How to use:** Cite as the authoritative source for FOMC text data. Document the five-year lag for transcripts (vs. weeks for minutes) as a practical data access constraint.
- Status: `[ ] Unverified`

---

**Federal Reserve Board. "Transcripts and Other Historical Materials." FederalReserve.gov, accessed April 2026.**

- URL: `https://www.federalreserve.gov/monetarypolicy/fomc_historical.htm`
- **Type:** Official government website.
- **Summary:** The Fed's own page for accessing FOMC transcripts, Bluebooks, Greenbooks, and summaries of individual economic projections. Materials released with approximately five-year delay.
- **Relevance:** *Section 4.* Companion to FRASER — some materials are available here that may not yet be on FRASER.
- Status: `[ ] Unverified`

---

### 4.2 Methodological: ECB Communication Corpus

**Fraccaroli, Nicolo, Arnaud Capon, Jean-Charles Bricongne, and Burkhard Raunig. "European Central Bank's Monetary Policy Decisions: A Dataset of Two Decades of Press Conferences." *Data in Brief* 21 (December 2018): 2488–2494.**

- DOI: `10.1016/j.dib.2018.11.130`
- **Type:** Peer-reviewed data descriptor.
- **Summary:** Provides a structured database of ECB monetary policy press conferences, including introductory statements and Q&A transcripts. Covers three main ECB communication tools: press conferences, speeches, and interviews from February 1997 to July 2020.
- **Relevance:** *Section 4 (Central Bank — ECB).* The primary structured data source for ECB communication analysis. Ready-to-use dataset for NLP research.
- **How to use:** Cite as the canonical ECB communication dataset. Direct readers to this for ECB analysis parallel to FRASER for the Fed.
- Status: `[ ] Unverified`

---

**European Central Bank. "Speeches Dataset." ECB.europa.eu, accessed April 2026.**

- URL: `https://www.ecb.europa.eu/press/key/html/downloads.en.html`
- **Type:** Official dataset.
- **Summary:** Precompiled dataset of all ECB speeches with metadata, updated monthly. Released explicitly to assist NLP researchers studying central bank communication impact on markets.
- **Relevance:** *Section 4.* Official ECB resource specifically designed for NLP research — notable that the ECB itself recognizes and supports this use case.
- Status: `[ ] Unverified`

---

### 4.3 Methodological: Central Bank NLP Research

**Bholat, David, Stephen Hansen, Pedro Santos, and Cheryl Schonhardt-Bailey. "Text Mining for Central Banks." *Centre for Central Banking Studies Handbook* no. 33. London: Bank of England, 2015.**

- URL: `https://www.bankofengland.co.uk/ccbs/text-mining-for-central-banks`
- **Type:** Central bank handbook / technical guide.
- **Summary:** Practical guide to text mining methods for central bank applications. Covers preprocessing, sentiment analysis, topic modeling, and text classification applied to central bank documents. Written by Bank of England researchers for central banking practitioners.
- **Relevance:** *Section 4.* Authoritative guide on how central banks themselves approach text mining of their own communications. Useful for understanding the structure and conventions of central bank text.
- **How to use:** Cite as a domain-expert guide to central bank text data. The BoE perspective complements the Fed/ECB sources.
- **Cross-reference:** Also relevant to Chapter 7 (Central Bank Language).
- Status: `[ ] Unverified`

---

**Bank for International Settlements. "CB-LMs: Language Models for Central Banking." BIS Working Papers no. 1215. Basel: BIS, October 2024.**

- URL: `https://www.bis.org/publ/work1215.pdf`
- **Type:** Central bank working paper.
- **Summary:** Assembles a corpus of central banking text including 37,037 research papers and 18,345 speeches for language model development. Develops domain-specific language models for central banking text analysis.
- **Relevance:** *Section 4.* Documents the scale of central bank text data available (37K papers + 18K speeches) and demonstrates domain-specific language model training on this corpus.
- **How to use:** Cite for the corpus statistics and to show that central banks are actively building NLP tools for their own domain.
- **Cross-reference:** Also relevant to Chapter 4 (Financial Language Models) and Chapter 7 (Central Bank Language).
- Status: `[ ] Unverified`

---

## 5. Social Media Sources

### 5.1 Foundational: Social Media Financial Data

**Cookson, J. Anthony, Joseph Engelberg, and William Mullins. "Does Partisanship Shape Investor Beliefs? Evidence from the COVID-19 Pandemic." *Review of Asset Pricing Studies* 10, no. 4 (December 2020): 863–893.**

- DOI: `10.1093/rapstu/raaa018`
- **Type:** Peer-reviewed journal article.
- **Summary:** Uses party-identifying language ("Liberal Media," "MAGA") to identify Republican users on StockTwits. Finds that partisan Republicans' equity beliefs remain unfazed during COVID-19 while other users become more pessimistic. Stocks with greatest partisan disagreement on StockTwits have significantly more trading in the broader market, explaining 28% of the increase in stock turnover during the pandemic.
- **Relevance:** *Section 5 (Social Media).* Demonstrates a sophisticated use of StockTwits as an academic data source. The methodology for identifying user demographics from text content is directly applicable to readers building social media NLP pipelines.
- **How to use:** Cite as a model for how academic researchers use social media financial data. The "language as demographic signal" approach is a creative NLP application.
- Status: `[ ] Unverified`

---

### 5.2 Reference: API Access and Platform Changes

**Pfeffer, Jürgen, Daniel Matter, Kokil Jaidka, Onur Varol, Afra Mashhadi, Jana Lasser, Dennis Assenmacher, et al. "RIP Twitter API: A Eulogy to Its Vast Research Contributions." arXiv preprint, arXiv:2404.07340, April 2024.**

- URL: `https://arxiv.org/abs/2404.07340`
- **Type:** Preprint.
- **Summary:** Documents the impact of Twitter/X API pricing changes on academic research. Twitter-based studies had increased by a median of 25% annually from 2006 to 2023, but following the decision to charge for data, studies dropped by 13%. The paper catalogs the vast body of research that relied on free Twitter API access, effectively serving as a historical record of the platform's research contribution.
- **Relevance:** *Section 5 (Social Media — Twitter/X).* Essential context for the Twitter/X API section. Documents the transition from free academic access to the current tiered pricing ($200/month Basic to $42,000/month Enterprise). Helps readers understand why historical Twitter studies may not be replicable at the same cost.
- **How to use:** Cite as the authoritative account of Twitter's API transition and its research impact. The 25% annual growth → 13% decline statistic vividly illustrates the platform shift.
- Status: `[ ] Unverified`

---

**Coalition for Independent Technology Research. "Letter: Twitter's New API Plans Will Devastate Public Interest Research." February 2023.**

- URL: `https://independenttechresearch.org/letter-twitters-new-api-plans-will-devastate-public-interest-research/`
- **Type:** Open letter / advocacy document.
- **Summary:** Signed by over 100 researchers, this letter documents the academic community's response to Twitter's API pricing changes. Argues that the loss of affordable access threatens research on misinformation, public health, election integrity, and market manipulation.
- **Relevance:** *Section 5.* Provides the institutional perspective on API access changes. Useful for contextualizing the data access landscape readers will navigate.
- **Note:** Advocacy document, not peer-reviewed. Use for context.
- Status: `[ ] Unverified`

---

### 5.3 Reference: Reddit API Changes

**TechCrunch. "Reddit Will Begin Charging for Access to Its API." April 18, 2023.**

- URL: `https://techcrunch.com/2023/04/18/reddit-will-begin-charging-for-access-to-its-api/`
- **Type:** News article / trade press.
- **Summary:** Documents Reddit's announcement that it would begin charging for API access effective July 1, 2023, at $0.24 per 1,000 API calls. The free API had been available since 2008. The change eliminated third-party apps and priced out many academic researchers. Reddit maintains a free tier for personal/academic/non-commercial use, rate-limited to 100 requests per minute with OAuth.
- **Relevance:** *Section 5 (Social Media — Reddit).* Essential context for the Reddit/PRAW section. The free tier (100 req/min) is still viable for academic research, but with significant limitations compared to pre-2023 access.
- **How to use:** Cite to document the current Reddit API landscape. Emphasize the free academic tier still exists but with constraints.
- **Note:** Trade press, not academic. Use for factual reporting on API changes.
- Status: `[ ] Unverified`

---

## 6. Web Scraping Ethics and Legal Considerations

### 6.1 Foundational: Legal Framework

***Van Buren v. United States*, 593 U.S. 374 (2021).**

- URL: `https://www.supremecourt.gov/opinions/20pdf/19-783_k53l.pdf`
- **Type:** U.S. Supreme Court opinion.
- **Summary:** In a 6-3 opinion authored by Justice Barrett (June 3, 2021), the Court held that the CFAA's "exceeds authorized access" provision applies only when someone accesses information that is entirely off-limits — not when someone accesses permitted information for unauthorized purposes. Establishes a "gates-up-or-down" test: liability turns on whether the information accessed was within areas the user was authorized to access at all.
- **Relevance:** *Section 6 (Legal Considerations).* The foundational CFAA case for web scraping legality. Narrowed the CFAA so that accessing publicly available data cannot trigger criminal liability, even in violation of terms of service.
- **How to use:** Cite as the Supreme Court precedent establishing that scraping publicly available data is not a CFAA violation. This is the most important legal reference for the chapter.
- Status: `[ ] Unverified`

---

***hiQ Labs, Inc. v. LinkedIn Corp.*, 31 F.4th 1180 (9th Cir. 2022).**

- URL: `https://cdn.ca9.uscourts.gov/datastore/opinions/2022/04/18/17-16783.pdf`
- **Type:** U.S. Court of Appeals (9th Circuit) opinion.
- **Summary:** On remand from the Supreme Court following *Van Buren*, the Ninth Circuit reaffirmed that scraping publicly available data on a website does not violate the CFAA. Applied the *Van Buren* "gates-up-or-down" framework: publicly available website data has no access barriers, therefore scraping it cannot trigger CFAA liability. However, the case ultimately settled with hiQ agreeing to stop scraping LinkedIn — based on *contract* claims (User Agreement breach), not CFAA.
- **Relevance:** *Section 6.* The most directly relevant web scraping case. The dual outcome is critical for readers: CFAA doesn't apply to public data, but contract/ToS claims can still restrict scraping. This distinction matters for financial data scrapers.
- **How to use:** Cite alongside *Van Buren* to give readers the complete legal picture. Emphasize the CFAA/contract distinction — CFAA protection doesn't override Terms of Service agreements.
- Status: `[ ] Unverified`

---

### 6.2 Contextual: Ethical Frameworks

**Krotov, Vlad, and Leigh Silva. "Legality and Ethics of Web Scraping." In *Proceedings of the Twenty-Fourth Americas Conference on Information Systems (AMCIS)*. New Orleans, LA: AIS, August 2018.**

- URL: Search AMCIS 2018 proceedings
- **Type:** Peer-reviewed conference paper.
- **Summary:** Surveys the legal and ethical landscape of web scraping. Discusses robots.txt compliance, Terms of Service considerations, and proposes an ethical framework for data collection from web sources.
- **Relevance:** *Section 6 (Ethics and Legal).* Provides a structured ethical framework beyond just legal compliance. Useful for the chapter's argument that responsible data acquisition is both an ethical obligation and a practical necessity.
- **How to use:** Cite for the ethical framework, complementing the legal cases above.
- Status: `[ ] Unverified`

---

## 7. Building a Reliable Data Pipeline

### 7.1 Methodological: Data Versioning

**Iterative.ai. "DVC: Data Version Control." Documentation, accessed April 2026.**

- URL: `https://doc.dvc.org/`
- **Type:** Technical documentation.
- **Summary:** Open-source tool for data management, ML pipeline automation, and experiment management. Unlike Git-LFS, DVC doesn't require a special server, has no file size limits, and supports ML-specific features (pipeline management, metrics tracking, experiment reproducibility). DVC files in the Git repository enable reproducible workflows. Can store data on S3, GCS, Azure, or local storage.
- **Relevance:** *Section 8 (Data Versioning).* The primary tool recommendation for versioning large text datasets. DVC's advantages over git-lfs (no server requirement, no file size limits, ML-native features) make it the better choice for this project.
- **How to use:** Compare DVC vs. git-lfs concretely. DVC wins on: no server requirement, no file size limit, ML pipeline support, multiple storage backend options.
- Status: `[ ] Unverified`

---

### 7.2 Methodological: Data Provenance

**Longpre, Shayne, Robert Mahari, Anthony Chen, Naana Obeng-Marnu, Damien Sileo, William Brannon, Niklas Muennighoff, et al. "The Data Provenance Initiative: A Large Scale Audit of Dataset Licensing and Attribution in AI." arXiv preprint, arXiv:2310.16787, October 2023. Published in *Nature Machine Intelligence* 2, no. 8 (2024): 883–896.**

- DOI: `10.1038/s42256-024-00878-8`
- **Type:** Peer-reviewed journal article.
- **Summary:** Large-scale audit of popular AI datasets for licensing and attribution. Finds license omission rates of over 70% and error rates over 50% on popular dataset hosting sites. Develops tools and standards for tracing dataset lineage including source, creators, licenses, and subsequent use.
- **Relevance:** *Section 7 (Pipeline Design — Provenance).* Makes the case for rigorous data provenance tracking in financial NLP pipelines. The 70% license omission finding motivates building provenance into the pipeline from day one, not as an afterthought.
- **How to use:** Cite to motivate the provenance tracking design. The licensing audit statistics are compelling evidence for why this matters.
- Status: `[ ] Unverified`

---

### 7.3 Contextual: Reproducibility in ML

**Kästner, Christian. "Versioning, Provenance, and Reproducibility in Production Machine Learning." Medium / Carnegie Mellon University, 2020.**

- URL: `https://ckaestne.medium.com/versioning-provenance-and-reproducibility-in-production-machine-learning-355c48665005`
- **Type:** Technical blog post (faculty-authored).
- **Summary:** Argues that versioning, provenance tracking, and reproducibility are essential tools for responsible ML engineering. Provides a framework for debugging, reliable experiments, trustworthy deployments, security safeguards, and accountability/auditing.
- **Relevance:** *Section 7 and Section 8.* Articulates the *why* behind data versioning and provenance — useful for readers who need motivation beyond "it's best practice."
- **How to use:** Use for framing the argument. Pair with the Longpre et al. (2024) paper for empirical evidence.
- **Note:** Blog post, not peer-reviewed. Use for framing, not as primary citation.
- Status: `[ ] Unverified`

---

## 8. Survey and Cross-Cutting References

### 8.1 Surveys of Financial Text Data Sources

**Gentzkow, Matthew, Bryan Kelly, and Matt Taddy. "Text as Data." *Journal of Economic Literature* 57, no. 3 (September 2019): 535–574.**

- DOI: `10.1257/jel.20181020`
- **Type:** Peer-reviewed survey article.
- **Summary:** Canonical introduction to text-as-data methods in economics. Discusses what makes text different from other data, surveys statistical methods, and reviews applications. The methodological foundation for treating text as a data source.
- **Relevance:** *Entire chapter.* Provides the theoretical justification for treating text as data worthy of rigorous pipeline design.
- **How to use:** Cite early in the chapter to establish the "text is data" framing that motivates everything that follows.
- **Cross-reference:** Already cited in Chapter 1 research.
- Status: `[ ] Unverified`

---

**Li, Qing, Chao Wang, and Jiawei Han. "Natural Language Processing in Finance: A Survey." *Information Fusion* 114 (February 2025): 102755.**

- DOI: `10.1016/j.inffus.2024.102755`
- **Type:** Peer-reviewed survey article.
- **Summary:** Comprehensive 2024/2025 survey covering ten major financial NLP applications. Categorizes financial data into corporate data, public news/announcements, and social media data — a taxonomy directly applicable to this chapter's structure.
- **Relevance:** *Entire chapter.* The data taxonomy (corporate / news / social) provides an academic grounding for the chapter's organizational structure.
- **How to use:** Cite for the data taxonomy framework.
- **Cross-reference:** Already cited in Chapter 1 research.
- Status: `[ ] Unverified`

---

**Loughran, Tim, and Bill McDonald. "Textual Analysis in Accounting and Finance: A Survey." *Journal of Accounting Research* 54, no. 4 (September 2016): 1187–1230.**

- DOI: `10.1111/1475-679X.12123`
- **Type:** Peer-reviewed survey article.
- **Summary:** Comprehensive survey of textual analysis methods in accounting and finance. Covers data collection challenges, preprocessing, and methodological nuances specific to financial text.
- **Relevance:** *Entire chapter.* Addresses data collection challenges that motivate the pipeline design sections.
- **Cross-reference:** Already cited in Chapter 1 research.
- Status: `[ ] Unverified`

---

## Cross-Chapter References

| Source | Ch 2 Section | Also Relevant To |
|--------|-------------|------------------|
| Loukas et al. (2021) EDGAR-CORPUS | Sec 1 (EDGAR) | Ch 3 (Training Data), Ch 4 (Financial LMs) |
| Bao & Datta (2014) | Sec 1 (EDGAR Risk Factors) | Ch 6 (Corporate Disclosure) |
| Loughran & McDonald (2014) Readability | Sec 1 (EDGAR) | Ch 3 (NLP Foundations), Ch 6 (Disclosure) |
| Price et al. (2012) | Sec 3 (Earnings Calls) | Ch 6 (Earnings Calls) |
| Divernois & Filipović (2023) | Sec 5 (StockTwits) | Ch 8 (Social Media) |
| Cookson et al. (2020) | Sec 5 (StockTwits) | Ch 8 (Social Media) |
| FRASER Archive | Sec 4 (Central Bank) | Ch 7 (Central Bank Language) |
| ECB Speeches Dataset | Sec 4 (Central Bank) | Ch 7 (Central Bank Language) |
| BIS CB-LMs (2024) | Sec 4 (Central Bank) | Ch 4 (Financial LMs), Ch 7 (Central Bank) |
| Bholat et al. (2015) | Sec 4 (Central Bank) | Ch 7 (Central Bank Language) |
| Gentzkow et al. (2019) | Entire chapter | Ch 1, Ch 3 |
| Li et al. (2025) | Entire chapter | All chapters |
| Manela & Moreira (2017) | Sec 2 (News) | Ch 1 (Historical Examples) |
| Huang et al. (2014) | Sec 2 (Analyst Reports) | Ch 6 (Corporate Disclosure) |
| *Van Buren* (2021) | Sec 6 (Legal) | Ch 13 (Ethics and Limits) |
| *hiQ v. LinkedIn* (2022) | Sec 6 (Legal) | Ch 13 (Ethics and Limits) |

---

## Research Gaps

The following areas need additional sourcing:

- [ ] **Bloomberg vs. Refinitiv vs. NewsAPI vs. Alpaca News comparison table** — Need specific academic studies or industry reports comparing coverage breadth, latency, historical depth, and cost across these providers. Current search results yielded terminal comparisons (Bloomberg vs. Capital IQ) but not API-specific comparisons for NLP use cases.
- [ ] **Seeking Alpha transcript scraping legality** — Need specific legal analysis or Terms of Service documentation regarding scraping Seeking Alpha earnings transcripts. The hiQ v. LinkedIn framework applies, but SA-specific precedent would strengthen the section.
- [ ] **BoJ English-language releases and BoE Monetary Policy Committee archives** — Need structured data source references comparable to FRASER (Fed) and ECB speeches dataset. Search for BoJ's English publications portal and BoE's speech archive.
- [ ] **Deduplication methodology for multi-source text data** — Need academic papers on text deduplication specifically in financial contexts (same event covered by multiple sources, syndicated content, etc.).
- [ ] **Timestamp normalization across sources** — Need references on handling timezone differences, publication vs. event timestamps, and point-in-time concerns when combining data from EDGAR, news APIs, and social media.
- [ ] **PRAW library documentation and current rate limits** — Need to verify current PRAW documentation against Reddit's post-2023 API structure. The free academic tier (100 req/min with OAuth) needs confirmation.
- [ ] **robots.txt specification and ethical scraping frameworks** — RFC 9309 (the 2022 Robots Exclusion Protocol standard) should be cited as the technical specification. Search for academic frameworks beyond Krotov & Silva (2018).

---

## Verification Priority

Start SMU Library verification with these sources first:

1. **Loukas et al. (2021)** — EDGAR-CORPUS (practical tool + academic validation)
2. ***Van Buren v. United States* (2021)** — Supreme Court CFAA precedent
3. ***hiQ Labs v. LinkedIn* (2022)** — Web scraping case law
4. **Bao & Datta (2014)** — Risk factor text extraction from EDGAR
5. **Loughran & McDonald (2014)** — Readability measurement in filings
6. **Fraccaroli et al. (2018)** — ECB press conference dataset
7. **Divernois & Filipović (2023)** — StockTwits data quality validation
8. **Cookson et al. (2020)** — StockTwits as academic data source
9. **Pfeffer et al. (2024)** — Twitter API research impact
10. **Longpre et al. (2024)** — Data provenance audit (Nature MI)

---

*Research compiled April 2026. All citations require manual verification through SMU Library before inclusion in final manuscript.*
