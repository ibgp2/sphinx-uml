# Configuration 
## `conf.py`

To configure this extension in a Sphinx documentation, update the `conf.py`:

* `sphinx_pyreverse_output` (see `--output`), default is `"png"`;
* `sphinx_pyreverse_filter_mode` (see `--filter_mode`), default is `None`;
* `sphinx_pyreverse_class` (see `--class`), default is `None`;
* `sphinx_pyreverse_show_ancestors` (see `--show_ancestors`), default is `None`;
* `sphinx_pyreverse_all_ancestors` (see `--all_ancestors`), default is `None`;
* `sphinx_pyreverse_show_associated` (see `--show_associated`), default is `None`;
* `sphinx_pyreverse_all_associated` (see `--all_associated`), default is `None`;
* `sphinx_pyreverse_show_builtin` (see `--show_builtin`), default is `None`;
* `sphinx_pyreverse_module_names` (see `--module_names`), default is `None`;
* `sphinx_pyreverse_only_classnames` (see `--only_classnames`), default is `None`;
* `sphinx_pyreverse_ignore` (see `--ignore`), default is `None`;

The options related to image output are now irrelevant.

* `sphinx_pyreverse_image_max_width` (int) Rendered output max width in pixels. default is `1000`;
* `sphinx_pyreverse_image_scale` (float) Scale the rendered output. default is `1.0`;
* `sphinx_pyreverse_colorized` (see `--colorized`), default is `None`.

See also [example/docs/doc.conf] as an example.

## Environment

By default, the directive provided by this package is named `uml`. Optionally, you can
rename it by defining its name through the `SPHINX_UML_DIRECTIVE` environment variable.
