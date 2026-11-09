# Tier-1 SMU Library Verification Worklist

Foundational sources that must be verified before publication. Per [research_review.md §7.1](../manuscript/research_review.md): top-five economics journals (JF, JFE, RFS, AER, QJE, Econometrica) plus foundational NLP papers (Transformer, BERT, RAG, Word2Vec, GloVe, BPE, the two FinBERTs).

**Total:** 40 sources

**Workflow per source:**
1. Locate the paper in SMU Library (digital archives, JSTOR, Wiley, etc.).
2. Download PDF and verify the citation details against what's in `research.md`.
3. Read the abstract + introduction + conclusion. Skim the methods.
4. Capture 2-3 specific findings with page numbers in the research.md entry as a
   `Verification notes:` block under the `Status:` line.
5. Flip the status: `[ ] Unverified` → `[x] Verified via SMU Library YYYY-MM-DD`.
6. Re-run `python -m tools.research_to_bibtex --write` to regenerate the bib
   if anything changed (DOI fix, author correction, etc.).

**Time estimate:** 15-30 min per source (Tier 1 papers reward careful reading).

---

### 1. `akerlof_1970`  · _cited in ch01_

**Akerlof, George A.** *The Market for 'Lemons': Quality Uncertainty and the Market Mechanism.* Quarterly Journal of Economics, 1970.
`DOI: 10.2307/1879431`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 2. `antweiler_frank_2004`  · _cited in ch01,ch08_

**Antweiler, Werner; Frank, Murray Z..** *Is All That Talk Just Noise? The Information Content of Internet Stock Message Boards.* Journal of Finance, 2004.
`DOI: 10.1111/j.1540-6261.2004.00662.x`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 3. `fama_1970`  · _cited in ch01_

**Fama, Eugene F.** *Efficient Capital Markets: A Review of Theory and Empirical Work.* Journal of Finance, 1970.
`DOI: 10.1111/j.1540-6261.1970.tb00518.x`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 4. `fama_1991`  · _cited in ch01_

**Fama, Eugene F.** *Efficient Capital Markets: II.* Journal of Finance, 1991.
`DOI: 10.1111/j.1540-6261.1991.tb04636.x`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 5. `grossman_stiglitz_1980`  · _cited in ch01_

**Grossman, Sanford J.; Stiglitz, Joseph E..** *On the Impossibility of Informationally Efficient Markets.* American Economic Review, 1980.
`URL: https://www.aeaweb.org/aer/top20/70.3.393-408.pdf`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 6. `hayek_1945`  · _cited in ch01_

**Hayek, Friedrich A.** *The Use of Knowledge in Society.* American Economic Review, 1945.
`URL: https://www.econlib.org/library/Essays/hykKnw.html`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 7. `jegadeesh_wu_2013`  · _cited in ch01,ch03_

**Jegadeesh, Narasimhan; Wu, Di.** *Word Power: A New Approach for Content Analysis.* Journal of Financial Economics, 2013.
`DOI: 10.1016/j.jfineco.2013.08.012`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 8. `kahneman_tversky_1979`  · _cited in ch01_

**Kahneman, Daniel; Tversky, Amos.** *Prospect Theory: An Analysis of Decision under Risk.* Econometrica, 1979.
`DOI: 10.2307/1914185`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 9. `loughran_mcdonald_2011`  · _cited in ch01,ch03,ch04,ch11_

**Loughran, Tim; McDonald, Bill.** *When Is a Liability Not a Liability? Textual Analysis, Dictionaries, and 10-Ks.* Journal of Finance, 2011.
`DOI: 10.1111/j.1540-6261.2010.01625.x`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 10. `manela_moreira_2017`  · _cited in ch01,ch02,ch05,ch10_

**Manela, Asaf; Moreira, Alan.** *News Implied Volatility and Disaster Concerns.* Journal of Financial Economics, 2017.
`DOI: 10.1016/j.jfineco.2016.01.032`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 11. `shiller_2017`  · _cited in ch01,ch13_

**Shiller, Robert J.** *Narrative Economics.* American Economic Review, 2017.
`DOI: 10.1257/aer.107.4.967`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 12. `tetlock_2007`  · _cited in ch01,ch05,ch08_

**Tetlock, Paul C.** *Giving Content to Investor Sentiment: The Role of Media in the Stock Market.* Journal of Finance, 2007.
`DOI: 10.1111/j.1540-6261.2007.01232.x`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 13. `tetlock_etal_2008`  · _cited in ch01_

**Tetlock, Paul C.; Saar-Tsechansky, Maytal; Macskassy, Sofus.** *More Than Words: Quantifying Language to Measure Firms' Fundamentals.* Journal of Finance, 2008.
`DOI: 10.1111/j.1540-6261.2008.01362.x`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 14. `tversky_kahneman_1981`  · _cited in ch01_

**Tversky, Amos; Kahneman, Daniel.** *The Framing of Decisions and the Psychology of Choice.* Science, 1981.
`DOI: 10.1126/science.7455683`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 15. `loughran_mcdonald_2014`  · _cited in ch02_

**Loughran, Tim; McDonald, Bill.** *Measuring Readability in Financial Disclosures.* Journal of Finance, 2014.
`DOI: 10.1111/jofi.12162`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 16. `mikolov_etal_2013_distributed`  · _cited in ch03_

**Mikolov, Tomas; Sutskever, Ilya; Chen, Kai; Corrado, Greg S.; Dean, Jeff.** *Distributed Representations of Words and Phrases and Their Compositionality.* Advances in Neural Information Processing Systems 26 (NIPS 2013), 2013.
`URL: https://arxiv.org/abs/1310.4546`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 17. `pennington_etal_2014`  · _cited in ch03_

**Pennington, Jeffrey; Socher, Richard; Manning, Christopher.** *GloVe: Global Vectors for Word Representation.* Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP), 2014.
`DOI: 10.3115/v1/D14-1162`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 18. `sennrich_etal_2016`  · _cited in ch03_

**Sennrich, Rico; Haddow, Barry; Birch, Alexandra.** *Neural Machine Translation of Rare Words with Subword Units.* Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 2016.
`DOI: 10.18653/v1/P16-1162`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 19. `araci_2019_finbert`  · _cited in ch04_

**Araci, Dogu Tan.** *FinBERT: Financial Sentiment Analysis with Pre-trained Language Models.* arXiv preprint, arXiv:1908.10063, 2019.
`URL: https://arxiv.org/abs/1908.10063`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 20. `devlin_etal_2019`  · _cited in ch04_

**Devlin, Jacob; Chang, Ming-Wei; Lee, Kenton; Toutanova, Kristina.** *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.* Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT), 2019.
`DOI: 10.18653/v1/N19-1423`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 21. `huang_etal_2023_finbert`  · _cited in ch04_

**Huang, Allen H.; Wang, Hui; Yang, Yi.** *FinBERT: A Large Language Model for Extracting Information from Financial Text.* Contemporary Accounting Research, 2023.
`DOI: 10.1111/1911-3846.12832`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 22. `vaswani_etal_2017`  · _cited in ch04_

**Vaswani, Ashish; Shazeer, Noam; Parmar, Niki; Uszkoreit, Jakob; Jones, Llion; Gomez, Aidan N.; Kaiser, Łukasz; Polosukhin, Illia.** *Attention Is All You Need.* Advances in Neural Information Processing Systems 30 (NeurIPS 2017), 2017.
`URL: https://arxiv.org/abs/1706.03762`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 23. `baker_wurgler_2006`  · _cited in ch05,ch10_

**Baker, Malcolm; Wurgler, Jeffrey.** *Investor Sentiment and the Cross-Section of Stock Returns.* Journal of Finance, 2006.
`DOI: 10.1111/j.1540-6261.2006.00885.x`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 24. `garcia_2013`  · _cited in ch05,ch10_

**García, Diego.** *Sentiment during Recessions.* Journal of Finance, 2013.
`DOI: 10.1111/jofi.12027`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 25. `kolari_pynnonen_2010`  · _cited in ch06_

**Kolari, James W.; Pynnönen, Seppo.** *Event Study Testing with Cross-Sectional Correlation of Abnormal Returns.* Review of Financial Studies, 2010.
`DOI: 10.1093/rfs/hhq072`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 26. `gorodnichenko_etal_2023`  · _cited in ch07,ch10_

**Gorodnichenko, Yuriy; Pham, Tho; Talavera, Oleksandr.** *The Voice of Monetary Policy.* American Economic Review, 2023.
`DOI: 10.1257/aer.20220129`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 27. `nakamura_steinsson_2018`  · _cited in ch07_

**Nakamura, Emi; Steinsson, Jón.** *High-Frequency Identification of Monetary Non-Neutrality: The Information Effect.* Quarterly Journal of Economics, 2018.
`DOI: 10.1093/qje/qjy004`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 28. `bradley_etal_2024`  · _cited in ch08_

**Bradley, Daniel; Jr., Jan Hanousek; Jame, Russell; Xiao, Zicheng.** *Place Your Bets? The Value of Investment Research on Reddit's Wallstreetbets.* Review of Financial Studies, 2024.
`DOI: 10.1093/rfs/hhad098`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 29. `chen_etal_2014`  · _cited in ch08_

**Chen, Hailiang; De, Prabuddha; Hu, Yu Jeffrey; Hwang, Byoung-Hyoun.** *Wisdom of Crowds: The Value of Stock Opinions Transmitted Through Social Media.* Review of Financial Studies, 2014.
`DOI: 10.1093/rfs/hhu001`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 30. `cookson_etal_2023`  · _cited in ch08_

**Cookson, J. Anthony; Engelberg, Joseph; Mullins, William.** *Echo Chambers.* Review of Financial Studies, 2023.
`DOI: 10.1093/rfs/hhac058`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 31. `pedersen_2022`  · _cited in ch08_

**Pedersen, Lasse Heje.** *Game On: Social Networks and Markets.* Journal of Financial Economics, 2022.
`DOI: 10.1016/j.jfineco.2022.05.002`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 32. `billio_etal_2012`  · _cited in ch09,ch10_

**Billio, Monica; Getmansky, Mila; Lo, Andrew W.; Pelizzon, Loriana.** *Econometric Measures of Connectedness and Systemic Risk in the Finance and Insurance Sectors.* Journal of Financial Economics, 2012.
`DOI: 10.1016/j.jfineco.2011.12.010`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 33. `calomiris_mamaysky_2019`  · _cited in ch10_

**Calomiris, Charles W.; Mamaysky, Harry.** *How News and Its Context Drive Risk and Returns around the World.* Journal of Financial Economics, 2019.
`DOI: 10.1016/j.jfineco.2018.11.009`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 34. `hamilton_1989`  · _cited in ch10_

**Hamilton, James D.** *A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle.* Econometrica, 1989.
`DOI: 10.2307/1912559`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 35. `harvey_etal_2016`  · _cited in ch11_

**Harvey, Campbell R.; Liu, Yan; Zhu, Heqing.** *… and the Cross-Section of Expected Returns.* Review of Financial Studies, 2016.
`DOI: 10.1093/rfs/hhv059`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 36. `mclean_pontiff_2016`  · _cited in ch11,ch13_

**McLean, R. David; Pontiff, Jeffrey.** *Does Academic Research Destroy Stock Return Predictability?.* Journal of Finance, 2016.
`DOI: 10.1111/jofi.12365`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 37. `white_2000`  · _cited in ch11_

**White, Halbert.** *A Reality Check for Data Snooping.* Econometrica, 2000.
`DOI: 10.1111/1468-0262.00152`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 38. `lewis_etal_2020`  · _cited in ch12_

**Lewis,  Patrick; others.** *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.* Advances in Neural Information Processing Systems 33 (NeurIPS 2020), 2020.
`URL: https://arxiv.org/abs/2005.11401`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 39. `brunnermeier_pedersen_2009`  · _cited in ch13_

**Brunnermeier, Markus K.; Pedersen, Lasse Heje.** *Market Liquidity and Funding Liquidity.* Review of Financial Studies, 2009.
`DOI: 10.1093/rfs/hhn098`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`

### 40. `stein_2009`  · _cited in ch13_

**Stein, Jeremy C.** *Presidential Address: Sophisticated Investors and Market Efficiency.* Journal of Finance, 2009.
`DOI: 10.1111/j.1540-6261.2009.01472.x`

- [ ] Located PDF at SMU Library
- [ ] Citation details confirmed (author / title / venue / vol / issue / pages / year)
- [ ] Read abstract + introduction + conclusion
- [ ] Captured 2-3 page-anchored findings
- [ ] Updated `research.md` Status to `[x] Verified via SMU Library YYYY-MM-DD`
