## Install

## Setup(MacOS)

```sh
# Try Conda first. If unsuccessful in installing dependencies in one go from file, install them one by one
pip install -r requirements-macos.txt
conda env create comfy --file=environment-macos.yaml
conda activate comfy
conda install --file requirements-macos.txt
python main.py
```

## Setup(Windows/WSL with CUDA)

### 1.a Check Dev Environment is Ok

- Highly recommend that pip & python are installed/managed by anaconda. It's worth the time uninstalling and then reinstalling python & pip entirely to ensure this is the case.

```sh
which conda
# -> /c/ProgramData/anaconda3/Scripts/conda
conda --version
# -> conda 24.5.0

pip --version
# -> pip 24.0 from C:\ProgramData\anaconda3\Lib\site-packages\pip (python 3.11)
which pip
# -> /c/ProgramData/anaconda3/Scripts/pip

python --version
# -> Python 3.11.7
which python
# -> /c/ProgramData/anaconda3/python
```

### Check Cuda Drivers Installed & Versions

```sh
nvcc --version

# Prints something like this. Version 12.1 is the Cuda version configured(if multiple versions are installed)

# nvcc: NVIDIA (R) Cuda compiler driver
# Copyright (c) 2005-2023 NVIDIA Corporation
# Built on Wed_Feb__8_05:53:42_Coordinated_Universal_Time_2023
# Cuda compilation tools, release 12.1, V12.1.66
# Build cuda_12.1.r12.1/compiler.32415258_0

# View the highest version of Cuda your GPU supports.
nvidia-smi
```

    - View the defined Cuda driver for your machine.
    - Make sure to run in Git Bash.
    - The Powershell & Command prompt has been observed to spit out stale results.

### 1.b Install the CUDA built primary torch libs so other packages don't complain later.

Replace the url in the following `pip install` command with a url you find on the PyTorch [website](https://pytorch.org/get-started/locally/).

Note: The url below, https://download.pytorch.org/whl/cu121, needs to be replaced to match your CUDA version.

```sh
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install torchsde
pip install -r requirements.txt
```

### 2. Install packages using both pip & conda.

Some packages aren't available on conda so we have to install via pip. They're not mutually exclusive.

```sh
pip install -r requirements-windows.txt
conda env create comfy --file=environment-windows.yml -y
conda activate comfy
```

### Run app

```sh
python main.py
```

### Check Torch Installation

- Verify CUDA Installation works

```sh
echo '
python
import torch
x = torch.rand(5, 3)
print(x)
' > test-torch.py
```

- Run test

```sh
python test-torch.py

# Should print something similar

# tensor([[0.3380, 0.3845, 0.3217],
#         [0.8337, 0.9050, 0.2650],
#         [0.2979, 0.7141, 0.9069],
#         [0.1449, 0.1132, 0.1375],
#         [0.4675, 0.3947, 0.1426]])
```

## Containerization

```sh
docker build .
docker build -t primetimetran/comfy .
docker images
docker run IMAGE_ID -p 8080:8188 --gpus all

# One liner
docker build -t primetimetran/comfy . && IMAGE_ID=$(docker images | awk 'NR==2 {print $3}') && docker run -p 8080:8188 $IMAGE_ID
```

```sh
# Run container from image and map ports
docker run IMAGE_ID -p 8080:8188

# Pass CLI arguments before image_id
docker run --platform=linux/x86_64 -p 808080:8188 --gpus all 3acc6c7db9dc
docker exec -it CONTAINER_ID /bin/bash
```

- Install package before running container
  - Use wrapper.sh
  - Install additional pacakges after image is built

```sh
docker run -p 8080:8188 IMAGE_ID "<additional-package>"
docker run -p 8080:8188 --gpus all -e ADDITIONAL_PACKAGES="" IMAGE_ID
```

### Troubleshooting

```sh
pip uninstall torch torchvision torchaudio -y

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
# pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 --use-deprecated=legacy-resolver

pip install -r requirements.txt
```
