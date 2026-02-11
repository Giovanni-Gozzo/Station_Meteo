import pytest
from unittest.mock import MagicMock, patch
import pandas as pd
from app.controllers.meteo_controller import MeteoController
from app.structures.linked_list import LinkedList
from app.models.meteo import Meteo

class TestController:
    @patch("app.controllers.meteo_controller.MeteoPipeline")
    def test_get_latest_meteo_data(self, MockPipeline):
        pipeline_instance = MockPipeline.return_value
        
        data = {
            "heure_de_paris": ["2023-10-27T10:00:00+02:00"],
            "station_id": ["31069001"],
            "nom_station": ["TOULOUSE-BLAGNAC"],
            "ville": ["Toulouse"],
            "temperature_en_degre_c": [18.5],
            "humidite": [75.0],
            "pression": [1015.0],
            "pluie": [0.0],
            "pluie_intensite_max": [0.0],
            "force_moyenne_du_vecteur_vent": [10.0],
            "force_rafale_max": [15.0],
            "direction_du_vecteur_vent_moyen": [180.0],
            "direction_du_vecteur_de_rafale_de_vent_max": [190.0],
            "direction_du_vecteur_de_vent_max_en_degres": [185.0]
        }
        pipeline_instance.run.return_value = pd.DataFrame(data)
        
        controller = MeteoController()
        result = controller.get_latest_meteo_data(["31069001"])
        
        assert isinstance(result, LinkedList)
        assert len(list(result)) == 1
        
        item = list(result)[0]
        assert "StationDisplay" in str(item)
        assert item.get_station().get_station_id() == "31069001"

    @patch("app.controllers.meteo_controller.MeteoPipeline")
    def test_get_latest_meteo_data_empty(self, MockPipeline):
        pipeline_instance = MockPipeline.return_value
        pipeline_instance.run.return_value = pd.DataFrame()
        
        controller = MeteoController()
        result = controller.get_latest_meteo_data(["id"])
        
        assert isinstance(result, LinkedList)
        assert len(list(result)) == 0

    @patch("app.controllers.meteo_controller.MeteoPipeline")
    def test_get_latest_meteo_data_error(self, MockPipeline):
        pipeline_instance = MockPipeline.return_value
        df = pd.DataFrame({"col": [1]})
        pipeline_instance.run.return_value = df
        
        controller = MeteoController()
        result = controller.get_latest_meteo_data(["id"])
        
        assert len(list(result)) == 0
