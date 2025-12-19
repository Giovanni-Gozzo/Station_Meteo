"""
Contrôleur pour la gestion des données météo.
Orchestre la récupération depuis le pipeline et la transformation en objets modèles.
"""
from datetime import datetime
import pandas as pd

from app.services.pipeline import MeteoPipeline
from app.models.meteo_builder import MeteoBuilder
from app.models.station_display import StationDisplay
from app.structures.linked_list import LinkedList

class MeteoController:
    """Orchestre la récupération et la transformation des données météo."""

    def __init__(self):
        self.pipeline = MeteoPipeline()

    def get_latest_meteo_data(self, dataset_ids: list[str]):
        """Exécute la pipeline et convertit le résultat en objets Meteo."""
        df = self.pipeline.run(dataset_ids)
        if df.empty:
            return LinkedList()

        meteo_objects = LinkedList()
        print(df.columns)
        for _, row in df.iterrows():
            try:
                # Fonction locale pour sécuriser l'accès aux données
                def safe_get(row_data, key, default):
                    value = row_data.get(key, default)
                    if pd.isna(value):
                        return default
                    return value

                date_val = safe_get(row, "heure_de_paris", None)

                if isinstance(date_val, str):
                    date_val = datetime.fromisoformat(date_val)

                # Utilisation du Builder
                builder = MeteoBuilder()
                meteo = (builder
                    .with_date(date_val)
                    .with_station(
                        safe_get(row, "nom_station", "Inconnue"),
                        safe_get(row, "ville", "Toulouse"),
                        safe_get(row, "station_id", "")
                    )
                    .with_vent(
                        safe_get(row, "direction_du_vecteur_de_vent_max_en_degres", 0.0),
                        safe_get(row, "direction_du_vecteur_vent_moyen", 0.0),
                        safe_get(row, "direction_du_vecteur_de_rafale_de_vent_max", 0.0),
                        safe_get(row, "force_moyenne_du_vecteur_vent", 0),
                        safe_get(row, "force_rafale_max", 0)
                    )
                    .with_pluie(
                        safe_get(row, "pluie_intensite_max", 0),
                        safe_get(row, "pluie", 0)
                    )
                    .with_atmosphere(
                        safe_get(row, "temperature_en_degre_c", 0.0),
                        safe_get(row, "humidite", 0.0),
                        safe_get(row, "pression", 0.0)
                    )
                    .build())

                # Utilisation du Decorator
                decorated_meteo = StationDisplay(meteo)
                meteo_objects.add(decorated_meteo)

            except Exception as e: # pylint: disable=broad-exception-caught
                print(f"[⚠️] Erreur lors de la création de l’objet Meteo : {e}")
                continue

        return meteo_objects
