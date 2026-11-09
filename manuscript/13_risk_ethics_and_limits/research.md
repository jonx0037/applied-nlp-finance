# Chapter 13 — Risk, Ethics, and the Limits of Financial NLP — Annotated Bibliography

**Purpose:** This chapter provides an honest, intellectually serious treatment of what NLP cannot do and what it shouldn't do in financial markets. It covers model fragility at tail events, the narrative fallacy, market manipulation via language, the regulatory landscape, systemic risk from correlated NLP strategies, alternative data ethics, and a practitioner's candid assessment of the field's current state.

**What this chapter needs from its sources:**
- Model fragility and distribution shift during crises
- The narrative fallacy and cognitive biases in pattern-finding
- Market manipulation via language (pump-and-dump, coordinated campaigns)
- Regulatory landscape (SEC, FINRA, MiCA) for AI-driven trading
- Systemic risk from correlated/crowded NLP strategies
- Reflexivity in NLP-driven markets
- Alternative data ethics, privacy, and insider information boundaries
- Adversarial attacks on financial NLP systems

**Citation format:** Chicago (Notes and Bibliography), 17th edition.

**Note on chapter tone:** This is the book's most humanistic chapter alongside Chapter 1. Where Chapter 1 makes the *positive* case for financial NLP from a narrative perspective, Chapter 13 makes the *cautionary* case from the same tradition. The sources span behavioral economics, philosophy of finance, regulatory law, and adversarial ML — reflecting the breadth of concerns a responsible practitioner must consider.

---

## 1. Model Fragility at Tail Events

### 1.1 Foundational: Black Swans and Model Failure

**Taleb, Nassim Nicholas. *The Black Swan: The Impact of the Highly Improbable*. New York: Random House, 2007.**

- ISBN: `978-1-4000-6351-2`
- **Type:** Book.
- **Summary:** Introduces the "Black Swan" concept: rare, unpredictable events with extreme impact that humans retrospectively rationalize into coherent narratives. Argues that standard statistical models systematically underestimate tail risk because they are calibrated on normal-regime data. The "narrative fallacy" describes our tendency to construct post-hoc stories explaining unpredictable events, creating an illusion of understanding.
- **Relevance:** *Section 1 (Model Fragility) and Section 2 (Narrative Fallacy).* The central philosophical reference for the chapter. NLP models trained on normal-market language face two Talebian problems: (1) they fail to interpret crisis language correctly (distribution shift), and (2) they inherit human narrative biases from their training data (narrative fallacy). A model that finds "coherent sentiment patterns" may be fitting noise, not signal.
- **How to use:** Frame Sections 1 and 2 around Taleb's framework. Model fragility at tail events is a specific instance of Black Swan risk: NLP models are calibrated on normal-regime text and fail when crisis language diverges from training distributions. The narrative fallacy section should cite Taleb's concept directly.
- Status: `[ ] Unverified`

---

### 1.2 Foundational: COVID as Distribution Shift Case Study

**Baker, Scott R., Nicholas Bloom, Steven J. Davis, Kyle Kost, Marco Sammon, and Tasaneeya Viratyosin. "The Unprecedented Stock Market Reaction to COVID-19." *Review of Asset Pricing Studies* 10, no. 4 (December 2020): 742–758.**

- DOI: `10.1093/rapstu/raaa008`
- **Type:** Peer-reviewed journal article.
- **Summary:** Documents that no previous infectious disease outbreak affected the stock market as forcefully as COVID-19. Government restrictions and voluntary social distancing — not the disease itself — drove the crash. Text analysis decomposes the causal mechanism.
- **Relevance:** *Section 1 (Model Fragility).* COVID is the chapter's primary case study for model fragility. Sentiment models trained pre-2020 had never seen pandemic-specific language ("lockdown," "social distancing," "flattening the curve"), causing systematic misinterpretation during the period when accurate analysis mattered most.
- **Cross-reference:** Already cited in Chapter 10 research.
- Status: `[ ] Unverified`

---

## 2. The Narrative Fallacy

### 2.1 Foundational: Cognitive Biases and Decision-Making

**Kahneman, Daniel. *Thinking, Fast and Slow*. New York: Farrar, Straus and Giroux, 2011.**

- ISBN: `978-0-374-27563-1`
- **Type:** Book.
- **Summary:** Presents the System 1/System 2 framework for human cognition. System 1 is fast, automatic, and pattern-seeking; System 2 is slow, deliberative, and logical. Cognitive biases arise because System 1's heuristics — including narrative construction, anchoring, and availability — don't always lead to correct conclusions. Decades of research showing systematic errors in human judgment.
- **Relevance:** *Section 2 (Narrative Fallacy).* NLP models trained on human-generated text inherit System 1 biases. When a model identifies "coherent sentiment patterns" in financial text, it may be detecting the narrative structures humans impose on random events, not genuine predictive signal. The model's training data is *itself* the product of biased human cognition.
- **How to use:** Cite alongside Taleb (2007) for the cognitive foundation. Kahneman explains *why* humans create false narratives (System 1 pattern-matching); Taleb explains *why this fails* in finance (tail events violate pattern assumptions). Together they frame the epistemological challenge NLP faces.
- Status: `[ ] Unverified`

---

### 2.2 Foundational: Narrative Economics as Both Opportunity and Risk

**Shiller, Robert J. "Narrative Economics." *American Economic Review* 107, no. 4 (April 2017): 967–1004.**

- DOI: `10.1257/aer.107.4.967`
- **Summary:** Narratives go viral and drive economic behavior. Economic narratives are "contagious stories that have the potential to change how people make economic decisions."
- **Relevance:** *Section 2 (Narrative Fallacy).* Shiller's narrative economics framework — used in Chapter 1 to justify financial NLP — has a dark side explored here. If narratives drive markets, then NLP models that detect and trade on narratives may *amplify* narrative contagion rather than exploit it. The same mechanism that makes text informative also makes it dangerous: narratives can be false, manipulated, or self-reinforcing.
- **How to use:** Revisit Chapter 1's Shiller citation from the opposite perspective. Chapter 1 argued "narratives move markets, so NLP can extract signal." Chapter 13 argues "narratives move markets, so NLP can amplify manipulation and create feedback loops." Same framework, opposite implication.
- **Cross-reference:** Already cited in Chapter 1 research.
- Status: `[ ] Unverified`

---

## 3. Market Manipulation via Language

### 3.1 Empirical: Crypto Pump-and-Dump

**Kamps, Josh, and Bennett Kleinberg. "To the Moon: Defining and Detecting Cryptocurrency Pump-and-Dumps." *Crime Science* 7, article 18 (December 2018).**

- DOI: `10.1186/s40163-018-0093-5`
- **Summary:** Defines and detects crypto pump-and-dump schemes using anomaly detection on trading data. Fraudulent activity clusters on specific exchanges and coins.
- **Relevance:** *Section 3 (Manipulation).* The primary reference for language-based market manipulation detection.
- **Cross-reference:** Already cited in Chapter 8 research.
- Status: `[ ] Unverified`

---

**Xu, Jiahua, and Benjamin Livshits. "The Anatomy of a Cryptocurrency Pump-and-Dump Scheme." In *Proceedings of the 28th USENIX Security Symposium*, 1609–1625. Santa Clara, CA: USENIX, August 2019.**

- URL: `https://www.usenix.org/conference/usenixsecurity19/presentation/xu-jiahua`
- **Summary:** Detailed anatomy of Telegram-based pump-and-dump operations. Groups exceeding two million members coordinate to inflate and dump coins.
- **Relevance:** *Section 3.* Documents the scale and mechanics of coordinated language-based manipulation.
- **Cross-reference:** Already cited in Chapter 8 research.
- Status: `[ ] Unverified`

---

## 4. Regulatory Landscape

### 4.1 Reference: SEC and FINRA Guidance on AI

**U.S. Securities and Exchange Commission. "2025 Examination Priorities." Division of Examinations, October 2024.**

- URL: `https://www.sec.gov/about/reports-publications/2025-examination-priorities`
- **Type:** Regulatory guidance document.
- **Summary:** Lists AI as a top examination priority for 2025. Focus areas include: accuracy of AI capability claims (combating "AI-washing"), policies for monitoring and supervising AI use, regulatory technology for automated processes, and broker-dealer conflicts from predictive data analytics and ML. The SEC has been weighing rules related to broker/dealer and RIA conflicts involving AI/ML.
- **Relevance:** *Section 4 (Regulatory Landscape — SEC).* The most current SEC guidance on AI in financial markets. Readers building NLP-based trading systems must understand these examination priorities, particularly the AI-washing concern (making unsubstantiated claims about AI capabilities in marketing).
- **How to use:** Cite as the current SEC stance. Emphasize that the SEC's concern is not with AI use per se, but with (1) misleading claims about AI capabilities, (2) inadequate supervision of AI systems, and (3) conflicts of interest from predictive analytics.
- Status: `[ ] Unverified`

---

**Financial Industry Regulatory Authority (FINRA). "Algorithmic Trading." FINRA Key Topics, accessed April 2026.**

- URL: `https://www.finra.org/rules-guidance/key-topics/algorithmic-trading`
- **Type:** Regulatory guidance.
- **Summary:** FINRA Rule 3110 requires member firms to establish policies and procedures for technology governance, including AI usage. FINRA has issued regulatory notices reminding firms of obligations concerning AI, particularly around supervisory controls and risk management.
- **Relevance:** *Section 4 (Regulatory Landscape — FINRA).* FINRA's technology governance requirements apply directly to NLP-based trading systems. Firms deploying sentiment-driven strategies need supervisory controls documented under Rule 3110.
- Status: `[ ] Unverified`

---

### 4.2 Reference: EU MiCA and Digital Finance

**European Parliament and Council. "Regulation (EU) 2023/1114 on Markets in Crypto-Assets (MiCA)." *Official Journal of the European Union* L 150 (June 9, 2023).**

- URL: `https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R1114`
- **Type:** Legislation.
- **Summary:** Establishes uniform EU rules for crypto-assets, including authorization and supervision requirements for issuers and service providers. Prohibits insider trading, market manipulation, and other abusive practices. Bans algorithmic stablecoins. Fully applicable since December 2024.
- **Relevance:** *Section 4 (Regulatory Landscape — EU).* MiCA's market manipulation prohibitions apply to NLP-based crypto trading strategies. The prohibition on algorithmic stablecoins reflects regulatory concern about automated financial systems. While focused on crypto, MiCA signals the regulatory direction for AI-driven trading more broadly.
- **How to use:** Cite as the primary EU reference. The market manipulation and insider trading prohibitions are the most relevant provisions for NLP practitioners.
- Status: `[ ] Unverified`

---

## 5. Systemic Risk from Correlated NLP Strategies

### 5.1 Foundational: Liquidity Spirals and Crowded Trades

**Brunnermeier, Markus K., and Lasse Heje Pedersen. "Market Liquidity and Funding Liquidity." *Review of Financial Studies* 22, no. 6 (June 2009): 2201–2238.**

- DOI: `10.1093/rfs/hhn098`
- **Type:** Peer-reviewed journal article (top-3 finance journal).
- **Summary:** Models the mutually reinforcing relationship between market liquidity and funding liquidity. Traders provide market liquidity, but their ability to do so depends on funding. Under certain conditions, margins are destabilizing: market liquidity and funding liquidity become mutually reinforcing, creating "liquidity spirals." Explains why liquidity can suddenly dry up, exhibits commonality across securities, and co-moves with the market — especially during downturns.
- **Relevance:** *Section 5 (Systemic Risk).* The theoretical foundation for understanding what happens when many NLP-driven strategies crowd into the same positions. If many funds use FinBERT to trade earnings call sentiment, they will simultaneously buy/sell the same stocks, creating exactly the liquidity spiral Brunnermeier-Pedersen describe. The resulting crowding is invisible to individual backtests but catastrophic in aggregate.
- **How to use:** Central to Section 5. Present the liquidity spiral as the mechanism by which NLP strategy crowding creates systemic fragility. The key insight: when everyone uses the same sentiment model, the model's success becomes its own risk factor.
- Status: `[ ] Unverified`

---

### 5.2 Foundational: Crowded Trades and Externalities

**Stein, Jeremy C. "Presidential Address: Sophisticated Investors and Market Efficiency." *Journal of Finance* 64, no. 4 (August 2009): 1517–1548.**

- DOI: `10.1111/j.1540-6261.2009.01472.x`
- **Type:** Peer-reviewed journal article (AFA Presidential Address).
- **Summary:** Argues that complications arise when arbitrageurs inflict negative externalities on each other in the process of pursuing the same trading strategy. No individual trader knows how much capital has been deployed by others using the same model. This information asymmetry about crowding creates coordination problems and potential for cascading unwinding.
- **Relevance:** *Section 5 (Systemic Risk).* Stein formalizes the crowding externality: each NLP strategy user makes the strategy worse for every other user, but no individual user can observe the aggregate crowding level. This is directly applicable to NLP strategies: if you can't know how many other funds are trading on FinBERT earnings sentiment, you can't assess the systemic risk of your own position.
- **How to use:** Cite alongside Brunnermeier-Pedersen (2009). Stein provides the game-theoretic framing (negative externalities, coordination failure); Brunnermeier-Pedersen provides the mechanism (liquidity spirals). Together they explain why homogeneous NLP strategies create fragility.
- Status: `[ ] Unverified`

---

## 6. Ethics of Alternative Data

### 6.1 Contextual: Privacy and Financial Data

**Bank for International Settlements. "Regulating AI in the Financial Sector: Recent Developments and Main Challenges." FSI Insights no. 63. Basel: BIS, December 2024.**

- URL: `https://www.bis.org/fsi/publ/insights63.pdf`
- **Type:** Central bank policy report.
- **Summary:** Surveys recent regulatory developments for AI in financial services globally. Documents the tension between AI innovation and privacy/fairness concerns. Notes that some banks have been cautious in adopting AI due to uncertainties about regulatory expectations on accountability, ethics, data privacy, fairness, transparency, and explainability.
- **Relevance:** *Section 6 (Ethics of Alternative Data).* Provides the global regulatory perspective on AI ethics in finance. The documented tension between innovation and privacy/fairness captures the central dilemma readers face: aggressive alternative data collection yields alpha but creates regulatory and ethical risk.
- **How to use:** Cite as the international perspective complementing the US (SEC/FINRA) and EU (MiCA) references.
- Status: `[ ] Unverified`

---

## 7. Reflexivity in NLP-Driven Markets

### 7.1 Foundational: Reflexivity Theory

**Soros, George. *The Alchemy of Finance: Reading the Mind of the Market*. New York: Simon & Schuster, 1987.**

- ISBN: `978-0-471-04206-4`
- **Type:** Book.
- **Summary:** Introduces the theory of reflexivity: a bidirectional feedback loop where market participants' beliefs about the future influence the present (through trading), which in turn alters the future they were trying to predict. Positive feedback loops can create self-reinforcing boom-bust cycles. Soros argues that markets are not merely passive reflectors of fundamentals — they actively shape them.
- **Relevance:** *Section 7 (Reflexivity) and Section 5 (Systemic Risk).* Reflexivity is the deepest theoretical concern for NLP-driven trading. If NLP models detect "hawkish Fed sentiment" and traders sell bonds, the resulting yield spike changes the economic outlook the Fed was commenting on, potentially causing the Fed to adjust communication — which the NLP model then processes again. The model is not observing a fixed system; it is participating in the system it tries to predict.
- **How to use:** Present reflexivity as the philosophical challenge for financial NLP. The book's core thesis — "text captures why markets move" — assumes text is a *signal* about an external reality. Soros argues that text is also a *cause* of that reality. When NLP becomes widespread, the system becomes reflexive: models trade on text, trades change prices, changed prices change the narratives, changed narratives change the models' inputs.
- Status: `[ ] Unverified`

---

## 8. Adversarial Attacks on Financial NLP

### 8.1 Contextual: Adversarial ML and Data Poisoning

**National Institute of Standards and Technology. "Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations." NIST AI 100-2e2025. Gaithersburg, MD: NIST, 2025.**

- URL: `https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2025.pdf`
- **Type:** Government standards document.
- **Summary:** Comprehensive taxonomy of adversarial ML attacks including: training-phase attacks (data poisoning, backdoor insertion), inference-phase attacks (prompt injection, evasion), and availability/integrity attacks. Provides standardized terminology and mitigation frameworks. The 2025 edition includes LLM-specific attack vectors.
- **Relevance:** *Section 8 (Adversarial Attacks).* The authoritative reference for adversarial ML taxonomy. Financial NLP systems face unique adversarial threats: (1) data poisoning — injecting manipulative social media posts into sentiment training data, (2) prompt injection — manipulating LLM-based analysis systems, (3) evasion — crafting language that fools sentiment classifiers while containing manipulative intent.
- **How to use:** Cite as the standardized framework for adversarial attacks. Map NIST's general taxonomy to financial NLP-specific threats. The data poisoning vector is particularly concerning: if an adversary can influence the social media text that feeds a sentiment model, they can manipulate the model's outputs without ever touching the model itself.
- Status: `[ ] Unverified`

---

## 9. A Practitioner's Honest Assessment

### 9.1 Empirical: Post-Publication Alpha Decay

**McLean, R. David, and Jeffrey Pontiff. "Does Academic Research Destroy Stock Return Predictability?" *Journal of Finance* 71, no. 1 (February 2016): 5–32.**

- DOI: `10.1111/jofi.12365`
- **Summary:** Portfolio returns are 26% lower out-of-sample and 58% lower post-publication. Academic dissemination degrades alpha.
- **Relevance:** *Section 9 (Honest Assessment).* The NLP strategies this book teaches will face the same post-publication decay. An honest assessment must acknowledge that documenting alpha strategies accelerates their decay.
- **Cross-reference:** Already cited in Chapter 11 research.
- Status: `[ ] Unverified`

---

### 9.2 Empirical: What Financial NLP Actually Delivers

**Li, Qing, Chao Wang, and Jiawei Han. "Natural Language Processing in Finance: A Survey." *Information Fusion* 114 (February 2025): 102755.**

- DOI: `10.1016/j.inffus.2024.102755`
- **Summary:** Comprehensive survey of ten major financial NLP applications. Covers both capabilities and limitations of current approaches.
- **Relevance:** *Section 9.* The most current panoramic assessment of what financial NLP can and cannot do. Provides the factual basis for the "honest assessment" section.
- **Cross-reference:** Already cited in Chapters 1–4 research.
- Status: `[ ] Unverified`

---

## Cross-Chapter References

| Source | Ch 13 Section | Also Relevant To |
|--------|-------------|------------------|
| Taleb (2007) | Sec 1, 2 (Fragility, Narrative Fallacy) | Foundational |
| Kahneman (2011) | Sec 2 (Cognitive Biases) | Ch 1 (Framing Effects) |
| Shiller (2017) | Sec 2 (Narrative Risk) | Ch 1 (Narrative Economics — positive case) |
| Brunnermeier & Pedersen (2009) | Sec 5 (Liquidity Spirals) | Ch 10 (Regime Detection — crises) |
| Stein (2009) | Sec 5 (Crowding Externalities) | Ch 11 (Evaluation — systemic risk) |
| Soros (1987) | Sec 7 (Reflexivity) | Ch 1 (Philosophical Foundation) |
| Kamps & Kleinberg (2018) | Sec 3 (P&D Detection) | Ch 8 (Social Media) |
| Xu & Livshits (2019) | Sec 3 (Telegram P&D) | Ch 8 (Crypto) |
| Baker et al. (2020) | Sec 1 (COVID Case Study) | Ch 10 (Case Studies) |
| McLean & Pontiff (2016) | Sec 9 (Alpha Decay) | Ch 11 (Evaluation) |
| Li et al. (2025) | Sec 9 (Current State) | All chapters |
| NIST (2025) | Sec 8 (Adversarial ML) | Ch 12 (Security) |
| SEC (2024) | Sec 4 (Regulation) | Ch 12 (Deployment — compliance) |
| BIS (2024) | Sec 6 (Ethics) | Ch 7 (Central Bank), Ch 12 (Deployment) |
| MiCA (2023) | Sec 4 (EU Regulation) | Ch 8 (Crypto) |

---

## Research Gaps

The following areas need additional sourcing:

- [ ] **NLP model performance degradation during 2008 financial crisis** — Need a study specifically documenting how text/sentiment models trained pre-2008 performed during the crisis. COVID (Baker et al. 2020) is the primary crisis case study, but a 2008 example would strengthen the argument with a longer historical perspective.
- [ ] **Distribution shift in financial language: crisis vs. normal** — Need a paper that quantitatively measures how financial language distributions change during crises (vocabulary shifts, sentiment calibration changes, emergence of novel terminology). This would provide the empirical evidence behind the "model fragility" argument.
- [ ] **SEC enforcement cases involving social media manipulation** — Need specific SEC enforcement actions (not just guidance) related to social media-driven market manipulation. The SEC has brought cases against individuals for pump-and-dump schemes using social media — documenting specific cases would ground Section 3.
- [ ] **FINRA Rule 3110 implementation for AI/ML trading systems** — Need specific guidance or interpretive letters on how Rule 3110's supervisory requirements apply to NLP-based trading systems. The gap between the general rule and specific AI/ML application is where compliance uncertainty lies.
- [ ] **Adversarial attacks on financial sentiment models specifically** — Need a paper demonstrating adversarial attacks on FinBERT or similar financial NLP models. Can an adversary craft social media posts that fool sentiment classifiers while being detectable by humans? This would make the adversarial threat concrete.
- [ ] **Insider trading boundaries for alternative text data** — Need legal analysis addressing where alternative data collection (social media scraping, satellite imagery, web traffic data) crosses the line into material non-public information. The Raj Rajaratnam case and subsequent SEC guidance may provide precedent.
- [ ] **De Bondt and Thaler (1985) on overreaction** — The notes mention this as a potential behavioral finance source. Their paper on overreaction in stock markets would complement Kahneman's cognitive bias framework.
- [ ] **Barberis and Thaler (2003) "A Survey of Behavioral Finance"** — A comprehensive behavioral finance survey would strengthen the narrative fallacy section with broader academic grounding.

---

## Verification Priority

Start SMU Library verification with these sources first:

1. **Brunnermeier & Pedersen (2009)** — Liquidity spirals (RFS — central to systemic risk argument)
2. **Stein (2009)** — Crowding externalities (JF Presidential Address)
3. **Taleb (2007)** — Black Swan (book — verify edition and ISBN)
4. **Kahneman (2011)** — Thinking, Fast and Slow (book — verify edition)
5. **Soros (1987)** — Alchemy of Finance (book — verify edition and ISBN)
6. **Baker et al. (2020)** — COVID market crash (if not already verified from Ch 10)
7. **NIST (2025)** — Adversarial ML taxonomy (government document)
8. **SEC (2024)** — 2025 examination priorities (regulatory document)
9. **MiCA (2023)** — EU regulation text
10. **McLean & Pontiff (2016)** — Alpha decay (if not already verified from Ch 11)

---

*Research compiled April 2026. All citations require manual verification through SMU Library before inclusion in final manuscript.*
