# Python REPL, packages, virtual environments and poetry

<!-- TOC -->

- [Python REPL, packages, virtual environments and poetry](#python-repl-packages-virtual-environments-and-poetry)
    - [Python Shell and REPL](#python-shell-and-repl)
    - [Packages](#packages)
        - [What are packages?](#what-are-packages)
        - [Types of packages](#types-of-packages)
            - [Python build-in packages](#python-build-in-packages)
            - [3rd party packages](#3rd-party-packages)
        - [Installing packages](#installing-packages)
        - [Useful packages commands](#useful-packages-commands)
    - [Virtual environments](#virtual-environments)
        - [Create a virtual env](#create-a-virtual-env)
        - [Activate the virtual env](#activate-the-virtual-env)
        - [Deactivate venv](#deactivate-venv)
    - [Python is poetry](#python-is-poetry)
        - [Installing poetry](#installing-poetry)
        - [Init or install](#init-or-install)
        - [create, activate and exit](#create-activate-and-exit)
        - [pyproject.yml](#pyprojectyml)
        - [install / show / remove packages](#install--show--remove-packages)
        - [Additional config](#additional-config)
    - [Homework](#homework)

<!-- /TOC -->

## Python Shell and REPL

Python gives you the ability to tinker and run commands without writing a script.

It gives you an interactive shell out of the box.

```bash
$ python3 # and hit ENTER
```

Now you have an interactive shell which evaluates your python instructions. Neat!

Let's try some commands.

```python
>>> 15 / 2

>>> d = 15 // 2

>>> [i for i in range(0,10)] # list comprehension

>>> [i for i in range(0,10) if i % 2 == 0]

>>> {i:i**2 for i in range(0,5)} # dict comprehension. notice i:i**2 key-value pair

>>> def yah():
>>>     print('hello)

>>> ls
```

Python has some special modules that we can import from shell.

```python

>>> import this
>>> import antigravity
```

For one-liners you can use

```bash
$ python3 -c "print('hello');print('world')"
```


## Packages

### What are packages?

A python package is basically a folder having `__init__.py` and other `*.py` files that are "packaged" together in one file for easy distribution.

### Types of packages

Depending on where you install packages there are:

- system wide packages
- user local packages
- virtual environments packages

Depending if installed or not:

- built-in pacakges
- 3rd party packages

#### Python build-in packages

Python comes with a lot of useful packages pre installed.

Here is the list of [packages](https://docs.python.org/3/library/index.html).

Open a python shell and execute the commands.

```python
>>> import sys
>>> sys.path

>>> d = {chr(i):i for i in range(80,100)}
>>> from pprint import pprint, pformat

>>> pprint(d)
>>> d_formatted = pformat(d)
```

#### 3rd party packages

A whole universe of 3rd party packages can be found on [pypi](https://pypi.org/).

Search for **ipython**.

### Installing packages

By default from version **>3.4**, python is shipped with it's own package manager named **pip**.

Let's install a package.

```bash
$ python3 -m pip install ipython
```

NOTE: if you know have only one version of python installed, you can use `pip install ipython`.

Let's use the newly installed package.

```bash
$ python3 -m ipython # or just `ipython` on some systems
```

### Useful packages commands

```bash
$ python -m pip install -U pip # upgrade pip to latest version
$ python3 -m pip --help
$ pip uninstall <package name>
$ pip list
$ pip freeze
$ pip freeze > requirements.txt
```

## Virtual environments

[Virtual environments](https://docs.python.org/3/tutorial/venv.html) are configurations of python versions and a set of packages installed only for that python version.

They are very useful if you are working on multiple projects. All project related dependencies / packages contained in the virtual environment.

### Create a virtual env

```bash
$ python -m venv .venv # .venv is the folder name. it can be anything
```

Great. You've created a python virtual environment. Now what?

### Activate the virtual env

```bash
$ source ./.venv/bin/activate
```

Note: `. ./.venv/bin/activate` works too. source is aliased as ".".

Let's see what packages are installed.

```bash
$ pip list
$ pip install black
$ pip list
```

Note: All packages runned with `python` will use the `virtual env` binary, not the global, system one.

### Deactivate venv

```bash
$ deactivate
```

If you do not need the virtual environment anymore, you can just delete the folder where you created it.

## Python is poetry

[Poetry](https://python-poetry.org/docs/) is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

Poetry is a tool that acts as a virtual environment, package manager and package creator, all in one. It's a tool that manages all python for your project.

### Installing poetry

```bash
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
$ poetry --version
$ poetry --help
```

If the command is not found, set your PATH for [poetry](https://python-poetry.org/docs/#installation).

### Init or install

If we are starting a project from scratch, we need to use init. If we git clone a project, we use install

```bash
$ poetry init # or poetry install on cloned repos
```

### create, activate and exit

```bash
$ poetry init
$ ls -lah # notice no venv created yet

$ poetry shell
$ exit # leave virtual environment
```

Additional information about where does poetry create the venv can be seen with

```bash
$ poetry env info
```

### pyproject.yml

`Pyproject.yml` is a file containing all information about the python project. It included production packages, development packages, python version and more.

This file holds all project information and dependencies and should not be deleted.

### install / show / remove packages

Installing packages requires adding them to your project.

```bash
$ poetry add black
$ poetry add isort --dev
$ poetry add isort pylint --dev

$ less pyproject.yml
```

Adding packages will create or update a file named `poetry.lock`. This file has all package versions and exact hashes for your packages.

Showing installed packages in current venv.

```bash
$ poetry show
```

Removing packages

```bash
$ poetry remove black
```

### Additional config

By default poetry does not create virtual environments in current project folder. This can be changed using this setting.

```bash
$ export PIPENV_VENV_IN_PROJECT=true
```

## Homework

- Create a project using poetry
- Add `black`, `isort`, `pylint` as dev dependencies
- Add a **main.py** with some lines of code. ( anything )
- Add project to git
- Push project to your github account
- Pat yourself on the back for a job well done!

Optional for now but needs to be done

- integrate `black`, `isort` and `pylint` in your IDE ( on save runs black, isort and pylint )
- add `export PIPENV_VENV_IN_PROJECT=true` to `.bashrc` file
