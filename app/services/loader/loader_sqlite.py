import os
import sqlite3
import pandas as pd
from app.services.loader.loader_base import Loader

class SQLiteLoader(Loader):
    """Loader pour charger les données dans une base SQLite."""

    def __init__(self, db_path: str = "data/meteo.db"):
        self.db_path = db_path
        # Crée le dossier s’il n’existe pas
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

    def load(self, df: pd.DataFrame, table_name: str):
        """Charge le DataFrame dans une table SQLite."""
        if df is None or df.empty:
            raise ValueError("Le DataFrame est vide, rien à charger.")

        try:
            with sqlite3.connect(self.db_path) as conn:
                df.to_sql(table_name, conn, if_exists="replace", index=False)
                print(f"[LOADER] ✅ Données chargées avec succès dans '{table_name}' ({len(df)} lignes)")
        except Exception as e:
            raise RuntimeError(f"[LOADER] ❌ Erreur lors du chargement SQLite : {e}")
