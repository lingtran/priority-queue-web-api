FROM python:3.7-buster

ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
    && apt-get -y install bash gcc postgresql linux-headers-amd64 \
    && rm -rf /var/lib/apt/lists/*
RUN set -ex && mkdir /app
WORKDIR /app
COPY . /app
RUN set -ex && pip3 install -r requirements.txt
CMD ["sh", "-c", "flask db upgrade"]