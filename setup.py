#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name = "mypackage",  # FIXME change this to your egg name, which should match the root directory name in src/,
                         #       e.g. `mypackage` if your directory name is `src/mypackage`.
    version = "0.0.1",
    packages = find_packages("src"),
    package_dir = { "": "src" },
    install_requires = [  # FIXME array entries follow same logic as lines in requirements.txt
        "setuptools",
        # "requests>=2.24,<3.0",
        # "tzlocal",
        # "datadog==0.39.0",
    ],
    entry_points = {
        "console_scripts": [
            "mypackage-util = mypackage:main",  # FIXME define here any scripts you'd like to expose from your project;
                                                #       this will create a script called `mypackage-util` that calls
                                                #       mypackage.main as its entrypoint
        ]
    },
)
