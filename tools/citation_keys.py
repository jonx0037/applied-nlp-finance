"""Citation key generation for *Applied NLP for Finance*.

Pure functions only — no I/O, no side effects. Convention documented in
``manuscript/99_bibliography/CITATIONS.md``.

Public API
----------
ascii_fold(s) : Fold accents to ASCII, lowercase, strip non-alphanumeric except ``_``.
surname(author) : Extract surname from a BibTeX-form author string.
title_keyword(title) : Pick the first non-stopword from a title (for collision disambiguation).
generate_key(authors, year, ...) : Generate a citation key per the project convention.
"""

from __future__ import annotations

import re
import unicodedata

# Common stopwords skipped when picking a title keyword for collision disambiguation.
TITLE_STOPWORDS: frozenset[str] = frozenset(
    {
        "a", "an", "the",
        "and", "or", "but", "nor", "yet", "so",
        "of", "in", "on", "at", "by", "for", "to", "from", "with", "as", "into",
        "is", "are", "was", "were", "be", "been", "being",
        "this", "that", "these", "those",
    }
)

# Words that strongly suggest an organizational (rather than personal) author.
_ORG_SIGNALS: frozenset[str] = frozenset(
    {
        "commission", "bank", "department", "ministry", "office", "bureau",
        "federation", "association", "society", "institute", "fund", "corporation",
        "company", "council", "board", "authority", "system", "service", "agency",
        "reserve", "treasury", "exchange",
    }
)


def ascii_fold(text: str) -> str:
    """Fold a string to lowercase ASCII suitable for a citation key fragment.

    Accents are decomposed and dropped; apostrophes, hyphens, and other
    non-alphanumeric characters are removed; the result is lowercased.
    Underscores are preserved (they are the key separator).

    Examples
    --------
    >>> ascii_fold("García")
    'garcia'
    >>> ascii_fold("O'Reilly")
    'oreilly'
    >>> ascii_fold("Saar-Tsechansky")
    'saartsechansky'
    >>> ascii_fold("François")
    'francois'
    >>> ascii_fold("loughran_mcdonald")
    'loughran_mcdonald'
    """
    folded = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9_]", "", folded.lower())


def surname(author: str) -> str:
    """Extract the folded surname from an author name.

    Accepts BibTeX ``Last, First`` form (preferred) or ``First Last`` (fallback).
    Particles like "Van Der", "de la", and "von" are joined with the surname so
    the resulting key stays distinctive — ``Van Der Berg`` → ``vanderberg``.

    Examples
    --------
    >>> surname("Fama, Eugene F.")
    'fama'
    >>> surname("García, Diego")
    'garcia'
    >>> surname("Van Der Berg, Maria")
    'vanderberg'
    >>> surname("McDonald, Bill")
    'mcdonald'
    """
    name = author.strip()
    if not name:
        return ""
    last = name.split(",", 1)[0] if "," in name else name.rsplit(" ", 1)[-1]
    return ascii_fold(last)


def _is_organizational(author: str) -> bool:
    """Heuristic: organizational authors lack a comma and contain institution words."""
    if "," in author:
        return False
    tokens = {w.lower() for w in re.findall(r"[A-Za-z]+", author)}
    return bool(_ORG_SIGNALS & tokens)


def _organizational_key(author: str) -> str:
    """Generate a short key from an organizational author name.

    Strategy:
      1. If the author contains a parenthetical abbreviation, use that.
         ``Financial Industry Regulatory Authority (FINRA)`` → ``finra``
      2. Otherwise, take initials of significant (non-stopword) words.
         ``Securities and Exchange Commission`` → ``sec``

    Examples
    --------
    >>> _organizational_key("Securities and Exchange Commission")
    'sec'
    >>> _organizational_key("Financial Industry Regulatory Authority (FINRA)")
    'finra'
    >>> _organizational_key("Alternative Investment Management Association (AIMA)")
    'aima'
    """
    paren_match = re.search(r"\(([A-Z][A-Za-z0-9]+)\)", author)
    if paren_match:
        return ascii_fold(paren_match.group(1).lower())

    # Strip any trailing parenthetical content so it doesn't bias the initials
    base = re.sub(r"\s*\([^)]*\)\s*$", "", author).strip()
    significant_words = [
        w for w in re.findall(r"[A-Za-z]+", base) if w.lower() not in TITLE_STOPWORDS
    ]
    initials = "".join(w[0] for w in significant_words).lower()
    return ascii_fold(initials) or ascii_fold(base.replace(" ", ""))


def title_keyword(title: str) -> str:
    """Pick the first non-stopword word of a title, folded — for disambiguation.

    The main title (before any colon) is preferred over subtitle, because
    distinguishers usually live in the main title.

    Examples
    --------
    >>> title_keyword("Prospect Theory: An Analysis of Decision under Risk")
    'prospect'
    >>> title_keyword("The Framing of Decisions and the Psychology of Choice")
    'framing'
    >>> title_keyword("On the Impossibility of Informationally Efficient Markets")
    'impossibility'
    >>> title_keyword("A Survey of Deep Learning for Finance")
    'survey'
    """
    main = title.split(":", 1)[0]
    words = re.findall(r"[A-Za-z]+", main)
    for word in words:
        if word.lower() not in TITLE_STOPWORDS:
            return ascii_fold(word)
    return ascii_fold(words[0]) if words else ""


def generate_key(
    authors: list[str],
    year: int,
    title: str = "",
    *,
    disambiguator: str | None = None,
) -> str:
    """Generate a citation key per the project's convention.

    Parameters
    ----------
    authors
        Author names in BibTeX ``Last, First`` form. Must be non-empty.
    year
        Publication year as an integer.
    title
        Title of the work. Used only when ``disambiguator='title'`` is requested.
    disambiguator
        Optional disambiguator to append after the year:

        * ``None`` (default) — no disambiguator; produces the base key.
        * ``'title'`` — append the first non-stopword from ``title``.
        * any other string — append the literal string, ASCII-folded.

    Returns
    -------
    str
        A lowercase, underscore-separated citation key.

    Raises
    ------
    ValueError
        If ``authors`` is empty.

    Examples
    --------
    >>> generate_key(["Fama, Eugene F."], 1970)
    'fama_1970'
    >>> generate_key(["Loughran, Tim", "McDonald, Bill"], 2011)
    'loughran_mcdonald_2011'
    >>> generate_key(["Gentzkow, Matthew", "Kelly, Bryan", "Taddy, Matt"], 2019)
    'gentzkow_etal_2019'
    >>> generate_key(["García, Diego"], 2013)
    'garcia_2013'
    >>> generate_key(
    ...     ["Kahneman, Daniel", "Tversky, Amos"],
    ...     1979,
    ...     title="Prospect Theory: An Analysis of Decision under Risk",
    ...     disambiguator="title",
    ... )
    'kahneman_tversky_1979_prospect'
    >>> generate_key(["Securities and Exchange Commission"], 2025)
    'sec_2025'
    """
    if not authors:
        raise ValueError("At least one author is required to generate a citation key")

    # "others" is the BibTeX marker for truncated "et al." — treat as 3+ authors.
    has_others = any(a.strip().lower() == "others" for a in authors)

    if len(authors) == 1 and _is_organizational(authors[0]):
        base = _organizational_key(authors[0])
    elif len(authors) == 1:
        base = surname(authors[0])
    elif has_others or len(authors) > 2:
        base = f"{surname(authors[0])}_etal"
    else:
        base = f"{surname(authors[0])}_{surname(authors[1])}"

    key = f"{base}_{year}"

    if disambiguator == "title":
        kw = title_keyword(title)
        if kw:
            key = f"{key}_{kw}"
    elif disambiguator:
        key = f"{key}_{ascii_fold(disambiguator)}"

    return key.lower()
