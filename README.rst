.. role:: bash(code)
  :language: bash

*******
opus-ui
*******

.. image:: https://github.com/Dashstrom/opus-ui/actions/workflows/docs.yml/badge.svg
  :target: https://github.com/Dashstrom/opus-ui/actions/workflows/docs.yml
  :alt: CI : Docs

.. image:: https://github.com/Dashstrom/opus-ui/actions/workflows/lint.yml/badge.svg
  :target: https://github.com/Dashstrom/opus-ui/actions/workflows/lint.yml
  :alt: CI : Lint

.. image:: https://github.com/Dashstrom/opus-ui/actions/workflows/tests.yml/badge.svg
  :target: https://github.com/Dashstrom/opus-ui/actions/workflows/tests.yml
  :alt: CI : Tests

.. image:: https://img.shields.io/pypi/v/opus-ui.svg
  :target: https://pypi.org/project/opus-ui
  :alt: PyPI : opus-ui

.. image:: https://img.shields.io/pypi/pyversions/opus-ui.svg
  :target: https://pypi.org/project/opus-ui
  :alt: Python : versions

.. image:: https://img.shields.io/badge/license-MIT-green.svg
  :target: https://github.com/Dashstrom/opus-ui/blob/main/LICENSE
  :alt: License : MIT

Description
###########

UI for opus models.

Installation
############

You can install :bash:`opus-ui` via `pip <https://pypi.org/project/pip/>`_
from `PyPI <https://pypi.org/project>`_

..  code-block:: bash

  pip install opus-ui

Usage
#####

..  code-block:: bash

  opus-ui --version
  opus-ui --help

Development
###########

Contributing
************

Contributions are very welcome. Tests can be run with :bash:`poe check`, please
ensure the coverage at least stays the same before you submit a pull request.

Setup
*****

You need to install `Poetry <https://python-poetry.org/docs/#installation>`_
and `Git <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>`_
for work with this project.

..  code-block:: bash

  git clone https://github.com/Dashstrom/opus-ui
  cd opus-ui
  poetry install --all-extras
  poetry run poe setup
  poetry shell

Poe
********

Poe is available for help you to run tasks.

..  code-block:: text

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

Commit
******

If the linting is not successful, you can't commit.
For forcing the commit you can use the next command :

..  code-block:: bash

  git commit --no-verify -m 'MESSAGE'

How to add dependency
*********************

..  code-block:: bash

  poetry add 'PACKAGE'

Ignore illegitimate warnings
****************************

To ignore illegitimate warnings you can add :

- **# NoQA: ERROR_CODE** on the same line for ruff.
- **# type: ignore[ERROR_CODE]** on the same line for mypy.
- **# pragma: no cover** on the same line to ignore line for coverage.
- **# doctest: +SKIP** on the same line for doctest.

Uninstall
#########

..  code-block:: bash

  pip uninstall opus-ui

License
#######

This work is licensed under `MIT <https://github.com/Dashstrom/opus-ui/-/raw/main/LICENSE>`_.
