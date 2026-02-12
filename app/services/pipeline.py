"""
Module définissant le pipeline principal de traitement.
"""
import os
from typing import List
from datetime import datetime, timedelta
import pandas as pd

from app.services.cleaning.cleaning_type import TypeCleaner
from app.services.cleaning.cleaning_nulls import CleaningNulls
from app.services.cleaning.cleaning_nulls import CleaningNulls
from app.services.cleaning.cleaning_outliers import OutlierCleaner
from app.services.cleaning.cleaning_units import UnitCleaner
from app.services.cleaning.cleaner_pipeline import CleaningPipeline
from app.services.extractor.csv_extraction_command import CSVExtractionCommand
from app.structures.queue import Queue


class MeteoPipeline:
    """Pipeline complète pour extraire, nettoyer et sauvegarder les données météo."""
    # pylint: disable=too-few-public-methods

    def __init__(self, output_dir: str = "data/extracted"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def run(self, dataset_ids: List[str]) -> pd.DataFrame:
        """Exécute la pipeline pour plusieurs stations."""
        # pylint: disable=too-many-locals

        stations_structure = Queue()

        for station_id in dataset_ids:
            stations_structure.add(station_id)

        all_dataframes = []

        now = datetime.now()
        one_hour_ago_iso = (now - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%S")

        print(f"[INFO] Extraction des relevés depuis : {one_hour_ago_iso}")

        # Itération sur la structure via son itérateur
        for dataset_id in stations_structure:
            print(f"\n[INFO] 📡 Station : {dataset_id}")

            command = CSVExtractionCommand(dataset_id)
            df = command.execute()

            if df is None or df.empty:
                print(f"[⚠️] Aucune donnée pour {dataset_id}")
                continue

            # Nettoyage
            cleaning_pipeline = CleaningPipeline()
            cleaning_pipeline.add(
                CleaningNulls(columns=["temperature_en_degre_c", "humidite", "pression"])
            )
            cleaning_pipeline.add(TypeCleaner())
            cleaning_pipeline.add(UnitCleaner())
            cleaning_pipeline.add(OutlierCleaner())
            df = cleaning_pipeline.run(df)

            timestamp = now.strftime("%Y%m%d_%H%M")
            filepath = os.path.join(self.output_dir, f"{dataset_id}_{timestamp}.csv")
            df.to_csv(filepath, index=False)
            print(f"[✅] Sauvegardé : {filepath}")
            df['station_id'] = dataset_id
            all_dataframes.append(df)

        if all_dataframes:
            combined_df = pd.concat(all_dataframes, ignore_index=True)
            return combined_df
        return pd.DataFrame()
