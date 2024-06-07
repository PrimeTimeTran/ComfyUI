# Docker

- Run container using image 223c9ff3559d & expose port `8188` to host port `80`

```sh
docker run 223c9ff3559d -p 80:8188
```

- Build and immediately run

```sh
docker build -t comfy . && IMAGE_ID=$(docker images | awk 'NR==2 {print $3}') && docker run --platform=linux/amd64 -p 8080:80 $IMAGE_ID
```

- SSH into container 223c9ff3559d

```sh
docker exec -it 223c9ff3559d /bin/bash
```

- Stop containers & remove. remove images & builds.

```sh
docker rm -f $(docker ps -aq) && docker rmi -f $(docker images -aq) && docker builder prune -a -f && docker image prune -a -y
```

- Listed one at a time.
```sh
docker container prune
docker image prune
docker image prune -a
docker volume prune
docker network prune
docker system prune
docker system prune -a --volumes
```

```sh
docker save -o comfy_image.tar primetimetran/comfy:latest
```

### Images

### Create Base NIVIDIA/Cuda/Conda Image
- Base Image with Cuda & Conda
```sh
FROM --platform=linux/x86_64 nvidia/cuda:12.1.1-runtime-ubuntu22.04

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -O https://repo.anaconda.com/miniconda/Miniconda3-py311_24.4.0-0-Linux-x86_64.sh \
    && bash Miniconda3-py311_24.4.0-0-Linux-x86_64.sh -b -p /opt/miniconda \
    && rm Miniconda3-py311_24.4.0-0-Linux-x86_64.sh

ENV PATH="/opt/miniconda/bin:$PATH"
```

- Pull image and build from Dockerfile
```sh
docker pull nvidia/cuda:12.1.1-runtime-ubuntu22.04 && docker build -t base-cuda-conda .
# Cuda 12.1, Miniconda3, Python 3.11, Ubuntu22.04


docker build -t base-cuda-conda .
```

- Tag an image and push it
```sh
docker tag local-image:tagname new-repo:tagname
docker push new-repo:tagname
```

### Running with NVIDIA

```sh
docker run dd0de1e2e55b -p 80:8188 --gpus all
```