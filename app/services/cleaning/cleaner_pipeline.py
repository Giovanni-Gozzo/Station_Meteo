"""
Module gérant le pipeline de nettoyage des données.
Permet d'enchaîner plusieurs étapes de nettoyage.
"""
import pandas as pd
from typing import List
from app.services.cleaning.cleaning_base import DataCleaner

class CleaningPipeline:
    """Permet de chaîner plusieurs cleaners."""

    def __init__(self):
        self.cleaners: List[DataCleaner] = []

    def add(self, cleaner: DataCleaner):
        """Ajoute un cleaner au pipeline."""
        self.cleaners.append(cleaner)

    def run(self, df: pd.DataFrame) -> pd.DataFrame:
        """Exécute tous les cleaners sur le DataFrame."""
        cleaned_df = df.copy()
        for cleaner in self.cleaners:
            cleaned_df = cleaner.clean(cleaned_df)
        return cleaned_df
