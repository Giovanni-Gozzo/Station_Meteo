import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Configuration:
    """
    Singleton pour gérer la configuration globale de l'application.
    Assure qu'une seule instance de configuration existe.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Configuration, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.DATA_DIR = os.path.join(BASE_DIR, "..", "Data")
        self.METEO_IDS_FILE = "meteo_ids.csv"
        self.DEFAULT_SORT = "date"
        self.DEFAULT_ORDER = "desc"
        self.OUTPUT_DIR = "data/extracted"

    def get(self, key, default=None):
        return getattr(self, key, default)

    def __getitem__(self, item):
        return getattr(self, item)

CONFIG = Configuration()
