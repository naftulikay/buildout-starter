buildout-starter
================

A project creation utility for starting zc.buildout Python and Django projects. 
In practical terms, `buildout-starter` is a Python script for quickly and easily
creating Python and Django projects preconfigured with Buildout and setuptools.

##Installation##

The only prerequisites for installing the project are a Python interpreter and a
bit of luck. To quickly install the script, simply use `pip`:

    sudo pip install buildout-starter

If you don't have or want `pip` for some reason, you can use `easy_install`, too:

    sudo easy_install buildout-starter

If you're a bit more adventurous, you can clone the project and compile it from 
source _because you can_:

    # clone the repository
    git clone git://github.com/rfkrocktk/buildout-starter.git
    # cd into it
    cd buildout-starter
    # bootstrap the buildout
    python buildout.py
    # run buildout to set everything up
    bin/buildout
    # manually install the project
    sudo python setup.py install

##Usage##

Script usage attempts to be as easy as possible. Here is the script help page:

```
usage: buildout-start [-h] [-p PACKAGE_NAME] [--django] [--ipython] [--pydev]
                      [--git]
                      name [parent_dir]

Creates a zc.buildout Python project with a given name.

positional arguments:
  name                  The name of the project to create.
  parent_dir            The optional parent directory to create the project
                        in. Defaults to the current directory.

optional arguments:
  -h, --help            show this help message and exit
  -p PACKAGE_NAME, --package-name PACKAGE_NAME
                        The package name to use when creating the project. By
                        default, the [name] is sanitized and used, but there
                        are times when this yields undesirable results. Pass a
                        custom name here to force a specific package name.
  --django              Create a Django project rather than a simple Python
                        project.
  --ipython             Generate an IPython interpreter in addition to the
                        regular Python interpreter in the bin directory.
  --pydev               Generate PyDev Eclipse project files.
  --git                 Generate a Git repository in the newly created
                        project. Includes .gitignore definitions.
```

In plain terms, if you'd like to create a barebones Python Buildout project, 
install the project first and then call

     buildout-start myawesomeproject

If you'd like to add in features, you can selectively add options mentioned 
above to integrate those features in your new project:

    buildout-start --ipython --git myawesomeproject

Django projects are easily created by passing the `--django` flag:

    buildout-start --ipython --django --git myawesomeproject

`buildout-starter` automatically sanitizes project names into Python package names
where applicable. This is done by removing all non-alphanumeric characters and 
simply replacing hyphens with underscores. This means a project name like 
`buildout-starter` would be sanitized to be `buildout_starter`. If this is undesired,
the package/sanitized project name can be submitted manually:

    buildout-start --ipython --git -p buildoutstarter buildout-starter

If you'd like to create the package in a directory other than the current one, 
you can specify that directory after the project name:

    buildout-start --git myawesomeproject ~/Documents/Projects/
