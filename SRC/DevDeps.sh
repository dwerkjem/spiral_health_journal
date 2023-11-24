#!/bin/bash

# Define dependencies
dependencies=("libboost-all-dev")

# Function to install a single dependency
install_dependency() {
    echo "Installing $1..."
    sudo apt-get install "$1"
}

# Parse command-line arguments
automatic_install=false
while getopts ":y" opt; do
  case $opt in
    y)
      automatic_install=true
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
  esac
done

# Install dependencies
for dep in "${dependencies[@]}"; do
    if [ "$automatic_install" = true ] ; then
        install_dependency "$dep"
    else
        read -rp "Do you want to install $dep? [Y/n] " answer
        case $answer in
            [Yy]* ) install_dependency "$dep";;
            * ) echo "Skipping $dep";;
        esac
    fi
done
