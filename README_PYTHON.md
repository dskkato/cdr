# Python Development

This repository contains a Python implementation of the Common Data Representation (CDR) library. This guide explains how to set up a development environment, run linters with pre-commit, and execute the test suite.

## Environment Setup

1. Ensure Python 3.10 or newer is installed.
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install the package with development dependencies:
   ```bash
   pip install -e .[dev]
   ```

## pre-commit

This project uses [pre-commit](https://pre-commit.com/) to run formatting and linting tools.

- Install the Git hook scripts:
  ```bash
  pre-commit install
  ```
- Run all checks:
  ```bash
  pre-commit run --all-files
  ```

## Testing

Run the unit tests with [pytest](https://pytest.org/):

```bash
pytest
```
