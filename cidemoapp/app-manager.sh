#!/bin/bash
python manage.py migrate
python manage.py collectstatic

python manage.py makemigrations meets
python manage.py migrate meets

echo Starting Gunicorn.
exec gunicorn cidemoapp.wsgi:application \
    --name cidemoapp \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    "$@"

