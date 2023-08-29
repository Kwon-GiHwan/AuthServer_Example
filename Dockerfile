FROM python:3.10-alpine as requirements-stage

WORKDIR /tmp

RUN pip install poetry==1.4.2

COPY pyproject.toml /tmp/
COPY poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.10-alpine

WORKDIR /app

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev\
    && apk del build-deps

RUN apk add mpc1-dev
RUN apk add build-base

COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

ENTRYPOINT ["python3", "./api_server.py"]



