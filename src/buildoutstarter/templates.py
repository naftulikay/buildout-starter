SETUP_SCRIPT_TEMPLATE = """#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = "{{ sanitized_project_name }}",
    version = "0.0.1-SNAPSHOT",
    packages = find_packages('src'),
    package_dir = { '': 'src'},
    install_requires = ['setuptools', {% if is_django %}
        'django == 1.5',{%- endif %}{% if is_ipython %}
        'ipython >= 0.13.1',{%- endif %}
    ],
)"""

BUILDOUT_CONFIG_TEMPLATE = """[buildout]
parts = python_section{% if is_pydev %} pydev_section{% endif %}{% if is_django %} django_section{% endif %}{% if is_ipython %} ipython_section{% endif %}
develop = .
eggs = {{ sanitized_project_name }}
versions = versions

[versions] {% if is_django %}
django = 1.5.0{%- endif %}
ipython = 0.13.1

[python_section]
recipe = zc.recipe.egg
interpreter = python
eggs = ${buildout:eggs}{% if is_pydev %}

[pydev_section]
# for working in eclipse
recipe = collective.recipe.pydevproject
name = {{ project_name }}
src = src
python_version = python 2.7
python_interpreter = Default
eggs = ${buildout:eggs}{%- endif %}{% if is_ipython %}

[ipython_section]
recipe = zc.recipe.egg:scripts
eggs = ${buildout:eggs}
    ipython
scripts = ipython{%- endif %}{% if is_django %}

[django_section]
recipe = djangorecipe
project = {{ sanitized_project_name }}
projectegg = {{ sanitized_project_name }}
settings = settings
control-script = django
eggs = ${buildout:eggs}
wsgi = true
fcgi = true{%- endif %}"""

GITIGNORE_TEMPLATE = """# Python Ignore Filters
*.pyc
*.pyo

# Buildout Ignore Filters
bin
develop-eggs
eggs
parts
.installed.cfg
src/{{ sanitized_project_name }}.egg-info{% if is_pydev %}

# PyDev Filters
.pydevproject{%- endif %}"""

