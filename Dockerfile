FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


RUN mkdir /app
WORKDIR /app

COPY . /app

EXPOSE 5000
