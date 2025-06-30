# Configuration 
## `conf.py`

To configure this extension in a Sphinx documentation, update the `conf.py`:

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

## Environment

By default, the directive provided by this package is named `uml`. Optionally, you can
rename it by defining its name through the `SPHINX_UML_DIRECTIVE` environment variable.
