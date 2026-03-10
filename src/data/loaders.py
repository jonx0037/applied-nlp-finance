"""Standardized data loading utilities for financial text datasets."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Callable

import pandas as pd


def load_dataset(
    name: str,
    split: str = "train",
    *,
    cache_dir: Path | None = None,
) -> pd.DataFrame:
    """Load a named financial text dataset (FiQA, SEntFiN, etc.).

    Provides a unified interface for loading well-known financial NLP
    benchmark datasets. Datasets are downloaded and cached on first use.

    Parameters
    ----------
    name : str
        Dataset name. Supported: ``"fiqa"``, ``"sentfin"``,
        ``"financial_phrasebank"``, ``"fpb"``, ``"stocktwits"``.
    split : str
        Dataset split (``"train"``, ``"validation"``, ``"test"``).
    cache_dir : Path | None
        Directory for caching downloaded datasets.

    Returns
    -------
    pd.DataFrame
        DataFrame with at least ``"text"`` and ``"label"`` columns.
    """
    # TODO: implement — map dataset names to Hugging Face Hub identifiers
    # or custom download URLs, fetch if not cached, convert to DataFrame,
    # and apply standard column naming conventions.
    raise NotImplementedError


def load_filings(
    path: Path,
    filing_type: str = "10-K",
) -> pd.DataFrame:
    """Load preprocessed SEC filings from disk.

    Parameters
    ----------
    path : Path
        Directory or file path containing filing data (CSV/Parquet).
    filing_type : str
        Filter by filing type. Defaults to ``"10-K"``.

    Returns
    -------
    pd.DataFrame
        DataFrame with columns: ``"accession_number"``, ``"ticker"``,
        ``"filing_date"``, ``"filing_type"``, ``"text"``, ``"sections"``.
    """
    # TODO: implement — read files from the path, filter by filing_type,
    # parse dates, and return a standardised DataFrame.
    raise NotImplementedError


def load_transcripts(path: Path) -> pd.DataFrame:
    """Load earnings call transcripts from disk.

    Parameters
    ----------
    path : Path
        Directory or file containing transcript data.

    Returns
    -------
    pd.DataFrame
        DataFrame with columns: ``"ticker"``, ``"date"``, ``"quarter"``,
        ``"year"``, ``"prepared_remarks"``, ``"qa_section"``,
        ``"full_text"``.
    """
    # TODO: implement — read transcript files (JSON/CSV/Parquet),
    # normalise schema, and return a standardised DataFrame.
    raise NotImplementedError


def load_news(
    path: Path,
    source: str | None = None,
) -> pd.DataFrame:
    """Load news articles with optional source filtering.

    Parameters
    ----------
    path : Path
        Directory or file containing news data.
    source : str | None
        Optional filter by news source name.

    Returns
    -------
    pd.DataFrame
        DataFrame with columns: ``"title"``, ``"source"``,
        ``"published_at"``, ``"url"``, ``"content"``, ``"description"``.
    """
    # TODO: implement — read news data files, optionally filter by
    # source, parse dates, and return a standardised DataFrame.
    raise NotImplementedError


class DataRegistry:
    """Registry of available datasets with metadata.

    Provides a central registry for discovering and loading datasets
    used throughout the book's examples. Custom datasets can be
    registered alongside the built-in ones.

    Examples
    --------
    >>> registry = DataRegistry()
    >>> registry.register("my_dataset", loader_fn=my_loader, metadata={"size": 1000})
    >>> df = registry.get("my_dataset")
    """

    def __init__(self) -> None:
        # TODO: implement — initialise internal storage for registered
        # datasets and pre-register built-in financial datasets.
        self._registry: dict[str, dict[str, Any]] = {}

    def register(
        self,
        name: str,
        loader_fn: Callable[..., pd.DataFrame],
        metadata: dict[str, Any] | None = None,
    ) -> None:
        """Register a dataset with its loader function and metadata.

        Parameters
        ----------
        name : str
            Unique dataset name.
        loader_fn : Callable[..., pd.DataFrame]
            Callable that returns a DataFrame when invoked.
        metadata : dict[str, Any] | None
            Optional metadata (description, size, source URL, etc.).
        """
        # TODO: implement — validate inputs, store in internal registry,
        # raise ValueError on duplicate names unless overwrite=True.
        raise NotImplementedError

    def list_datasets(self) -> list[str]:
        """List all registered dataset names.

        Returns
        -------
        list[str]
            Sorted list of registered dataset names.
        """
        # TODO: implement — return sorted list of keys from the registry.
        raise NotImplementedError

    def get(self, name: str, **kwargs: Any) -> pd.DataFrame:
        """Load and return a registered dataset by name.

        Parameters
        ----------
        name : str
            Name of the registered dataset.
        **kwargs
            Additional keyword arguments passed to the loader function.

        Returns
        -------
        pd.DataFrame
            The loaded dataset.

        Raises
        ------
        KeyError
            If the dataset name is not registered.
        """
        # TODO: implement — look up the loader function in the registry,
        # call it with any kwargs, and return the result.
        raise NotImplementedError
