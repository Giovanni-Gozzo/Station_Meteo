from abc import ABC, abstractmethod
import pandas as pd

class Extractor(ABC):
    """Classe abstraite de base pour tous les extracteurs."""

    @abstractmethod
    def fetch(self):
        """Récupère les données depuis la source."""
        pass

    @abstractmethod
    def get_data(self) -> pd.DataFrame:
        """Transforme les données brutes en DataFrame pandas."""
        pass
