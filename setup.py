"""
cat_fact
-------

The client interface for cat fact

Install
~~~~~~~

..code:: bash

    python setyp.py install
"""

import sys
import re
import os.path

from setuptools import setup, find_packages


def get_version():
    """Returns the package version taken from version.py
    """
    root = os.path.dirname(__file__)
    version_path = os.path.join(root, "cat_fact/__init__.py")
    text = open(version_path).read()
    rx = re.compile("^__version__ = '(.*)'", re.M)
    m = rx.search(text)
    version = m.group(1)
    return version


install_requires = [
    "click>=6.7",
    "requests>=2.21"
]


setup(
    name="cat_fact",
    version=get_version(),
    author="The great me",
    author_email="author@me.com",
    description="A cat fact cli",
    long_description=__doc__,
    install_requires=install_requires,
    packages=find_packages(),
    entry_points="""
        [console_scripts]
        catFact = cat_fact.cli:cli
    """
)

