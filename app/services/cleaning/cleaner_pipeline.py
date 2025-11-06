import pandas as pd
from app.services.cleaning.cleaning_base import DataCleaner

class CleaningPipeline:
    """Permet de chaîner plusieurs cleaners."""

    def __init__(self):
        self.cleaners: list[DataCleaner] = []

    def add(self, cleaner: DataCleaner):
        self.cleaners.append(cleaner)

    def run(self, df: pd.DataFrame) -> pd.DataFrame:
        cleaned_df = df.copy()
        for cleaner in self.cleaners:
            cleaned_df = cleaner.clean(cleaned_df)
        return cleaned_df
