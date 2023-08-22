#!/usr/bin/env bash
db_host="root"
db_port=3306

while ! nc $db_host $db_port; do
  >&2 echo "DB is unavailable - sleeping"
  sleep 1
done

echo "database migrations"

python3 /app/api/main.py