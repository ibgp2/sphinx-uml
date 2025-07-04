.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python3 -c "$$BROWSER_PYSCRIPT"
PROJECT := sphinx_uml

help:
	@python3 -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-doc clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style with flake8
	poetry run flake8 src tests

test: ## run tests quickly with the default Python
	poetry run pytest

test-all: ## run tests on every Python version with tox
	poetry run tox

coverage: ## check code coverage quickly with the default Python
	poetry run coverage run -m pytest
	poetry run coverage html
	poetry run coverage xml
	$(BROWSER) htmlcov/index.html

clean-doc:
	rm -rf docs/_build
	rm -rf docs/_autosummary
	rm -f docs/$(PROJECT).*.rst

docs: clean-doc ## generate Sphinx HTML documentation, including API docs
	poetry run sphinx-apidoc -f -o docs/ src/ --separate
	poetry run sphinx-build -b html docs/ docs/_build/html
	$(BROWSER) docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: dist ## package and upload a release
	poetry publish

dist: clean ## builds source and wheel package
	poetry build

install: clean dist ## install the package to the active Python's site-packages
	pip3 install dist/*whl --break-system-packages --force-reinstall --no-deps
