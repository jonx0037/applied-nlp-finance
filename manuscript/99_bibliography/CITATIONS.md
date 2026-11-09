# Citation Conventions — *Applied NLP for Finance*

This document defines the conventions for citations in this book. It is the authoritative reference; if `references.bib` and this document disagree, this document wins and the bib is regenerated.

## Citation Style

**Chicago Notes and Bibliography, 17th edition**, rendered via `biblatex-chicago`. Footnote citations in prose; full bibliography at the end.

LaTeX setup (for whichever publishing pipeline lands later):

```latex
\usepackage[notes,backend=biber,authordate]{biblatex-chicago}
\addbibresource{manuscript/99_bibliography/references.bib}
```

For per-chapter sub-bibliographies (designed in but not yet rendered):

```latex
\printbibliography[keyword=ch01, title={Chapter 1 References}]
```

The `keyword=chNN` filter works because every entry tags its chapter affiliations in the `keywords` field.

## Citation Key Convention

**Format:** `lastname_year[_keyword]` — lowercase, underscore-separated.

### The Rule

```
generate_key(authors, year, title) -> str:
    if len(authors) == 1:
        base = surname(authors[0])
    elif len(authors) == 2:
        base = f"{surname(authors[0])}_{surname(authors[1])}"
    else:
        base = f"{surname(authors[0])}_etal"
    key = f"{base}_{year}".lower()
    return ascii_fold(key)   # strips accents, removes apostrophes
```

### Examples

| Pattern | Example |
|---|---|
| Single author | `fama_1970`, `tetlock_2007`, `shiller_2017` |
| Two authors | `loughran_mcdonald_2011`, `grossman_stiglitz_1980` |
| Three+ authors | `gentzkow_etal_2019`, `vaswani_etal_2017` |
| Same authors + same year collision | `kahneman_tversky_1979_prospect`, `kahneman_tversky_1981_framing` |
| Same first author + different co-authors + same year | append first distinguishing word of title |
| Organizational author | `sec_2025_edgar_api`, `federalreserve_2026_fraser` |
| Accented surnames | `garcia_2013` (from "García"), `francois_etal_2024` (from "François") |
| Apostrophes in surnames | `oreilly_2020` (from "O'Reilly") |

### Disambiguation Algorithm (for collisions)

When `lastname[_lastname2]_year` is not unique:

1. **Same authors, different papers, same year** — append the first non-trivial word of the title, lowercased. Skip articles (`a`, `an`, `the`), prepositions, and conjunctions.
   - `kahneman_tversky_1979_prospect` (from *Prospect Theory: An Analysis of Decision under Risk*)
   - `kahneman_tversky_1981_framing` (from *The Framing of Decisions and the Psychology of Choice*)

2. **Same first author, different co-authors, same year** — append the second author's surname (or `etal_keyword` for 3+ authors).
   - `tetlock_macskassy_2008` and `tetlock_saar-tsechansky_2008`

3. **Same first author, different co-authors, three+ authors each, same year** — fall back to `_etal_` plus a title keyword.
   - `tetlock_etal_2008_news` and `tetlock_etal_2008_dispersion`

### Why This Convention

- **biblatex-compatible.** Both `lastname_year` and `LastnameYear` work, but lowercase underscores avoid casing issues with `\citeauthor` and survive case-insensitive filesystems unchanged.
- **Readable in raw Markdown / LaTeX source.** `\autocite{loughran_mcdonald_2011}` scans faster than `\autocite{LoughranMcDonald2011}`.
- **Stable under author-order corrections.** If verification reveals corrected author order, the key stays the same as long as the first author is correct.
- **Mechanical, not aesthetic.** Two humans following the algorithm produce identical keys. No judgment calls.
- **Matches spoken form.** Jonathan refers to anchor sources as "Loughran-McDonald 2011" — the key encoding mirrors the spoken form.

### What Not to Do

- ❌ `2011_loughran_mcdonald` — year first breaks alphabetical scan-by-author intuition.
- ❌ `Loughran-McDonald2011` — hyphens conflict with biblatex's range syntax in some commands.
- ❌ `lm2011` — initials are ambiguous (Lo-Mendelson? Loughran-McDonald? Lewis-Manela?).
- ❌ Including punctuation, accents, or non-ASCII in the key itself. (Keep them in the `author` field; only fold the key.)

## `references.bib` Organization

**Flat alphabetical within entry-type blocks.** The file is organized by entry type — `@article`, `@book`, `@misc`, `@incollection`/`@inproceedings`, `@online` — with alphabetical ordering by citation key within each block. Comment fenceposts mark the blocks.

**Chapter affiliations live in metadata, not file layout.** Each entry includes a non-standard `keywords` field listing the chapters that cite it:

```bibtex
@article{loughran_mcdonald_2011,
    author       = {Loughran, Tim and McDonald, Bill},
    title        = {When Is a Liability Not a Liability? Textual Analysis, Dictionaries, and 10-Ks},
    journaltitle = {Journal of Finance},
    year         = {2011},
    volume       = {66},
    number       = {1},
    pages        = {35--65},
    doi          = {10.1111/j.1540-6261.2010.01625.x},
    keywords     = {ch01, ch03, ch04, ch05, ch11},
}
```

biblatex passes `keywords` through harmlessly and uses it for `\printbibliography[keyword=ch01]`. The author-facing per-chapter scan view lives in the separately-generated [`manuscript/references_master_index.md`](../references_master_index.md).

### Rationale for Flat Alphabetical (vs. Per-Chapter Sections)

Eleven anchor sources are cited across 3–7 chapters each (Loughran-McDonald, Tetlock, Shiller, Li et al. 2025, Gentzkow-Kelly-Taddy, etc., per [research_review.md §3.2](../research_review.md)). Per-chapter file sections force either:

- Duplicating these entries across multiple sections (breaks biber: duplicate keys), or
- Arbitrarily picking one chapter for each anchor source (loses cross-reference information).

Flat alphabetical + `keywords` metadata preserves cross-reference information without duplication, and the generated index gives the author the per-chapter view they want for scanning.

## Required Field Sets per Entry Type

| Type | Required | Recommended | Optional |
|---|---|---|---|
| `@article` | `author`, `title`, `journaltitle`, `year` | `volume`, `number`, `pages`, `doi` | `month`, `issn` |
| `@book` | `author`/`editor`, `title`, `publisher`, `year` | `location`, `isbn` | `edition`, `series` |
| `@incollection` | `author`, `title`, `booktitle`, `editor`, `publisher`, `year` | `location`, `pages`, `isbn` | — |
| `@inproceedings` | `author`, `title`, `booktitle`, `year` | `publisher`, `pages`, `eventtitle` | `doi` |
| `@misc` (preprint) | `author`, `title`, `year`, `howpublished` | `eprint`, `eprinttype`, `eprintclass`, `url` | — |
| `@online` (docs / regulatory) | `author`/organization, `title`, `year`, `url`, `urldate` | `note` (Wayback URL) | — |
| **All entries** | — | `keywords` (chapter list — our convention) | — |

Entries missing a required field are flagged by `tools/research_to_bibtex.py` in the conversion warnings; entries missing recommended fields produce informational notes but don't block the build.

## Author Field Formatting

Use BibTeX's `Last, First and Last, First` form, **always**. Even single authors get the comma-form:

```bibtex
author = {Fama, Eugene F.}
author = {Loughran, Tim and McDonald, Bill}
author = {Gentzkow, Matthew and Kelly, Bryan and Taddy, Matt}
```

biblatex parses this correctly; `First Last` form is ambiguous for "Van Der Berg, Maria" and similar.

For organizational authors, use the `{{...}}` double-brace form to prevent biblatex from parsing it as a personal name:

```bibtex
author = {{Securities and Exchange Commission}}
author = {{Federal Reserve Bank of St. Louis}}
```

## Verification Status

Every entry in `research.md` files has a `Status:` line:

```markdown
- Status: `[ ] Unverified`
```

After SMU Library verification:

```markdown
- Status: `[x] Verified via SMU Library 2026-MM-DD`

  **Verification notes:**
  - p. 42: Three-form taxonomy explicitly defined as weak/semi-strong/strong.
  - p. 51: Footnote 11 acknowledges that "the speed of price adjustment to information has not been measured directly."
  - Confirmed DOI 10.1111/j.1540-6261.1970.tb00518.x resolves to the Wiley archive.
```

Tier classification (per [research_review.md §7.1](../research_review.md)) determines verification priority:

- **Tier 1** (~30) — Top-five journals (JF, JFE, RFS, AER, QJE, Econometrica) + foundational NLP. Must verify before publication.
- **Tier 2** (~50) — Chapter-anchoring papers. Verify before drafting the chapter.
- **Tier 3** (~40) — Supporting citations. Verify during revision.
- **Tier 4** (~20) — Public docs and regulations. May not need verification.

## Special Cases

### Preprints That Have Been Peer-Reviewed Since

If a research.md entry cites an arXiv preprint and the paper has since appeared in a peer-reviewed venue, **cite the peer-reviewed version**. Update the `research.md` entry, then regenerate `references.bib`. Keep a `note` field linking to the preprint for readers who want the open-access version.

Per [research_review.md §7.3](../research_review.md), specifically re-check these during Tier 1 verification:
- Glasserman-Lin 2023
- FinGPT (Yang et al. 2023)
- BloombergGPT (Wu et al. 2023)
- FinMTEB (Tang & Yang 2025)

### Regulatory Documents

Use `@online` with `urldate` (the date the URL was retrieved) and capture a Wayback Machine snapshot URL in `note`. Regulatory pages are revised in place; the snapshot URL preserves the version the book references.

```bibtex
@online{sec_2025_examination_priorities,
    author   = {{Securities and Exchange Commission}},
    title    = {2025 Examination Priorities},
    year     = {2025},
    url      = {https://www.sec.gov/...},
    urldate  = {2026-04-15},
    note     = {Archived snapshot: https://web.archive.org/web/2026.../...},
    keywords = {ch13},
}
```

### Two FinBERTs

Araci (2019) and Huang et al. (2023) are **distinct models** with different architectures and training data, both named "FinBERT" by their respective authors. Per [research_review.md §7.3](../research_review.md), force two distinct keys:

- `araci_2019_finbert` — original FinBERT, BERT-base + financial PhraseBank fine-tuning
- `huang_etal_2023_finbert` — Huang's FinBERT, BERT-base + 4.9B-token financial corpus

The dedup pass in `tools/research_to_bibtex.py` must **never** collapse these on title alone.

### Non-English Sources

Preserve diacritics and non-ASCII characters in BibTeX field values (`author`, `title`). `ascii_fold` runs **only on the citation key**, never on the field content. UTF-8 round-trips cleanly through bibtexparser and biber.

## Regenerating `references.bib`

Always regenerate the file from `research.md` sources rather than hand-editing:

```bash
cd applied-nlp-finance
source .venv/bin/activate

# Dry-run: show what would change
uv run python -m tools.research_to_bibtex --check

# Regenerate
uv run python -m tools.research_to_bibtex --write

# Cross-check DOIs against CrossRef
uv run python -m tools.verify_doi --all

# Regenerate the per-chapter index
uv run python -m tools.build_master_index
```

If you hand-edit `references.bib` directly, the next regeneration will overwrite your changes. The source of truth is `manuscript/*/research.md`.
