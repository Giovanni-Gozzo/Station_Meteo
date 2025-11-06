from abc import ABC, abstractmethod
import pandas as pd

class Loader(ABC):
    """Classe abstraite pour tous les loaders."""

    @abstractmethod
    def load(self, df: pd.DataFrame, table_name: str):
        """Charge un DataFrame dans une destination donnée."""
        pass
