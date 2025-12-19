from app.services.extractor.command import Command
from app.services.extractor.csv_extractor import CSVExtractor
from datetime import datetime, timedelta

class CSVExtractionCommand(Command):
    """
    Commande concrète pour exécuter l'extraction des données au format CSV.
    Implémente le pattern Command.
    """
    def __init__(self, dataset_id: str):
        self.dataset_id = dataset_id
        self.extractor = CSVExtractor(dataset_id)

    def execute(self):
        now = datetime.now()
        one_hour_ago_iso = (now - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%S")
        now_iso = now.strftime("%Y-%m-%dT%H:%M:%S")

        self.extractor.add_filter("heure_de_paris", ">", one_hour_ago_iso)
        self.extractor.add_filter("heure_de_paris", "<", now_iso)
        
        self.extractor.fetch()
        return self.extractor.get_data()
