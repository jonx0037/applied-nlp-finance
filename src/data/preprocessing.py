"""Text cleaning and normalization for financial documents."""

from __future__ import annotations


def clean_financial_text(
    text: str,
    remove_tables: bool = True,
    *,
    remove_html: bool = True,
    fix_encoding: bool = True,
    normalize_whitespace: bool = True,
    lowercase: bool = False,
) -> str:
    """Clean raw financial text.

    Applies a pipeline of cleaning operations suitable for SEC filings,
    earnings transcripts, news articles, and other financial text.

    Parameters
    ----------
    text : str
        Raw text to clean.
    remove_tables : bool
        Whether to strip embedded tables and tabular data.
    remove_html : bool
        Whether to strip HTML/SGML tags.
    fix_encoding : bool
        Whether to fix common encoding issues (e.g. ``&amp;`` -> ``&``).
    normalize_whitespace : bool
        Whether to collapse multiple whitespace chars to single spaces.
    lowercase : bool
        Whether to convert text to lowercase.

    Returns
    -------
    str
        Cleaned text.
    """
    # TODO: implement — apply the following pipeline:
    # 1. Strip HTML/SGML tags using BeautifulSoup or regex
    # 2. Fix HTML entities and encoding issues
    # 3. Remove tables (detect ASCII/HTML table patterns)
    # 4. Normalize Unicode characters
    # 5. Collapse whitespace
    # 6. Optionally lowercase
    raise NotImplementedError


def normalize_tickers(
    text: str,
    ticker_map: dict | None = None,
) -> str:
    """Normalize ticker symbol mentions to canonical forms.

    Handles variations like ``$AAPL``, ``AAPL``, ``Apple Inc.``,
    ``Apple``, and maps them to a canonical form (e.g. ``AAPL``).

    Parameters
    ----------
    text : str
        Text containing ticker symbol mentions.
    ticker_map : dict | None
        Optional mapping from aliases to canonical tickers. If ``None``,
        a default map is loaded.

    Returns
    -------
    str
        Text with normalized ticker references.
    """
    # TODO: implement — build a regex for $TICKER patterns and known
    # company name aliases, replace each match with the canonical ticker,
    # handle edge cases (e.g. "Apple" in non-financial context).
    raise NotImplementedError


def segment_document(
    text: str,
    section_patterns: dict | None = None,
) -> dict[str, str]:
    """Segment a financial document into labeled sections.

    Identifies standard sections in SEC filings (MD&A, Risk Factors,
    Financial Statements, etc.) and returns them as a mapping.

    Parameters
    ----------
    text : str
        Full document text.
    section_patterns : dict | None
        Optional mapping from section names to regex patterns that
        identify section headers. If ``None``, default patterns for
        10-K and 10-Q filings are used.

    Returns
    -------
    dict[str, str]
        Mapping of section names to their text content. Keys include
        ``"mda"``, ``"risk_factors"``, ``"financial_statements"``,
        ``"notes"``, and ``"other"``.
    """
    # TODO: implement — compile section header patterns, scan the
    # document for section boundaries using regex and heuristics,
    # extract text between boundaries, and normalise section names.
    raise NotImplementedError


def tokenize_financial(
    text: str,
    method: str = "wordpiece",
) -> list[str]:
    """Financial-aware tokenization.

    Handles ticker symbols (``$AAPL``), monetary amounts (``$1.5B``),
    percentages, dates, and common financial abbreviations without
    splitting them incorrectly.

    Parameters
    ----------
    text : str
        Input text.
    method : str
        Tokenization method: ``"wordpiece"``, ``"bpe"``, or
        ``"whitespace"``.

    Returns
    -------
    list[str]
        List of tokens.
    """
    # TODO: implement — pre-process financial-specific patterns
    # (tickers, currency amounts, percentages) to protect them from
    # sub-word splitting, then apply the chosen tokenizer.
    raise NotImplementedError


def build_financial_stopwords(
    base: str = "english",
    additions: list[str] | None = None,
) -> set[str]:
    """Build a domain-adapted stopword list for financial text.

    Starts from a standard stopword list and adds financial
    boilerplate terms (e.g. ``"pursuant"``, ``"herein"``,
    ``"thereof"``).

    Parameters
    ----------
    base : str
        Base stopword language (``"english"``).
    additions : list[str] | None
        Additional stopwords to include.

    Returns
    -------
    set[str]
        Combined set of stopwords.
    """
    # TODO: implement — load base stopwords from NLTK or spaCy,
    # add curated financial boilerplate words (from SEC filings),
    # merge with user-supplied additions, and return as a set.
    raise NotImplementedError
