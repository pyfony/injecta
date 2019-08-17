#!/bin/bash
shopt -s globstar
set -e

PATH=$PWD/.venv:$PATH
export PYTHONPATH="$PWD/src"

for x in **/*Test.py; do printf "\nRunning $x:\n\n" && python "$x"; done
