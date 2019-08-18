#!/bin/bash
set -e

[[ ! $PATH =~ iniconda ]] && echo "Miniconda paths not found in the PATH environment variable, check your Miniconda installation." && exit

echo "Creating conda environment"
conda env create create -f environment.yml -p .venv

CONDA_ENV_PATH="$PWD/.venv"

while read requirement; do $CONDA_ENV_PATH/python -m pip install $requirement; done < requirements.txt
while read requirement; do $CONDA_ENV_PATH/python -m pip install $requirement; done < requirements_dev.txt
