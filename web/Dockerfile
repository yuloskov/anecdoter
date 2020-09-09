FROM python:3.7-alpine

# Main application setup
WORKDIR /application

ARG BASE_DIR

COPY ${BASE_DIR}/requirements.txt .

RUN pip3 install -r requirements.txt

COPY ${BASE_DIR} .

