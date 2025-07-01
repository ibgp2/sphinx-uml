# Terminology 
## reStructuredText (`.rst`)

[reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
is the default plaintext markup language used by Sphinx.

## Sphinx extension

A __Sphinx extension__ is a Python package that provides [roles and
directives](https://www.sphinx-doc.org/en/master/development/tutorials/extending_syntax.html#).
They are use to intepret part of `.rst` file.

## Role

A _role_ is invoked when processing a command inline.

```rst
Some text with a :hello:`world` role.
```

## Sphinx directive

A _directive_ is invoked when processing a paragraph involved in a `.rst` file:

```rst
.. hello:: world
```

### Optional parameters

A directive may support optional parameters depending on its specifications:

```rst
.. hello:: world
    :param1:
    :param2:
    :param3: some value

	some content
```

The specifications are class attributes of the class implementing
the Sphinx directive. See
[this tutorial](https://www.sphinx-doc.org/en/master/development/tutorials/extending_syntax.html).

### Configuration

A directive may be configured from the `docs/conf.py` Sphinx configuration file
(see the configuration section).
