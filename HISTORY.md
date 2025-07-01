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

## 0.2.0 (2025-06-30)

* __Packaging__:
  * Reorganized sources.
  * Added license (BSD-3).
  * Added badges. See `README.md`.
* __CI__:
  * Updated `publish_on_pypi.yml`
* __Documentation:__
  * Improved sphinx templates (see `example/docs/_templates`)
  * Using `inheritance-diagram` option to customize `uml-sphinx` diagram display.
* __Bug fixes:__
  * `pyreverse2`: fixed output if `--sphinx-html-dir` is omitted.
  * Fixed graphviz output if a tooltip would have contained special characters
    * See, e.g., `pyreverse2 --output svg pylint.typing`

## 0.3.0 (2025-07-01)

* __CI:__
  * Updated `.readthedocs.yml` so that the API documentation is auto-generated.
* __API__:
  * Added the `UmlNode.to_dot` method.
  * Added the `guess_svg_basename` function.
* __Features:__
  * An "Open in a new tab" link is now displayed below each UML diagram. 

## 0.3.1 (2025-07-01)

* __API__:
  * `UMLGenerateDirective.html_root_dir` now returns a `pathlib.Path` instance.
*  __Bug fixes:__
  * Fixed "Open in a new tab" link URL.

## 0.3.2 (2025-07-01)

* __Documentation__
  * Reorganized/fixed the package documentation.
