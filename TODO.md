1. Improve packaging, e.g., as done in:

- `sphinx.ext.email` (becauses it uses `poetry`)
- `sphinx.ext.autodoc` (because it ships an entry point)

2. Replace the `SphinxProxyHTML` class by a mechanism inspired from `sphinx.ext.inheritance`

3. Delve in `pyreverse` so that we don't have to craft command line argument to initialize it.

4. Tests, CI

- including pyreverse2
