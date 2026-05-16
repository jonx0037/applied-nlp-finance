# Chapter 4 — Transformers, LLMs, and Financial Language Models — Annotated Bibliography

**Purpose:** This chapter provides deep treatment of transformer architecture and modern LLM workflows in the financial domain. It covers domain-adapted models (FinBERT, BloombergGPT, FinGPT), fine-tuning strategies (continued pretraining, LoRA, distillation), and the expanding role of LLM-based workflows (zero-shot classification, structured extraction, LLM-as-judge, agentic pipelines). The chapter equips readers to choose the right model for each task.

**What this chapter needs from its sources:**
- The original transformer and BERT papers (architectural foundation)
- Domain-adapted financial models and their training methodology
- Fine-tuning techniques (continued pretraining, LoRA, distillation)
- LLM workflow methodologies (prompting, structured extraction, LLM-as-judge)
- Financial NLP benchmarks for comparing model families
- Cost/latency/accuracy tradeoff data for production deployment decisions

**Citation format:** Chicago (Notes and Bibliography), 17th edition.

**Note on source maturity:** This chapter spans three temporal eras — BERT (2018–2019), domain-adapted models (2019–2023), and LLM workflows (2023–present). Sources from the third era are disproportionately preprints and technical reports, reflecting the field's rapid pace. The manuscript should acknowledge this temporal reality.

---

## 1. BERT Architecture Review

### 1.1 Foundational: Transformer Architecture

**Vaswani, Ashish, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, and Illia Polosukhin. "Attention Is All You Need." In *Advances in Neural Information Processing Systems 30 (NeurIPS 2017)*, 5998–6008. Long Beach, CA, 2017.**

- URL: `https://arxiv.org/abs/1706.03762`
- **Type:** Peer-reviewed conference paper. Over 173,000 citations.
- **Summary:** Proposes the Transformer architecture, based solely on attention mechanisms without recurrence or convolutions. Self-attention relates all positions in a sequence to compute representations, enabling full parallelization and dramatically reducing training time. Achieves state-of-the-art on machine translation benchmarks.
- **Relevance:** *Section 1 (BERT Architecture Review).* The foundational architecture paper. Every model discussed in this chapter — BERT, FinBERT, BloombergGPT, GPT-4, Claude — is built on this architecture. Readers need to understand self-attention, positional encoding, and the encoder-decoder structure.
- **How to use:** Brief review focused on self-attention mechanism and positional encoding — the aspects most relevant to understanding why transformers handle financial text better than RNNs (long-range dependencies, parallel processing of entire documents).
- Status: `[ ] Unverified`

---

### 1.2 Foundational: BERT

**Devlin, Jacob, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding." In *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT)*, 4171–4186. Minneapolis, MN: Association for Computational Linguistics, June 2019.**

- DOI: `10.18653/v1/N19-1423`
- **Type:** Peer-reviewed conference paper. Over 28,000 citations.
- **Summary:** Introduces BERT, which pre-trains deep bidirectional representations by jointly conditioning on both left and right context in all layers using masked language modeling (MLM) and next sentence prediction (NSP). Pre-trained BERT can be fine-tuned with one additional output layer for downstream tasks without substantial architectural modification.
- **Relevance:** *Section 1 (BERT Architecture Review).* The model that launched the pre-train/fine-tune paradigm now used by all financial NLP models. Readers must understand MLM, bidirectional context, and the fine-tuning mechanism to follow the rest of the chapter.
- **How to use:** Focus on three aspects most relevant to financial fine-tuning: (1) the MLM objective and what it means for learning financial vocabulary, (2) the [CLS] token and sequence classification, and (3) the fine-tuning protocol (adding a classification head, adjusting learning rates).
- Status: `[ ] Unverified`

---

### 1.3 Foundational: RoBERTa

**Liu, Yinhan, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. "RoBERTa: A Robustly Optimized BERT Pretraining Approach." arXiv preprint, arXiv:1907.11692, July 2019.**

- URL: `https://arxiv.org/abs/1907.11692`
- **Type:** Preprint (highly cited, foundational).
- **Summary:** Demonstrates that BERT was significantly undertrained and that carefully tuning hyperparameters and training data size yields large performance gains. Key improvements: training longer with bigger batches, removing NSP objective, training on longer sequences, and dynamic masking. Matches or exceeds all post-BERT models.
- **Relevance:** *Section 1–2 (Architecture and Domain Adaptation).* RoBERTa is the base model for several financial NLP approaches (including the SEntFiN benchmark results). Its finding that BERT was undertrained has direct implications for financial domain adaptation — more data and longer training help.
- **How to use:** Cite as the paper that established best practices for BERT pretraining — practices directly applicable to financial continued pretraining.
- Status: `[ ] Unverified`

---

## 2. Why General-Purpose BERT Underperforms on Financial Text

### 2.1 Methodological: Domain Adaptation Theory

**Gururangan, Suchin, Ana Marasović, Swabha Swayamdipta, Kyle Lo, Iz Beltagy, Doug Downey, and Noah A. Smith. "Don't Stop Pretraining: Adapt Language Models to Domains and Tasks." In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL)*, 8342–8360. Online: Association for Computational Linguistics, July 2020.**

- DOI: `10.18653/v1/2020.acl-main.740`
- **Type:** Peer-reviewed conference paper. Over 2,600 citations.
- **Summary:** Systematically studies domain-adaptive pretraining (DAPT) and task-adaptive pretraining (TAPT) across four domains and eight tasks. Finds that a second phase of in-domain pretraining consistently improves performance, even under low-resource settings. Multi-phase adaptive pretraining (DAPT + TAPT) offers the largest gains.
- **Relevance:** *Section 2 (Why General BERT Underperforms) and Section 4 (Fine-Tuning).* The theoretical and empirical justification for domain adaptation. Explains *why* FinBERT and similar models exist: continued pretraining on financial text corrects the vocabulary mismatch and distributional differences between general and financial corpora.
- **How to use:** Central to Sections 2 and 4. The DAPT → TAPT progression maps directly onto the financial NLP workflow: pretrain on general text → continue on financial corpus → fine-tune on specific task (sentiment, NER, etc.).
- Status: `[ ] Unverified`

---

### 2.2 Empirical: Financial Vocabulary Mismatch

**Loughran, Tim, and Bill McDonald. "When Is a Liability Not a Liability? Textual Analysis, Dictionaries, and 10-Ks." *Journal of Finance* 66, no. 1 (February 2011): 35–65.**

- DOI: `10.1111/j.1540-6261.2010.01625.x`
- **Type:** Peer-reviewed journal article.
- **Summary:** Three-fourths of Harvard GI "negative" words are misclassified in financial contexts. Financial text uses common English words with specialized meanings.
- **Relevance:** *Section 2.* The vocabulary mismatch problem demonstrated by Loughran-McDonald for dictionaries is equally relevant for BERT: a model trained on Wikipedia will encode "liability" as negative, but in a 10-K filing it's neutral accounting terminology. This is the same domain-specificity problem at the embedding level.
- **How to use:** Brief reference to connect the dictionary-level finding (Chapter 3) to the embedding-level problem. The same domain mismatch that broke lexicons also degrades general BERT.
- **Cross-reference:** Already cited in Chapters 1 and 3 research.
- Status: `[ ] Unverified`

---

## 3. FinBERT and Domain-Adapted Models

### 3.1 Foundational: FinBERT (Araci)

**Araci, Dogu Tan. "FinBERT: Financial Sentiment Analysis with Pre-trained Language Models." arXiv preprint, arXiv:1908.10063, August 2019.**

- URL: `https://arxiv.org/abs/1908.10063`
- **Type:** Preprint.
- **Summary:** Adapts BERT to finance by further pretraining on Reuters' TRC2 financial corpus, then fine-tuning for sentiment classification. Achieves state-of-the-art on FiQA sentiment scoring and Financial PhraseBank, improving over previous best by 14 percentage points. The ProsusAI/finbert model on Hugging Face has become the most widely used financial sentiment model.
- **Relevance:** *Section 3 (FinBERT).* The canonical financial BERT model. This is the model most readers will actually use in practice, and it's the primary model implemented in the companion code (`src/models/finbert.py`).
- **How to use:** Central to Section 3. Walk through the three-stage pipeline: general BERT pretraining → financial corpus continued pretraining → task-specific fine-tuning. The 14pp improvement over baselines quantifies the value of domain adaptation.
- Status: `[ ] Unverified`

---

### 3.2 Foundational: FinBERT (Huang, Wang, Yang)

**Huang, Allen H., Hui Wang, and Yi Yang. "FinBERT: A Large Language Model for Extracting Information from Financial Text." *Contemporary Accounting Research* 40, no. 2 (Summer 2023): 806–841.**

- DOI: `10.1111/1911-3846.12832`
- **Type:** Peer-reviewed journal article.
- **Summary:** A distinct FinBERT model (different from Araci 2019) that adapts BERT to finance and demonstrates it substantially outperforms the Loughran-McDonald dictionary, Naive Bayes, SVM, random forest, CNN, and LSTM in sentiment classification of analyst reports. FinBERT's advantage is especially salient with small training samples and on texts containing financial words not frequent in general texts.
- **Relevance:** *Section 3 (FinBERT).* This peer-reviewed FinBERT paper (published in a top accounting journal, unlike the Araci preprint) provides rigorous benchmarking against classical methods. The "small training sample" finding is practically important — many financial NLP tasks have limited labeled data.
- **How to use:** Cite alongside Araci (2019) to show there are multiple FinBERT implementations. The head-to-head comparison against L-M dictionary, classical ML, and deep learning provides the strongest evidence for the domain-adapted transformer advantage.
- **Note:** There are two distinct models both called "FinBERT" — Araci (2019) and Huang et al. (2023). The chapter should clarify this naming collision.
- Status: `[ ] Unverified`

---

### 3.3 Foundational: BloombergGPT

**Wu, Shijie, Ozan Irsoy, Steven Lu, Vadim Dabravolski, Mark Dredze, Sebastian Gehrmann, Prabhanjan Kambadur, David Rosenberg, and Gideon Mann. "BloombergGPT: A Large Language Model for Finance." arXiv preprint, arXiv:2303.17564, March 2023.**

- URL: `https://arxiv.org/abs/2303.17564`
- **Type:** Preprint (industry research report).
- **Summary:** A 50-billion parameter decoder-only language model trained on 363 billion tokens of Bloomberg's proprietary financial data plus 345 billion tokens of general-purpose data (708B total). Based on the BLOOM architecture (70 transformer decoder layers). Outperforms existing models on financial tasks without sacrificing general LLM performance. Training Chronicles (Appendix C) document practical training challenges.
- **Relevance:** *Section 3 (Domain-Adapted Models).* The most ambitious domain-specific financial LLM to date. Represents a fundamentally different approach from FinBERT: training a large model from scratch on mixed financial/general data, rather than fine-tuning a smaller model.
- **How to use:** Cite as the upper bound of what's possible with massive financial pretraining. The mixed-data approach (financial + general) is an important design choice. Note the key limitation: the model is proprietary and not publicly available, unlike FinBERT and FinGPT.
- Status: `[ ] Unverified`

---

### 3.4 Foundational: FinGPT

**Yang, Hongyang, Xiao-Yang Liu, and Christina Dan Wang. "FinGPT: Open-Source Financial Large Language Models." In *Proceedings of the FinLLM Symposium at IJCAI 2023*. Macau, August 2023.**

- URL: `https://arxiv.org/abs/2306.06031`
- **Type:** Peer-reviewed workshop paper.
- **Summary:** Presents FinGPT, an open-source financial LLM that takes a data-centric approach. Unlike BloombergGPT's from-scratch training, FinGPT uses lightweight low-rank adaptation (LoRA) on existing open-source LLMs, combined with an automatic data curation pipeline. Demonstrates applications in robo-advising, algorithmic trading, and low-code development.
- **Relevance:** *Section 3 (Domain-Adapted Models).* The open-source counterpart to BloombergGPT. FinGPT's LoRA-based approach is more accessible to the book's audience — readers can actually reproduce and adapt it. The data-centric philosophy (curate financial data, adapt existing models) is the pragmatic approach most practitioners will follow.
- **How to use:** Present as the practical alternative to BloombergGPT. The LoRA-based approach connects to Section 4's fine-tuning discussion, and the open-source availability makes it reproducible for readers.
- Status: `[ ] Unverified`

---

### 3.5 Foundational: Financial NLP Benchmark

**Shah, Raj, Kunal Chawla, Dheeraj Eidnani, Agam Shah, Wendi Du, Sudheer Chava, Natraj Raman, Charese Smiley, Jiaao Chen, and Diyi Yang. "When FLUE Meets FLANG: Benchmarks and Large Pretrained Language Model for Financial Domain." In *Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, 2063–2083. Abu Dhabi: Association for Computational Linguistics, December 2022.**

- DOI: `10.18653/v1/2022.emnlp-main.148`
- **Type:** Peer-reviewed conference paper.
- **Summary:** Introduces FLUE (Financial Language Understanding Evaluation), a comprehensive benchmark suite for financial NLP including sentiment analysis, NER, structure boundary detection, question answering, and stock movement prediction. Also introduces FLANG, a financial language model that achieves state-of-the-art on FLUE tasks.
- **Relevance:** *Section 3 (Benchmarking) and Section 7 (Choosing the Right Model).* FLUE provides the standardized evaluation framework for comparing FinBERT, BloombergGPT, FinGPT, and general-purpose models. Essential for making the "which model to use" argument data-driven.
- **How to use:** Cite as the benchmark reference for comparing financial models. FLUE tasks map to practical use cases readers will encounter.
- Status: `[ ] Unverified`

---

## 4. Fine-Tuning on Custom Financial Corpora

### 4.1 Methodological: Parameter-Efficient Fine-Tuning (LoRA)

**Hu, Edward J., Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. "LoRA: Low-Rank Adaptation of Large Language Models." In *Proceedings of the Tenth International Conference on Learning Representations (ICLR)*. Virtual, April 2022.**

- URL: `https://arxiv.org/abs/2106.09685`
- **Type:** Peer-reviewed conference paper.
- **Summary:** Freezes pre-trained model weights and injects trainable low-rank decomposition matrices into each transformer layer. Reduces trainable parameters by 10,000x and GPU memory by 3x compared to full fine-tuning. Performs on-par or better than full fine-tuning on RoBERTa, DeBERTa, GPT-2, and GPT-3.
- **Relevance:** *Section 4 (Fine-Tuning).* LoRA is the dominant parameter-efficient fine-tuning method and the approach used by FinGPT. For readers working with limited compute budgets (which is most of the audience), LoRA makes domain adaptation practical.
- **How to use:** Central to the fine-tuning section. Compare full fine-tuning (all parameters), adapter layers (adding small modules), and LoRA (low-rank weight updates) as a three-tier complexity ladder. The 10,000x parameter reduction and 3x memory savings are concrete, quotable numbers.
- Status: `[ ] Unverified`

---

### 4.2 Methodological: Knowledge Distillation

**Sanh, Victor, Lysandre Debut, Julien Chaumond, and Thomas Wolf. "DistilBERT, a Distilled Version of BERT: Smaller, Faster, Cheaper, Lighter." In *NeurIPS 2019 Workshop on Energy Efficient Machine Learning and Cognitive Computing*. Vancouver, BC, December 2019.**

- URL: `https://arxiv.org/abs/1910.01108`
- **Type:** Workshop paper (highly cited).
- **Summary:** Introduces DistilBERT, a 40% smaller BERT that retains 97% of language understanding capability while being 60% faster. Uses knowledge distillation during pretraining with a triple loss (language modeling + distillation + cosine-distance). Reduces layers by 2x while keeping architecture otherwise identical.
- **Relevance:** *Section 4 (Fine-Tuning) and Section 6 (Cost/Latency Tradeoff).* DistilBERT represents the "cheaper, faster" tier of the cost/latency/accuracy matrix. For production financial NLP systems processing millions of documents, the 40% size reduction and 60% speedup with only 3% accuracy loss is often the right tradeoff.
- **How to use:** Cite as the exemplar of the distillation approach. Position in the tradeoff matrix: DistilBERT occupies the sweet spot between classical methods (fast but less accurate) and full BERT (accurate but slower).
- Status: `[ ] Unverified`

---

## 5. LLM-Based Financial Workflows

### 5.1 Methodological: LLM-as-Judge

**Zheng, Lianmin, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, et al. "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena." In *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*. New Orleans, LA, 2023.**

- URL: `https://arxiv.org/abs/2306.05685`
- **Type:** Peer-reviewed conference paper.
- **Summary:** Systematically studies using strong LLMs as judges for evaluating model outputs. Finds that GPT-4 achieves over 80% agreement with human preferences. Documents biases (position, verbosity, self-enhancement) and proposes mitigations. Introduces MT-Bench (multi-turn evaluation) and Chatbot Arena (crowdsourced preferences).
- **Relevance:** *Section 5 (LLM-as-Judge Labeling).* The foundational reference for the LLM-as-judge methodology, which is increasingly used in financial NLP to label training data: use a frontier model (GPT-4, Claude) to label financial sentiment, then train a smaller, faster model (FinBERT) on those labels for production deployment.
- **How to use:** Cite as the methodological foundation. The 80% human agreement figure provides credibility, while the documented biases (especially position bias) inform practical guidelines for financial labeling workflows. The financial application: use Claude to label 10K sentences of financial sentiment, then train a FinBERT classifier on those labels.
- Status: `[ ] Unverified`

---

### 5.2 Contextual: LLMs in Financial Applications (Surveys)

**Li, Yinheng, Shaofei Wang, Han Ding, and Hang Chen. "Large Language Models in Finance: A Survey." In *Proceedings of the Fourth ACM International Conference on AI in Finance (ICAIF '23)*, 374–382. Brooklyn, NY: ACM, November 2023.**

- DOI: `10.1145/3604237.3626869`
- **Type:** Peer-reviewed conference paper.
- **Summary:** Surveys LLM applications in finance including sentiment analysis, named entity recognition, financial reasoning, and risk assessment. Categorizes approaches by task type and model architecture.
- **Relevance:** *Section 5 (LLM Workflows) and Section 7 (Choosing the Right Model).* Provides a structured overview of where LLMs are being applied in finance, helping readers understand which tasks benefit most from the LLM paradigm.
- **How to use:** Cite as the ICAIF survey for a concise overview of the financial LLM landscape.
- Status: `[ ] Unverified`

---

**Lee, Jimin, Mogan Gim, Jy-yong Sohn, and Jaeho Lee. "A Survey of Large Language Models in Finance (FinLLMs)." arXiv preprint, arXiv:2402.02315, February 2024.**

- URL: `https://arxiv.org/abs/2402.02315`
- **Type:** Preprint.
- **Summary:** Comprehensive overview of financial LLMs covering history, techniques, performance, opportunities, and challenges. Provides eight advanced financial NLP tasks and datasets for developing sophisticated FinLLMs. Covers the full spectrum from FinBERT through BloombergGPT to prompted GPT-4.
- **Relevance:** *Sections 3–7 (entire chapter).* The most comprehensive FinLLM survey available, covering the full model taxonomy this chapter presents.
- **How to use:** Cite as the comprehensive reference for readers who want deeper coverage of any model discussed in the chapter.
- Status: `[ ] Unverified`

---

## 6. Cost/Latency/Accuracy Tradeoff Matrix

### 6.1 Empirical: Model Comparison Data

**Karanikola, Aikaterini, Gregory Davrazos, Charalampos M. Liapis, and Sotiris Kotsiantis. "Financial Sentiment Analysis: Classic Methods vs. Deep Learning Models." *Intelligent Decision Technologies* 17 (2023): 893–915.**

- DOI: `10.3233/IDT-230478`
- **Type:** Peer-reviewed journal article.
- **Summary:** Head-to-head comparison of classical ML algorithms and ensembles against BERT and RoBERTa on financial sentiment tasks. Provides the accuracy data for the classical-vs-transformer comparison.
- **Relevance:** *Section 6 (Tradeoff Matrix).* Provides one axis (accuracy) of the tradeoff matrix. Combine with latency and cost data from other sources for the full picture.
- **Cross-reference:** Already cited in Chapter 3 research.
- Status: `[ ] Unverified`

---

## 7. Choosing the Right Model

### 7.1 Contextual: The Model Selection Framework

**Li, Qing, Chao Wang, and Jiawei Han. "Natural Language Processing in Finance: A Survey." *Information Fusion* 114 (February 2025): 102755.**

- DOI: `10.1016/j.inffus.2024.102755`
- **Type:** Peer-reviewed survey article.
- **Summary:** Comprehensive 2024/2025 survey covering ten major financial NLP applications. Discusses the practical considerations (latency, cost, deployment complexity) that should inform model selection.
- **Relevance:** *Section 7 (Choosing the Right Model).* The most current survey, capturing the post-LLM landscape. Useful for grounding the decision framework in current best practices.
- **Cross-reference:** Already cited in Chapters 1–3 research.
- Status: `[ ] Unverified`

---

## Cross-Chapter References

| Source | Ch 4 Section | Also Relevant To |
|--------|-------------|------------------|
| Vaswani et al. (2017) Transformer | Sec 1 (Architecture) | Foundational for entire book |
| Devlin et al. (2019) BERT | Sec 1 (Architecture) | Ch 5 (Sentiment Models) |
| Araci (2019) FinBERT | Sec 3 (FinBERT) | Ch 5 (Sentiment), Ch 6 (Earnings Calls), Ch 10 (Regime Detection) |
| Huang et al. (2023) FinBERT-CAR | Sec 3 (FinBERT) | Ch 6 (Analyst Reports) |
| Wu et al. (2023) BloombergGPT | Sec 3 (Financial LLMs) | Ch 12 (Deployment) |
| Yang et al. (2023) FinGPT | Sec 3 (Open-source) | Ch 12 (Deployment) |
| Hu et al. (2022) LoRA | Sec 4 (Fine-tuning) | Ch 12 (Deployment — model serving) |
| Sanh et al. (2019) DistilBERT | Sec 4, 6 (Distillation, Tradeoffs) | Ch 12 (Deployment — latency) |
| Gururangan et al. (2020) DAPT | Sec 2, 4 (Domain Adaptation) | General methodology |
| Zheng et al. (2023) LLM-as-Judge | Sec 5 (LLM Workflows) | Ch 11 (Evaluation) |
| Shah et al. (2022) FLUE/FLANG | Sec 3 (Benchmarks) | Ch 11 (Evaluation) |
| Loughran & McDonald (2011) | Sec 2 (Vocabulary Mismatch) | Ch 1, Ch 3, Ch 5 |
| Karanikola et al. (2023) | Sec 6 (Tradeoffs) | Ch 3 (Classical vs. DL) |

---

## Research Gaps

The following areas need additional sourcing:

- [ ] **Llama-finance and open-source financial LLM variants** — Need specific papers on Llama-2/3 financial fine-tunes beyond FinGPT. Search for "Llama finance fine-tune" or check Hugging Face model cards for documented financial adaptations.
- [ ] **Structured extraction benchmarks (JSON-mode accuracy)** — Need a rigorous study measuring JSON extraction accuracy from financial documents using GPT-4/Claude structured output modes. The FinTagging benchmark (arXiv:2505.20650, 2025) may address this — verify.
- [ ] **Cost comparison data: OpenAI API vs. Claude API vs. self-hosted** — Need current pricing data and processing cost estimates for typical financial document volumes. This changes frequently — may need to be presented as a methodology (cost-per-token × tokens-per-document × documents-per-quarter) rather than fixed numbers.
- [ ] **Latency benchmarks: FinBERT inference vs. GPT-4 API vs. distilled model** — Need specific timing data on CPU and GPU for financial document classification. Check MLCommons or Hugging Face inference benchmarks.
- [ ] **Prompt engineering patterns for financial analysis** — Need a systematic study of prompt patterns (CoT, few-shot exemplar selection, output formatting) specifically for financial tasks. The "Prompt Engineering and Format on LLMs in the Financial Domain" paper (ResearchGate, 2025) may address this.
- [ ] **Agentic financial analysis pipeline examples** — Need academic or industry references documenting multi-step LLM reasoning over financial filings (e.g., extract risk factors → cross-reference with peer filings → generate relative risk assessment). This is an emerging area with limited formal literature.
- [ ] **Adapter layers for financial BERT** — Need references on adapter-based fine-tuning (Houlsby et al. 2019) applied to financial models, as a middle ground between full fine-tuning and LoRA.
- [ ] **Inter-annotator agreement for financial sentiment** — Need references establishing human agreement baselines for financial sentiment labeling to compare against LLM-as-judge performance.

---

## Verification Priority

Start SMU Library verification with these sources first:

1. **Vaswani et al. (2017)** — Transformer architecture (foundational)
2. **Devlin et al. (2019)** — BERT (foundational)
3. **Araci (2019)** — FinBERT (central to chapter and companion code)
4. **Huang et al. (2023)** — FinBERT in CAR (peer-reviewed validation)
5. **Wu et al. (2023)** — BloombergGPT (largest financial LLM)
6. **Gururangan et al. (2020)** — Domain adaptation theory
7. **Hu et al. (2022)** — LoRA (practical fine-tuning method)
8. **Shah et al. (2022)** — FLUE benchmark
9. **Zheng et al. (2023)** — LLM-as-Judge methodology
10. **Yang et al. (2023)** — FinGPT (open-source alternative)

---

*Research compiled April 2026. All citations require manual verification through SMU Library before inclusion in final manuscript.*
