#!/usr/bin/env python
"""
Created on Oct 2, 2012

@author: alendit
"""
import os

from setuptools import setup


def read(fname):
    """Reads a file in from disk and returns its contents"""
    with open(
        os.path.join(os.path.dirname(__file__), fname), "r", encoding="utf-8"
    ) as file_handle:
        return file_handle.read()


setup(
    name="sphinx-pyreverse",
    version="0.0.18",
    author="Dimitri Vorona",
    author_email="vorona@in.tum.de",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Utilities",
    ],
    description=(
        "A simple sphinx extension to generate " "UML diagrams with pyreverse"
    ),
    extras_require={
        "deploy": [
            # deps for deploying
            "twine",
        ],
        "pil": [
            # because of the vaious ways of getting PIL we reccomend, but do
            # not enfore, pillow
            "pillow",
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
    long_description=read("README.rst"),
    packages=["sphinx_pyreverse"],
    url="https://github.com/alendit/sphinx-pyreverse",
    entry_points={
        "console_scripts": [
            "pyreverse2 = sphinx_pyreverse.cli:run_pyreverse2",
        ]
    }
)
