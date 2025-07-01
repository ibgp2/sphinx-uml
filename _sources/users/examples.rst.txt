Examples
========

This page gathers some examples of UML diagrams produced by ``sphinx-uml``.

Classes diagram
---------------

To generate a ``pyreverse`` classes diagram in you RST output, use
the following snippet by replacing ``sphinx_uml`` by any module
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
