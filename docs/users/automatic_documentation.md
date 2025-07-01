# Using `sphinx-uml` in auto-generated documentation

Using Sphinx templates, one can call the `uml` directive in the auto-generated
documentation pages. 

## Extensions (`docs/conf.py`) 

Enable the following extensions:

```py
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
	# ...
    "sphinx.ext.graphviz",  # https://stackoverflow.com/a/59319659/14851404
    "sphinx_uml"
]
``` 

## Templates

[Sphinx templates](https://www.sphinx-doc.org/en/master/development/html_themes/templating.html)
are used to customize how Sphinx generate package and module pages. Otherwise, Sphinx use its
own default templates.

Custom templates are usually stored in `docs/_templates`.
They are typically based on `sphinx/templates/apidoc/*jinja` files.
See `example/docs/_templates` as an example.

## Building the documentation

To be taken into account,  the `--templatedir` option is needed when building the
documentation. See `example/Makefile`:

_Example:_

```bash
poetry run sphinx-apidoc -f -o docs/ src/ --separate --templatedir=docs/_templates
poetry run sphinx-build -b html docs/ docs/_build/html
```

See [`example/docs/_templates`](https://github.com/ibgp2/sphinx-uml/tree/main/example/docs/_templates)
and [`example/Makefile`](https://github.com/ibgp2/sphinx-uml/tree/main/example/docs/_templates)
as an example.

