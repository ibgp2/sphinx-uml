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
