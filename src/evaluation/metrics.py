"""NLP and financial evaluation metrics."""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd


def sharpe_ratio(
    returns: pd.Series,
    risk_free_rate: float = 0.0,
    annualize: bool = True,
) -> float:
    """Calculate the annualized Sharpe ratio.

    Parameters
    ----------
    returns : pd.Series
        Period returns (daily, weekly, etc.).
    risk_free_rate : float
        Risk-free rate (annualized). Defaults to ``0.0``.
    annualize : bool
        Whether to annualize the ratio. Assumes 252 trading days
        if the index is daily.

    Returns
    -------
    float
        The Sharpe ratio.
    """
    # TODO: implement — compute excess returns over the risk-free rate,
    # calculate mean and standard deviation, optionally annualize
    # using sqrt(252) for daily data, and return the ratio.
    raise NotImplementedError


def calmar_ratio(returns: pd.Series) -> float:
    """Calculate the Calmar ratio (annualized return / max drawdown).

    Parameters
    ----------
    returns : pd.Series
        Period returns.

    Returns
    -------
    float
        The Calmar ratio.
    """
    # TODO: implement — compute annualized return and maximum drawdown,
    # return the ratio. Handle the case where max drawdown is zero.
    raise NotImplementedError


def information_ratio(
    returns: pd.Series,
    benchmark_returns: pd.Series,
) -> float:
    """Calculate the Information Ratio relative to a benchmark.

    Parameters
    ----------
    returns : pd.Series
        Strategy returns.
    benchmark_returns : pd.Series
        Benchmark returns (same frequency and index).

    Returns
    -------
    float
        The Information Ratio.
    """
    # TODO: implement — compute active returns (strategy - benchmark),
    # calculate mean and tracking error of active returns, return
    # the annualized ratio.
    raise NotImplementedError


def max_drawdown(returns: pd.Series) -> float:
    """Calculate the maximum drawdown from peak to trough.

    Parameters
    ----------
    returns : pd.Series
        Period returns.

    Returns
    -------
    float
        Maximum drawdown as a positive fraction (e.g. ``0.25`` for 25%).
    """
    # TODO: implement — compute cumulative wealth curve, track the
    # running maximum, compute drawdown at each point, and return
    # the maximum drawdown.
    raise NotImplementedError


def hit_rate(
    predictions: pd.Series,
    actuals: pd.Series,
) -> float:
    """Calculate the hit rate (accuracy) of directional predictions.

    Parameters
    ----------
    predictions : pd.Series
        Predicted values or signals.
    actuals : pd.Series
        Actual realised values.

    Returns
    -------
    float
        Fraction of correct directional predictions.
    """
    # TODO: implement — compare the sign of predictions with the sign
    # of actuals, compute the fraction that match.
    raise NotImplementedError


def directional_accuracy(
    signal: pd.Series,
    returns: pd.Series,
) -> float:
    """Calculate directional accuracy of a signal against forward returns.

    Parameters
    ----------
    signal : pd.Series
        Trading signal (positive = long, negative = short).
    returns : pd.Series
        Forward returns.

    Returns
    -------
    float
        Fraction of periods where signal direction matches return
        direction.
    """
    # TODO: implement — align signal and returns, compare signs,
    # compute the accuracy. Handle zero-signal and zero-return cases.
    raise NotImplementedError


def nlp_classification_report(
    y_true: Any,
    y_pred: Any,
    labels: list[str] | None = None,
) -> dict:
    """Classification metrics tailored for financial sentiment.

    Computes per-class and aggregate metrics including precision,
    recall, F1, and financial-specific metrics like the cost-weighted
    accuracy that penalises misclassifying positive sentiment as
    negative (and vice versa) more heavily than confusing either with
    neutral.

    Parameters
    ----------
    y_true : array-like
        True labels.
    y_pred : array-like
        Predicted labels.
    labels : list[str] | None
        Label names. Defaults to ``["positive", "negative", "neutral"]``.

    Returns
    -------
    dict
        Nested dict with per-class metrics and macro/weighted averages,
        plus a ``"confusion_matrix"`` and ``"cost_weighted_accuracy"``.
    """
    # TODO: implement — compute sklearn classification_report metrics,
    # build confusion matrix, compute cost-weighted accuracy using a
    # financial cost matrix where positive/negative confusion is more
    # costly than neutral confusion.
    raise NotImplementedError


def signal_decay_analysis(
    signal: pd.Series,
    returns: pd.Series,
    horizons: list[int],
) -> pd.DataFrame:
    """Analyze how signal predictiveness decays over different horizons.

    Computes the correlation (IC) and rank correlation (Rank IC) between
    the signal and forward returns at various look-ahead horizons.

    Parameters
    ----------
    signal : pd.Series
        Trading signal indexed by date.
    returns : pd.Series
        Asset returns indexed by date.
    horizons : list[int]
        List of forward return horizons (in periods) to evaluate.

    Returns
    -------
    pd.DataFrame
        DataFrame indexed by horizon with columns: ``"ic"`` (Pearson
        correlation), ``"rank_ic"`` (Spearman correlation),
        ``"ic_t_stat"`` (t-statistic), ``"hit_rate"``.
    """
    # TODO: implement — for each horizon, compute forward returns
    # at that lag, align with the signal, compute IC, Rank IC,
    # t-statistic, and hit rate. Return as a DataFrame.
    raise NotImplementedError
