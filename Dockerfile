FROM python:3.6.9-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apk update && apk add gcc

# RUN pip install --upgrade pip pipenv

# COPY Pipfile Pipfile.lock ./

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . ./