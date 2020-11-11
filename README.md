# buildout-starter [![Build Status][travis.svg]][travis]

Example project to get you going with Buildout.

## Requirements

 - `pyenv`: Make sure that `pyenv` is installed and on your `PATH`

## Getting Started

With `pyenv` installed, install the project-specified Python version:

```shell
pyenv install
```

This will read the `.python-version` file in the local directory and ensure that the right Python version is installed
and configured. If the Python version is already installed, there is no need to reinstall it.

Next, install `buildout`:

```shell
pip install -r requirements.txt
```

> **NOTE:** With a standard Python installation using `pyenv`, it's usually not necessary to use the `--user` flag with
> `pip install`, if you're doing something more exotic, you might need to.

This will install all dependencies listed in `requirements.txt`. In a Buildout project, usually the only dependency
listed here will be `zc.buildout` itself, and `buildout` will use its own internal mechanisms for managing dev and
runtime dependencies and utilities.

```shell
buildout
```

Running `buildout` will download dependencies and setup the local project for development. If you add/remove/update
dependencies, you'll need to run `buildout` again. More generally, if you change `setup.py` or `buildout.cfg`, run
`buildout` to get everything up to date.

Finally, you'll now notice executables in `bin/`:

 - `bin/python`: the Python interpreter for the project.
 - `bin/ipython`: an IPython interactive environment for the project.
 - `bin/test`: the Nose test runner, will execute all tests found in any project file named `tests.py`. Suppports both
   Nose tests and traditional `unittest` tests.
 - `bin/mypackage-util`: entry-point to the current project's `mypackage.main` function.

All of these scripts use Buildout's local eggs in a sandbox. This makes things especially nice when interactively
engaging with your source code using IPython: you can import `mypackage` and any other Python libraries used by the
project.

## Files

### `.python-version`

Used by `pyenv` to specify the Python version for the current project.

### `buildout.cfg`

An INI-format configuration file for Buildout. To adapt for your use, replace `mypackage` in this file with the name
of your egg. This name should match the directory name in `src/`.

### `requirements.txt`

`pip` requirements file; only contains `zc.buildout` to get the `buildout` tool installed locally.

### `setup.py`

The traditional `setuptools` definition file for your project. This defines many different things, but primarily
specifies your project's dependencies and scripts it exposes. To adapt for your use, replace `mypackage` with your egg
name. This name should match the directory name in `src/`.

### `src/mypackage`

The root directory for your project. Rename this directory if you have changed your project/egg name.

## License

Licensed at your discretion under either:

 - [Apache Software License, Version 2.0](./LICENSE-APACHE)
 - [MIT License](./LICENSE-MIT)

 [travis]: https://travis-ci.org/naftulikay/buildout-starter
 [travis.svg]: https://travis-ci.org/naftulikay/buildout-starter.svg?branch=master
