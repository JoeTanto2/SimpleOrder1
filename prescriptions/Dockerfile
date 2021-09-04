FROM python:3.9

ENV PYTHONBUFFERED 1

WORKDIR /dockerapp

COPY requirements.txt /dockerapp/requirements.txt

RUN pip install -r requirements.txt

COPY . /dockerapp
