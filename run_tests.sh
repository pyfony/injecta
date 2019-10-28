#!/bin/bash
shopt -s globstar
set -e

for x in **/*Test.py; do printf "\nRunning $x:\n\n" && python "$x"; done
