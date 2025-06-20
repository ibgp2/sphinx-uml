#!/usr/bin/env python
import os

from setuptools import setup


def read(fname):
    """Reads a file in from disk and returns its contents"""
    with open(
        os.path.join(os.path.dirname(__file__), fname), "r", encoding="utf-8"
    ) as file_handle:
        return file_handle.read()


setup(
    name="sphinx-uml",
    version="0.0.18",
    author="Marc-Olivier Buob",
    author_email="marc-olivier.buob@nokia-bell-labs.com",
    classifiers=[
      "Development Status :: 2 - Pre-Alpha",
      "Intended Audience :: Developers",
      "License :: OSI Approved :: Python Software Foundation License",
      "Natural Language :: English",
      "Programming Language :: Python :: 3 :: Only",
      "Programming Language :: Python :: 3.9",
      "Programming Language :: Python :: 3.10",
      "Programming Language :: Python :: 3.11",
      "Programming Language :: Python :: 3.12",
      "Programming Language :: Python :: 3.13",
      "Topic :: Documentation :: Sphinx",
    ],
    description=(
        "A simple sphinx extension to generate UML diagrams with pyreverse. "
    ),
    extras_require={
        "deploy": [
            # deps for deploying
            "twine",
        ],
        "tests": [
            "black==24.10.0",
            "docutils",
            "flake8",
            "isort==5.8.0",
            "pylint>=3.3.1",
            "pytest",
            "pytest-cov",
            "sphinx>=8.1.3",
            "sphinx-rtd-theme>=3.0.1",
        ],
    },
    install_requires=[
        "astroid>=2.5.7",
        "docutils",
        "pylint",  # for `pyreverse`
        "sphinx",
    ],
    keywords="sphinx extension uml pyreverse",
    license="GPLv3",
    long_description=read("README.md"),
    packages=["sphinx_uml"],
    url="https://github.com/ibgp2/sphinx-pyreverse",
    entry_points={
        "console_scripts": [
            "pyreverse2 = sphinx_uml.cli:run_pyreverse2",
        ]
    }
)
