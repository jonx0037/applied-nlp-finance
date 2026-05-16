# Chapter 8 — Social Media and Alternative Text Data — Annotated Bibliography

**Purpose:** This chapter handles noisier, higher-frequency, and legally complex text sources. It uses Reddit's WallStreetBets as a case study, covers bot detection and data quality filtering, compares news vs. social media sentiment dynamics, examines short squeeze detection, and explores crypto social media channels.

**What this chapter needs from its sources:**
- GameStop/WallStreetBets case study with rigorous academic analysis
- StockTwits data quality, self-labeling bias, and predictive power
- Bot detection and coordinated inauthentic behavior in financial social media
- News vs. social media sentiment comparison (lead-lag, correlation, divergence)
- Short squeeze and pump-and-dump detection from text patterns
- Crypto social media (Discord, Telegram) data access and analysis
- Theoretical framework for social media's role in price formation

**Citation format:** Chicago (Notes and Bibliography), 17th edition.

**Note on source diversity:** This chapter draws from an unusually wide range of disciplines — finance journals (JFE, RFS), computational social science, crime science (Kamps-Kleinberg), information systems, and network science. The GameStop episode alone generated papers in nature, financial economics, and computational linguistics venues. The editorial challenge is maintaining rigor while covering a topic that attracts hype.

---

## 1. Reddit WallStreetBets: Signal vs. Noise

### 1.1 Foundational: GameStop Academic Studies

**Costola, Michele, Marco Nofer, Oliver Hinz, and Loriana Pelizzon. "Self-Induced Consensus of Reddit Users to Characterise the GameStop Short Squeeze." *Scientific Reports* 12, article 13263 (August 2022).**

- DOI: `10.1038/s41598-022-17925-2`
- **Type:** Peer-reviewed journal article (Nature portfolio).
- **Summary:** Analyzes the GameStop short squeeze through r/wallstreetbets Reddit data. Finds that GME-related comment occurrence and sentiment increased significantly *before* the short squeeze. A small minority of 462 influential subredditors disproportionately impacted GME stock returns and volatility.
- **Relevance:** *Section 1 (WSB Case Study).* The primary peer-reviewed GameStop study in a high-impact journal. The "462 influential users" finding is critical — it shows that social media influence is concentrated, not democratic, which has implications for signal extraction and manipulation detection.
- **How to use:** Central to the GameStop case study. The pre-squeeze buildup in sentiment and the concentration of influence among a small minority provide concrete, data-driven narratives.
- **Cross-reference:** Already cited in Chapter 1 research.
- Status: `[ ] Unverified`

---

**Bradley, Daniel, Jan Hanousek Jr., Russell Jame, and Zicheng Xiao. "Place Your Bets? The Value of Investment Research on Reddit's Wallstreetbets." *Review of Financial Studies* 37, no. 5 (May 2024): 1409–1459.**

- DOI: `10.1093/rfs/hhad098`
- **Type:** Peer-reviewed journal article (top-3 finance journal).
- **Summary:** Examines "due diligence" (DD) buy recommendations on WSB. Pre-GameStop, DD recommendations yield 1.1% two-day returns, 2% monthly drift, and nearly 5% quarterly drift — suggesting genuine stock-picking skill. Post-GameStop, predictability is eliminated as WSB shifts toward attention-grabbing and price-pressure stocks. Retail trading increases sharply in the intraday window following DD publication.
- **Relevance:** *Section 1 (WSB Case Study).* The definitive RFS paper on WSB's information content. The pre/post-GameStop structural break is a key finding: WSB contained genuine alpha *before* it went viral, but the signal degraded after mainstream attention. This is a concrete example of alpha decay through crowding.
- **How to use:** Central to Section 1. Present the pre-GME DD findings as evidence that social media *can* carry genuine information, then the post-GME findings as evidence that signal quality degrades when platforms attract attention-seekers.
- Status: `[ ] Unverified`

---

**Long, Wenjie, Brian Lucey, Aleksandar Šević, and Lamia Nouri. "'I Just Like the Stock': The Role of Reddit Sentiment in the GameStop Share Rally." *Financial Review* 58, no. 1 (February 2023): 19–37.**

- DOI: `10.1111/fire.12328`
- **Type:** Peer-reviewed journal article.
- **Summary:** WSB sentiment displays significant predictive associations with intraday GameStop returns, volatility, bid-ask spreads, and volumes.
- **Relevance:** *Section 1.* Complements Costola et al. (2022) with intraday-level analysis.
- **Cross-reference:** Already cited in Chapter 1 research.
- Status: `[ ] Unverified`

---

### 1.2 Theoretical: Social Networks and Asset Pricing

**Pedersen, Lasse Heje. "Game On: Social Networks and Markets." *Journal of Financial Economics* 146, no. 3 (December 2022): 1097–1119.**

- DOI: `10.1016/j.jfineco.2022.05.002`
- **Type:** Peer-reviewed journal article.
- **Summary:** Develops a model where four investor types — naive learners, fanatics (possibly spreading misinformation), rational short-term, and rational long-term — trade in the presence of a social network. Shows that social networks generate bubbles, high volume bursts, price momentum, and reversal. Fanatic and rational views dominate over time, with relative importance depending on influencer following. Discusses the GameStop case and Robinhood platform outages.
- **Relevance:** *Section 1 (Theoretical Framework).* Provides the formal economic theory for why social media affects asset prices — the chapter's theoretical foundation. The four-investor-type model helps readers understand *why* social sentiment is informative (wisdom of crowds) and *when* it's noise (fanatic manipulation).
- **How to use:** Cite early as the theoretical framework. Pedersen's model explains both the signal (naive investors aggregating dispersed information) and the noise (fanatics spreading misinformation), which structures the chapter's signal-vs-noise discussion.
- Status: `[ ] Unverified`

---

## 2. StockTwits and Microblogging Sentiment

### 2.1 Foundational: StockTwits Data Quality

**Cookson, J. Anthony, Joseph Engelberg, and William Mullins. "Echo Chambers." *Review of Financial Studies* 36, no. 2 (February 2023): 450–500.**

- DOI: `10.1093/rfs/hhac058`
- **Type:** Peer-reviewed journal article (top-3 finance journal).
- **Summary:** Studies 400,000 StockTwits users and finds striking evidence of echo chambers: self-described bulls are 5x more likely to follow bullish users than bears. Bulls see 62 more bullish messages and 24 fewer bearish messages than bears over 50 days. Echo chambers exist even among professional investors, are strongest for investors who trade on beliefs, and beliefs formed in echo chambers are associated with lower ex-post returns, more information siloing, and more trading volume.
- **Relevance:** *Section 2 (StockTwits).* The primary reference for understanding StockTwits data quality and bias. Echo chambers mean that aggregate StockTwits sentiment is *not* a simple consensus measure — it's inflated by selective exposure. NLP systems that naively aggregate sentiment without accounting for echo chamber effects will overweight the dominant narrative.
- **How to use:** Central to Section 2. The 5x following bias and lower return association are concrete, quotable findings. Frame echo chambers as a form of data quality issue specific to social media — the data is biased at the network level, not just the individual message level.
- Status: `[ ] Unverified`

---

**Divernois, Marc-Aurèle, and Damir Filipović. "StockTwits Classified Sentiment and Stock Returns." *Digital Finance* 5 (2023): 607–636.**

- DOI: `10.1007/s42521-023-00102-z`
- **Type:** Peer-reviewed journal article.
- **Summary:** Uses StockTwits self-labeled bullish/bearish data (2010–2020). ML classifiers trained on self-labeled messages achieve 85.9% accuracy, comparable to human annotator agreement (80–85%).
- **Relevance:** *Section 2 (StockTwits).* Validates the self-labeling mechanism and establishes classification baselines.
- **Cross-reference:** Already cited in Chapter 2 research.
- Status: `[ ] Unverified`

---

**Renault, Thomas. "Intraday Online Investor Sentiment and Return Patterns in the U.S. Stock Market." *Journal of Banking & Finance* 84 (November 2017): 25–40.**

- DOI: `10.1016/j.jbankfin.2017.07.002`
- **Type:** Peer-reviewed journal article.
- **Summary:** Half-hour StockTwits sentiment aggregation predicts same-day S&P 500 returns. Intraday effect driven by novice trader sentiment shifts.
- **Relevance:** *Section 2.* Demonstrates predictive power at high frequency from StockTwits data.
- **Cross-reference:** Already cited in Chapter 5 research.
- Status: `[ ] Unverified`

---

### 2.2 Foundational: Social Media and Stock Prediction (Early Work)

**Chen, Hailiang, Prabuddha De, Yu Jeffrey Hu, and Byoung-Hyoun Hwang. "Wisdom of Crowds: The Value of Stock Opinions Transmitted Through Social Media." *Review of Financial Studies* 27, no. 5 (May 2014): 1367–1403.**

- DOI: `10.1093/rfs/hhu001`
- **Type:** Peer-reviewed journal article (top-3 finance journal).
- **Summary:** Investigates whether investor opinions on social media platforms predict future stock returns and earnings surprises. Finds that views in both articles and commentaries predict future returns and earnings surprises.
- **Relevance:** *Section 2 (Historical Context).* The earliest top-journal validation that social media investor opinions carry genuine predictive information. Provides the academic foundation for treating social media text as a legitimate data source.
- **How to use:** Cite as the foundational "wisdom of crowds" paper for financial social media. Predates the StockTwits and WSB studies, establishing the field.
- Status: `[ ] Unverified`

---

## 3. News Momentum vs. Social Media Momentum

### 3.1 Empirical: Comparative Dynamics

**Azar, Pablo D., and Andrew W. Lo. "The Wisdom of Twitter Crowds: Predicting Stock Market Reactions to FOMC Meetings via Twitter Feeds." *Journal of Portfolio Management* 42, no. 5 (2016): 123–134.**

- DOI: `10.3905/jpm.2016.42.5.123`
- **Type:** Peer-reviewed journal article.
- **Summary:** Compares Twitter sentiment with traditional news sentiment for predicting market reactions to FOMC meetings. Demonstrates that Twitter sentiment provides incremental information beyond news for specific event types.
- **Relevance:** *Section 3 (News vs. Social Media).* Direct comparison of Twitter and news sentiment for a specific, well-defined market event (FOMC meetings). The "when does social media add value beyond news?" question is the section's core theme.
- Status: `[ ] Unverified`

---

**Tetlock, Paul C. "Giving Content to Investor Sentiment: The Role of Media in the Stock Market." *Journal of Finance* 62, no. 3 (June 2007): 1139–1168.**

- DOI: `10.1111/j.1540-6261.2007.01232.x`
- **Summary:** WSJ pessimism predicts market pressure and reversion; high/low pessimism predicts volume.
- **Relevance:** *Section 3.* The baseline for news sentiment against which social media sentiment should be compared. Tetlock's WSJ findings establish what news *alone* can predict — social media's value is in the increment above this.
- **Cross-reference:** Already cited in Chapters 1 and 5 research.
- Status: `[ ] Unverified`

---

## 4. Bot Detection and Data Quality

### 4.1 Methodological: Bot and Coordinated Behavior Detection

**Cresci, Stefano. "A Decade of Social Bot Detection." *Communications of the ACM* 63, no. 10 (October 2020): 72–83.**

- DOI: `10.1145/3409116`
- **Type:** Peer-reviewed journal article (CACM).
- **Summary:** Comprehensive survey of social bot detection over the 2010–2020 decade. Covers the evolution from simple heuristics (account age, posting frequency) to sophisticated ML approaches (behavioral analysis, network features, linguistic fingerprinting). Documents the arms race between bot creators and detectors.
- **Relevance:** *Section 4 (Bot Detection).* The canonical survey of bot detection methodology. Provides the technical framework for the filtering pipeline the chapter teaches.
- **How to use:** Cite as the comprehensive reference. The "arms race" framing is important — readers need to understand that bot detection is an ongoing challenge, not a solved problem. Simple heuristics (account age < 30 days, posting frequency > 50/day) catch naive bots but miss sophisticated ones.
- Status: `[ ] Unverified`

---

### 4.2 Empirical: Financial Market Manipulation via Social Media

**Cookson, J. Anthony, Joseph Engelberg, and William Mullins. "Does Partisanship Shape Investor Beliefs? Evidence from the COVID-19 Pandemic." *Review of Asset Pricing Studies* 10, no. 4 (December 2020): 863–893.**

- DOI: `10.1093/rapstu/raaa018`
- **Type:** Peer-reviewed journal article.
- **Summary:** Uses party-identifying language to identify political affiliation on StockTwits. Partisan Republicans' equity beliefs remained unfazed during COVID-19. Stocks with greatest partisan disagreement had significantly more trading, explaining 28% of increased turnover.
- **Relevance:** *Section 4 (Data Quality).* Demonstrates that social media financial data is contaminated by non-financial beliefs (political partisanship). This is a form of data quality challenge: sentiment that appears bullish may reflect political identity rather than informed investment views.
- **Cross-reference:** Already cited in Chapter 2 research.
- Status: `[ ] Unverified`

---

## 5. Short Squeeze Detection

### 5.1 Foundational: Pump-and-Dump Detection

**Kamps, Josh, and Bennett Kleinberg. "To the Moon: Defining and Detecting Cryptocurrency Pump-and-Dumps." *Crime Science* 7, article 18 (December 2018).**

- DOI: `10.1186/s40163-018-0093-5`
- **Type:** Peer-reviewed journal article.
- **Summary:** Synthesizes classical pump-and-dump literature with cryptocurrency markets. Proposes criteria for defining crypto pump-and-dumps and uses anomaly detection on trading data (sudden price and volume spikes) to flag potential schemes. Finds that fraudulent activity clusters on specific exchanges and coins.
- **Relevance:** *Section 5 (Short Squeeze Detection).* The primary academic reference for pump-and-dump detection methodology. While focused on crypto, the anomaly detection framework (identifying unusual co-occurrence of price spikes, volume spikes, and text mention spikes) transfers to equity short squeeze detection.
- **How to use:** Cite as the foundational P&D detection paper, then adapt the framework for the equity short squeeze context. The "text + price + volume" multi-signal approach is the right architecture for squeeze detection.
- Status: `[ ] Unverified`

---

## 6. Crypto Social Media Channels

### 6.1 Empirical: Crypto Sentiment and Price Prediction

**Kraaijeveld, Olivier, and Johannes De Smedt. "The Predictive Power of Public Twitter Sentiment for Forecasting Cryptocurrency Prices." *Journal of International Financial Markets, Institutions and Money* 65 (March 2020): 101188.**

- DOI: `10.1016/j.intfin.2020.101188`
- **Type:** Peer-reviewed journal article.
- **Summary:** Examines whether Twitter sentiment predicts cryptocurrency price movements. Finds that sentiment has predictive power for certain cryptocurrencies, particularly Bitcoin, but the relationship is more complex than simple positive/negative sentiment → price direction.
- **Relevance:** *Section 6 (Crypto Social Media).* Validates social media sentiment as a signal source for crypto markets — which are inherently more social-media-driven than traditional equity markets.
- **How to use:** Cite to establish that crypto social media analysis has empirical grounding. Note the platform-specific challenges: crypto communities span Twitter/X, Discord, Telegram, and on-chain data, making multi-platform aggregation essential.
- Status: `[ ] Unverified`

---

### 6.2 Empirical: Telegram Pump-and-Dump Groups

**Xu, Jiahua, and Benjamin Livshits. "The Anatomy of a Cryptocurrency Pump-and-Dump Scheme." In *Proceedings of the 28th USENIX Security Symposium*, 1609–1625. Santa Clara, CA: USENIX, August 2019.**

- URL: `https://www.usenix.org/conference/usenixsecurity19/presentation/xu-jiahua`
- **Type:** Peer-reviewed conference paper (top security venue).
- **Summary:** Provides a detailed anatomy of crypto pump-and-dump operations orchestrated through Telegram groups, some exceeding two million members. Documents the mechanics: organizers announce a target coin, members buy simultaneously to inflate the price, then organizers sell. Analyzes hundreds of pump events and the information dynamics within Telegram channels.
- **Relevance:** *Section 6 (Crypto Social Media — Telegram).* The primary reference for Telegram-based crypto manipulation. The detailed operational anatomy is directly useful for building detection systems.
- **How to use:** Cite to ground the Telegram discussion in documented manipulation patterns. The multi-million-member group sizes illustrate the scale of coordination possible on these platforms.
- Status: `[ ] Unverified`

---

## 7. Cross-Cutting and Historical Sources

**Antweiler, Werner, and Murray Z. Frank. "Is All That Talk Just Noise? The Information Content of Internet Stock Message Boards." *Journal of Finance* 59, no. 3 (June 2004): 1259–1294.**

- DOI: `10.1111/j.1540-6261.2004.00662.x`
- **Summary:** 1.5M messages on Yahoo Finance/Raging Bull. Messages predict volatility; disagreement predicts volume. Economically small but statistically significant effect on returns.
- **Relevance:** Historical starting point for the social media → markets literature.
- **Cross-reference:** Already cited in Chapter 1 research.
- Status: `[ ] Unverified`

---

**Bollen, Johan, Huina Mao, and Xiaojun Zeng. "Twitter Mood Predicts the Stock Market." *Journal of Computational Science* 2, no. 1 (March 2011): 1–8.**

- DOI: `10.1016/j.jocs.2010.12.007`
- **Summary:** 86.7% accuracy in predicting DJIA daily direction from Twitter mood. Specific mood dimension ("Calm") is predictive.
- **Relevance:** The canonical early Twitter-to-market paper. Include with appropriate caveats about replication concerns.
- **Cross-reference:** Already cited in Chapter 1 research.
- Status: `[ ] Unverified`

---

**Pfeffer, Jürgen, et al. "RIP Twitter API: A Eulogy to Its Vast Research Contributions." arXiv preprint, arXiv:2404.07340, April 2024.**

- URL: `https://arxiv.org/abs/2404.07340`
- **Summary:** Documents impact of Twitter/X API pricing changes on research. Studies dropped 13% after API monetization.
- **Relevance:** Essential context for the current data access landscape.
- **Cross-reference:** Already cited in Chapter 2 research.
- Status: `[ ] Unverified`

---

## Cross-Chapter References

| Source | Ch 8 Section | Also Relevant To |
|--------|-------------|------------------|
| Costola et al. (2022) | Sec 1 (GameStop) | Ch 1 (Historical Examples) |
| Bradley et al. (2024) | Sec 1 (WSB DD) | Ch 5 (Signal Construction — alpha decay) |
| Pedersen (2022) | Sec 1 (Theory) | Ch 10 (Regime Detection — bubbles) |
| Cookson et al. (2023) Echo Chambers | Sec 2 (StockTwits) | Ch 13 (Ethics — information silos) |
| Cookson et al. (2020) Partisanship | Sec 4 (Data Quality) | Ch 2 (Data Sources), Ch 13 (Ethics) |
| Chen et al. (2014) | Sec 2 (Historical) | Foundational |
| Renault (2017) | Sec 2 (Intraday) | Ch 5 (Temporal Aggregation) |
| Divernois & Filipović (2023) | Sec 2 (StockTwits Data) | Ch 2 (Data Sources) |
| Kamps & Kleinberg (2018) | Sec 5 (Pump-and-Dump) | Ch 13 (Ethics — manipulation) |
| Xu & Livshits (2019) | Sec 6 (Telegram P&D) | Ch 13 (Ethics — manipulation) |
| Cresci (2020) | Sec 4 (Bot Detection) | Ch 13 (Ethics — integrity) |
| Antweiler & Frank (2004) | Sec 7 (Historical) | Ch 1 |
| Bollen et al. (2011) | Sec 7 (Historical) | Ch 1 |
| Pfeffer et al. (2024) | Sec 7 (API Access) | Ch 2 |
| Tetlock (2007) | Sec 3 (News Baseline) | Ch 1, Ch 5 |

---

## Research Gaps

The following areas need additional sourcing:

- [ ] **Discord financial data scraping** — Need references on accessing and analyzing financial Discord communities. Discord's API is less documented for research use than Reddit or Twitter. Look for papers that scraped crypto Discord servers and address the technical and legal challenges.
- [ ] **Sentiment sampling strategies for high-noise sources** — Need a paper comparing random vs. stratified vs. targeted high-frequency sampling of social media text. In high-volume, noisy environments, sampling strategy significantly affects signal quality.
- [ ] **Short squeeze linguistic indicators** — Need a paper specifically identifying linguistic patterns (specific phrases, emoji usage, call-to-action language) that precede short squeeze events. The Bradley et al. (2024) WSB paper captures some of this but a dedicated linguistic analysis would be stronger.
- [ ] **SEC enforcement cases involving social media manipulation** — Need specific SEC enforcement actions related to social media-driven market manipulation (pump-and-dump via Twitter/Reddit/Telegram). These provide legal context for the manipulation detection discussion and connect to Chapter 13.
- [ ] **Cross-platform sentiment aggregation** — Need a study that systematically combines sentiment from multiple platforms (Twitter + Reddit + StockTwits + news) and tests whether multi-platform aggregation outperforms single-platform signals.
- [ ] **Meme stock index construction** — Need a reference for systematically defining and tracking meme stocks using social media mention frequency. Some recent working papers construct dynamic meme stock indices from WSB mention data.
- [ ] **Reddit data access post-2023** — Need updated guidance on accessing Reddit data for academic research after the 2023 API pricing changes. The free academic tier (100 req/min) may be sufficient for research but not for real-time trading systems.

---

## Verification Priority

Start SMU Library verification with these sources first:

1. **Bradley et al. (2024)** — WSB due diligence research (RFS — definitive WSB paper)
2. **Cookson et al. (2023)** — Echo chambers on StockTwits (RFS)
3. **Pedersen (2022)** — Social networks and markets theory (JFE)
4. **Costola et al. (2022)** — GameStop study (if not already verified from Ch 1)
5. **Chen et al. (2014)** — Wisdom of crowds in social media (RFS)
6. **Kamps & Kleinberg (2018)** — Crypto pump-and-dump detection
7. **Cresci (2020)** — Bot detection survey (CACM)
8. **Xu & Livshits (2019)** — Telegram pump-and-dump anatomy
9. **Kraaijeveld & De Smedt (2020)** — Crypto Twitter sentiment
10. **Divernois & Filipović (2023)** — StockTwits data quality

---

*Research compiled April 2026. All citations require manual verification through SMU Library before inclusion in final manuscript.*
