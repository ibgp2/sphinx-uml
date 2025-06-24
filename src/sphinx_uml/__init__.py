__author__ = "Marc-Olivier Buob"
__maintainer__ = "Marc-Olivier Buob"
__email__ = "marc-olivier.buob@nokia-bell-labs.com"
__license__ = "BSD-3"
__version__ = "0.1.0"
__all__ = ["UMLGenerateDirective"]


import os
from sphinx.application import Sphinx
from sphinx.util.typing import ExtensionMetadata
from .uml_generate_directive import UMLGenerateDirective


def setup(app: Sphinx) -> ExtensionMetadata:
    """Setup directive"""
    app.setup_extension('sphinx.ext.graphviz')
    app.add_config_value('uml_graph_attrs', {}, '')
    app.add_config_value('uml_node_attrs', {}, '')
    app.add_config_value('uml_edge_attrs', {}, '')
    app.add_config_value('uml_alias', {}, '')

    # Allow override of the directive, defaulting to 'uml'
    directive_name_to_use = os.environ.get("SPHINX_UML_DIRECTIVE", "uml")
    app.add_directive(directive_name_to_use, UMLGenerateDirective)

    # pylint.pyreverse options
    app.add_config_value("sphinx_pyreverse_output", default="svg", rebuild="env")
    app.add_config_value("sphinx_pyreverse_filter_mode", default=None, rebuild="env")
    app.add_config_value("sphinx_pyreverse_class", default=None, rebuild="env")
    app.add_config_value("sphinx_pyreverse_show_ancestors", default=None, rebuild="env")
    app.add_config_value("sphinx_pyreverse_all_ancestors", default=None, rebuild="env")
    app.add_config_value(
        "sphinx_pyreverse_show_associated", default=None, rebuild="env"
    )
    app.add_config_value("sphinx_pyreverse_all_associated", default=None, rebuild="env")
    app.add_config_value("sphinx_pyreverse_show_builtin", default=None, rebuild="env")
    app.add_config_value("sphinx_pyreverse_module_names", default=None, rebuild="env")
    app.add_config_value(
        "sphinx_pyreverse_only_classnames", default=None, rebuild="env"
    )
    app.add_config_value("sphinx_pyreverse_ignore", default=None, rebuild="env")
    app.add_config_value(
        "sphinx_pyreverse_image_max_width", default=1000, rebuild="env"
    )
    app.add_config_value("sphinx_pyreverse_image_scale", default=1.0, rebuild="env")
    app.add_config_value("sphinx_pyreverse_colorized", default=None, rebuild="env")

    return {
        "version": __version__,
        "parallel_read_safe": True
    }
