# Offline Translator

[![CI : Docs](https://github.com/Dashstrom/offline-translator/actions/workflows/docs.yml/badge.svg)](https://github.com/Dashstrom/offline-translator/actions/workflows/docs.yml)
[![CI : Lint](https://github.com/Dashstrom/offline-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/Dashstrom/offline-translator/actions/workflows/lint.yml)
[![CI : Tests](https://github.com/Dashstrom/offline-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/Dashstrom/offline-translator/actions/workflows/tests.yml)
[![GitHub : Repo size](https://img.shields.io/github/repo-size/Dashstrom/offline-translator)](https://github.com/Dashstrom/offline-translator)
[![PyPI : Version](https://img.shields.io/pypi/v/offline-translator.svg)](https://pypi.org/project/offline-translator)
[![PyPI : Download](https://pepy.tech/project/offline-translator)](https://static.pepy.tech/badge/offline-translator)
[![License : MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/Dashstrom/offline-translator/blob/main/LICENSE)

## Description

Offline Translator GUI using Opus-MT.

## Installation

First, you need to install [Python](https://www.python.org/downloads).

Then you need to install `pipx` for install `offline-translator` as an application.

```bash
  pip install pipx
  pipx ensurepath
  pipx install offline-translator
  offline-translator
```

## Development

### Contributing

Contributions are very welcome. Tests can be run with `poe check`, please
ensure the coverage at least stays the same before you submit a pull request.

### Setup

You need to install [Poetry](https://python-poetry.org/docs/#installation)
and [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
for work with this project.

```bash
git clone https://github.com/Dashstrom/offline-translator
cd offline-translator
poetry install --all-extras
poetry run poe setup
poetry shell
```

### Poe

Poe is available for help you to run tasks.

```text
test           Run test suite.
lint           Run linters : ruff linter, ruff formatter and mypy.
format         Run linters in fix mode.
check          Run all checks : lint, test and docs.
cov            Run coverage for generate report and html.
open-cov       Open html coverage report in webbrowser.
docs           Build documentation.
open-docs      Open documentation in webbrowser.
setup          Setup pre-commit.
pre-commit     Run pre-commit.
clean          Clean cache files
```

### Commit

If the linting is not successful, you can't commit.
For forcing the commit you can use the next command :

```bash
git commit --no-verify -m 'MESSAGE'
```

### How to add dependency

```bash
poetry add 'PACKAGE'
```

### Ignore illegitimate warnings

To ignore illegitimate warnings you can add :

- `# noqa: ERROR_CODE` on the same line for ruff.
- `# type: ignore[ERROR_CODE]` on the same line for mypy.
- `# pragma: no cover` on the same line to ignore line for coverage.
- `# doctest: +SKIP` on the same line for doctest.

## Uninstall

```bash
pip uninstall offline-translator
```

## License

This work is licensed under [MIT](https://github.com/Dashstrom/offline-translator/blob/main/LICENSE).
