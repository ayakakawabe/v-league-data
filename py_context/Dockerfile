FROM python:latest
RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN python3 -m venv .venv
RUN .venv/bin/activate && pip install -U pip && pip install -r requirements.txt
WORKDIR /app
