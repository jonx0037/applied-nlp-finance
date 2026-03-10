"""Signal construction from NLP model outputs for trading systems."""

from __future__ import annotations

import pandas as pd


class SentimentSignal:
    """Convert raw sentiment scores to tradeable signals.

    Implements temporal aggregation, normalisation, and multi-source
    combination of text-derived sentiment scores into signals suitable
    for systematic trading strategies.

    Parameters
    ----------
    aggregation : str
        Temporal aggregation method (``"ewm"``, ``"rolling_mean"``,
        ``"rolling_median"``). Defaults to ``"ewm"``.
    window : int
        Aggregation window in periods. Defaults to ``20``.
    zscore_window : int
        Window for z-score normalisation. Defaults to ``252`` (approx.
        one trading year).

    Examples
    --------
    >>> signal = SentimentSignal(aggregation="ewm", window=20)
    >>> raw = pd.Series([0.5, -0.2, 0.3], index=pd.date_range("2024-01-01", periods=3))
    >>> aggregated = signal.aggregate(raw, raw.index)
    """

    def __init__(
        self,
        aggregation: str = "ewm",
        window: int = 20,
        zscore_window: int = 252,
    ) -> None:
        # TODO: implement — validate aggregation method, store
        # configuration parameters.
        self.aggregation = aggregation
        self.window = window
        self.zscore_window = zscore_window

    def aggregate(
        self,
        scores: pd.Series,
        timestamps: pd.DatetimeIndex,
    ) -> pd.Series:
        """Apply temporal aggregation to raw sentiment scores.

        Parameters
        ----------
        scores : pd.Series
            Raw sentiment scores (e.g. from FinBERT or LLM).
        timestamps : pd.DatetimeIndex
            Timestamps corresponding to each score.

        Returns
        -------
        pd.Series
            Temporally smoothed signal.
        """
        # TODO: implement — align scores to timestamps, apply the
        # chosen aggregation method (EWM, rolling mean, etc.), and
        # return the smoothed series.
        raise NotImplementedError

    def normalize(
        self,
        signal: pd.Series,
        method: str = "zscore",
    ) -> pd.Series:
        """Normalize the aggregated signal.

        Parameters
        ----------
        signal : pd.Series
            Aggregated sentiment signal.
        method : str
            Normalisation method: ``"zscore"``, ``"minmax"``,
            ``"percentile"``.

        Returns
        -------
        pd.Series
            Normalized signal.
        """
        # TODO: implement — apply rolling z-score, min-max scaling,
        # or percentile ranking using the configured window.
        raise NotImplementedError

    def combine_signals(
        self,
        signals: dict[str, pd.Series],
        weights: dict[str, float] | None = None,
    ) -> pd.Series:
        """Combine multiple signal sources into a composite signal.

        Parameters
        ----------
        signals : dict[str, pd.Series]
            Mapping from signal name to signal series.
        weights : dict[str, float] | None
            Optional weights per signal. If ``None``, equal weights
            are used.

        Returns
        -------
        pd.Series
            Weighted composite signal.
        """
        # TODO: implement — align all signals on a common index,
        # apply weights (equal if not specified), compute weighted
        # sum, and return the composite signal.
        raise NotImplementedError


def align_to_market_time(
    signal: pd.Series,
    market_calendar: pd.DatetimeIndex,
) -> pd.Series:
    """Align a text-derived signal to the market trading calendar.

    Text events (news articles, filings) may arrive outside of market
    hours. This function maps each signal value to the next valid
    trading day to avoid look-ahead bias.

    Parameters
    ----------
    signal : pd.Series
        Text-derived signal indexed by event timestamp.
    market_calendar : pd.DatetimeIndex
        Index of valid trading days/times.

    Returns
    -------
    pd.Series
        Signal reindexed to market calendar timestamps.
    """
    # TODO: implement — for each signal timestamp, find the next
    # valid trading time using searchsorted or merge_asof. Handle
    # weekends, holidays, and pre/post-market events. Forward-fill
    # gaps where no new signal is available.
    raise NotImplementedError


def check_lookahead_bias(
    signal: pd.Series,
    event_times: pd.DatetimeIndex,
) -> dict:
    """Validate signal construction for look-ahead bias.

    Checks whether any signal values at time ``t`` could have been
    influenced by information that was not yet available at ``t``.

    Parameters
    ----------
    signal : pd.Series
        Constructed signal indexed by time.
    event_times : pd.DatetimeIndex
        Timestamps when the underlying events actually occurred
        (e.g. filing dates, article publication times).

    Returns
    -------
    dict
        Validation report with:
        - ``"has_bias"`` (bool): whether look-ahead bias was detected.
        - ``"violations"`` (list[dict]): details of each violation.
        - ``"fraction_biased"`` (float): proportion of biased samples.
        - ``"recommendation"`` (str): suggested fix.
    """
    # TODO: implement — compare each signal timestamp to the
    # corresponding event time, flag cases where signal_time <
    # event_time (signal is using future information), compute
    # summary statistics, and return the validation report.
    raise NotImplementedError
