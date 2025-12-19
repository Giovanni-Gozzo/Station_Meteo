"""
Module de nettoyage pour les valeurs nulles.
"""
import pandas as pd
from app.services.cleaning.cleaning_base import DataCleaner

class CleaningNulls(DataCleaner):
    """
    Classe de nettoyage pour supprimer les lignes contenant des valeurs nulles
    dans certaines colonnes spécifiées.
    """
    # pylint: disable=too-few-public-methods

    def __init__(self, columns: list[str]):
        """
        Initialise le nettoyeur.

        :param columns: Liste des colonnes à vérifier pour les valeurs nulles.
        """
        if not isinstance(columns, list) or not all(isinstance(c, str) for c in columns):
            raise ValueError("Le paramètre 'columns' doit être une liste de chaînes de caractères.")

        self.columns = columns

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Supprime les lignes contenant des valeurs nulles dans les colonnes spécifiées.

        :param df: DataFrame à nettoyer.
        :return: Nouveau DataFrame nettoyé.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Le paramètre 'df' doit être un DataFrame pandas.")

        missing_cols = [col for col in self.columns if col not in df.columns]
        if missing_cols:
            raise KeyError(f"Les colonnes suivantes sont absentes du DataFrame : {missing_cols}")

        cleaned_df = df.dropna(subset=self.columns)

        removed_count = len(df) - len(cleaned_df)
        print(
            f"[CLEANING] {removed_count} ligne(s) supprimée(s) à cause de valeurs nulles "
            f"dans les colonnes : {self.columns}"
        )

        return cleaned_df
