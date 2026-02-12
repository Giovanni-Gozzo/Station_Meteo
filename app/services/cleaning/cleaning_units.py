"""
Module de nettoyage pour la normalisation des unités.
"""
import pandas as pd
from app.services.cleaning.cleaning_base import DataCleaner

class UnitCleaner(DataCleaner):
    """
    Normalise les unités des colonnes pour correspondre aux attentes des autres cleaners.
    Exemple: Conversion de la pression de Pascal (Pa) vers Hectopascal (hPa).
    """

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """Convertit les unités."""
        cleaned_df = df.copy()
        
        # Conversion Pression : Pa -> hPa
        if "pression" in cleaned_df.columns:
            # On suppose que si la pression est > 10000, c'est en Pa (1 hPa = 100 Pa)
            # Une pression atmosphérique standard est ~1013 hPa ou 101300 Pa
            mask_pa = cleaned_df["pression"] > 2000  # Seuil arbitraire pour distinguer hPa et Pa
            if mask_pa.any():
                cleaned_df.loc[mask_pa, "pression"] = cleaned_df.loc[mask_pa, "pression"] / 100.0
                print(f"[CLEANING] 🔄 Conversion Pression (Pa -> hPa) sur {mask_pa.sum()} ligne(s)")

        return cleaned_df
