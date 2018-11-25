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
