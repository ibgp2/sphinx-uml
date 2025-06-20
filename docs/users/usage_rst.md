# Usage in a `.rst` file

Add `"sphinx_uml"` to the extensions list in your `conf.py` (make sure it is
in the `PYTHONPATH`).

Call the `uml` directive with path to python module as content.
The ``:classes:`` and ``:packages:`` flags specify which UML diagrams to show.

```rst
.. uml:: {{modulename}}
    :classes:
    :packages:
```
