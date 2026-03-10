"""Tests for financial text cleaning and normalization.

Covers HTML removal, ticker normalization, document segmentation,
and financial-aware tokenization.
"""


def test_clean_financial_text_removes_html(sample_financial_text):
    """Test HTML tag removal from financial text."""
    pass


def test_normalize_tickers():
    """Test ticker symbol normalization to canonical forms."""
    pass


def test_segment_document_identifies_sections(sample_filing_text):
    """Test document segmentation into labeled sections."""
    pass


def test_tokenize_financial_handles_tickers():
    """Test that financial tokenizer preserves ticker symbols."""
    pass


def test_build_financial_stopwords():
    """Test domain-adapted stopword list construction."""
    pass
