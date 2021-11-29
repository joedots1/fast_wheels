FROM python:3.8.3-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

# install python dependencies
COPY pyproject.toml /usr/src/app 
ENV PYTHONPATH=${PYTHONPATH}:${PWD} 
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# add app
COPY . /usr/src/app

CMD uvicorn app.main:app --reload --workers 4 --host 0.0.0.0 --port 8000
