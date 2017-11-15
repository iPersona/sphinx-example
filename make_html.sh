#!/bin/sh

# venv/bin/sphinx-quickstart
# venv/bin/sphinx-apidoc -o docs/ code/
cd docs
make html SPHINXBUILD=../venv/bin/sphinx-build
cd ..