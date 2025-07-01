.PHONY: clean docs install
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys
from pathlib import Path

makefiles = sys.argv[1:]

for makefile in makefiles:
	with Path(makefile).open("r") as fh:
		for line in fh:
			match = re.match(r'^([a-zA-Z0-9._-]+):.*?## (.*)$$', line)
			if match:
				target, help = match.groups()
				print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python3 -c "$$BROWSER_PYSCRIPT"
PROJECT := unext

help:
	@python3 -c "$$PRINT_HELP_PYSCRIPT" $(MAKEFILE_LIST)

clean: clean-doc

clean-build:  ## remove build artifacts
	rm -fr dist/

install:
	poetry build
	poetry run pip install pip
	poetry install
	pip3 install dist/*whl --no-deps --force-reinstall --break-system-packages 

install-sphinx-standard:
	poetry install --with docs

install-sphinx-custom:
	cd .. && rm -f dist/sphinx_uml*whl && python3 -m build && cp dist/sphinx_uml*whl example/dist && cd -
	poetry run pip install dist/sphinx_uml*whl --force-reinstall --no-deps

install-doc: install-sphinx-standard install-sphinx-custom

clean-doc:
	rm -rf docs/_build
	rm -rf docs/_autosummary
	rm -f docs/example.*.rst docs/example.rst docs/modules.rst

docs: clean-doc
	poetry run sphinx-apidoc -f -o docs/ src/ --separate --templatedir=docs/_templates
	poetry run sphinx-build -b html docs/ docs/_build/html
	$(BROWSER) docs/_build/html/index.html
