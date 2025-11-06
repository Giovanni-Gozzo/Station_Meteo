import pandas as pd
import io
from app.services.extractor.api_extractor import APIExtractor

class ParquetExtractor(APIExtractor):
    """Extracteur Parquet depuis l’API OpenData Toulouse Métropole."""

    def __init__(self, dataset_id: str):
        super().__init__(dataset_id, export_format="parquet")

    def get_data(self) -> pd.DataFrame:
        if self.raw_data is None:
            raise ValueError("Aucune donnée brute. Appelez fetch() d'abord.")
        return pd.read_parquet(io.BytesIO(self.raw_data))
