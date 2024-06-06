#!/bin/bash
set -e

cd /app

echo "Conda version: $(conda --version)"
echo "Conda version: $(which conda)"

echo "Python version: $(python --version)"
echo "Python version: $(which python)"

echo "pip version: $(pip --version)"
echo "pip version: $(which pip)"

echo "Inside $(pwd)"
ls 

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install torchsde
pip install -r requirements.txt

# If Docker complains it doesn't 
# understand the main.py it might be whitespace errors
# sed -i 's/\r//' entrypoint.sh

exec python main.py