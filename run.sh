#!/bin/sh

set -e

. /venv/bin/activate

while ! nc $db_host $db_port; do
  >&2 echo "DB is unavailable"
  sleep 1
done

exec poetry run python ./api/main.py