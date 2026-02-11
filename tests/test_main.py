import pytest
from unittest.mock import patch, MagicMock
from app.main import app, get_sort_key
from app.models.meteo import Meteo
from app.models.station import Station
from app.models.station_display import StationDisplay
from datetime import datetime
import sys

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

class TestMain:
    def test_index_route(self, client):
        with patch("pandas.read_csv") as mock_read_csv:
            mock_read_csv.return_value = MagicMock()
            mock_read_csv.return_value.__getitem__.return_value.tolist.return_value = ["31069001"]
            
            response = client.get("/")
            assert response.status_code == 200
            assert b"31069001" in response.data

    def test_index_route_error(self, client):
        with patch("pandas.read_csv", side_effect=Exception("Error")):
            response = client.get("/")
            assert response.status_code == 200

    def test_data_route_no_selection(self, client):
        response = client.get("/data")
        assert response.status_code == 302 # Redirect

    @patch("app.main.controller.get_latest_meteo_data")
    def test_data_route_success(self, mock_get_data, client, sample_meteo):
        mock_get_data.return_value = [StationDisplay(sample_meteo)]
        
        response = client.get("/data?station_id=31069001")
        assert response.status_code == 200
        assert b"Toulouse" in response.data

    @patch("app.main.controller.get_latest_meteo_data")
    def test_data_route_error(self, mock_get_data, client):
        mock_get_data.side_effect = Exception("Pipeline Error")
        
        response = client.get("/data?station_id=31069001")
        assert response.status_code == 200
        assert b"Aucune donn" in response.data

    def test_get_sort_key(self, sample_meteo):        
        display = StationDisplay(sample_meteo)
        
        assert get_sort_key(display, "date") == sample_meteo.get_date()
        assert get_sort_key(display, "station_id") == "31069001"
        assert get_sort_key(display, "ville") == "Toulouse"
        assert get_sort_key(display, "unknown") == sample_meteo.get_date()

    def test_main_execution(self):
        import runpy
        import os
        
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        main_path = os.path.join(base_dir, "app", "main.py")
        
        with patch("flask.Flask.run") as mock_run:
            runpy.run_path(main_path, run_name="__main__")
            mock_run.assert_called_once()
