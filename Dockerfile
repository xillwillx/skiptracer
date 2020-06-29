FROM python:3.7-slim

MAINTAINER sietekk "sietekk@gmail.com"

COPY requirements.txt /app/requirements.txt

RUN pip3 install --no-cache-dir -r /app/requirements.txt

COPY  . /app

WORKDIR /app/src

FROM ubuntu:latest
MAINTAINER Furkan SAYIM <furkan.sayim@yandex.com>

RUN apt-get update \
    && apt-get install git -y \
    && apt-get install python -y \
    && apt-get install python-pip -y \
    && git clone https://github.com/xillwillx/skiptracer.git

RUN pip install -r skiptracer/requirements.txt

CMD python skiptracer.py

WORKDIR /skiptracer
