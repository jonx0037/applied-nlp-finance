# Chapter 3 — NLP Foundations for Finance — Annotated Bibliography

**Purpose:** This chapter establishes the NLP baseline so readers understand what transformers improved upon. It covers tokenization, bag-of-words, TF-IDF, word embeddings (Word2Vec, GloVe, fastText), classical sentiment approaches (VADER, lexicon-based), and financial benchmarks. It makes the pragmatic case for when classical methods remain the right choice.

**What this chapter needs from its sources:**
- Original papers for each foundational NLP method (Word2Vec, GloVe, fastText, TF-IDF, VADER)
- The Loughran-McDonald lineage and its correction of Harvard GI for finance
- Financial NLP benchmark datasets (FiQA, SEntFiN, Financial PhraseBank)
- Head-to-head comparisons of classical vs. transformer methods on financial text
- Domain-specific embedding studies showing where general models fail
- Tokenization references, especially subword methods and financial edge cases

**Citation format:** Chicago (Notes and Bibliography), 17th edition.

---

## 1. Tokenization for Financial Text

These sources establish the technical foundation for tokenization and address financial-domain challenges.

### 1.1 Foundational: NLP Textbooks

**Jurafsky, Daniel, and James H. Martin. *Speech and Language Processing*. 3rd ed. (draft). Stanford, CA, 2025.**

- URL: `https://web.stanford.edu/~jurafsky/slp3/`
- **Type:** Textbook (online draft, continuously updated).
- **Summary:** The standard NLP textbook. Chapter 2 covers regular expressions, text normalization, and tokenization. Discusses whitespace tokenization, word boundary ambiguities ("New York," "rock 'n' roll," "I'm"), and normalization decisions. Updated through January 2026.
- **Relevance:** *Section 1 (Tokenization).* The authoritative reference for tokenization fundamentals. Provides the general framework before introducing financial-specific challenges (ticker symbols, numerical expressions, abbreviations).
- **How to use:** Cite as the general NLP reference, then immediately pivot to financial edge cases that standard tokenizers mishandle.
- Status: `[ ] Unverified`

---

**Manning, Christopher D., Prabhakar Raghavan, and Hinrich Schütze. *Introduction to Information Retrieval*. Cambridge: Cambridge University Press, 2008.**

- ISBN: `978-0-521-86571-5`
- URL: `https://nlp.stanford.edu/IR-book/`
- **Type:** Textbook.
- **Summary:** The standard information retrieval textbook. Chapters 6–7 introduce document scoring, term weighting, and the TF-IDF scheme, followed by the vector space model. Also covers tokenization, stemming, and the bag-of-words model.
- **Relevance:** *Section 1 (Tokenization) and Section 2 (Bag-of-Words, TF-IDF).* The canonical reference for TF-IDF and vector space models. These are the document representations readers will use as baselines.
- **How to use:** Cite for TF-IDF and bag-of-words formal definitions. The textbook's treatment is rigorous and widely recognized.
- Status: `[ ] Unverified`

---

### 1.2 Methodological: Subword Tokenization

**Sennrich, Rico, Barry Haddow, and Alexandra Birch. "Neural Machine Translation of Rare Words with Subword Units." In *Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, 1715–1725. Berlin: Association for Computational Linguistics, August 2016.**

- DOI: `10.18653/v1/P16-1162`
- **Type:** Peer-reviewed conference paper.
- **Summary:** Introduces Byte-Pair Encoding (BPE) for neural machine translation, enabling open-vocabulary handling by encoding rare/unknown words as sequences of subword units. BPE has since become the dominant subword tokenization method used by BERT, GPT, and virtually all modern language models.
- **Relevance:** *Section 1 (Tokenization).* BPE is how transformer tokenizers handle financial neologisms, compound terms, and out-of-vocabulary words. Understanding BPE explains why FinBERT tokenizes "EBITDA" differently from a general BERT model — and why this matters for downstream performance.
- **How to use:** Cite as the origin of the subword tokenization approach that readers will encounter in Chapter 4's transformer models. Bridges classical tokenization (this chapter) to modern approaches (next chapter).
- **Cross-reference:** Also relevant to Chapter 4 (Transformers and Financial Language Models).
- Status: `[ ] Unverified`

---

## 2. Bag-of-Words, TF-IDF, and Financial Lexicons

### 2.1 Foundational: TF-IDF

**Salton, Gerard, and Christopher Buckley. "Term-Weighting Approaches in Automatic Text Retrieval." *Information Processing & Management* 24, no. 5 (1988): 513–523.**

- DOI: `10.1016/0306-4573(88)90021-0`
- **Type:** Peer-reviewed journal article.
- **Summary:** Presents 20 years of experimental evidence showing that text indexing systems based on appropriately weighted single terms produce superior retrieval results to more elaborate text representations. Summarizes insights gained in automatic term weighting and provides baseline single-term-indexing models.
- **Relevance:** *Section 2 (TF-IDF).* The foundational reference for term weighting, including the TF-IDF formulation. Essential for historical context — this is where the field started.
- **How to use:** Cite as the origin of TF-IDF. The paper's argument that "simple term weighting outperforms elaborate representations" foreshadows the chapter's conclusion about when classical methods still win.
- Status: `[ ] Unverified`

---

### 2.2 Foundational: Financial Sentiment Lexicons

**Loughran, Tim, and Bill McDonald. "When Is a Liability Not a Liability? Textual Analysis, Dictionaries, and 10-Ks." *Journal of Finance* 66, no. 1 (February 2011): 35–65.**

- DOI: `10.1111/j.1540-6261.2010.01625.x`
- **Type:** Peer-reviewed journal article.
- **Summary:** Shows that nearly three-fourths of "negative" words in the Harvard General Inquirer are misclassified in financial contexts. Develops six financial sentiment word lists (negative, positive, litigious, uncertainty, constraining, superfluous) with 2,337 domain-specific negative words. Linked to 10-K filing returns, trading volume, volatility, fraud, material weakness, and unexpected earnings.
- **Relevance:** *Section 2 (Financial Lexicons).* The single most important source for this section. The L-M dictionary is the *de facto* standard for dictionary-based financial sentiment analysis. The three-fourths misclassification statistic is the chapter's most vivid example of why domain-specific NLP matters.
- **How to use:** Central to Section 2. Walk through specific examples of misclassified words (liability, tax, cost, capital) to make the domain-adaptation argument concrete and memorable.
- **Cross-reference:** Already cited in Chapter 1 research.
- Status: `[ ] Unverified`

---

**Stone, Philip J., Dexter C. Dunphy, Marshall S. Smith, and Daniel M. Ogilvie. *The General Inquirer: A Computer Approach to Content Analysis*. Cambridge, MA: MIT Press, 1966.**

- ISBN: `978-0-262-69011-9`
- **Type:** Book.
- **Summary:** Introduces the Harvard General Inquirer, a computer system for content analysis that attaches syntactic, semantic, and pragmatic information to words. The Harvard IV-4 dictionary — the most widely used component — categorizes words into positive and negative sentiment categories among 182 total categories.
- **Relevance:** *Section 2 (Financial Lexicons — Harvard GI).* The historical baseline that Loughran-McDonald corrected. Readers need to understand what the GI is to appreciate why its financial misclassifications matter.
- **How to use:** Cite alongside Loughran-McDonald (2011) as the "before" picture. The GI was developed for general social science content analysis — its failure on financial text illustrates domain specificity.
- Status: `[ ] Unverified`

---

**Loughran, Tim, and Bill McDonald. "Textual Analysis in Accounting and Finance: A Survey." *Journal of Accounting Research* 54, no. 4 (September 2016): 1187–1230.**

- DOI: `10.1111/1475-679X.12123`
- **Type:** Peer-reviewed survey article.
- **Summary:** Comprehensive survey covering bag-of-words, readability, word lists, Zipf's law, cosine similarity, and Naive Bayes in financial text analysis. Documents implementation challenges and nuances specific to financial applications.
- **Relevance:** *Sections 2–5 (entire chapter).* The definitive survey of classical financial NLP methods. Covers virtually every technique this chapter introduces.
- **How to use:** Cite as the field's comprehensive self-assessment. Particularly useful for the "implementation challenges" discussion — real-world issues like document length normalization and section-specific analysis.
- **Cross-reference:** Already cited in Chapters 1 and 2 research.
- Status: `[ ] Unverified`

---

### 2.3 Methodological: Data-Driven Word Weighting

**Jegadeesh, Narasimhan, and Di Wu. "Word Power: A New Approach for Content Analysis." *Journal of Financial Economics* 110, no. 3 (December 2013): 712–729.**

- DOI: `10.1016/j.jfineco.2013.08.012`
- **Type:** Peer-reviewed journal article.
- **Summary:** Develops a data-driven approach to weighting words based on stock market reaction, rather than using pre-defined dictionaries. Finds that term weighting choice is at least as important as word list accuracy. The approach also successfully quantifies IPO prospectus tone.
- **Relevance:** *Section 2 (TF-IDF and Beyond).* Demonstrates the evolution from manually curated dictionaries (Harvard GI, L-M) to data-driven approaches. Bridges the gap between classical lexicon methods and the supervised learning approaches in later sections.
- **How to use:** Cite as the pivotal paper showing that *how* you weight words matters as much as *which* words you track. This insight foreshadows the embedding approaches in Section 3.
- **Cross-reference:** Already cited in Chapter 1 research.
- Status: `[ ] Unverified`

---

## 3. Word Embeddings in Financial Context

### 3.1 Foundational: Word2Vec

**Mikolov, Tomas, Kai Chen, Greg Corrado, and Jeffrey Dean. "Efficient Estimation of Word Representations in Vector Space." arXiv preprint, arXiv:1301.3781, January 2013.**

- URL: `https://arxiv.org/abs/1301.3781`
- **Type:** Preprint (highly cited, foundational).
- **Summary:** Proposes two architectures (CBOW and Skip-gram) for computing continuous vector representations of words from very large datasets. Demonstrates that the resulting vectors capture syntactic and semantic word relationships (e.g., "king" - "man" + "woman" ≈ "queen"). Trained high-quality vectors from 1.6 billion words in less than a day.
- **Relevance:** *Section 3 (Word2Vec).* The paper that launched modern word embeddings. Essential foundational reference.
- **How to use:** Cite as the origin of Word2Vec. The word analogy examples are useful pedagogically but note that financial analogies (e.g., "bull" - "market" + "investor" ≈ ?) often fail with general-purpose vectors.
- Status: `[ ] Unverified`

---

**Mikolov, Tomas, Ilya Sutskever, Kai Chen, Greg S. Corrado, and Jeff Dean. "Distributed Representations of Words and Phrases and Their Compositionality." In *Advances in Neural Information Processing Systems 26 (NIPS 2013)*, 3111–3119. Lake Tahoe, NV, 2013.**

- URL: `https://arxiv.org/abs/1310.4546`
- **Type:** Peer-reviewed conference paper (NeurIPS). Over 30,000 citations.
- **Summary:** Extends the original Word2Vec with negative sampling (a simplified alternative to hierarchical softmax), subsampling of frequent words for speedup, and a method for learning phrase representations. These improvements made Word2Vec practical at scale.
- **Relevance:** *Section 3 (Word2Vec).* The companion paper that made Word2Vec practically usable. Negative sampling is the training approach readers will encounter in implementations.
- **How to use:** Cite alongside the original Word2Vec paper for completeness. The phrase-learning capability (identifying "New York" as a single unit) is directly relevant to financial entity recognition.
- Status: `[ ] Unverified`

---

### 3.2 Foundational: GloVe

**Pennington, Jeffrey, Richard Socher, and Christopher Manning. "GloVe: Global Vectors for Word Representation." In *Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, 1532–1543. Doha, Qatar: Association for Computational Linguistics, October 2014.**

- DOI: `10.3115/v1/D14-1162`
- **Type:** Peer-reviewed conference paper.
- **Summary:** Proposes GloVe, a global log-bilinear regression model that combines advantages of global matrix factorization (like LSA) and local context window methods (like Word2Vec). Trains on the nonzero elements of word-word co-occurrence matrices. Pre-trained vectors available on Wikipedia + Gigaword (6B tokens) and Common Crawl (840B tokens).
- **Relevance:** *Section 3 (GloVe).* The primary alternative to Word2Vec. Pre-trained GloVe vectors are commonly used as baselines in financial NLP papers (including Loukas et al. 2021 EDGAR-CORPUS, which showed domain-specific embeddings outperform GloVe on financial tasks).
- **How to use:** Cite as the GloVe reference. Emphasize that pre-trained GloVe captures general semantics but not domain-specific financial meanings — this motivates domain-adapted embeddings.
- Status: `[ ] Unverified`

---

### 3.3 Foundational: fastText

**Bojanowski, Piotr, Edouard Grave, Armand Joulin, and Tomas Mikolov. "Enriching Word Vectors with Subword Information." *Transactions of the Association for Computational Linguistics* 5 (June 2017): 135–146.**

- DOI: `10.1162/tacl_a_00051`
- **Type:** Peer-reviewed journal article.
- **Summary:** Represents each word as a bag of character n-grams, with word vectors as the sum of n-gram representations. This enables generating embeddings for out-of-vocabulary words — a critical advantage for financial text with frequent neologisms, ticker symbols, and compound terms.
- **Relevance:** *Section 3 (fastText).* The subword approach is particularly valuable for financial text. Terms like "EBITDA," "FinTech," "DeFi," and novel compound terms can be handled without retraining — unlike Word2Vec and GloVe, which produce zero vectors for OOV words.
- **How to use:** Emphasize the OOV advantage for financial NLP. Financial language evolves rapidly (new tickers, new acronyms, new products), and fastText's subword approach handles this evolution gracefully.
- Status: `[ ] Unverified`

---

### 3.4 Empirical: Domain-Specific Financial Embeddings

**Loukas, Lefteris, Manos Fergadiotis, Ion Androutsopoulos, and Prodromos Malakasiotis. "EDGAR-CORPUS: Billions of Tokens Make the World Go Round." In *Proceedings of the Third Workshop on Economics and Natural Language Processing*, 13–18. Punta Cana, Dominican Republic: Association for Computational Linguistics, November 2021.**

- DOI: `10.18653/v1/2021.econlp-1.2`
- **Type:** Peer-reviewed workshop paper.
- **Summary:** Trains EDGAR-W2V word embeddings on the EDGAR-CORPUS (25+ years of 10-K filings). Demonstrates superiority over generic GloVe embeddings on financial NLP tasks.
- **Relevance:** *Section 3 (Financial Embeddings).* The key empirical evidence that domain-specific embeddings outperform general-purpose ones on financial tasks. The comparison against GloVe provides a concrete benchmark.
- **How to use:** Cite as evidence for the domain-adaptation argument. The EDGAR-W2V vs. GloVe comparison is the empirical proof that financial text needs domain-specific representations.
- **Cross-reference:** Already cited in Chapter 2 research (EDGAR data source).
- Status: `[ ] Unverified`

---

## 4. Classical Sentiment Approaches

### 4.1 Foundational: VADER

**Hutto, C. J., and Eric Gilbert. "VADER: A Parsimonious Rule-Based Model for Sentiment Analysis of Social Media Text." In *Proceedings of the Eighth International AAAI Conference on Weblogs and Social Media (ICWSM-14)*. Ann Arbor, MI: AAAI, June 2014.**

- URL: `https://ojs.aaai.org/index.php/ICWSM/article/view/14550`
- **Type:** Peer-reviewed conference paper.
- **Summary:** Introduces VADER (Valence Aware Dictionary and sEntiment Reasoner), a rule-based sentiment tool attuned to social media. Achieves correlation (r = 0.881) comparable to individual human raters (r = 0.888), and F1 = 0.96 on tweet classification (vs. human F1 = 0.84). Combines a gold-standard lexicon with five grammatical/syntactical rules for sentiment intensity (capitalization, degree modifiers, conjunctions, punctuation, negation).
- **Relevance:** *Section 4 (Classical Sentiment).* VADER is the most commonly used rule-based baseline in financial NLP papers. Its simplicity, speed, and no-training-required nature make it the natural starting point for readers building sentiment systems.
- **How to use:** Cite as the VADER reference. Emphasize its design for social media — this is both its strength (handles informal text well) and limitation (not calibrated for financial language). Its performance on financial text is a key benchmark question.
- Status: `[ ] Unverified`

---

### 4.2 Benchmark: Financial NLP Datasets

**Maia, Macedo, Siegfried Handschuh, André Freitas, Brian Davis, Ross McDermott, Manel Zarrouk, and Alexandra Balahur. "WWW'18 Open Challenge: Financial Opinion Mining and Question Answering." In *Companion Proceedings of The Web Conference 2018*, 1941–1942. Lyon, France: ACM, April 2018.**

- DOI: `10.1145/3184558.3192301`
- **Type:** Peer-reviewed workshop paper.
- **Summary:** Introduces the FiQA (Financial Question Answering) benchmark, including Task 1: aspect-based financial sentiment analysis. The dataset contains 1,174 financial news headlines and tweets with continuous sentiment scores [-1, 1] and entity-level targets. Has become a standard benchmark for evaluating financial sentiment models.
- **Relevance:** *Section 4 (Benchmarking Classical Methods).* FiQA is one of the two benchmark datasets named in the chapter plan. Provides the labeled data against which classical and transformer approaches can be compared.
- **How to use:** Cite as the FiQA benchmark reference. Use it to establish performance baselines for VADER, TextBlob, and L-M dictionary approaches.
- Status: `[ ] Unverified`

---

**Sinha, Ankur, Satishwar Kedas, Rishu Kumar, and Pekka Korhonen. "SEntFiN 1.0: Entity-Aware Sentiment Analysis for Financial News." *Journal of the Association for Information Science and Technology* 73, no. 9 (September 2022): 1314–1335.**

- DOI: `10.1002/asi.24634`
- **Type:** Peer-reviewed journal article.
- **Summary:** Introduces SEntFiN, a human-annotated dataset of 10,753 financial news headlines with entity-sentiment annotations. Notably, 2,847 headlines contain multiple entities with potentially conflicting sentiments. Augmented with 1,000+ financial entities and 5,000+ entity phrases. RoBERTa and FinBERT achieve highest accuracy (94.29%) and F1 (93.27%).
- **Relevance:** *Section 4 (Benchmarking).* SEntFiN is the second benchmark dataset named in the chapter plan. Its entity-aware design captures a real-world challenge: the same sentence can be positive for one company and negative for another.
- **How to use:** Cite as the SEntFiN benchmark reference. The multi-entity conflicting sentiment challenge is particularly useful for illustrating limitations of classical bag-of-words approaches.
- Status: `[ ] Unverified`

---

**Malo, Pekka, Ankur Sinha, Pekka Korhonen, Jyrki Wallenius, and Pyry Takala. "Good Debt or Bad Debt: Detecting Semantic Orientations in Economic Texts." *Journal of the Association for Information Science and Technology* 65, no. 4 (April 2014): 782–796.**

- DOI: `10.1002/asi.23062`
- **Type:** Peer-reviewed journal article.
- **Summary:** Investigates semantic orientation detection in financial text, accommodating phrase-structure information and domain-specific language. Main contribution: the Financial PhraseBank, a human-annotated dataset for training and evaluating financial sentiment models. Demonstrates that the overall semantic orientation of a sentence can differ from that of individual words — a key challenge for lexicon-based approaches.
- **Relevance:** *Section 4 (Benchmarking).* The Financial PhraseBank is widely used for training and evaluating financial sentiment models, including FinBERT. Provides a third benchmark alongside FiQA and SEntFiN.
- **How to use:** Cite as the Financial PhraseBank reference. The phrase-level vs. word-level sentiment distinction directly motivates the progression from lexicon-based methods (this chapter) to contextualized models (Chapter 4).
- Status: `[ ] Unverified`

---

## 5. When Classical NLP Is Still the Right Choice

### 5.1 Empirical: Classical vs. Transformer Comparison

**Karanikola, Aikaterini, Gregory Davrazos, Charalampos M. Liapis, and Sotiris Kotsiantis. "Financial Sentiment Analysis: Classic Methods vs. Deep Learning Models." *Intelligent Decision Technologies* 17 (2023): 893–915.**

- DOI: `10.3233/IDT-230478`
- **Type:** Peer-reviewed journal article.
- **Summary:** Rigorously tests numerous classical ML classification algorithms and ensembles against five deep learning pre-trained models (including BERT and RoBERTa) on financial sentiment tasks. Provides the most direct head-to-head comparison of classical vs. transformer approaches available in the financial NLP literature.
- **Relevance:** *Section 5 (When Classical NLP Wins).* The definitive empirical comparison for this chapter's concluding argument. Provides the data to make the nuanced case: transformers generally win on accuracy, but classical methods offer advantages in speed, interpretability, and data efficiency.
- **How to use:** Central to Section 5. Use the specific accuracy comparisons to quantify the accuracy/speed/interpretability tradeoff. Avoid overselling either approach.
- Status: `[ ] Unverified`

---

### 5.2 Contextual: Practical Considerations

**Gentzkow, Matthew, Bryan Kelly, and Matt Taddy. "Text as Data." *Journal of Economic Literature* 57, no. 3 (September 2019): 535–574.**

- DOI: `10.1257/jel.20181020`
- **Type:** Peer-reviewed survey article.
- **Summary:** Surveys text-as-data methods in economics. Includes practical discussion of when simpler methods (bag-of-words, TF-IDF) are appropriate vs. when more complex approaches are justified — a key consideration for researchers choosing methods.
- **Relevance:** *Section 5.* The "right tool for the right problem" framing. Gentzkow et al. are careful to note that simpler methods often suffice, especially when interpretability and computational cost matter.
- **How to use:** Cite for the pragmatic perspective on method selection.
- **Cross-reference:** Already cited in Chapters 1 and 2 research.
- Status: `[ ] Unverified`

---

**Kearney, Colm, and Sha Liu. "Textual Sentiment in Finance: A Survey of Methods and Models." *International Review of Financial Analysis* 33 (May 2014): 171–185.**

- DOI: `10.1016/j.irfa.2014.02.006`
- **Type:** Peer-reviewed survey article.
- **Summary:** Surveys content analysis methods and empirical models for financial textual sentiment. Captures the state of the field in the pre-deep-learning era, documenting what worked with classical methods.
- **Relevance:** *Section 5.* Provides the historical perspective on what classical methods achieved before transformers. Useful for calibrating expectations — many classical results were already practically useful.
- **Cross-reference:** Already cited in Chapter 1 research.
- Status: `[ ] Unverified`

---

### 5.3 Empirical: Latency and Production Considerations

**Li, Qing, Chao Wang, and Jiawei Han. "Natural Language Processing in Finance: A Survey." *Information Fusion* 114 (February 2025): 102755.**

- DOI: `10.1016/j.inffus.2024.102755`
- **Type:** Peer-reviewed survey article.
- **Summary:** Comprehensive 2024/2025 survey of ten major financial NLP applications. Discusses practical considerations including latency, cost, and production deployment — factors that often favor classical methods.
- **Relevance:** *Section 5.* The most current survey, capturing the post-LLM landscape where the classical-vs-transformer tradeoff has become even more pronounced (with LLMs adding a third tier of cost/capability).
- **Cross-reference:** Already cited in Chapters 1 and 2 research.
- Status: `[ ] Unverified`

---

## Cross-Chapter References

| Source | Ch 3 Section | Also Relevant To |
|--------|-------------|------------------|
| Loughran & McDonald (2011) | Sec 2 (Lexicons) | Ch 1, Ch 5 (Sentiment), Ch 6 (Disclosure) |
| Loughran & McDonald (2016) Survey | Sec 2–5 (Entire chapter) | Ch 1, Ch 2 |
| Sennrich et al. (2016) BPE | Sec 1 (Tokenization) | Ch 4 (Transformers) |
| Loukas et al. (2021) EDGAR-W2V | Sec 3 (Financial Embeddings) | Ch 2 (EDGAR), Ch 4 (Training Data) |
| Malo et al. (2014) PhraseBank | Sec 4 (Benchmarks) | Ch 4 (FinBERT Training), Ch 5 (Sentiment) |
| Sinha et al. (2022) SEntFiN | Sec 4 (Benchmarks) | Ch 5 (Sentiment), Ch 9 (Entity Extraction) |
| Maia et al. (2018) FiQA | Sec 4 (Benchmarks) | Ch 4 (Model Evaluation), Ch 5 (Sentiment) |
| Gentzkow et al. (2019) | Sec 5 (Method Selection) | Ch 1, Ch 2 |
| Li et al. (2025) Survey | Sec 5 (Production) | All chapters |
| Jegadeesh & Wu (2013) | Sec 2 (Word Weighting) | Ch 1, Ch 5 (Signal Construction) |
| Karanikola et al. (2023) | Sec 5 (Classical vs. DL) | Ch 4 (Transformers benchmark) |

---

## Research Gaps

The following areas need additional sourcing:

- [ ] **Tokenizer comparison on financial text** — Need a study specifically comparing spaCy, NLTK, and Hugging Face tokenizers on financial text. Financial edge cases (ticker symbols as common words — "COST," "CAT," "FORD"; numerical expressions like "10-K," "P/E," "$3.50B"; abbreviations like "EPS," "EBITDA") are well-known problems but lack a systematic benchmark study.
- [ ] **TextBlob financial performance** — VADER has published benchmarks, but TextBlob's performance on financial text is less documented. Search for specific evaluation studies.
- [ ] **Harvard GI vs. Loughran-McDonald: specific word reclassification examples** — The L-M paper notes the three-fourths misclassification rate, but a detailed table of specific reclassified words (with financial context examples) would strengthen the chapter's pedagogical argument. The L-M Master Dictionary at `sraf.nd.edu` may provide this.
- [ ] **Latency benchmarks: classical vs. BERT on typical financial documents** — Need specific timing data (e.g., TF-IDF inference in <1ms vs. BERT inference at 50-100ms per document on CPU). Industry benchmarks from FactSet, Bloomberg, or academic papers with timing comparisons would be valuable.
- [ ] **fastText on financial neologisms** — Need a study demonstrating fastText's handling of novel financial terms (DeFi, NFT, SPAC, meme stock) via subword embeddings. The EDGAR-W2V paper (Loukas et al. 2021) uses Word2Vec, not fastText — a fastText-on-financial-text study would fill a gap.
- [ ] **Financial PhraseBank update status** — The original Malo et al. (2014) PhraseBank may have been updated. Check for newer versions or expanded datasets.

---

## Verification Priority

Start SMU Library verification with these sources first:

1. **Loughran & McDonald (2011)** — The chapter's most important source (if not already verified from Ch 1)
2. **Mikolov et al. (2013a)** — Word2Vec original paper (arXiv:1301.3781)
3. **Mikolov et al. (2013b)** — Word2Vec NIPS paper (negative sampling)
4. **Pennington et al. (2014)** — GloVe
5. **Bojanowski et al. (2017)** — fastText
6. **Hutto & Gilbert (2014)** — VADER
7. **Malo et al. (2014)** — Financial PhraseBank
8. **Sinha et al. (2022)** — SEntFiN benchmark
9. **Karanikola et al. (2023)** — Classical vs. deep learning comparison
10. **Salton & Buckley (1988)** — TF-IDF foundation

---

*Research compiled April 2026. All citations require manual verification through SMU Library before inclusion in final manuscript.*
