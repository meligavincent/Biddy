#!/bin/sh
python manage.py makemigrations
# Appliquer les migrations de la base de données
python manage.py migrate --no-input

# Collecter les fichiers statiques
python manage.py collectstatic --no-input

# Charger les données YAML si nécessaire
python manage.py load_yaml_data data.yaml

# Créer un superutilisateur sans interaction
python create_superuser.py

# Lancer Gunicorn
# Lancer Gunicorn en arrière-plan
gunicorn Biddy.wsgi:application --bind 0.0.0.0:8000 &

# Exécuter le script d'upload automatique après un délai pour s'assurer que l'application est prête
sleep 30  # Attendre 30 secondes avant d'exécuter le script d'upload (ajustez le temps si nécessaire)
python manage.py load_yaml_data data.yaml # Assurez-vous que ce script est créé pour gérer l'upload automatique

# Garder le conteneur en cours d'exécution
wait
