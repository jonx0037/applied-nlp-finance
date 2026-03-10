"""Logging configuration for the applied-nlp-finance package."""

from __future__ import annotations

import logging
from pathlib import Path


def setup_logger(
    name: str,
    level: str = "INFO",
    log_file: Path | None = None,
    *,
    fmt: str = "%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    datefmt: str = "%Y-%m-%d %H:%M:%S",
) -> logging.Logger:
    """Configure a logger with console and optional file output.

    Creates a logger with a consistent format for the applied-nlp-finance
    package. Supports both console (stderr) and file handlers.

    Parameters
    ----------
    name : str
        Logger name (typically ``__name__`` of the calling module).
    level : str
        Logging level (``"DEBUG"``, ``"INFO"``, ``"WARNING"``,
        ``"ERROR"``, ``"CRITICAL"``). Defaults to ``"INFO"``.
    log_file : Path | None
        Optional path to a log file. If provided, a ``FileHandler``
        is added in addition to the console handler.
    fmt : str
        Log message format string.
    datefmt : str
        Date format string for log timestamps.

    Returns
    -------
    logging.Logger
        Configured logger instance.

    Examples
    --------
    >>> logger = setup_logger("my_module", level="DEBUG")
    >>> logger.info("Processing started")
    """
    # TODO: implement — create or retrieve the named logger, set the
    # level, create a Formatter with the given fmt/datefmt, add a
    # StreamHandler for console output, optionally add a FileHandler,
    # avoid duplicate handlers if called multiple times, and return
    # the logger.
    raise NotImplementedError


def get_logger(name: str) -> logging.Logger:
    """Get or create a logger by name.

    Convenience wrapper that returns an existing logger if already
    configured, or creates a new one with default settings.

    Parameters
    ----------
    name : str
        Logger name (typically ``__name__``).

    Returns
    -------
    logging.Logger
        Logger instance. If not previously configured via
        :func:`setup_logger`, a logger with ``"INFO"`` level and
        console output is returned.
    """
    # TODO: implement — check if a logger with the given name already
    # has handlers configured. If so, return it directly. Otherwise,
    # call setup_logger with default parameters and return.
    raise NotImplementedError
