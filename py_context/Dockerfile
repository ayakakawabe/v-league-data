FROM python:latest
RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip install --user -r /requirements.txt
WORKDIR /app
