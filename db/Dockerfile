FROM mongo:latest

ARG BASE_DIR
COPY ${BASE_DIR}/jokes.csv /jokes.csv
COPY ${BASE_DIR}/docker-import.sh /docker-entrypoint-initdb.d