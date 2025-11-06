import pandas as pd
from app.services.cleaning.cleaning_base import DataCleaner

class OutlierCleaner(DataCleaner):
    """Supprime les valeurs aberrantes selon des bornes logiques."""

    def __init__(self, rules: dict):
        """
        rules = {
            "temperature": (-30, 60),
            "humidite": (0, 100),
            "pression": (850, 1100)
        }
        """
        self.rules = rules

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        cleaned_df = df.copy()

        for col, (min_val, max_val) in self.rules.items():
            if col in cleaned_df.columns:
                cleaned_df = cleaned_df[
                    (cleaned_df[col] >= min_val) & (cleaned_df[col] <= max_val)
                ]

        return cleaned_df
