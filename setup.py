#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = "buildoutstarter",
    version = "0.0.1-SNAPSHOT",
    packages = find_packages('src'),
    package_dir = { '': 'src'},
    install_requires = ['setuptools', 
    ],
)