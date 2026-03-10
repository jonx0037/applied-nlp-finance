"""Shared test fixtures for applied-nlp-finance test suite.

Provides sample data, model stubs, and common test utilities
used across multiple test modules.
"""

import pytest
import pandas as pd
import numpy as np


@pytest.fixture
def sample_financial_text():
    """Sample financial text for testing NLP pipelines."""
    return (
        "The company reported strong Q3 earnings, with revenue increasing 15% "
        "year-over-year to $2.3 billion. Management expressed confidence in the "
        "full-year outlook despite ongoing macroeconomic headwinds."
    )


@pytest.fixture
def sample_sentiment_scores():
    """Sample sentiment score time series for testing signal construction."""
    dates = pd.date_range("2024-01-01", periods=100, freq="B")
    scores = pd.Series(np.random.randn(100) * 0.3, index=dates, name="sentiment")
    return scores


@pytest.fixture
def sample_returns():
    """Sample daily return series for backtesting tests."""
    dates = pd.date_range("2024-01-01", periods=100, freq="B")
    returns = pd.Series(np.random.randn(100) * 0.01, index=dates, name="returns")
    return returns


@pytest.fixture
def sample_filing_text():
    """Sample SEC filing excerpt for entity extraction and preprocessing tests."""
    return (
        "ITEM 1A. RISK FACTORS\n\n"
        "The following risk factors could materially affect our business. "
        "Apple Inc. (AAPL) is a significant customer representing approximately "
        "12% of our total revenue. Any reduction in orders from Apple could "
        "adversely impact our financial results. Our supply chain depends on "
        "Taiwan Semiconductor Manufacturing Company (TSMC) for chip fabrication."
    )


@pytest.fixture
def sample_entities():
    """Sample extracted entities for knowledge graph tests."""
    return [
        {"text": "Apple Inc.", "type": "COMPANY", "id": "AAPL"},
        {"text": "TSMC", "type": "COMPANY", "id": "TSM"},
        {"text": "Tim Cook", "type": "PERSON", "role": "CEO"},
    ]
