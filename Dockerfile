FROM base-cuda-conda

WORKDIR /app
COPY . .

RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# For opencv-python
# https://stackoverflow.com/questions/55313610/importerror-libgl-so-1-cannot-open-shared-object-file-no-such-file-or-directo
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# No such file or directory
RUN apt-get update
RUN apt install -y libgl1-mesa-glx

RUN chmod +x /app/setup.sh /app/entrypoint.sh /app/wrapper-entrypoint.sh

RUN /app/setup.sh
# # Info: Points host port 80 to container
# # docker run -p 80:3000 image_id
# # Container must have process running on port 3000 assuming that's how we start.
EXPOSE 8080
# RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/bin/bash", "/app/wrapper-entrypoint.sh"]
