#!/bin/bash

SCRIPT_PATH="$(readlink -f "$0")"
SOURCE_FOLDER=$(dirname "$SCRIPT_PATH")

# Check if the source folder exists
if [ ! -d "$SOURCE_FOLDER" ]; then
    echo "Error: Source folder '$SOURCE_FOLDER' does not exist."
    exit 1
fi

conda build purge
build_path=$(conda build --output .)
conda build --debug .
anaconda upload "$build_path"