FROM python:latest
RUN pip install --user --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip install --user -r /requirements.txt
WORKDIR /app
