#!/bin/bash
set -e

cd /app
echo "Inside $(pwd)"
ls 
echo "Conda version: $(conda --version)"
echo "Conda version: $(which conda)"

echo "Python version: $(python --version)"
echo "Python version: $(which python)"

echo "pip version: $(pip --version)"
echo "pip version: $(which pip)"

python -m venv venv
source venv/bin/activate
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install torchsde
pip install -r requirements.txt
