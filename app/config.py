"""
Module de configuration de l'application.
Contient la classe Configuration (Singleton) qui expose les constantes globales.
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Configuration:
    """
    Singleton pour gérer la configuration globale de l'application.
    Assure qu'une seule instance de configuration existe.
    """
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Configuration, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # pylint: disable=invalid-name
        if self._initialized:
            return
        self.DATA_DIR = os.path.join(BASE_DIR, "..", "Data")
        self.METEO_IDS_FILE = "meteo_ids.csv"
        self.DEFAULT_SORT = "date"
        self.DEFAULT_ORDER = "desc"
        self.OUTPUT_DIR = "data/extracted"
        self._initialized = True

    def get(self, key, default=None):
        """
        Récupère une valeur de configuration.
        :param key: Nom de l'attribut
        :param default: Valeur par défaut si non trouvé
        :return: Valeur de l'attribut
        """
        return getattr(self, key, default)

    def __getitem__(self, item):
        return getattr(self, item)

# Instance unique
CONFIG = Configuration()
