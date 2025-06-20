# Documentation (`sphinx`)
## Dependencies

Ensure that all the needed dependencies are intalled in `poetry`:
```bash
poetry install --with docs
```

## With `make`

```bash
poetry run make docs
```

## Without `make`

```bash
poetry run sphinx-apidoc -f -o docs/ src/
poetry run sphinx-build -b html docs/ docs/_build
```

# Sphinx extensions
## Inheritance diagrams

The [`inheritance-diagram` Sphinx extension](https://www.sphinx-doc.org/en/master/usage/extensions/inheritance.html) is used to generate a UML graph when documentating a Python class.

In practice, it enables the `.. inheritance-diagram::` command in a RST string (as a docstring or `jinja` template).
It takes a module or a class name as a parameter.

What must be displayed can be specified by a list of [dedicated options](https://www.sphinx-doc.org/en/master/usage/extensions/inheritance.html)):

- `:parts:` to alter the way the node are labeled
- `:include-subclasses:` to indicate whether the subclasses must be displauyed
- `:top-classes:` to limit the exploration of parent classes
- ...

_Example:_

```python3
class A:
	"""
	Class :py:class:`A` is amazing.

	.. inheritance-diagram:: A
		:include-subclasses:
		:parts: 1
	"""
	pass

class B(A):
	"""
	Class :py:class:`B` is amazing.

	.. inheritance-diagram:: B
		:include-subclasses:
		:parts: 1
	"""
	pass
```

The graph style (image type, colors, fonts, etc.) is delegated to the [`sphinx.ext.graphviz` Sphinx extension](https://www.sphinx-doc.org/en/master/usage/extensions/inheritance.html).

Note the [`inheritance-diagram` Sphinx extension](https://www.sphinx-doc.org/en/master/usage/extensions/inheritance.html) seem to only support Graphviz to render UML graphs.
Tools like [`mermaid`](https://github.com/mgaitan/sphinxcontrib-mermaid/blob/master/README.rst) or [`plantuml`](https://github.com/sphinx-contrib/plantuml) are not supported.

## Documentation from docstring (`sphinx-apidoc`)

[Sphinx](https://www.sphinx-doc.org/en/master/) ships two commands to generate
a documentation, namely:

- `sphinx-apidoc` that generates `.rst` files from the docstrings annotating the python code.
- `sphinx-build` that converts those `.rst` files to another format (e.g., HTML or LaTeX).

```bash
sphinx-apidoc -f -o docs/ src/ --separate --templatedir=docs/.templates
sphinx-build -b html docs/ docs/_build/html
```

### Templates

`sphinx-apidoc` relies on several [`jinja` templates](https://jinja.palletsprojects.com/en/stable/templates/).

- `module.rst.jinja`
- `package.rst.jinja`
- `toc.rst.jinja`

The default templates are shipped in the sphinx package (see, e.g,  `~/.local/lib/python3.13/site-packages/sphinx/templates/apidoc/`).

__Note:__ `package.rst.jinja` behaves differently if you call `sphinx-apidoc`
with or without the [`--separate`
option](https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html).

### Custom templates

One can define [custom templates](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-templates_path) so that they supersede the default `jinja` templates as follows.

1) Define by defining in `docs/conf.py` a directory containing the custom templates.
For example, to use `docs/.templates/*.jinja` files, add in `docs/conf.py` the following python instruction:

```python
templates_path = [".templates"]
```

2) Create the needed files from the original templates and tune them (based on this [discussion](https://stackoverflow.com/a/59319659/14851404)):

- `docs/.templates/package.rst.jinja`
- `docs/.templates/module.rst.jinja `

## Sphinx and graphviz

[Graphviz](https://graphviz.org/) is a tool used to display a graph structures using various image formats.
In particular, it is used by the [`inheritance-diagram` Sphinx extension](https://www.sphinx-doc.org/en/master/usage/extensions/inheritance.html) to generate UML graphs.

### Image format

[Graphviz](https://graphviz.org/) ships several utilities (including the `dot` command).
By default, `dot` (and thus `sphinx.ext.graphviz`) generates PNG files.
However, SVG format is often more desirable to get a better rendering.

The output image used by `sphinx.ext.graphviz` can be specified in `docs/conf.py`,
as explained in the [Graphviz documentation](https://www.sphinx-doc.org/en/master/usage/extensions/graphviz.html):

```python
graphviz_output_format = "svg"
```

### Graph style

Graphviz relies on a `.dot` file that specifies the graph structure and styles:

- [`graph` attributes](https://graphviz.org/docs/graph/);
- [`node`-based attributes](https://graphviz.org/docs/node/);
- [`edge`-based attributes](https://graphviz.org/docs/edge/).

These three sets of styles initialized by three dedicated
dictionnaries that are specified in `docs/conf.py`, respectively:

- [`inheritance_graph_attrs`](https://www.sphinx-doc.org/en/master/usage/extensions/inheritance.html#confval-inheritance_graph_attrs);
- [`inheritance_node_attrs`](https://www.sphinx-doc.org/en/master/usage/extensions/inheritance.html#confval-inheritance_node_attrs);
- [`inheritance_edge_attrs`](https://www.sphinx-doc.org/en/master/usage/extensions/inheritance.html#confval-inheritance_edge_attrs).

The colors are specified assuming a light theme.

_Example:_

```python
bgcolor = "transparent"
fgcolor = "black"
inheritance_graph_attrs = {
    "rankdir": "TB",
    "fontcolor": fgcolor,
    "bgcolor": bgcolor,
}
inheritance_node_attrs = inheritance_edge_attrs = {
    "color": fgcolor,
    "fontcolor": fgcolor,
}
```

_Remarks:_

* Graphviz colors must follow [these specifications](https://graphviz.org/docs/attr-types/color/)
* There is no need to rely on CSS when using the [`pydata` Sphinx theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/): the colors are automatically reversed in dark mode.
* Some other themes can generate CSS-aware graphs, see e.g, the [`sphinx-immaterial` theme](https://jbms.github.io/sphinx-immaterial/graphviz.html).
