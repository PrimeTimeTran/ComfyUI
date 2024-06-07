#!/bin/bash
set -e

cd /app
echo "Inside $(pwd)"
ls 
echo "Conda version: $(conda --version)"
echo "which Conda: $(which conda)"

echo "Python version: $(python --version)"
echo "which Python: $(which python)"

echo "pip version: $(pip --version)"
echo "which pip: $(which pip)"

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install torchsde scikit-image psutil einops aiohttp segment_anything cv spandrel kornia
pip install opencv-python piexif ultralytics

if [ -n "$ADDITIONAL_PACKAGES" ]; then
    pip install $ADDITIONAL_PACKAGES
fi
