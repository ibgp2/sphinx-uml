# Sphinx-uml

`sphinx-uml` is a simple sphinx extension to generate a UML diagram from python
modules, inspired from
[`sphinx-pyreverse`](https://github.com/sphinx-pyreverse/sphinx-pyreverse/).

Contrary to [`sphinx-pyreverse`](https://github.com/sphinx-pyreverse/sphinx-pyreverse/),
`sphinx-uml` does not call the `pyreverse` command and outputs SVG UML diagrams.
This makes the UML diagram responsive to light/black Sphinx themes.

If the path of the HTML documentation is supplied, `sphinx-uml` outputs
navigable UML diagrams: one can click the class / attribute / method names
to browse the corresponding documentation page.

There are two way to make those diagrams:

* using the `uml` Sphinx directive (in a documentation page)
* using the `pyreverse2` command, shipped with this package, and which extends
  the original `pyreverse` command.

## Installation

```bash
git clone 
```

This extension requires `pyreverse` from `pylint`.

## Usage
### Documentation

Add `"sphinx_uml"` to the extensions list in your `conf.py` (make sure it is
in the `PYTHONPATH`).

Call the `uml` directive with path to python module as content.
The ``:classes:`` and ``:packages:`` flags specify which UML diagrams to show.

```rst
.. uml:: {{modulename}}
	:classes:
	:packages:
```

### Automatic documentation

Using Sphinx templates, one can call the `uml` directive in the auto-generated
documentation pages. See the [templages](example/_templates) provided in our
[toy `example` package](example/).

## Configuration 
### `conf.py`

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

### Environment

By default, the directive provided by this package is named `uml`. Optionally, you can
rename it by defining its name through the `SPHINX_UML_DIRECTIVE` environment variable.

## Troubleshooting

`sphinx-uml` uses `sphinx-docs`' logging API to write information to the log files.

To use it run your ``sphinx-build`` command with ``-v -v -v -w $(pwd)/sphinx.log`` .

For more information see:

* [`-v switch`](https://www.sphinx-doc.org/en/master/man/sphinx-build.html#cmdoption-sphinx-build-v)
* [`-w switch`](https://www.sphinx-doc.org/en/master/man/sphinx-build.html#cmdoption-sphinx-build-w)
