FROM --platform=linux/x86_64 continuumio/miniconda3

WORKDIR /app
COPY ./app2 .

# COPY requirements.txt .
# COPY environment.yml .
# # RUN pip install -r requirements.txt

RUN bash -c 'ls'
RUN bash -c 'pwd'

# 80
EXPOSE 80
ENTRYPOINT ["./entrypoint.sh"]

