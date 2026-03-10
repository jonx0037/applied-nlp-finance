"""Configuration management for the applied-nlp-finance package."""

from __future__ import annotations

from pathlib import Path
from typing import Any


class Config:
    """Project-wide configuration.

    Loads configuration from a YAML or TOML file and provides
    convenient access to common paths and settings. Supports
    dot-notation key lookup for nested values.

    Parameters
    ----------
    config_path : Path | None
        Path to a YAML or TOML configuration file. If ``None``,
        searches for ``config.yaml`` or ``pyproject.toml`` in the
        project root, falling back to sensible defaults.

    Examples
    --------
    >>> cfg = Config()
    >>> cfg.data_dir
    PosixPath('/path/to/project/data')
    >>> cfg.get("models.finbert.batch_size", default=32)
    32
    """

    def __init__(self, config_path: Path | None = None) -> None:
        # TODO: implement — if config_path is provided, load from it
        # (detect YAML vs TOML by extension). Otherwise, search for
        # config files in the project root. Merge loaded config with
        # default values. Store the merged config as a nested dict.
        self._config_path = config_path
        self._data: dict[str, Any] = {}

    def get(self, key: str, default: Any = None) -> Any:
        """Get a config value with dot-notation support.

        Parameters
        ----------
        key : str
            Dot-separated key path (e.g. ``"models.finbert.device"``).
        default : Any
            Value to return if the key is not found.

        Returns
        -------
        Any
            The configuration value, or ``default`` if not found.
        """
        # TODO: implement — split key by ".", traverse the nested
        # config dict, return the value or default.
        raise NotImplementedError

    @property
    def data_dir(self) -> Path:
        """Path to the project data directory.

        Returns
        -------
        Path
            Defaults to ``<project_root>/data``.
        """
        # TODO: implement — return the configured data directory,
        # creating it if it does not exist.
        raise NotImplementedError

    @property
    def model_dir(self) -> Path:
        """Path to the model artifacts directory.

        Returns
        -------
        Path
            Defaults to ``<project_root>/models``.
        """
        # TODO: implement — return the configured model directory,
        # creating it if it does not exist.
        raise NotImplementedError

    @property
    def cache_dir(self) -> Path:
        """Path to the cache directory.

        Returns
        -------
        Path
            Defaults to ``<project_root>/.cache``.
        """
        # TODO: implement — return the configured cache directory,
        # creating it if it does not exist.
        raise NotImplementedError


def get_api_key(service: str) -> str:
    """Retrieve an API key from environment variables or a ``.env`` file.

    Looks for the key in the following order:
    1. Environment variable ``<SERVICE>_API_KEY`` (upper-cased).
    2. A ``.env`` file in the project root.

    Parameters
    ----------
    service : str
        Service name (e.g. ``"openai"``, ``"newsapi"``, ``"reddit"``).

    Returns
    -------
    str
        The API key.

    Raises
    ------
    ValueError
        If the API key cannot be found.
    """
    # TODO: implement — check os.environ for the uppercased key name,
    # fall back to loading from a .env file using python-dotenv,
    # raise ValueError if not found.
    raise NotImplementedError


def get_project_root() -> Path:
    """Find the project root directory.

    Walks up from the current file's directory until it finds a
    directory containing ``pyproject.toml``, ``setup.py``, or ``.git``.

    Returns
    -------
    Path
        Absolute path to the project root.

    Raises
    ------
    FileNotFoundError
        If no project root marker is found.
    """
    # TODO: implement — start from Path(__file__).resolve().parent,
    # walk up the directory tree checking for marker files, return
    # the first directory that contains one.
    raise NotImplementedError
