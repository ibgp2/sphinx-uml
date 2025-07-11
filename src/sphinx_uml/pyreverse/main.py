"""
Based on the :py:mod:`pylint.pyreverse.main` module.
Under Debian, see the
``/usr/lib/python3/dist-packages/pylint/pyreverse/main.py``

**Background:**

We must overlad the :py:class:`pylint.pyreverse.main.Run` class as we need
an extra option to set the directory where Sphinx stores its output HTML files.

However, adding this option is not straightforward.
The :py:meth:`pylint.pyreverse.main.Run.__init__` constructor is monolotic
and runs the following operations:

- parsing the arguments from the CLI;
- initializing the configuration needed by the :py:meth:`pyreverse.run` method;
- calling the :py:meth:`pylint.pyreverse.main.Run.run` method with the
  remaining arguments;
- exiting the program using the :py:func:`sys.exit` function!

This design prevents to call `pyreverse` multiple times, which is needed to
process by a Sphinx extension producing muliple UML diagrams.

To address this problem, this file scatters those steps as follows:

- The :py:class:`ParsePyreverseArgs` class parses the arguments;
- The :py:class:`Run.__init__` constructor takes in parameter the configuration
  obtained from the :py:class:`ParsePyreverseArgs` class;
- The :py:class:`Run.run` constructor takes in parameter the remaining
  CLI arguments, obtained from the :py:attr:`ParsePyreverseArgs.remaining_args`
  attribute;
"""

# Inherited imports
from pylint.pyreverse.main import (
    augmented_sys_path,
    check_graphviz_availability,
    check_if_graphviz_supports_format,
    DiadefsHandler,
    DIRECTLY_SUPPORTED_FORMATS,
    # discover_package_path,
    insert_default_options,
    Linker,
    project_from_files,
    writer,
)

from pylint.config.arguments_manager import _ArgumentsManager
from pylint.config.arguments_provider import _ArgumentsProvider

# Custom imports
import argparse
from pylint.pyreverse.main import Run as _Run, OPTIONS as _OPTIONS
from .dot_printer import DotPrinter
from .sphinx_html_proxy import SphinxHtmlProxy


# << Added options
OPTIONS = [
    option
    for option in sorted(list(_OPTIONS) + [
        (
            "sphinx-html-dir",
            {
                "default": "",
                "type": "path",
                "short": "d",
                "action": "store",
                "metavar": "<input_directory>",
                "help": (
                    "set the root directory of the HTML "
                    "documentation generated by Sphinx."
                ),
            },
        )
    ])
]
# >>


class ParsePyreverseArgs(_Run):
    options = OPTIONS
    name = "pyreverse"

    # << Based on _Run.__init__
    def __init__(self, args: list[str]):
        """
        Constructor.
        Based on :py:meth:`pylint.pyreverse.main.Run.__init__`.

        Args:
            args (list[str]): The arguments passed to the script.
                *Example:* ``sys.argv[1:]``.
        """
        _ArgumentsManager.__init__(self, prog="pyreverse", description=__doc__)
        _ArgumentsProvider.__init__(self, self)

        # Parse options
        insert_default_options()
        # << We need to save them to call Run.run(...)
        self.remaining_args = self._parse_command_line_configuration(args)
        # >>

        if self.config.output_format not in DIRECTLY_SUPPORTED_FORMATS:
            check_graphviz_availability()
            print(
                f"Format {self.config.output_format} isn't supported natively."
                " pyreverse2 will try to generate it using Graphviz..."
            )
            check_if_graphviz_supports_format(self.config.output_format)


class Run:
    def __init__(self, config: argparse.Namespace):
        """
        Constructor.

        Args:
            config (argparse.Namespace): The configuration parsed from the
                command line. See also the ;py:class;`ParsePyreverseArgs`
                class.

        Returns:
            The execution code (``0`` means everything is fine).
        """
        # pylint.pyreverse.main.Run is meant to be called only once
        # so let's rewrite __init__:
        self.config = config

    def diadefs(self, args: list[str]):
        # Squeeze extra_packages_paths, because it explores src/
        # TODO: We should see what pyreverse does
        # (especially, what is the value of self.config.source_roots)
        # <<
        # extra_packages_paths = list({
        #     discover_package_path(
        #         arg,                      # example.module.submodule.c1
        #         self.config.source_roots  # ()
        #     )
        #     for arg in args
        # })
        # ===
        extra_packages_paths = list()
        # >>

        with augmented_sys_path(extra_packages_paths):
            project = project_from_files(
                args,
                project_name=self.config.project,
                black_list=self.config.ignore_list,
                verbose=self.config.verbose,
            )
            linker = Linker(project, tag=True)
            handler = DiadefsHandler(self.config)
            diadefs = handler.get_diadefs(project, linker)
            return diadefs

    def run(self, args: list[str]) -> int:
        """
        Checks the arguments and pyreverses the input project.

        Args:
            args (list[str]): The remaining arguments, that are not yet
                handled by the constructor, typically, the class or module
                being pyreversed.
                *Example:* ``['example.module.submodule.c1']``.
        """
        dwriter = writer.DiagramWriter(self.config)
        # << Writer hijacking
        dwriter.printer_class = DotPrinter
        dwriter.api_doc = SphinxHtmlProxy()
        dwriter.api_doc.set_sphinx_html_dir(self.config.sphinx_html_dir)
        # NB: dwriter.write calls DotPrinter.__init__(...)
        diadefs = self.diadefs(args)
        # >>
        dwriter.write(diadefs)
        return 0
