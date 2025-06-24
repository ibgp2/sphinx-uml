import argparse
from pathlib import Path
from docutils import nodes
from docutils.parsers.rst import directives
from pylint.pyreverse.main import writer
from sphinx.ext.graphviz import (
    figure_wrapper,
    graphviz,
)
from sphinx.util.docutils import SphinxDirective
from sphinx.util.typing import ExtensionMetadata, OptionSpec
from typing import TYPE_CHECKING
from typing import ClassVar


class UmlNode(graphviz):
    """
    Defines a UML ``docutils`` node.
    We populate its attribute so that we can rely on the
    default ``graphviz`` node.
    """
    @classmethod
    def from_dot(cls, dotcode: str) -> "UmlNode":
        """
        Builds a :py:class:`UmlNode` instance from a Graphviz
        dot string.

        Args:
            dotcode (str): A Graphviz dot string.
                *Example:* ``digraph G {0 -> 1}``

        Returns:
            The resulting :py:class:`UmlNode` instance.
        """
        node = cls()
        node["code"] = dotcode
        node["options"] = {"graphviz_dot": "dot"}

        # We rely on graph inheritance CSS class to be responsive
        # to dark/light theme
        node["classes"] = ["uml"]
        return node

    @classmethod
    def from_pyreverse(
        cls,
        diadefs: list,
        config: argparse.Namespace
    ) -> "UmlNode":
        """
        Builds a :py:class:`UmlNode` from diagram definitions
        obtained from pyreverse.

        Args:
            dotcode (str): A Graphviz dot string.
                *Example:* ``digraph G {0 -> 1}``

        Returns:
            The resulting :py:class:`UmlNode` instance.
        """
        from .pyreverse import DotPrinter, SphinxHtmlProxy
        dwriter = writer.DiagramWriter(config)
        dwriter.printer_class = DotPrinter
        # TODO Buidl xrefs as in
        # /usr/lib/python3/dist-packages/sphinx/ext/inheritance_diagram.py
        dwriter.api_doc = SphinxHtmlProxy()
        dwriter.api_doc.sphinx_html_dir = config.sphinx_html_dir
        dwriter.write(diadefs)
        dotcode = "\n".join(dwriter.printer.lines)
        return cls.from_dot(dotcode)


class UMLGenerateDirective(SphinxDirective):
    """
    UML directive to generate a pyreverse diagram
    """

    # Sphinx stuff to control argument passing
    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec: ClassVar[OptionSpec] = {
        "parts": int,
        "caption": directives.unchanged,
        "classes": directives.flag,
        "packages": directives.flag,
    }

    # a list of modules which have been parsed by pyreverse
    # generated_modules = []

#     def _validate(self):
#         """Validates that the RST parameters are valid"""
#         valid_flags = {":classes:", ":packages:"}
#         unknown_arguments = set(self.arguments[1:]) - valid_flags
#         if unknown_arguments:
#             raise ValueError(
#                 (
#                     f"invalid flags encountered: {unknown_arguments}. "
#                     f"Must be one of {valid_flags}"
#                 )
#             )

    def _build_command(self, module_name, config):  # noqa: C901 func too-complex
        cmd = [
            "pyreverse",
            "--output",
            # <<
            # config.sphinx_pyreverse_output,
            # --
            "svg",
            # >>
            "--project",
            module_name,
        ]
        if config.sphinx_pyreverse_filter_mode:
            assert config.sphinx_pyreverse_filter_mode
            cmd.extend(("--filter-mode", config.sphinx_pyreverse_filter_mode))
        if config.sphinx_pyreverse_class:
            cmd.extend(("--class", config.sphinx_pyreverse_class))
        if config.sphinx_pyreverse_show_ancestors:
            cmd.extend(("--show-ancestors", config.sphinx_pyreverse_show_ancestors))
        if config.sphinx_pyreverse_all_ancestors:
            cmd.append("--all-ancestors")
        if config.sphinx_pyreverse_show_associated:
            cmd.extend(("--show-associated", config.sphinx_pyreverse_show_associated))
        if config.sphinx_pyreverse_all_associated:
            cmd.append("--all-associated")
        if config.sphinx_pyreverse_show_builtin:
            cmd.append("--show-builtin")
        if config.sphinx_pyreverse_module_names:
            cmd.extend(("--module-names", config.sphinx_pyreverse_module_names))
        if config.sphinx_pyreverse_only_classnames:
            cmd.append("--only-classnames")
        if config.sphinx_pyreverse_ignore:
            cmd.extend(("--ignore", config.sphinx_pyreverse_ignore))
        if config.sphinx_pyreverse_colorized:
            cmd.append("--colorized")

        # finally append the module to generate the uml for
        cmd.append(module_name)
        return cmd

    def html_root_dir(self) -> str:
        """
        Returns:
            The HTML prefix to move from the current HTML document
            to the HTML root directory.

        Example:
            Assume that:

            - the documentation is built in:
              ``"~/git/sphinx-uml/docs"``;
            - the current document is;
              ``"~/git/sphinx-uml/docs/users/examples.rst"``;

            Then, the returned value is ``"../"``.
            As the HTML hierarchy follows the RST hierarchy, we use
            this prefix to setup our :py:class:`SphinxHtmlProxy`.
        """
        doc = self.state.document
        env = doc.settings.env
        base_dir = Path(env.srcdir).absolute()
        cur_path = Path(doc.current_source)
        rel_path = str(cur_path.relative_to(base_dir).parent)
        if rel_path == ".":
            return rel_path
        n = len(rel_path.split("/"))
        ret = "/".join([".."] * n)
        return ret

    def run(self):
        """
        To test this extension, as a developer:

        .. shell
            make install-sphinx-custom clean-doc docs

        To test this `pyreverse2`, called by this extension:

        .. shell
            pyreverse2 \
               --output svg \
               --project example.a \
               --sphinx-html-dir docs/_html \
               --output-directory docs/ \
               -m y \
               example.a
        """
        module_name = self.arguments[0]
        # self._validate()

        #page_name = Path(doc.current_source)  # Prefixed by src.
        #module_name = page_name.with_suffix("").name

        output_format = "dot"
        pyprocess_args = [
#            "--output", output_format,           # -o
            "--sphinx-html-dir", self.html_root_dir(),
#            "--output-directory", str(uml_dir),
#            "--verbose",
#            "--project", module_name,            # -p
            # "--module-names", "y",             # -m
            module_name
        ]
        pyprocess_shell = "pyreverse2 " + " ".join(pyprocess_args)
        print(pyprocess_shell)

        # make install-sphinx-custom clean-doc docs
        from .pyreverse import Run, ParsePyreverseArgs

        parser = ParsePyreverseArgs(pyprocess_args)
        runner = Run(parser.config)
        diadefs = runner.diadefs(parser.remaining_args)
        node = UmlNode.from_pyreverse(diadefs, runner.config)

        if "caption" not in self.options:
            self.add_name(node)
            return [node]
        else:
            figure = figure_wrapper(self, node, self.options["caption"])
            self.add_name(figure)
            return [figure]
