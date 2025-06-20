`example` is a toy package example used to demonstrate our ability to
automatically generate the documentation using Sphinx.  In the process, we aim
at injecting the UML diagrams of each module at the right place.

# Pre-requisites

1) Install `python3` and `pip`.

* _Example:_ under Ubuntu:

```bash
sudo apt update
sudo apt install python3 python3-pip 
```

Install `poetry`:

```bash
pip install poetry
```

2) Optionally, install `make`.

* _Example:_ under Ubuntu:

```bash
sudo apt update
sudo apt install make
```

# Installation
## Long path

To install the `example` package in `poetry`, run:

```bash
poetry build
poetry install
```

_Remark:_ To install it outside of poetry you would run:

```bash
pip3 install dist/*whl --no-deps --force-reinstall --break-system-packages 
```

## Fast path

From this directory and assuming `make` is installed, run:

```
make install 
```

# Background 

A sphinx extension provides [roles and directives](https://www.sphinx-doc.org/en/master/development/tutorials/extending_syntax.html#). They are use to intepret part of `.rst` file.
* A _role_ is invoked when processing a command inline.

```rst
Some text with a :hello:`world` role.
```

* A _directive_ is invoked when processing a paragraph:

```rst
.. hello:: world
```

# Overview

`sphinx-pyreverse` provides the `..uml` directive (and no role). The `..uml` directive is described in [../README.rst](../README.rst).

_Example_

```rst
.. uml:: example.module.submodule 
	:classes:
	:packages:
```

For each python module being documented, thanks to [Sphinx templating](docs/developers/documentation.md), Sphinx call the `sphinx-pyreverse` to generate the corresponding UML diagram. See also:

* [`docs/_templates`] which stores the customized templates.
* [`docs/conf.py`] which enables the customized templates and configure the Sphinx extensions.

# Documentation 

## Long path

1) The following commands install Sphinx and its requirements in `poetry`.

```bash
poetry install --with docs
```

2) To install `sphinx-pyreverse` locally built in `poetry`, run:

```bash
cd ..
python3 -m build
mv dist/sphinx_pyreverse*whl example/dist/
cd example 
poetry run pip install dist/sphinx_pyreverse*whl
```

3) Build the documentation:

```bash
poetry run sphinx-apidoc -f -o docs/ src/ --separate --templatedir=docs/_templates
poetry run sphinx-build -b html docs/ docs/_build/html
```

## Fast path

From this directory and assuming `make` is installed, run:

```
make install-doc
make docs 
```

# Browse the documentation

Open [`docs/build/html/index.html`](docs/_build/html/index.html)
