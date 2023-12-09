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

.venv-SpiralHTJ/bin/python3 src/argparser.py "$@"