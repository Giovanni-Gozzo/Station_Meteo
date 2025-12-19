from flask import Flask, render_template, request, redirect, url_for
from app.controllers.meteo_controller import MeteoController
import pandas as pd
from datetime import datetime
import os
from app.config import CONFIG

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
    try:
        file_path = os.path.join(CONFIG["DATA_DIR"], CONFIG["METEO_IDS_FILE"])
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
    selected_station_ids = request.args.getlist('station_id')

    if not selected_station_ids:
        return redirect(url_for('select_station'))

    try:
        all_meteo_data = controller.get_latest_meteo_data(selected_station_ids)
        filtered_data = all_meteo_data

        unique_station_ids = sorted(list(set(selected_station_ids)))

    except Exception as e:
        print(f"Erreur lors du chargement des données pour {selected_station_ids}: {e}")
        filtered_data = []
        unique_station_ids = []

    sort_by = request.args.get('sort', CONFIG["DEFAULT_SORT"])
    order = request.args.get('order', CONFIG["DEFAULT_ORDER"])

    reverse_order = (order == 'desc')

    sorted_data = sorted(
        filtered_data,
        key=lambda m: get_sort_key(m, sort_by),
        reverse=reverse_order
    )

    return render_template(
        "meteo.html",
        meteo_data=sorted_data,
        unique_station_ids=unique_station_ids,
        selected_station_ids=selected_station_ids,
        sort_by=sort_by,
        order=order
    )


if __name__ == "__main__":
    app.run(debug=True)