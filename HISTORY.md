## 0.0.18 (2025-06-20): First draft

* First draft

## 0.1.0 (2025-06-20): First release

* __Packaging:__
  * Renamed the extension to `sphinx_uml`.
  * Migrated to [`poetry`](https://python-poetry.org/). See `pyproject.toml`.
  * Added [`bumpversion`](https://manpages.debian.org/testing/bumpversion/bumpversion.1.en.html) configuration. See `setup.cfg`.
  * Removed obsolete files.
* __CI:__
  * Added [Github actions](https://github.com/features/actions) (test, doc, publish). See `.github/`.
  * Added [ReadTheDoc](https://readthedocs.io/) hook.
* __Documentation:__
  * Migrated to [pydata theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/). See `docs/conf.py`.
  * Updated the documentation.
  * Enabled automatic API documentation.
  * Added a toy example project. See `example/`.

## 0.2.0

* __Packaging__:
  * Reorganized sources.
  * Added license (BSD-3).
  * Added badges. See `README.md`.
* __CI__:
  * Updated `publish_on_pypi.yml`
* __Documentation:__
  * Improved sphinx templates (see `example/docs/_templates`)
  * Using `inheritance-diagram` option to customize `uml-sphinx` diagram display.
