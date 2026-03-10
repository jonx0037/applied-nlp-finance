"""Named Entity Recognition (NER) for financial entities."""

from __future__ import annotations

from typing import Any

import pandas as pd


class FinancialNER:
    """Financial entity extraction pipeline.

    Wraps a spaCy NER model with custom patterns for financial entities
    such as companies, people, instruments, CUSIPs, ISINs, and LEIs.
    Supports both pretrained transformer-based models and rule-based
    pattern matching.

    Parameters
    ----------
    model : str
        spaCy model name. Defaults to ``"en_core_web_trf"`` for
        transformer-based NER.
    custom_patterns : list[dict] | None
        Additional entity patterns for the spaCy EntityRuler.
        Each dict should have ``"label"`` and ``"pattern"`` keys.

    Examples
    --------
    >>> ner = FinancialNER()
    >>> entities = ner.extract_entities("Apple reported Q4 revenue of $89.5B")
    >>> entities[0]["text"]
    'Apple'
    """

    def __init__(
        self,
        model: str = "en_core_web_trf",
        custom_patterns: list[dict] | None = None,
    ) -> None:
        # TODO: implement — load the spaCy model, add an EntityRuler
        # with financial patterns (ticker symbols, CUSIPs, ISINs,
        # monetary amounts, etc.), merge with custom_patterns if
        # provided.
        self.model_name = model
        self.custom_patterns = custom_patterns
        self._nlp: Any = None

    def extract_entities(self, text: str) -> list[dict]:
        """Extract financial entities from text.

        Parameters
        ----------
        text : str
            Input text (news article, filing excerpt, transcript, etc.).

        Returns
        -------
        list[dict]
            List of entity dicts with keys: ``"text"``, ``"label"``
            (e.g. ``"ORG"``, ``"PERSON"``, ``"MONEY"``, ``"TICKER"``,
            ``"CUSIP"``), ``"start"`` (char offset), ``"end"`` (char
            offset), ``"confidence"`` (float, if available).
        """
        # TODO: implement — run the spaCy pipeline on the text,
        # extract entities from doc.ents, add custom entity types
        # from the EntityRuler, and return structured results.
        raise NotImplementedError

    def extract_from_filing(self, filing_text: str) -> list[dict]:
        """Filing-specific entity extraction with CUSIP/LEI resolution.

        Applies specialized extraction logic for SEC filings, including
        CUSIP number detection, LEI resolution, and cross-referencing
        of entity mentions with the filing's cover page metadata.

        Parameters
        ----------
        filing_text : str
            Full or sectioned filing text.

        Returns
        -------
        list[dict]
            Entities with additional ``"cusip"``, ``"lei"``, and
            ``"cik"`` fields where resolvable.
        """
        # TODO: implement — extract entities using extract_entities(),
        # apply regex patterns for CUSIP (9-char alphanumeric) and
        # LEI (20-char alphanumeric) identifiers, cross-reference
        # with SEC EDGAR company lookup, and enrich entity records.
        raise NotImplementedError

    def disambiguate(self, entity: str, context: str) -> dict:
        """Resolve ambiguous entities using context.

        For example, disambiguate "Apple" as Apple Inc. (technology
        company) vs. an apple (fruit) based on surrounding text.

        Parameters
        ----------
        entity : str
            The ambiguous entity mention.
        context : str
            Surrounding text for disambiguation.

        Returns
        -------
        dict
            Resolved entity with ``"canonical_name"``, ``"entity_type"``,
            ``"confidence"``, and ``"alternative_interpretations"`` keys.
        """
        # TODO: implement — use context embeddings or a lightweight
        # classifier to determine the most likely entity interpretation.
        # Consider knowledge base lookups and co-occurrence statistics.
        raise NotImplementedError


class TickerResolver:
    """Resolve ticker symbols and company names to canonical identifiers.

    Maps free-text mentions of companies (e.g. ``"Apple"``, ``"AAPL"``,
    ``"Apple Inc."``) to canonical identifiers including ticker symbol,
    CIK, and FIGI.

    Parameters
    ----------
    reference_data : pd.DataFrame | None
        Reference table with columns ``"ticker"``, ``"company_name"``,
        ``"aliases"``, ``"cik"``, ``"figi"``. If ``None``, a default
        reference dataset is loaded.
    """

    def __init__(
        self,
        reference_data: pd.DataFrame | None = None,
    ) -> None:
        # TODO: implement — load reference data (from bundled CSV or
        # user-provided DataFrame), build a fuzzy matching index
        # using aliases and company names.
        self.reference_data = reference_data
        self._index: Any = None

    def resolve(
        self,
        mention: str,
        context: str | None = None,
    ) -> dict | None:
        """Resolve a mention to a canonical entity.

        Parameters
        ----------
        mention : str
            A company name or ticker mention from text.
        context : str | None
            Optional surrounding text to help disambiguation.

        Returns
        -------
        dict | None
            Resolved entity with ``"ticker"``, ``"company_name"``,
            ``"cik"``, ``"figi"``, ``"confidence"`` keys, or ``None``
            if no match is found.
        """
        # TODO: implement — first try exact match on ticker/name,
        # then fuzzy match on aliases, optionally use context for
        # disambiguation, and return the best match with confidence
        # score.
        raise NotImplementedError
