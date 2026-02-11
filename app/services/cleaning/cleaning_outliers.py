"""
Module de nettoyage pour les valeurs aberrantes (outliers).
"""
import pandas as pd
from app.services.cleaning.cleaning_base import DataCleaner

class OutlierCleaner(DataCleaner):
    """Supprime les valeurs aberrantes selon des bornes physiques logiques."""
    # pylint: disable=too-few-public-methods

    def __init__(self):
        """
        Définition des règles de nettoyage basées sur les modèles Vent, Pluie, Atmosphere.
        Ces bornes reflètent des valeurs physiques réalistes pour la météo.
        """
        self.rules = {
            # --- Atmosphère ---
            "temperature": (-30, 60),    # °C
            "temperature_en_degre_c": (-30, 60),
            "humidite": (0, 100),        # %
            "pression": (850, 1100),     # hPa

            # --- Vent ---
            "direction_du_vecteur_de_vent_max": (0, 360),            # degrés
            "direction_du_vecteur_vent_moyen": (0, 360),             # degrés
            "direction_du_vecteur_de_rafale_de_vent_max": (0, 360),  # degrés
            "force_moyenne_du_vecteur_vent": (0, 400),               # km/h
            "force_rafale_max": (0, 400),                            # km/h

            # --- Pluie ---
            "pluie_intensite_max": (0, 300),  # mm/h
            "pluie": (0, 500)                 # mm cumul
        }

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Supprime les lignes où les colonnes dépassent les bornes logiques.
        """
        cleaned_df = df.copy()
        initial_len = len(df)

        for col, (min_val, max_val) in self.rules.items():
            if col in cleaned_df.columns:
                before = len(cleaned_df)
                cleaned_df[col] = cleaned_df[col].astype(float)
                cleaned_df = cleaned_df[
                    (cleaned_df[col] >= min_val) & (cleaned_df[col] <= max_val)
                ]
                removed = before - len(cleaned_df)
                if removed > 0:
                    print(
                        f"[CLEANING] {removed} ligne(s) supprimée(s) "
                        f"(valeurs aberrantes dans '{col}' hors [{min_val}, {max_val}])"
                    )

        removed_total = initial_len - len(cleaned_df)
        print(
            f"[CLEANING] ✅ Total : {removed_total} ligne(s) supprimée(s) pour valeurs aberrantes"
        )
        return cleaned_df
