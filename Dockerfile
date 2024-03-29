# start from base
FROM ubuntu:20.04

LABEL maintainer="hendrikuwabara@gmail.com"

RUN apt-get update -y && \

apt-get install -y python3-pip python3-dev build-essential

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

CMD [ "python3", "-u", "./app/app.py" ]