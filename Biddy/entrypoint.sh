#!/bin/sh

# Appliquer les migrations de la base de données
python manage.py migrate --no-input

# Collecter les fichiers statiques
python manage.py collectstatic --no-input

# Charger les données YAML si nécessaire
python manage.py load_yaml_data data.yaml

# Créer un superutilisateur sans interaction
python create_superuser.py

# Lancer Gunicorn
gunicorn Biddy.wsgi:application --bind 0.0.0.0:8000
