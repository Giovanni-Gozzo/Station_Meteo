import pytest
from datetime import datetime
from app.models.station import Station
from app.models.vent import Vent
from app.models.pluie import Pluie
from app.models.atmosphere import Atmosphere
from app.models.meteo import Meteo

@pytest.fixture
def sample_date():
    return datetime(2023, 10, 27, 12, 0, 0)

@pytest.fixture
def sample_station():
    return Station("31069001", "TOULOUSE-BLAGNAC", "Toulouse")

@pytest.fixture
def sample_vent():
    return Vent(320.0, 310.0, 340.0, 15.5, 25.0)

@pytest.fixture
def sample_pluie():
    return Pluie(2.0, 5.5)

@pytest.fixture
def sample_atmosphere():
    return Atmosphere(20.5, 60.0, 1013.2)

@pytest.fixture
def sample_meteo(sample_date, sample_station, sample_vent, sample_pluie, sample_atmosphere):
    return Meteo(sample_date, sample_station, sample_vent, sample_pluie, sample_atmosphere)

@pytest.fixture
def mock_api_response_json():
    return {
        "results": [
            {
                "heure_de_paris": "2023-10-27T10:00:00+02:00",
                "station_id": "31069001",
                "nom_station": "TOULOUSE-BLAGNAC",
                "ville": "Toulouse",
                "temperature_en_degre_c": 18.5,
                "humidite": 75,
                "pression": 1015.0,
                "pluie": 0.0,
                "pluie_intensite_max": 0.0,
                "force_moyenne_du_vecteur_vent": 10.0,
                "force_rafale_max": 15.0,
                "direction_du_vecteur_vent_moyen": 180,
                "direction_du_vecteur_de_rafale_de_vent_max": 190,
                "direction_du_vecteur_de_vent_max_en_degres": 185
            }
        ]
    }
