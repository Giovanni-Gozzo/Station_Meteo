import pandas as pd
from io import StringIO
from app.services.extractor.api_extractor import APIExtractor

class CSVExtractor(APIExtractor):
    """Extracteur CSV depuis l’API OpenData Toulouse Métropole."""

    def __init__(self, dataset_id: str):
        super().__init__(dataset_id, export_format="csv")

    def get_data(self) -> pd.DataFrame:
        if self.raw_data is None:
            raise ValueError("Aucune donnée brute. Appelez fetch() d'abord.")
        return pd.read_csv(StringIO(self.raw_data))
