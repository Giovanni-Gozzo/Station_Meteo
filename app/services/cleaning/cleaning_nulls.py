import pandas as pd


class CleaningNulls:
    """
    Classe de nettoyage pour supprimer les lignes contenant des valeurs nulles
    dans certaines colonnes spécifiées.
    """

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

        # 🔹 Suppression des lignes contenant des NaN dans les colonnes cibles
        cleaned_df = df.dropna(subset=self.columns)

        print(f"[CLEANING] {len(df) - len(cleaned_df)} ligne(s) supprimée(s) à cause de valeurs nulles "
              f"dans les colonnes : {self.columns}")

        return cleaned_df
