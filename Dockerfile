FROM python:3.7-slim

MAINTAINER sietekk "sietekk@gmail.com"

COPY requirements.txt /app/requirements.txt

RUN pip3 install --no-cache-dir -r /app/requirements.txt

COPY  . /app

WORKDIR /app/src
