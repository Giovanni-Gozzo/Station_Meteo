import requests
from datetime import datetime
from urllib.parse import urlencode, unquote
from app.services.extractor.extractor_base import Extractor


class APIExtractor(Extractor):
    """Extracteur générique pour l'API OpenData Toulouse Métropole."""

    def __init__(self, dataset_id: str, export_format: str = "json", debug: bool = True):
        self.base_url = "https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets"
        self.dataset_id = dataset_id
        self.export_format = export_format.lower()
        self.raw_data = None
        self.filters = []
        self.debug = debug

        if self.export_format not in ("json", "csv", "parquet"):
            raise ValueError("Le format doit être 'json', 'csv' ou 'parquet'.")

    def get_endpoint(self) -> str:
        return f"{self.base_url}/{self.dataset_id}/exports/{self.export_format}"

    def add_filter(self, column: str, operator: str, value):
        """Ajoute un filtre sans écraser les précédents."""
        if operator not in (">", "<", ">=", "<=", "=", "!="):
            raise ValueError("Opérateur non valide. Utiliser >, <, >=, <=, =, !=")
        self.filters.append((column, operator, value))  # ✅ empile les filtres

    def build_where_clause(self) -> str:
        """Construit la clause WHERE (non encodée)."""
        if not self.filters:
            return None

        conditions = []
        for col, op, val in self.filters:
            if isinstance(val, datetime):
                val_str = f"date'{val.strftime('%Y-%m-%d')}'"
            elif isinstance(val, str):
                # Vérifie si c’est une date
                try:
                    datetime.strptime(val, "%Y-%m-%d")
                    val_str = f"date'{val}'"
                except ValueError:
                    val_str = f"'{val}'"
            else:
                val_str = str(val)

            conditions.append(f"{col} {op} {val_str}")

        return " AND ".join(conditions)

    def fetch(self, params: dict = None):
        """Télécharge les données depuis l'API."""
        url = self.get_endpoint()
        if params is None:
            params = {}

        where_clause = self.build_where_clause()
        if where_clause:
            params["where"] = where_clause

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
        except requests.RequestException as e:
            raise ConnectionError(f"Erreur lors de la récupération des données : {e}")

        if self.export_format == "json":
            self.raw_data = response.json()
        elif self.export_format == "csv":
            self.raw_data = response.text
        elif self.export_format == "parquet":
            self.raw_data = response.content

        return self.raw_data
