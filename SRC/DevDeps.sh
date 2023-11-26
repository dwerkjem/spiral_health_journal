#!/bin/bash

# Define dependencies
dependencies=("libboost-all-dev")

# Function to install a single dependency
install_dependency() {
    echo "Installing $1..."
    sudo apt-get install "$1"
}

# Function to check if a dependency is installed
check_dependency() {
    dpkg -s "$1" >/dev/null 2>&1
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
for dependency in "${dependencies[@]}"
do
    if check_dependency "$dependency"; then
        echo "$dependency is already installed."
    else
        if $automatic_install; then
            install_dependency "$dependency"
        else
            echo "Would you like to install $dependency? (y/n)"
            read -r answer
            if [ "$answer" != "${answer#[Yy]}" ] ;then
                install_dependency "$dependency"
            fi
        fi
    fi
done

echo ""

echo "Developer dependencies installed. You may now run 'make' to build the project."