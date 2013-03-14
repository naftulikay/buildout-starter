#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = "buildoutstarter",
    description = "A project creation utility for starting zc.buildout Python and Django projects.",
    url = "https://github.com/rfkrocktk/buildout-starter",
    author = "Naftuli Tzvi Kay",
    author_email = "naftulitzvikay@gmail.com",
    version = "0.1.0",
    license = "LGPL",
    packages = find_packages('src'),
    package_dir = { '': 'src'},
    install_requires = ['setuptools',
        'jinja2 == 2.6'
    ],
    entry_points = {
        'console_scripts': [
            'buildout-start = buildoutstarter:main',
        ],
    },
)
