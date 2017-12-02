#!/usr/bin/env bash
#be sure to update the version in setup.py and notebook_xterm/__init__.py
rm -rf dist/*
python setup.py sdist
python setup.py bdist_wheel
twine upload dist/*
