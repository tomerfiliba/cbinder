#!/usr/bin/env python
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

HERE = os.path.dirname(__file__)
exec(open(os.path.join(HERE, "cbinder", "version.py")).read())

setup(name = "cbinder",
    version = version_string,  # @UndefinedVariable
    description = "Generate ctypes bindings directly from H files",
    author = "Tomer Filiba",
    author_email = "tomerfiliba@gmail.com",
    license = "Apache v2",
    url = "http://cbinder.readthedocs.org",
    packages = ["cbinder"],
    platforms = ["POSIX", "Windows"],
    provides = ["cbinder"],
    requires = ["srcgen>=1.1"],
    install_requires = ["srcgen>=1.1"],
    keywords = "c, ctypes, bindings, generator",
    long_description = open(os.path.join(HERE, "README.rst"), "r").read(),
    classifiers = [
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Build Tools",
    ],
)

