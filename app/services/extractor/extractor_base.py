"""
Module définissant l'interface de base pour les extracteurs.
"""
from abc import ABC, abstractmethod
import pandas as pd

class Extractor(ABC):
    """Classe abstraite de base pour tous les extracteurs."""
    # pylint: disable=too-few-public-methods

    @abstractmethod
    def fetch(self):
        """Récupère les données depuis la source."""

    @abstractmethod
    def get_data(self) -> pd.DataFrame:
        """Transforme les données brutes en DataFrame pandas."""
