from datetime import datetime
from app.models.meteo import Meteo

class StationDisplay:
    """Décorateur pour l'objet Meteo afin de formater les données pour l'affichage."""

    def __init__(self, meteo: Meteo):
        self._meteo = meteo

    def get_date(self) -> datetime:
        return self._meteo.get_date()

    def get_station(self):
        return self._meteo.get_station()

    def get_vent(self):
        return self._meteo.get_vent()
    
    def get_pluie(self):
        return self._meteo.get_pluie()

    def get_atmosphere(self):
        return self._meteo.get_atmosphere()

    def formatted_date(self):
        return self._meteo.get_date().strftime('%d/%m/%Y à %Hh%M')

    def formatted_temp(self):
        return f"{self._meteo.get_atmosphere().get_temperature()} °C"

    def formatted_wind(self):
        return f"{self._meteo.get_vent().get_force_moyenne_du_vecteur_vent()} km/h"
    
    def formatted_humidity(self):
        return f"{self._meteo.get_atmosphere().get_humidite()} %"
    
    def formatted_pressure(self):
        return f"{self._meteo.get_atmosphere().get_pression()} hPa"

    def __repr__(self):
        return f"StationDisplay({self._meteo})"
