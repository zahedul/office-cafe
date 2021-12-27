FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y postgresql-client
RUN apt-get install -y gcc libc-dev netcat

RUN pip install --upgrade pip setuptools wheel
RUN pip install pipenv

COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --keep-outdated --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN apt-get clean
RUN rm -f /var/lib/apt/list/*

RUN useradd -ms /bin/bash officecafe
USER officecafe

RUN mkdir /home/officecafe/src
WORKDIR /home/officecafe/src
COPY ./src /home/officecafe/src


RUN mkdir -p /home/officecafe/src/media
RUN mkdir -p /home/officecafe/src/static
RUN mkdir -p /home/officecafe/log