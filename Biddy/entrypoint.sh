#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input
python manage.py load_yaml_data data.yaml
gunicorn  Biddy.wsgi:application --bind 0.0.0.0:8000