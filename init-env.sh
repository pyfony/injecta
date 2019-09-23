#!/bin/bash
set -e

[[ ! $PATH =~ iniconda ]] && echo "Miniconda paths not found in the PATH environment variable, check your Miniconda installation." && exit

if [ "$(expr substr $(uname -s) 1 10)" == "MINGW64_NT" ]; then
  IS_WINDOWS=1
else
  IS_WINDOWS=0
fi

echo "Self-updating conda"
conda update -n base -c defaults conda -y

echo "Creating conda environment"
conda env create create -f environment.yml -p .venv

CONDA_ENV_PATH="$PWD/.venv"

if [ $IS_WINDOWS == 1 ]; then
  PYTHON_EXECUTABLE_PATH="$CONDA_ENV_PATH/python"
else
  PYTHON_EXECUTABLE_PATH="$CONDA_ENV_PATH/bin/python"
fi

$PYTHON_EXECUTABLE_PATH -m pip install --upgrade pip

while read requirement; do $CONDA_ENV_PATH/python -m pip install $requirement; done < requirements.txt
while read requirement; do $CONDA_ENV_PATH/python -m pip install $requirement; done < requirements_dev.txt
