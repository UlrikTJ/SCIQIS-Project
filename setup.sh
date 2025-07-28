#!/bin/bash
set -e

# Determine project name based on current directory
PROJECT_NAME=$(basename "$PWD")
KERNEL_NAME="python-$PROJECT_NAME"

echo "🔧 Creating virtual environment with uv..."
uv venv
source .venv/bin/activate

echo "Initiating project"
uv init

echo "📦 Adding core packages (jupyterlab, ipykernel)..."
uv add jupyterlab ipykernel

echo "📋 Syncing dependencies..."
uv sync

echo "🧠 Registering Jupyter kernel: $KERNEL_NAME"
.venv/bin/python -m ipykernel install --user \
  --name "$KERNEL_NAME" \
  --display-name "Python ($PROJECT_NAME)"

echo "🚀 To launch Jupyter Lab with this environment:"
echo ".venv/bin/jupyter lab    or    uv run jupyter lab"
