## Setup

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Pip

pip freeze > requirements.txt
deactivate

pip list --format=freeze > requirements.txt

## Conda

conda info --envs
conda create -n myenv python=3.7
conda activate

conda install -y libtiff
conda install -y --force-reinstall pillow
