FROM python:3.7-slim

MAINTAINER sietekk "sietekk@gmail.com"

COPY requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt

COPY  . /app

WORKDIR /app/src

ENTRYPOINT [ "python3", "-m", "skiptracer" ]
