"""
Defines sphinx-wrappers for the pyreverse tool

First, Created on Oct 1, 2012, this file created on Oct 8, 2019

@author: alendit, doublethefish
"""

# import os
# import subprocess
from pathlib import Path

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util import logging

from typing import TYPE_CHECKING

# try:
#     from sphinx.util.compat import Directive
# except ImportError:
#     from docutils.parsers.rst import Directive  # pylint: disable=C0412
from sphinx.util.docutils import SphinxDirective


# <<<<<<<<<<<<<<<< DEBUG
#def html_visit_uml_node(self, node) -> None:
#    """
#    Output the graph for HTML.  This will insert a PNG with clickable
#    image map.
#    """
#    print("ZIZI DEBOUT")
#    graph = node['graph']
#
#    print("ENTERING html_visit_uml_node")
#    graph_hash = get_graph_hash(node)
#    name = 'inheritance%s' % graph_hash
#
#    # Create a mapping from fully-qualified class names to URLs.
#    graphviz_output_format = self.builder.env.config.graphviz_output_format.upper()
#    current_filename = path.basename(self.builder.current_docname + self.builder.out_suffix)
#    urls = {}
#    pending_xrefs = cast(Iterable[addnodes.pending_xref], node)
#    for child in pending_xrefs:
#        if child.get('refuri') is not None:
#            # Construct the name from the URI if the reference is external via intersphinx
#            if not child.get('internal', True):
#                refname = child['refuri'].rsplit('#', 1)[-1]
#            else:
#                refname = child['reftitle']
#
#            urls[refname] = child.get('refuri')
#        elif child.get('refid') is not None:
#            if graphviz_output_format == 'SVG':
#                urls[child['reftitle']] = current_filename + '#' + child.get('refid')
#            else:
#                urls[child['reftitle']] = '#' + child.get('refid')
#
#    print("CALLING generate_dot")
#    dotcode = graph.generate_dot(name, urls, env=self.builder.env)
#    print(dotcode)
#    render_dot_html(self, node, dotcode, {}, 'inheritance', 'inheritance',
#                    alt='Inheritance diagram of ' + node['content'])
#    raise nodes.SkipNode
# >>>>>>>>>>>>>>>>>


# try:
#     from PIL import Image as IMAGE
# except ImportError:  # pragma: no cover
#     IMAGE = None

# debugging with IPython
# ~ try:
# ~ from IPython import embed
# ~ except ImportError as e:
# ~ pass


# def subproc_wrapper(*args, **kwargs):  # pragma: no cover
#     """A shim which allows mocking of the subproc call when using pytest"""
#     subprocess.check_output(*args, **kwargs)

from sphinx.ext.graphviz import (
    figure_wrapper,
    graphviz,
)

class UmlNode(graphviz):
    """
    Defines a UML ``docutils`` node.
    """
    pass

import argparse
from pylint.pyreverse.diagrams import (
    ClassDiagram,
    ClassEntity,
    DiagramEntity,
    PackageDiagram,
    PackageEntity,
)
from sphinx.environment import BuildEnvironment
from typing import Iterable

# /usr/lib/python3/dist-packages/sphinx/ext/inheritance_diagram.py
class UmlGraph:
    """
    The :py:class:`UmlGraph` aims at exporting UML diagrams
    to SVG images. Its implementation is based on
    py:class:`sphinx.ext.inheritance_diagram.InheritanceGraph`
    so that we call the following function using it:

    - :py:func:`latex_visit_inheritance_diagram`
    - :py:func:`html_visit_inheritance_diagram`

    See:
    ``/usr/lib/python3/dist-packages/sphinx/ext/inheritance_diagram.py``
    """
    def __init__(
        self,
        #diadefs: Iterable[ClassDiagram | PackageDiagram],  # <----- Not picklizable
        config: argparse.Namespace,
        with_classes: bool = True,
        with_packages: bool = True,
    ):
        #print(f"UmlGraph({type(diadefs)=}, {type(config)=}, {with_classes=}, {with_packages=})")
        #self.diadefs = diadefs
        self.config = config
        self.with_classes = with_classes
        self.with_packages = with_packages

    def class_names(self, diagram: ClassDiagram) -> Iterable:
        """
        Retrieves all of the class names involved in a class diagram.
        Based on the :py:meth:`DiagramWriter.write_packages` method.

        Args:
            diagram (ClassDiagram): A class diagram.
        """
        for obj in sorted(diagram.objects, key=lambda x: x.title):
            obj.fig_id = obj.node.qname()
            if self.config.no_standalone and not any(
                obj in (rel.from_object, rel.to_object)
                for rel_type in ("specialization", "association", "aggregation")
                for rel in diagram.get_relationships(rel_type)
            ):
                continue
            yield obj.fig_id

    def module_names(self, diagram: PackageDiagram) -> Iterable:
        """
        Retrieves all of the module names involved in a module diagram.
        Based on the :py:meth:`DiagramWriter.write_classes` method.

        Args:
            diagram (ClassDiagram): A module diagram.
        """
        for module in sorted(diagram.modules(), key=lambda x: x.title):
            module.fig_id = module.node.qname()
            if self.config.no_standalone and not any(
                module in (rel.from_object, rel.to_object)
                for rel in diagram.get_relationships("depends")
            ):
                continue
            yield module.fig_id

    def vertex_names(self) -> Iterable:
        return []
#        """
#        Retrieves all of the vertex names involved in the graph.
#        Based on the :py:meth:`DiagramWriter.write` method.
#        """
#        for diagram in self.diadefs:
#            if isinstance(diagram, PackageDiagram):
#                yield from self.module_names(diagram)
#            elif isinstance(diagram, ClassDiagram):
#                yield from self.class_names(diagram)
#            else:
#                raise TypeError("{type(diagram=)}")
#
    def generate_dot(
        self,
        name: str,
        urls: dict[str, str] | None = None,
        env: BuildEnvironment | None = None,
        graph_attrs: dict | None = None,
        node_attrs: dict | None = None,
        edge_attrs: dict | None = None,
    ) -> str:
        """
        Generates a graphviz dot graph from the UML diagram definitions
        passed stored in :py:attr:`self.diadef`.

        Args:
            name (str): The name of the graph.
            urls (dict[str, str] | None): An optional dictionary mapping
                class names to HTTP URLs.
            graph_attrs (dict | None): An optional dictionary storing the
                graph-related Graphviz properties.
            node_attrs (dict | None): An optional dictionary storing the
                node-related Graphviz properties.
            edge_attrs (dict | None): An optional dictionary storing the
                edge-related Graphviz properties.
        """
        print("CALLING generate_dot")
        # Graphviz settings
        if urls is None:
            urls = {}
        g_attrs = self.default_graph_attrs.copy()
        n_attrs = self.default_node_attrs.copy()
        e_attrs = self.default_edge_attrs.copy()
        if graph_attrs is not None:
            g_attrs.update(graph_attrs)
        if node_attrs is not None:
            n_attrs.update(node_attrs)
        if edge_attrs is not None:
            e_attrs.update(edge_attrs)
        if env:
            g_attrs.update(env.config.inheritance_graph_attrs)
            n_attrs.update(env.config.inheritance_node_attrs)
            e_attrs.update(env.config.inheritance_edge_attrs)

        # Graphviz string
        dotcode = "digraph { A -> B; B -> C }"
#        dwriter = writer.DiagramWriter(self.config)
#        dwriter.printer_class = DotPrinter
#        dwriter.api_doc = SphinxHtmlProxy()
#        dwriter.api_doc.set_sphinx_html_dir(self.config.sphinx_html_dir)
#        dwriter.write(self.diadefs)
#        for diagram in self.diadefs:
#            if isinstance(diagram, PackageDiagram):
#                dwriter.write_packages(diagram)
#            else:
#                dwriter.write_diagrams(diagram)
#        dotcode = "\n".join(dwriter.printer.lines)
        return dotcode

from sphinx.util.typing import ExtensionMetadata, OptionSpec
from typing import ClassVar
from docutils.parsers.rst import directives

class UMLGenerateDirective(SphinxDirective):
    """UML directive to generate a pyreverse diagram"""

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

    # Internal stuff
    DIR_NAME = "uml_images"
    # a list of modules which have been parsed by pyreverse
    generated_modules = []

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
        print("ENTERING RUN")
        doc = self.state.document
        env = doc.settings.env
        # the top-level source directory
        base_dir = Path(env.srcdir).absolute()
        print(f"{doc.settings=}")
        # the directory of the file calling the directive
        rst_dir = Path(doc.current_source).parent.absolute()
        html_dir = rst_dir / "_html"
#        uml_dir = base_dir / self.DIR_NAME
#
#        if not uml_dir.exists():
#            uml_dir.mkdir()
#
#        env.uml_dir = Path(uml_dir)
        module_name = self.arguments[0]
        print(f"{module_name=}")
        # self._validate()

        #page_name = Path(doc.current_source)  # Prefixed by src.
        #module_name = page_name.with_suffix("").name

        output_format = "dot"
        pyprocess_args = [
#            "--output", output_format,           # -o
            "--sphinx-html-dir", ".", #str(base_dir / "build" / "_html"),   # -d
#            "--output-directory", str(uml_dir),
#            "--verbose",
#            "--project", module_name,            # -p
            # "--module-names", "y",             # -m
            module_name
        ]
        pyprocess_shell = "pyreverse2 " + " ".join(pyprocess_args)
        print(pyprocess_shell)

        # make install-sphinx-custom clean-doc docs
        from .pyreverse import Run, ParsePyreverseArgs, DotPrinter, SphinxHtmlProxy
        from pylint.pyreverse.main import writer

        parser = ParsePyreverseArgs(pyprocess_args)
        runner = Run(parser.config)

        # Inheritance-diagram like injection (our goal is to get .dot)
        diadefs = runner.diadefs(parser.remaining_args)
        print(f"DIADEFS {base_dir=} {html_dir=} {runner.config.sphinx_html_dir=}")
        for diagram in diadefs:
            print(type(diagram))

        node = UmlNode()
#        node.document = self.state.document
#        class_role = self.env.domains.python_domain.role("class")
#        # Store the original content for use as a hash
#        node["parts"] = self.options.get("parts", 0)  # To alter class name display

#        # <<< See inheritance_diagram.Run.run
#        # /usr/lib/python3/dist-packages/sphinx/ext/inheritance_diagram.py
#        try:
#            graph = UmlGraph(
#                #diadefs,
#                runner.config,
#                with_classes=("classes" in self.options),
#                with_packages=("packages" in self.options),
#            )
#        except Exception as e:
#            return [node.document.reporter.warning(e, line=self.lineno)]
#
#        # Create xref nodes for each target of the graph"s image map and
#        # add them to the doc tree so that Sphinx can resolve the
#        # references to real URLs later.  These nodes will eventually be
#        # removed from the doctree after we"re done with them.
#        for name in graph.vertex_names():
#            refnodes, _ = class_role(  # type: ignore[misc]
#                "class",
#                ":class:`%s`" % name,
#                name, 0, self.state.inliner
#            )
#            node.extend(refnodes)
#        # Store the graph object so we can use it to generate the
#        # dot file later
#        node["graph"] = graph

        dwriter = writer.DiagramWriter(runner.config)
        dwriter.printer_class = DotPrinter
        dwriter.api_doc = SphinxHtmlProxy()
        dwriter.api_doc.sphinx_html_dir = runner.config.sphinx_html_dir
        #assert len(diadefs) == 1, len(diadefs)
        if isinstance(diadefs, list) and len(diadefs) > 1:
            for diagram in diadefs:
                print(diagram)
            print("picking the first diagram")
            diadefs = diadefs[0]

        dwriter.write(diadefs)

        # TODO why my node is only considered as a "graphviz" node?
        node["code"] = "\n".join(dwriter.printer.lines)
        node["options"] = {"graphviz_dot": "dot"}
        # See sphinx.ext.graphviz:render_dot_html
        node["classes"] = ["inheritance"]

        #return [nodes.paragraph(text=module_name)]
        if "caption" not in self.options:
            self.add_name(node)
            print(f"---------> {node=}")
            return [node]
        else:
            figure = figure_wrapper(self, node, self.options["caption"])
            self.add_name(figure)
            print(f"---------> {figure=}")
            return [figure]
        # >>>

#        # Wild injection
#        runner.run(parser.remaining_args)
#        uri = str(
#            Path(".")
#            / self.DIR_NAME
#            / f"classes_{module_name}.{output_format}"
#        )
#
#        print("-" * 80)
#        print(uri)
#        print("-" * 80)
#        # To craft the available nodes and their kwargs parameters, see
#        # https://docutils.sourceforge.io/docutils/nodes.py
#        # https://docutils.sourceforge.io/docutils/writers/html4css1/__init__.py
#        p1 = nodes.paragraph()
#        p1 += nodes.literal(text=f"{pyprocess_shell}")
#        p2 = nodes.paragraph("URI")
#        p2 += nodes.reference(refuri=uri)
#
#
#        return [
#            # p1,
#            # p2,
#            # ./docs/uml_images/classes_example.module.submodule.c.svg)
#            nodes.image(uri=uri)
#        ]


# /usr/lib/python3/dist-packages/sphinx/ext/inheritance_diagram.py
# Must be moved to __init__.py

#from sphinx.application import Sphinx
#from sphinx.util.typing import ExtensionMetadata
#from sphinx.ext.inheritance_diagram import (
#    latex_visit_inheritance_diagram as latex_visit_uml_node,
#    html_visit_inheritance_diagram as html_visit_uml_node,
#    texinfo_visit_inheritance_diagram as tex_visit_uml_node,
#    skip,
#)
#
#def setup(app: Sphinx) -> ExtensionMetadata:
#    app.setup_extension("sphinx.ext.graphviz")
#    app.add_node(
#        UmlNode,  # Node type
#        latex=(skip, latex_visit_uml_node),
#        html=(toto, html_visit_uml_node),
#        text=(skip, None),
#        man=(skip, None),
#        texinfo=(tex_visit_uml_node, None)
#    )
#    app.add_directive("uml", UMLGenerateDirective)
#    app.add_config_value("uml_graph_attrs", {}, "")
#    app.add_config_value("uml_node_attrs", {}, "")
#    app.add_config_value("uml_edge_attrs", {}, "")
#    app.add_config_value("uml_alias", {}, "")
#    return {
#        "version": sphinx.__display_version__,
#        "parallel_read_safe": True
#    }
