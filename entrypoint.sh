#! /bin/bash

python manage.py makemigrations --no-input

python manage.py migrate --no-input

python manage.py collectstatic --no-input

hypercorn --reload --bind 0.0.0.0:8001 core.asgi:application