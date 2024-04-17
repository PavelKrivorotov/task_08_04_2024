# syntax=docker/dockerfile:1

FROM python:3.10-alpine3.15
WORKDIR /app/

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./.docker.env /app/.env

COPY ./start-app.sh /app/start-app.sh
RUN chmod u+x /app/start-app.sh

COPY ./src /app/src

# CMD [ "python", "/app/src/manage.py" ]
SHELL [ "/bin/bash", "-x", "start-app.sh" ]
