FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /dockerapp
COPY requirements.txt /dockerapp/
RUN pip install -r requirements.txt
COPY . /dockerapp/