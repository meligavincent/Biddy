FROM python:3.12.5-alpine3.20

# Met à jour pip
RUN pip3 install --upgrade pip

# Copie le fichier requirements.txt et installe les dépendances
COPY Biddy/requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt

# Copie le reste de l'application
COPY . /app/

# Copie le script d'entrée et le rend exécutable
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Définir le répertoire de travail
WORKDIR /app

# Définir le point d'entrée du conteneur
ENTRYPOINT [ "sh", "/entrypoint.sh" ]
