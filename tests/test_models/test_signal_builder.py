"""Tests for trading signal construction from NLP outputs.

Covers temporal aggregation, signal normalization, signal combination,
and look-ahead bias detection.
"""


def test_sentiment_signal_aggregate(sample_sentiment_scores):
    """Test temporal aggregation of raw sentiment scores."""
    pass


def test_signal_normalization_zscore(sample_sentiment_scores):
    """Test z-score normalization produces zero mean, unit variance."""
    pass


def test_combine_signals():
    """Test weighted signal combination."""
    pass


def test_check_lookahead_bias():
    """Test look-ahead bias detection in signal construction."""
    pass


def test_align_to_market_time(sample_sentiment_scores):
    """Test signal alignment to market trading calendar."""
    pass
