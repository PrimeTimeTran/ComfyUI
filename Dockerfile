FROM --platform=linux/x86_64 continuumio/miniconda3

WORKDIR /app
COPY . .
COPY entrypoint.sh .
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN bash -c 'ls'
RUN bash -c 'pwd'

# Info: Points host port 80 to container
# docker run -p 80:3000 image_id
# Container must have process running on port 3000 assuming that's how we start.

EXPOSE 80
ENTRYPOINT ["./entrypoint.sh"]

