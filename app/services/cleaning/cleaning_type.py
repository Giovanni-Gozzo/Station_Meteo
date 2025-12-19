"""
Module de nettoyage pour la conversion de types.
"""
import pandas as pd
from app.services.cleaning.cleaning_base import DataCleaner

class TypeCleaner(DataCleaner):
    """
    Nettoyage des colonnes pour convertir dans un type spécifique.
    Les lignes qui ne peuvent pas être converties sont supprimées.
    """
    # pylint: disable=too-few-public-methods

    DEFAULT_COLUMNS_TYPES = {
        "direction_du_vecteur_vent_moyen": float,
        "direction_du_vecteur_de_vent_max_en_degres": float,
        "humidite": float,
        "temperature_en_degre_c": float
    }

    def __init__(self, columns_types: dict = None):
        """
        :param columns_types: dictionnaire nom_colonne -> type_cible.
                              Si None, utilise DEFAULT_COLUMNS_TYPES.
        """
        self.columns_types = columns_types or self.DEFAULT_COLUMNS_TYPES

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """Convertit les colonnes et supprime les erreurs."""
        cleaned_df = df.copy()
        initial_len = len(cleaned_df)

        for col, target_type in self.columns_types.items():
            if col not in cleaned_df.columns:
                continue

            before_len = len(cleaned_df)

            if target_type == "datetime":
                cleaned_df[col] = pd.to_datetime(cleaned_df[col], errors='coerce')
            elif target_type in [int, float]:
                cleaned_df[col] = cleaned_df[col].astype(target_type)
            else:
                cleaned_df[col] = cleaned_df[col].astype(str)

            cleaned_df = cleaned_df.dropna(subset=[col])
            removed = before_len - len(cleaned_df)
            if removed > 0:
                print(
                    f"[CLEANING] {removed} ligne(s) supprimée(s) "
                    f"(conversion impossible pour '{col}' vers {target_type})"
                )

        total_removed = initial_len - len(cleaned_df)
        print(f"[CLEANING] ✅ Total : {total_removed} ligne(s) supprimée(s) pour conversions de type")
        return cleaned_df
