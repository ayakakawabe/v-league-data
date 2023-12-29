FROM python:latest
RUN apt-get update && \
    apt-get install -y \
    git \
    sudo
RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
WORKDIR /app
