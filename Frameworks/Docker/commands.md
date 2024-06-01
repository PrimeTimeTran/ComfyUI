- Export container port `8188` to host port `80`

```sh
docker run -p 80:8188
```

- build and immediately run

```sh
docker build -t comfy . && IMAGE_ID=$(docker images | awk 'NR==2 {print $3}') && docker run --platform=linux/amd64 -p 8080:80 $IMAGE_ID
```

- ssh into container 223c9ff3559d

```sh
docker exec -it 223c9ff3559d /bin/bash
```

- stop containers & remove. remove images & builds.

```sh
docker rm -f $(docker ps -aq) && docker rmi -f $(docker images -aq) && docker builder prune -a -f && docker image prune -a -y
```

docker container prune
docker image prune
docker image prune -a
docker volume prune
docker network prune
docker system prune
docker system prune -a --volumes

```
docker save -o comfy_image.tar primetimetran/comfy:latest
```
