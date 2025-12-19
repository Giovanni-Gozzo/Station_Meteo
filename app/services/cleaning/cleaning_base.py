"""
Module définissant l'interface pour les nettoyeurs de données.
"""
from abc import ABC, abstractmethod
import pandas as pd

class DataCleaner(ABC):
    """Classe de base pour tous les nettoyeurs de données."""
    # pylint: disable=too-few-public-methods

    @abstractmethod
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """Nettoie un DataFrame et retourne le résultat."""
