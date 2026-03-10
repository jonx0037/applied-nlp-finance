"""Tests for backtesting framework.

Covers signal backtesting, walk-forward validation,
purged cross-validation, and result container.
"""


def test_signal_backtester_run(sample_sentiment_scores, sample_returns):
    """Test basic backtest execution."""
    pass


def test_walk_forward_validation(sample_returns):
    """Test walk-forward validation produces correct number of folds."""
    pass


def test_purged_kfold_cv_no_leakage():
    """Test that purged k-fold CV prevents information leakage."""
    pass


def test_backtest_result_metrics(sample_returns):
    """Test BacktestResult computes standard performance metrics."""
    pass
