# Station Météo

Application simple pour visualiser les données météo de Toulouse Métropole.

## 🚀 Installation

1. Assurez-vous d'avoir Python installé.
2. Installez les dépendances :

```bash
pip install -r requirements.txt
```

## ▶️ Lancement Local

Depuis la racine du projet, lancez la commande :

```bash
python3 -m app.main
```

L'application sera accessible sur :
[http://127.0.0.1:5002](http://127.0.0.1:5002)

> **Note :** Le port par défaut est **5002** pour éviter les conflits avec le service AirPlay sur macOS (qui utilise souvent le port 5000).

## 🧪 Tests

Pour exécuter la suite de tests unitaires :

```bash
python3 -m pytest
```

## 🐳 Lancement avec Docker

Si vous préférez utiliser Docker :

1. Construisez et lancez le conteneur :
   ```bash
   docker compose up --build
   ```

2. Accédez à l'application via :
   [http://127.0.0.1:5001](http://127.0.0.1:5001)

> **Note :** Docker mappe le port interne 5002 vers le port **5001** de votre machine hôte.
