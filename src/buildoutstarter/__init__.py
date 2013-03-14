#!/usr/bin/env python

from buildoutstarter.config import BOOTSTRAP_URL
from buildoutstarter.templates import SETUP_SCRIPT_TEMPLATE, BUILDOUT_CONFIG_TEMPLATE, GITIGNORE_TEMPLATE

from jinja2 import Template

import argparse, os, re, shutil, subprocess, sys, urllib2

def main():
    parser = argparse.ArgumentParser(description = "Creates a zc.buildout Python project " + 
            "with a given name.")
    parser.add_argument("name", help="The name of the project to create.")
    parser.add_argument("parent_dir", help="The optional parent directory to create the " +
            "project in. Defaults to the current directory.", nargs="?", 
            default = os.getcwd())
    parser.add_argument("-p", "--package-name", help="The package name to use when creating " +
            "the project. By default, the [name] is sanitized and used, but there are times " +
            "when this yields undesirable results. Pass a custom name here to force a specific " +
            "package name.", default=None, required=False)
    parser.add_argument("--django", help="Create a Django project rather than a " +
            "simple Python project.", action="store_true")
    parser.add_argument("--ipython", help="Generate an IPython interpreter in addition " + 
            "to the regular Python interpreter in the bin directory.", action="store_true")
    parser.add_argument("--pydev", help="Generate PyDev Eclipse project files.",
            action="store_true")
    parser.add_argument("--git", help="Generate a Git repository in the newly " + 
            "created project. Includes .gitignore definitions.", action="store_true")
    args = parser.parse_args()
    
    parameters = GeneratorParameters(directory = os.path.join(args.parent_dir, args.name), 
            project_name = args.name, 
            sanitized_project_name = args.package_name if args.package_name else sanitize_name(args.name), 
            is_django = args.django, is_ipython = args.ipython, is_pydev = args.pydev,
            is_git = args.git)

    # if the parent directory doesn't exist, get outta here
    if not os.path.isdir(args.parent_dir):
        sys.stderr.write("ERROR: Directory '{}' doesn't exist!\n".format(args.parent_dir))
        sys.exit()

    # if the directory already exists
    if os.path.isdir(parameters.directory):
        sys.stderr.write("ERROR: Directory already exists for project '{}'\n".format(
            parameters.directory))
        sys.exit()

    # create project directory
    os.mkdir(parameters.directory)

    # get the bootstrap.py script
    print "Downloading bootstrap script...",
    sys.stdout.flush()
    download_bootstrap_script(parameters.directory)
    print "done!"

    # generate setup.py
    generate_setup_script(parameters)

    # generate buildout.cfg
    generate_buildout_config(parameters)
    
    # generate project contents
    generate_project_contents(parameters)
    
    # call bootstrap
    bootstrap_project(parameters.directory)

    # buildout the project
    buildout_project(parameters.directory)

    # if it's a django project, generate a django project
    if parameters.is_django:
        generate_django_project(parameters)

    # if git support is enabled, generate a git repository and .gitignore file
    if parameters.is_git:
        generate_git(parameters)

def download_bootstrap_script(directory):
    """Downloads the bootstrap.py script in the target directory."""
    with open(os.path.join(directory, "bootstrap.py"), "w") as outfile:
        outfile.write(urllib2.urlopen(BOOTSTRAP_URL).read())

def generate_setup_script(parameters):
    """Generates a setup.py script in the target directory."""
    with open(os.path.join(parameters.directory, "setup.py"), "w") as outfile:
        outfile.write(Template(SETUP_SCRIPT_TEMPLATE).render(parameters.to_dict()).strip())

def generate_buildout_config(parameters):
    """Generates a buildout configuration file in the target directory."""
    with open(os.path.join(parameters.directory, "buildout.cfg"), "w") as outfile:
        outfile.write(Template(BUILDOUT_CONFIG_TEMPLATE).render(parameters.to_dict()).strip())
     
def generate_git(parameters):
    """Generates a Git repository in the target directory."""
    # generate .gitignore
    with open(os.path.join(parameters.directory, ".gitignore"), "w") as outfile:
        outfile.write(Template(GITIGNORE_TEMPLATE).render(parameters.to_dict()).strip())
    # generate git repository.
    subprocess.call(["git", "init"], cwd=parameters.directory)
    # add .gitignore to git
    subprocess.call(["git", "add", ".gitignore"], cwd=parameters.directory)


def generate_project_contents(parameters):
    """Generates project directory structure and initial Python package."""
    if not parameters.is_django:
        # make source package dirs
        os.makedirs(os.path.join(parameters.directory, 'src', 
            parameters.sanitized_project_name))
        # touch initial file
        with open(os.path.join(parameters.directory, 'src', 
                parameters.sanitized_project_name, '__init__.py'), 'w'):
            pass
    else:
        os.mkdir(os.path.join(parameters.directory, 'src'))

def generate_django_project(parameters):
    """Fixes the Django project produced by the django recipe."""
    subprocess.call([os.path.join("bin", "python"), "-c", "from django.core.management import call_command ; " +
        "call_command('startproject', '{}', 'src')".format(parameters.sanitized_project_name)],
        cwd=parameters.directory)
    os.remove(os.path.join(parameters.directory, 'src', 'manage.py'))

def bootstrap_project(directory):
    """Run the bootstrap script."""
    subprocess.call(["python", "bootstrap.py"], cwd=directory)

def buildout_project(directory):
    """Run the buildout on the project."""
    subprocess.call(os.path.join("bin", "buildout"), cwd=directory)

def sanitize_name(project_name):
    """
    Sanitizes a project name to be a valid Python package name.
    
    Replaces hyphens with underscores and deletes periods and all other non-
    alphanumeric characters.
    """
    project_name = project_name.strip()
    # convert hyphens
    project_name = re.sub(r'-', "_", project_name)
    # obliterate other characters
    project_name = re.sub(r'[^_A-Za-z0-9]', '', project_name)

    return project_name

class GeneratorParameters:
    directory = None
    project_name = None
    sanitized_project_name = None
    is_django = False
    is_ipython = False
    is_pydev = False
    is_git = False

    def __init__(self, directory = None, project_name = None,
            sanitized_project_name = None, is_django = False, is_ipython = False,
            is_pydev = False, is_git = False):
        self.directory = directory
        self.project_name = project_name
        self.sanitized_project_name = sanitized_project_name
        self.is_django = is_django
        self.is_ipython = is_ipython
        self.is_pydev = is_pydev
        self.is_git = is_git

    def to_dict(self):
        return { 'directory': self.directory, 'project_name': self.project_name,
                'sanitized_project_name': self.sanitized_project_name, 
                'is_django': self.is_django, 'is_ipython': self.is_ipython,
                'is_pydev': self.is_pydev, 'is_git': self.is_git }

if __name__ == "__main__":
    main()
