"""
Module pour l'extraction de données au format JSON.
"""
import pandas as pd
from app.services.extractor.api_extractor import APIExtractor

class JSONExtractor(APIExtractor):
    """Extracteur JSON depuis l’API OpenData Toulouse Métropole."""

    def __init__(self, dataset_id: str):
        super().__init__(dataset_id, export_format="json")

    def get_data(self) -> pd.DataFrame:
        if self.raw_data is None:
            raise ValueError("Aucune donnée brute. Appelez fetch() d'abord.")

        df = pd.json_normalize(self.raw_data)
        return df
