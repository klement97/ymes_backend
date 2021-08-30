FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code

WORKDIR /code

# install psycopg2 dependencies
RUN apt-get update \
    && apt-get -y install libpq-dev gcc

# Copy requirements.txt before the code itself so
# we don't need to re install all packages on every code change.
COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/
