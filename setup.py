#!/usr/local/bin/python3

from grafana_import.constants import PKG_NAME, PKG_VERSION
from setuptools import setup, find_packages

# Global variables
name = PKG_NAME
version = PKG_VERSION
requires = ["grafana-api", "jinja2"]

setup(
    name=name,
    version=version,
    description='A Python-based application to import Grafana dashboards using the Grafana API and grafana-client python interface. Forked from="https://github.com/peekjef72/grafana-import-tool',
    long_description_content_type="text/markdown",
    long_description=open("README.md", "r").read(),
    author="author",
    author_email="",
    url="https://github.com/zerolimit5/grafana-import-tool",
    entry_points={"console_scripts": ["grafana-import = grafana_import.cli:main"]},
    packages=find_packages(),
    install_requires=requires,
    package_data={"": ["conf/*"]},
)
