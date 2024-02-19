.. role:: bash(code)
  :language: bash

******************
Offline Translator
******************

.. image:: https://github.com/Dashstrom/offline-translator/actions/workflows/docs.yml/badge.svg
  :target: https://github.com/Dashstrom/offline-translator/actions/workflows/docs.yml
  :alt: CI : Docs

.. image:: https://github.com/Dashstrom/offline-translator/actions/workflows/lint.yml/badge.svg
  :target: https://github.com/Dashstrom/offline-translator/actions/workflows/lint.yml
  :alt: CI : Lint

.. image:: https://github.com/Dashstrom/offline-translator/actions/workflows/tests.yml/badge.svg
  :target: https://github.com/Dashstrom/offline-translator/actions/workflows/tests.yml
  :alt: CI : Tests

.. image:: https://img.shields.io/pypi/v/offline-translator.svg
  :target: https://pypi.org/project/offline-translator
  :alt: PyPI : offline-translator

.. image:: https://img.shields.io/pypi/pyversions/offline-translator.svg
  :target: https://pypi.org/project/offline-translator
  :alt: Python : versions

.. image:: https://img.shields.io/badge/license-MIT-green.svg
  :target: https://github.com/Dashstrom/offline-translator/blob/main/LICENSE
  :alt: License : MIT

Description
###########

Offline translator GUI using Opus-MT.

Installation
############

First, you need to install `Python <https://www.python.org/downloads/>`_.

Then you need to install :bash:`pipx` for install :bash:`offline-translator` as an application.

..  code-block:: bash

  pip install pipx
  pipx ensurepath
  pipx install offline-translator
  offline-translator

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

  git lfs install
  git clone https://github.com/Dashstrom/offline-translator
  cd offline-translator
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

- **# noqa: ERROR_CODE** on the same line for ruff.
- **# type: ignore[ERROR_CODE]** on the same line for mypy.
- **# pragma: no cover** on the same line to ignore line for coverage.
- **# doctest: +SKIP** on the same line for doctest.

Uninstall
#########

..  code-block:: bash

  pip uninstall offline-translator

License
#######

This work is licensed under `MIT <https://github.com/Dashstrom/offline-translator/blob/main/LICENSE>`_.
