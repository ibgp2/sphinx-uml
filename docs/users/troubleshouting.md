# Troubleshooting

`sphinx-uml` uses the [Sphinx logging API](https://www.sphinx-doc.org/en/master/extdev/logging.html)
to write information to the log files.

To use it run your ``sphinx-build`` command with ``-v -v -v -w $(pwd)/sphinx.log``.

For more information, see:

* [`-v switch`](https://www.sphinx-doc.org/en/master/man/sphinx-build.html#cmdoption-sphinx-build-v)
* [`-w switch`](https://www.sphinx-doc.org/en/master/man/sphinx-build.html#cmdoption-sphinx-build-w)
