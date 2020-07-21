FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /bookstore
WORKDIR /bookstore
COPY ./bookstore /bookstore

RUN adduser -D user
USER user