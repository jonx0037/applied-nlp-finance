"""Backtesting framework for NLP-based trading strategies."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

import pandas as pd


@dataclass
class BacktestResult:
    """Container for backtest results.

    Attributes
    ----------
    returns : pd.Series
        Strategy return series.
    positions : pd.Series
        Position series over time.
    metrics : dict[str, float]
        Summary performance metrics (Sharpe, Calmar, max drawdown,
        hit rate, etc.).
    drawdown_series : pd.Series
        Running drawdown series.
    """

    returns: pd.Series
    positions: pd.Series
    metrics: dict[str, float] = field(default_factory=dict)
    drawdown_series: pd.Series = field(default_factory=lambda: pd.Series(dtype=float))


class SignalBacktester:
    """Backtest text-derived trading signals.

    Simulates a long/short strategy driven by NLP-derived signals,
    accounting for transaction costs, slippage, and position sizing.

    Parameters
    ----------
    initial_capital : float
        Starting capital in USD. Defaults to ``1_000_000``.
    transaction_cost_bps : float
        Round-trip transaction cost in basis points. Defaults to ``5.0``.

    Examples
    --------
    >>> bt = SignalBacktester(initial_capital=1_000_000, transaction_cost_bps=5.0)
    >>> result = bt.run(signal=my_signal, returns=market_returns)
    >>> print(result.metrics["sharpe_ratio"])
    """

    def __init__(
        self,
        initial_capital: float = 1_000_000,
        transaction_cost_bps: float = 5.0,
    ) -> None:
        # TODO: implement — store configuration, set up internal
        # accounting structures for capital, positions, and PnL.
        self.initial_capital = initial_capital
        self.transaction_cost_bps = transaction_cost_bps

    def run(
        self,
        signal: pd.Series,
        returns: pd.Series,
        *,
        position_sizing: str = "equal_weight",
        max_position: float = 1.0,
        rebalance_freq: str = "daily",
    ) -> BacktestResult:
        """Execute a backtest.

        Parameters
        ----------
        signal : pd.Series
            Trading signal indexed by date. Positive values indicate
            long positions, negative values indicate short positions.
        returns : pd.Series
            Asset returns indexed by date (same index as ``signal``).
        position_sizing : str
            Method for sizing positions: ``"equal_weight"``,
            ``"signal_proportional"``, ``"volatility_scaled"``.
        max_position : float
            Maximum absolute position size (as fraction of capital).
        rebalance_freq : str
            Rebalancing frequency (``"daily"``, ``"weekly"``,
            ``"monthly"``).

        Returns
        -------
        BacktestResult
            Backtest results with returns, positions, and metrics.
        """
        # TODO: implement — align signal and returns, convert signal
        # to positions using the sizing method, apply max position
        # constraints, compute PnL net of transaction costs at each
        # rebalance, compute cumulative returns and drawdowns,
        # calculate summary metrics, and return a BacktestResult.
        raise NotImplementedError

    def walk_forward(
        self,
        signal_fn: Callable[..., pd.Series],
        data: pd.DataFrame,
        train_window: int,
        test_window: int,
        *,
        step_size: int | None = None,
    ) -> list[BacktestResult]:
        """Walk-forward validation of a signal generation function.

        Trains the signal model on a rolling window and tests on the
        subsequent out-of-sample period.

        Parameters
        ----------
        signal_fn : Callable[..., pd.Series]
            Function that takes training data and produces a signal
            for the test period.
        data : pd.DataFrame
            Full dataset with features and returns.
        train_window : int
            Number of periods in each training window.
        test_window : int
            Number of periods in each test window.
        step_size : int | None
            Step size between windows. Defaults to ``test_window``.

        Returns
        -------
        list[BacktestResult]
            One :class:`BacktestResult` per walk-forward fold.
        """
        # TODO: implement — split data into rolling train/test
        # windows, call signal_fn on each training window, run
        # backtest on each test window, collect results.
        raise NotImplementedError


def purged_kfold_cv(
    data: pd.DataFrame,
    n_splits: int,
    embargo_pct: float,
) -> list[tuple]:
    """Purged k-fold cross-validation splits for time-series.

    Implements the purged k-fold method from Marcos Lopez de Prado's
    *Advances in Financial Machine Learning*, ensuring no information
    leakage between train and test sets.

    Parameters
    ----------
    data : pd.DataFrame
        Time-series data indexed by date.
    n_splits : int
        Number of cross-validation folds.
    embargo_pct : float
        Fraction of data to embargo (exclude) between train and test
        sets to prevent leakage from overlapping labels.

    Returns
    -------
    list[tuple]
        List of ``(train_indices, test_indices)`` tuples.
    """
    # TODO: implement — divide data into n_splits groups, for each
    # fold designate one group as test, purge any training samples
    # that overlap with test labels, add an embargo gap after each
    # test set boundary, and return the index arrays.
    raise NotImplementedError
