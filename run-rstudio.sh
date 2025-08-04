#!/bin/bash

# Check if a module name was provided as a parameter
if [ -z "$1" ]; then
    echo "Error: Please provide the name of the target module."
    echo "Usage: $0 <module_name>"
    exit 1
fi

# The first command-line parameter ($1) is the target module name
TARGET_MODULE="$1"

# Get the directory where this script is located
SCRIPT_DIR="$(dirname "$0")"

# Navigate up one level from the script's directory, then down into the target module
TARGET_DIR="${SCRIPT_DIR}/main/${TARGET_MODULE}"

# Check if the target directory exists
if [ ! -d "$TARGET_DIR" ]; then
    echo "Error: Target module directory '$TARGET_DIR' does not exist."
    exit 1
fi

# Change to the target directory to find the project file
cd "$TARGET_DIR"

# Find the first .Rproj file in the target directory
PROJECT_FILE=$(ls | grep '\.Rproj$' | head -n 1)

if [ -z "$PROJECT_FILE" ]; then
    echo "No .Rproj file found in the '$TARGET_MODULE' directory."
    exit 1
fi

echo "Opening project: $PROJECT_FILE from '$TARGET_MODULE'..."

# Open the R project file
rstudio "$PROJECT_FILE" &
