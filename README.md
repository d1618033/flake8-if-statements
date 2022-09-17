# flake8-if-statements

[![pypi](https://badge.fury.io/py/flake8-if-statements.svg)](https://pypi.org/project/flake8-if-statements)
[![Python: 3.6+](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://pypi.org/project/flake8-if-statements)
[![Downloads](https://img.shields.io/pypi/dm/flake8-if-statements.svg)](https://pypistats.org/packages/flake8-if-statements)
[![Build Status](https://travis-ci.org/d1618033/flake8-if-statements.svg?branch=master)](https://travis-ci.org/d1618033/flake8-if-statements)
[![Code coverage](https://codecov.io/gh/d1618033/flake8-if-statements/branch/master/graph/badge.svg)](https://codecov.io/gh/d1618033/flake8-if-statements)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://en.wikipedia.org/wiki/MIT_License)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Description

Flake8 linter for if statements


### Checks:


* IFS001: Use one liner so as not to repeat assignment to the same variable

e.g: 

Bad:

```python
if x == 1:
    y = 10
else:
    y = 11
```

Good:

```python
y = 10 if x == 1 else 11
```


## Installation

    pip install flake8-if-statements

## Usage

`flake8 <your code>`

## For developers

### Create venv and install deps

    make init

### Install git precommit hook

    make precommit_install

### Run linters, autoformat, tests etc.

    make pretty lint test

### Bump new version

    make bump_major
    make bump_minor
    make bump_patch

## License

MIT

## Change Log

Unreleased
-----

* ...

1.0.0 - 2022-09-17
-----

* Changed IFSTMT to IFS to comply with flake8
* Remove python3.6 support

0.1.0 - 2020-03-14
-----

* initial
