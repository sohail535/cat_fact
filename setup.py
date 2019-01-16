import sys
import re
import os.path

from setuptools import setup, find_packages


with open("README.md") as f:
    long_description = f.read()


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
    author="Shaik Sohail Yunus",
    author_email="sohail.yunusha1@gmail.com",
    maintainer="Shaik Sohail Yunus",
    maintainer_email="sohail.yunusha1@gmail.com",
    description="Get random cat facts fromt the internet " + u"\U0001F638",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    packages=find_packages(),
    url="https://github.com/sohail535/cat_fact",
    entry_points="""
        [console_scripts]
        catFact = cat_fact.cli:cli
    """
)

