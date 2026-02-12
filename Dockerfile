# Utiliser une image Python officielle légère
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier des dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code de l'application
COPY . .

# Exposer le port que Flask utilise par défaut (ou celui configuré)
EXPOSE 5002

# Commande pour démarrer l'application
CMD ["python", "-m", "app.main"]