# Configuration 
## `conf.py`

To configure this extension in a Sphinx documentation, update the `conf.py`:

* `uml_output` (see `--output`), default is `"png"`;
* `uml_filter_mode` (see `--filter_mode`), default is `None`;
* `uml_class` (see `--class`), default is `None`;
* `uml_show_ancestors` (see `--show_ancestors`), default is `None`;
* `uml_all_ancestors` (see `--all_ancestors`), default is `None`;
* `uml_show_associated` (see `--show_associated`), default is `None`;
* `uml_all_associated` (see `--all_associated`), default is `None`;
* `uml_show_builtin` (see `--show_builtin`), default is `None`;
* `uml_module_names` (see `--module_names`), default is `None`;
* `uml_only_classnames` (see `--only_classnames`), default is `None`;
* `uml_ignore` (see `--ignore`), default is `None`;

The options related to image output are now irrelevant.

* `uml_image_max_width` (int) Rendered output max width in pixels. default is `1000`;
* `uml_image_scale` (float) Scale the rendered output. default is `1.0`;
* `uml_colorized` (see `--colorized`), default is `None`.

See also [example/docs/doc.conf] as an example.

## Environment

By default, the directive provided by this package is named `uml`. Optionally, you can
rename it by defining its name through the `SPHINX_UML_DIRECTIVE` environment variable.
