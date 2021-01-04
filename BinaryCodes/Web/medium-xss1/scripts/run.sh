#!/bin/bash
service mysql start
service nginx start
cd /app && gunicorn website.wsgi --bind 0.0.0.0:8000 &
while true; do
    python /app/manage.py check_profiles
    sleep 1
done