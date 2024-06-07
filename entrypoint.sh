#!/bin/bash
set -e

cd /app

echo "Conda version: $(conda --version)"
echo "which Conda: $(which conda)"

echo "Python version: $(python --version)"
echo "which Python: $(which python)"

echo "pip version: $(pip --version)"
echo "which pip: $(which pip)"

echo "Inside $(pwd)"
ls 

# If Docker complains it doesn't 
# understand the main.py it might be whitespace errors
# sed -i 's/\r//' entrypoint.sh
exec python main.py