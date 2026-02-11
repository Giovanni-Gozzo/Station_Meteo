from datetime import datetime
import pytest
from app.models.meteo import Meteo
from app.models.meteo_builder import MeteoBuilder
from app.models.station import Station
from app.models.station_display import StationDisplay
from app.models.vent import Vent
from app.models.pluie import Pluie
from app.models.atmosphere import Atmosphere
import sys
from io import StringIO
from unittest.mock import patch

class TestModels:
    def test_station_init(self, sample_station):
        assert sample_station.get_station_id() == "31069001"
        assert sample_station.get_nom() == "TOULOUSE-BLAGNAC"
        assert sample_station.get_ville() == "Toulouse"
        assert "Station(id=31069001" in str(sample_station)

    def test_vent_init(self, sample_vent):
        assert sample_vent.get_direction_du_vecteur_de_vent_max() == 320.0
        assert sample_vent.get_force_moyenne_du_vecteur_vent() == 15.5
        assert sample_vent.get_direction_du_vecteur_de_rafale_de_vent_max() == 340.0
        assert "Vent(dir_max=320.0" in str(sample_vent)

    def test_pluie_init(self, sample_pluie):
        assert sample_pluie.get_pluie_intensite_max() == 2.0
        assert sample_pluie.get_pluie() == 5.5
        assert "Pluie(" in str(sample_pluie)
        assert "max=2.0" in str(sample_pluie)

    def test_atmosphere_init(self, sample_atmosphere):
        assert sample_atmosphere.get_temperature() == 20.5
        assert sample_atmosphere.get_humidite() == 60
        assert sample_atmosphere.get_pression() == 1013.2
        assert "Atmosphere(temp=20.5" in str(sample_atmosphere)

    def test_meteo_init(self, sample_meteo, sample_date):
        assert sample_meteo.get_date() == sample_date
        assert isinstance(sample_meteo.get_station(), Station)
        assert isinstance(sample_meteo.get_vent(), Vent)
        
        with pytest.raises(ValueError):
            sample_meteo.set_date("not-a-date")
            
        with pytest.raises(ValueError):
            sample_meteo.set_station("not-a-station")

        with pytest.raises(ValueError):
            sample_meteo.set_vent("not-a-vent")

        with pytest.raises(ValueError):
            sample_meteo.set_pluie("not-a-pluie")
            
        with pytest.raises(ValueError):
            sample_meteo.set_atmosphere("not-an-atmosphere")

        assert "Meteo(date=" in str(sample_meteo)

    def test_vent_validation(self):
        v = Vent(0.0, 0.0, 0.0, 0.0, 0.0)
        # Type checks
        with pytest.raises(ValueError): v.set_direction_du_vecteur_de_vent_max("0")
        with pytest.raises(ValueError): v.set_direction_du_vecteur_vent_moyen("0")
        with pytest.raises(ValueError): v.set_direction_du_vecteur_de_rafale_de_vent_max("0")
        with pytest.raises(ValueError): v.set_force_moyenne_du_vecteur_vent("0")
        with pytest.raises(ValueError): v.set_force_rafale_max("0")
        
        # Range checks
        with pytest.raises(ValueError): v.set_direction_du_vecteur_de_vent_max(-1.0)
        with pytest.raises(ValueError): v.set_direction_du_vecteur_de_vent_max(361.0)
        
        with pytest.raises(ValueError): v.set_direction_du_vecteur_vent_moyen(-1.0)
        with pytest.raises(ValueError): v.set_direction_du_vecteur_vent_moyen(361.0)

        with pytest.raises(ValueError): v.set_direction_du_vecteur_de_rafale_de_vent_max(-1.0)
        with pytest.raises(ValueError): v.set_direction_du_vecteur_de_rafale_de_vent_max(361.0)

        with pytest.raises(ValueError): v.set_force_moyenne_du_vecteur_vent(-1.0)
        with pytest.raises(ValueError): v.set_force_moyenne_du_vecteur_vent(401.0)

        with pytest.raises(ValueError): v.set_force_rafale_max(-1.0)
        with pytest.raises(ValueError): v.set_force_rafale_max(401.0)

    def test_atmosphere_validation(self):
        a = Atmosphere(0.0, 0.0, 0.0)
        with pytest.raises(ValueError): a.set_temperature("0")
        with pytest.raises(ValueError): a.set_temperature(-31.0)
        with pytest.raises(ValueError): a.set_temperature(61.0)

        with pytest.raises(ValueError): a.set_humidite("0")
        with pytest.raises(ValueError): a.set_humidite(-1.0)
        with pytest.raises(ValueError): a.set_humidite(101.0)
        
        with pytest.raises(ValueError): a.set_pression("0")

    def test_pluie_validation(self):
        p = Pluie(0.0, 0.0)
        with pytest.raises(ValueError): p.set_pluie_intensite_max("0")
        with pytest.raises(ValueError): p.set_pluie("0")
        
    def test_station_validation(self):
        s = Station("id", "nom", "ville")
        with pytest.raises(ValueError): s.set_station_id(123)
        with pytest.raises(ValueError): s.set_nom(123)
        with pytest.raises(ValueError): s.set_ville(123)


class TestMeteoBuilder:
    def test_build_complete(self, sample_date):
        builder = MeteoBuilder()
        meteo = (builder
            .with_date(sample_date)
            .with_station("Toulouse", "France", "123")
            .with_vent(10.0, 20.0, 30.0, 40.0, 50.0)
            .with_pluie(5.0, 10.0)
            .with_atmosphere(25.0, 50.0, 1013.0)
            .build())
            
        assert meteo.get_date() == sample_date
        assert meteo.get_station().get_station_id() == "123"
        assert meteo.get_atmosphere().get_temperature() == 25.0

    def test_build_partial_defaults(self):
        builder = MeteoBuilder()
        meteo = builder.build()
        
        assert isinstance(meteo.get_date(), datetime)
        assert meteo.get_station().get_nom() == "Inconnu"
        assert meteo.get_vent().get_force_moyenne_du_vecteur_vent() == 0
        assert meteo.get_pluie().get_pluie() == 0
        assert meteo.get_atmosphere().get_temperature() == 0


class TestStationDisplay:
    def test_display_methods(self, sample_meteo):
        display = StationDisplay(sample_meteo)
        
        assert display.get_date() == sample_meteo.get_date()
        assert display.get_station() == sample_meteo.get_station()
        assert display.get_vent() == sample_meteo.get_vent()
        assert display.get_pluie() == sample_meteo.get_pluie()
        assert display.get_atmosphere() == sample_meteo.get_atmosphere()
        
        assert display.formatted_date() == "27/10/2023 à 12h00"
        assert display.formatted_temp() == "20.5 °C"
        assert display.formatted_wind() == "15.5 km/h"
        assert display.formatted_humidity() == "60.0 %"
        assert display.formatted_pressure() == "1013.2 hPa"
        
        assert "StationDisplay(" in str(display)
