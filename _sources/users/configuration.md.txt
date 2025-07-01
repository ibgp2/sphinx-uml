# Configuration 
## Optional parameters

When calling the `.. uml` directive, you can pass the following options:

- ``:classes:`` enables the UML class diagram display;
- ``:packages:`` enables the package diagram display;
- ``:caption: S``, where ``S`` is an arbitrary RST line of text, defines the
  caption of the resulting image(s).


See the examples section.

## `conf.py`
### `sphinx-uml` specific options

To configure this extension in a Sphinx documentation, update the `docs/conf.py`:

_Example:_

```python
# sphinx-uml switches
uml_colorized = True  # colour the graphs
uml_all_ancestors = True  # give more Sphinx context
uml_all_associated = True
```

The table below list the supported parameters:

<table border=1 cellpadding=5>
<tr>
	<th>Sphinx option</th>
	<th><code>pyreverse2</code> option</th>
	<th>Default value</th>
</tr><tr>
	<td><code>uml_filter_mode</code></td>
	<td><code>--filter_mode FILTER</code></td>
	<td><code>"PUB_ONLY"</code></td>
</tr><tr>
	<td><code>uml_class</code></td>
	<td><code>--class CLASSES</code></td>
	<td><code>[]</code></td>
</tr><tr>
	<td><code>uml_show_ancestors</code></td>
	<td><code>--show_ancestors LEVEL</code></td>
	<td><code>None</code></td>
</tr><tr>
	<td><code>uml_all_ancestors</code></td>
	<td><code>--all_ancestors</code></td>
	<td><code>False</code></td>
</tr><tr>
	<td><code>uml_show_associated</code></td>
	<td><code>--show_associated</code></td>
	<td><code>None</code></td>
</tr><tr>
	<td><code>uml_all_associated</code></td>
	<td><code>--all_associated</code></td>
	<td><code>False</code></td>
</tr><tr>
	<td><code>uml_show_builtin</code></td>
	<td><code>--show_builtin</code></td>
	<td><code>False</code></td>
</tr><tr>
	<td><code>uml_module_names</code></td>
	<td><code>--module_names MODULES</code></td>
	<td><code>False</code></td>
</tr><tr>
	<td><code>uml_only_classnames</code></td>
	<td><code>--only_classnames</code></td>
	<td><code>False</code></td>
</tr><tr>
	<td><code>uml_ignore</code></td>
	<td><code>--ignore IGNORE</code></td>
	<td><code>("CVS",)</code></td>
</tr><tr>
	<td><code>uml_colorized</code></td>
	<td><code>--colorized</code></td>
	<td><code>False</code></td>
</tr>
</table>

See also:

* `example/docs/doc.conf` as an example:
* `pyreverse --help` for more details about each option.

### Environment

By default, the directive provided by this package is named `uml`. Optionally, you can
rename it by defining its name through the `SPHINX_UML_DIRECTIVE` environment variable.

## `sphinx-uml` inherited options

`sphinx-uml` uses relies on some display options provided by:

- `graphviz.ext.graphviz`
- `graphviz.ext.inheritance_diagram`

_Example:_

```python
# Options related to sphinx.ext.graphviz.
# Thus, it also impacts sphinx.ext.inheritance_diagram and sphinx_uml.
graphviz_output_format = "svg"

# Options related to sphinx.ext.inheritance_diagram
bgcolor = "transparent"
fgcolor = "black"  # Note that night mode will change this to white
inheritance_graph_attrs = {
    "rankdir": "BT",
    "fontcolor": fgcolor,
    "bgcolor": bgcolor,
}
inheritance_node_attrs = inheritance_edge_attrs = {
    "color": fgcolor,
    "fontcolor": fgcolor,
}
```


