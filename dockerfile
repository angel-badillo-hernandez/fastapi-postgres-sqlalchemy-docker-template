# Dockerfile

# pull the lastest official python docker image
FROM python:latest

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# upgrade pip & install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade -r requirements.txt

# copy project
COPY ./app /app