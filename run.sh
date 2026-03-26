#!/bin/bash

# Activate the virtual environment
if [ -d ".venv" ]; then
    source .venv/bin/activate
else
    echo "Virtual environment (.venv) not found. Please create it first using 'uv venv'."
    exit 1
fi

# Run ComfyUI on port 6003 with the manager enabled
python main.py --port 6003 --listen 0.0.0.0 --enable-manager
