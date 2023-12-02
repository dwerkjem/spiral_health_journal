#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# Purpose: run.sh is a bash script to help run the project with ease and consistency
# see README.md for more details
# Author: @dwerkjem (Derek R Neilson)
# License: (see documentation/LICENSE.md for more details)
# Version: 0.1.0
# DO NOT EDIT ANYTHING ABOVE THIS LINE

check_agreement() {
    if grep -Eiq ":\s*I agree" "$1"; then
        return 0 # Agreement found
    else
        echo "You must agree to the $1 to run the project."
        return 1 # Agreement not found
    fi
}

# List of files to check
files_to_check=("documentation/LICENSE.md" "documentation/DISCLAMER.md")

# Loop through files and check for agreement
for file in "${files_to_check[@]}"; do
    check_agreement "$file" || exit 1
done

# If all agreements are found, ask if the user wants to run the project
read -r -p "Do you want to run the project? (y/n) " answer
if [ "$answer" != "${answer#[Yy]}" ]; then
    echo "Do you want to set up a virtual environment and install requirements? (y/n)"
    read -r answer
    if [ "$answer" != "${answer#[Yy]}" ] ;then
        # Check if virtual environment already exists
        if [ ! -d ".venv-SpiralHTJ" ]; then
            echo "Setting up virtual environment and installing requirements..."
            python3 -m venv .venv-SpiralHTJ
        else
            echo "Virtual environment already exists."
        fi

        # Activate virtual environment and install requirements
        # shellcheck disable=SC1091
        source .venv-SpiralHTJ/bin/activate
        pip install -r requirements.txt
    else
        echo "Skipping virtual environment and requirements..."
    fi

else
    echo "Skipping running the project..."
fi
