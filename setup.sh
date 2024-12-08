#!/bin/bash

# Set the virtual environment directory name
VENV_DIR="venv"

# Check if virtual environment already exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv $VENV_DIR
else
    echo "Virtual environment already exists."
fi

# Activate the virtual environment
source $VENV_DIR/bin/activate

# Upgrade pip and install dependencies
echo "Upgrading pip..."
pip install --upgrade pip

pip install pip-tools

echo "Setup complete. Virtual environment is ready."
echo "To activate the environment, run: source $VENV_DIR/bin/activate"
