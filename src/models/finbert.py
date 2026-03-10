"""FinBERT wrapper for financial sentiment analysis and fine-tuning."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np


class FinBERTClassifier:
    """Wrapper for FinBERT inference and fine-tuning.

    Provides a high-level interface around the ProsusAI/finbert model
    for financial sentiment analysis. Supports batch inference,
    probability outputs, fine-tuning on custom datasets, and
    model serialisation.

    Parameters
    ----------
    model_name : str
        Hugging Face model identifier. Defaults to ``"ProsusAI/finbert"``.
    device : str | None
        Device to run inference on (``"cpu"``, ``"cuda"``, ``"mps"``).
        If ``None``, automatically selects the best available device.

    Examples
    --------
    >>> clf = FinBERTClassifier()
    >>> results = clf.predict(["Revenue beat expectations by 15%"])
    >>> results[0]["label"]
    'positive'
    """

    def __init__(
        self,
        model_name: str = "ProsusAI/finbert",
        device: str | None = None,
    ) -> None:
        # TODO: implement — load the tokenizer and model from
        # Hugging Face Hub, move to the specified device, and set
        # the model to eval mode for inference.
        self.model_name = model_name
        self.device = device
        self._model: Any = None
        self._tokenizer: Any = None

    def predict(
        self,
        texts: list[str],
        batch_size: int = 32,
    ) -> list[dict]:
        """Return sentiment predictions with scores.

        Parameters
        ----------
        texts : list[str]
            List of financial text passages to classify.
        batch_size : int
            Number of texts to process per batch.

        Returns
        -------
        list[dict]
            Each dict contains: ``"label"`` (``"positive"``,
            ``"negative"``, or ``"neutral"``), ``"score"`` (confidence
            for the predicted label), and ``"scores"`` (dict of all
            class probabilities).
        """
        # TODO: implement — tokenize texts in batches, run forward
        # pass through the model, apply softmax, and map logits to
        # human-readable labels.
        raise NotImplementedError

    def predict_proba(
        self,
        texts: list[str],
        batch_size: int = 32,
    ) -> np.ndarray:
        """Return probability distributions over sentiment classes.

        Parameters
        ----------
        texts : list[str]
            List of financial text passages.
        batch_size : int
            Batch size for inference.

        Returns
        -------
        np.ndarray
            Array of shape ``(len(texts), 3)`` with columns ordered
            as ``[positive, negative, neutral]``.
        """
        # TODO: implement — reuse predict() logic, extract the
        # probability distributions and stack into a numpy array.
        raise NotImplementedError

    def fine_tune(
        self,
        train_data: Any,
        val_data: Any,
        *,
        epochs: int = 3,
        learning_rate: float = 2e-5,
        batch_size: int = 16,
        output_dir: Path | None = None,
    ) -> dict:
        """Fine-tune FinBERT on a custom financial dataset.

        Parameters
        ----------
        train_data : Dataset
            Hugging Face Dataset with ``"text"`` and ``"label"`` columns.
        val_data : Dataset
            Validation dataset in the same format.
        epochs : int
            Number of training epochs.
        learning_rate : float
            Peak learning rate for the AdamW optimiser.
        batch_size : int
            Training batch size.
        output_dir : Path | None
            Directory to save checkpoints.

        Returns
        -------
        dict
            Training metrics including ``"train_loss"``,
            ``"val_loss"``, ``"val_accuracy"``, ``"val_f1"``,
            and ``"training_time_seconds"``.
        """
        # TODO: implement — set up Hugging Face Trainer with
        # appropriate training arguments, data collator, and
        # metrics computation. Run training and return metrics.
        raise NotImplementedError

    def save(self, path: Path) -> None:
        """Save the model and tokenizer to disk.

        Parameters
        ----------
        path : Path
            Directory to save the model artifacts.
        """
        # TODO: implement — save model weights, tokenizer, and
        # configuration to the specified path using Hugging Face's
        # save_pretrained interface.
        raise NotImplementedError

    @classmethod
    def load(cls, path: Path) -> "FinBERTClassifier":
        """Load a saved FinBERTClassifier from disk.

        Parameters
        ----------
        path : Path
            Directory containing the saved model artifacts.

        Returns
        -------
        FinBERTClassifier
            A ready-to-use classifier instance.
        """
        # TODO: implement — instantiate a new FinBERTClassifier,
        # load model and tokenizer from the path, and return the
        # configured instance.
        raise NotImplementedError
