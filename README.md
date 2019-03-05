[![Build Status](https://travis-ci.com/KhelaHobe/Backend.svg?branch=master)](https://travis-ci.com/KhelaHobe/Backend)
[![Coverage Status](https://coveralls.io/repos/github/KhelaHobe/Backend/badge.svg?branch=master)](https://coveralls.io/github/KhelaHobe/Backend?branch=master)
# KhelaHobe
Project Khelahobe is an online social application where users can create and join groups. Groups can challenge each other to play game based on mutual interest. [Project specification](https://paper.dropbox.com/doc/Project-KhelaHobe-Spec--AYqL9fIkEkW6XGPeSIDcxh~bAQ-FKa0RW5evbVd96nvyTAb8) will give an overview what we are aiming.

# Project setup

## Download
Get the repository in local machine

`git clone https://github.com/KhelaHobe/Backend.git`

## Setup python
We will use python 3.6 for this project. Ensure that you have already python 3.6 installed

`python3.6 --version`

You should create a virtual environmnet (which is a good practice) for this project in the repository directory if specified python version is not your default python.

`python3.6 -m venv env`

(Remember to actiavte the environment before working on)

`source env/bin/activate`

From now on all `python` commands will mean specified python version is being used.

## Unit test
We will use pytest 4.3. Test files are under UnitTests folder. Run unit tests using 
`pytest UnitTests/`

## Code lint
We will use pylint 2.3. [PEP8](https://www.python.org/dev/peps/pep-0008/) guide will be followed. Source folder contains sample.py which contains example of PEP8 style python codes

## CI
Will use [travis](https://travis-ci.com/KhelaHobe/Backend) for continuous integration, .travis.yml file is the configuration for travis.

## Coverage
To display unit testing coverage will use [coveralls](https://coveralls.io/github/KhelaHobe/Backend). Travis will post unit test report to coverage.
