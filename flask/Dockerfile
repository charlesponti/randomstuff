FROM python:3.6-alpine

RUN adduser -D microblog

WORKDIR /home/microblog

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY microblog.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP=microblog.py

RUN chmod -R microblog:microblog ./
USER microblog

EXPOSE 500
ENTRYPOINT ["boot.sh"]

# FROM ubuntu:18.10

# LABEL maintainer="Charles Ponti <cj@ponti.io>"

# RUN apt-get update
# RUN apt-get install -y python3 python3-dev python3-pip nginx
# RUN pip3 install uwsgi

# COPY ./ ./app
# WORKDIR ./app

# RUN pip3 install -r requirements.txt

# COPY ./nginx.conf /etc/nginx/sites-enabled/default

# CMD service nginx start && uwsgi -s /tmp/uwsgi.sock --chmod-socket=666 --manage-script-name --mount /=app:app