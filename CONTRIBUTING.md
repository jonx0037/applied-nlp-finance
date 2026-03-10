# Contributing to Applied NLP for Finance

Thank you for your interest in contributing! This repository is the companion code for *Applied NLP for Finance*. Contributions that improve code quality, fix bugs, or add educational value are welcome.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/applied-nlp-finance.git`
3. Install development dependencies: `pip install -e ".[dev,notebooks]"`
4. Create a feature branch: `git checkout -b feature/your-feature-name`

## Code Style

This project uses [Ruff](https://docs.astral.sh/ruff/) for linting and formatting:

```bash
# Check for issues
ruff check src/ tests/

# Auto-fix issues
ruff check --fix src/ tests/

# Format code
ruff format src/ tests/
```

- Line length: 100 characters
- Target Python version: 3.11
- Follow PEP 8 conventions

## Testing

All code changes should include or update tests:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test module
pytest tests/test_models/test_finbert.py
```

## Pull Request Process

1. Ensure all tests pass: `pytest`
2. Ensure code passes linting: `ruff check src/ tests/`
3. Update documentation if your change affects the public API
4. Write a clear PR description explaining the change and its motivation
5. Reference any related issues

## Reporting Issues

When reporting bugs, please include:
- Python version and OS
- Steps to reproduce
- Expected vs. actual behavior
- Relevant error messages or stack traces

## Manuscript Contributions

The manuscript in `/manuscript` is licensed under CC BY-NC 4.0. If you spot errors or have suggestions, please open an issue rather than a PR for manuscript content.
