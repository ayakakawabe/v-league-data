FROM python:3.9.18
RUN apt-get update && \
    apt-get install -y \
    git \
    sudo
RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt --user
WORKDIR /app
CMD [ "python","main.py" ]
