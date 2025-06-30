
Examples
========

This page gathers some examples of UML diagrams produced by ``sphinx-uml``.

Display parameters
------------------
Options
~~~~~~~

As shown in the following examples, the options passed to the ``.. uml``
directive defines what will be displayed and how it will be rendered.

- ``:classes:`` enables the UML class diagram display.
- ``:packages:`` enables the package diagram display.
- ``:caption: S``, where ``S`` is an arbitrary RST line of text, defines the
  caption of the resulting image(s).

Configuration
~~~~~~~~~~~~~

The display also depends on the parameters defined in your
Sphinx configuration file (e.g., ``docs/conf.py``).
The following output also uses pyreverse ``colorized`` and ``ancestors``
options by specifying the following in your Sphinx ``conf.py``.

.. code-block:: py

  # sphinx-uml switches
  uml_colorized = True  # colour the graphs
  uml_all_ancestors = True  # give more Sphinx context
  uml_all_associated = True

See the configuration section for further details.

Classes diagram
---------------

To generate a ``pyreverse`` classes diagram in you RST output, use
the following snippet by replacing ``sphinx_uml`` by your module
of interest.

.. code-block:: rst

  .. uml:: sphinx_uml
     :classes:
     :caption: Classes of ``sphinx_uml``

*Result:*

.. uml:: sphinx_uml
   :classes:
   :caption: Classes of ``sphinx_uml``


Packages diagram
----------------

To generate a high-level packages overview graph
simply use the following RST:

.. code-block:: rst

  .. uml:: sphinx_uml
     :packages:
     :caption: Packages of ``sphinx_uml``

*Result:*

.. uml:: sphinx_uml
   :packages:
   :caption: Packages of ``sphinx_uml``

Both
----

``classes`` and ``packages`` are not mutually exclusive:

.. code-block:: rst

  .. uml:: sphinx_uml
     :packages:
     :classes:
     :caption: Packages and classes of ``sphinx_uml``

*Result:*

.. uml:: sphinx_uml
   :packages:
   :classes:
   :caption: Both
