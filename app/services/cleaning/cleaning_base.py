import pandas as pd
from abc import ABC, abstractmethod

class DataCleaner(ABC):
    """Classe de base pour tous les nettoyeurs de données."""

    @abstractmethod
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """Nettoie un DataFrame et retourne le résultat."""
        pass
