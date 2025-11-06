from flask import Flask, render_template, request, redirect, url_for
from app.controllers.meteo_controller import MeteoController
import pandas as pd
from datetime import datetime
import os  # Pour gérer les chemins de fichiers

app = Flask(__name__)
controller = MeteoController()


# Logique pour extraire la clé de tri de l'objet Meteo
def get_sort_key(meteo_obj, sort_by):
    """Retourne la valeur de l'attribut à utiliser comme clé de tri."""
    if sort_by == 'date':
        return meteo_obj.get_date()
    elif sort_by == 'station_id':
        return meteo_obj.get_station().get_station_id()
    elif sort_by == 'ville':
        return meteo_obj.get_station().get_ville()
    return meteo_obj.get_date()


# --- Nouvelle Route d'Accueil : Afficher la sélection de station ---
@app.route("/")
def select_station():
    # 1. Charger la liste des IDs (nécessite uniquement cette étape au démarrage)
    try:
        # Assurez-vous que le chemin est correct pour votre environnement Flask
        file_path = os.path.join(os.path.dirname(__file__), "..", "Data", "meteo_ids.csv")
        df = pd.read_csv(file_path)
        all_ids = df["dataset_id"].tolist()
        unique_station_ids = sorted(list(set(all_ids)))

    except Exception as e:
        print(f"Erreur lors de la lecture du CSV pour les IDs: {e}")
        unique_station_ids = []

    return render_template("select_station.html", unique_station_ids=unique_station_ids)


# --- Nouvelle Route pour Afficher les Données Filtrées ---
@app.route("/data")
def show_meteo_data():
    # 1. Récupérer le paramètre de filtre OBLIGATOIRE de l'URL
    selected_station_id = request.args.get('station_id')

    if not selected_station_id:
        # Si aucun ID n'est fourni (l'utilisateur a accédé directement à /data), on redirige
        return redirect(url_for('select_station'))

    # 2. Charger UNIQUEMENT les données de la station sélectionnée
    # J'ajoute une nouvelle méthode hypothétique pour un chargement ciblé.
    # Votre contrôleur doit être capable de ne charger que les données pour cet ID.
    try:
        # Exemple de simulation: si votre contrôleur charge tout, filtrez ici.
        # Sinon, modifiez votre contrôleur pour charger uniquement selected_station_id
        all_meteo_data = controller.get_latest_meteo_data([selected_station_id])
        filtered_data = all_meteo_data  # Si le contrôleur a déjà filtré/chargé

        # Charger tous les IDs uniques à nouveau pour le menu déroulant de la page de données
        file_path = os.path.join(os.path.dirname(__file__), "..", "Data", "meteo_ids.csv")
        df = pd.read_csv(file_path)
        all_ids = df["dataset_id"].tolist()
        unique_station_ids = sorted(list(set(all_ids)))

    except Exception as e:
        print(f"Erreur lors du chargement des données pour {selected_station_id}: {e}")
        filtered_data = []
        unique_station_ids = []  # Ou gérer les erreurs

    # 3. Récupérer les paramètres de tri de l'URL
    sort_by = request.args.get('sort', 'date')
    order = request.args.get('order', 'desc')

    # 4. Tri des données filtrées
    reverse_order = (order == 'desc')

    sorted_data = sorted(
        filtered_data,
        key=lambda m: get_sort_key(m, sort_by),
        reverse=reverse_order
    )

    # 5. Rendu du template 'meteo.html'
    return render_template(
        "meteo.html",
        meteo_data=sorted_data,
        unique_station_ids=unique_station_ids,
        selected_station_id=selected_station_id,
        sort_by=sort_by,
        order=order
    )


if __name__ == "__main__":
    app.run(debug=True)