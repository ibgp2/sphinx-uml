# Usage in a `.rst` file

Add `"sphinx_uml"` to the extensions list in your `conf.py` (make sure it is
in the `PYTHONPATH`).

Call the `uml` directive with path to python module as content that supports
the following optional parameters:

- ``:classes:`` indicates whether the class diagram must be displayed.
- ``:packages:`` indicates whether the package diagram must be displayed.
- ``:caption:`` takes an arbitrary text in parameter which is used to label
  the displayed diagram(s).

```rst
.. uml:: {{modulename}}
    :classes:
    :packages:
    :caption: Diagram of {{modulename}}
```
