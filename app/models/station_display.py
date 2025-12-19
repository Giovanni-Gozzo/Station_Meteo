"""
Module contenant le décorateur pour l'affichage de la station.
"""
from datetime import datetime
from app.models.meteo import Meteo

class StationDisplay:
    """Décorateur pour l'objet Meteo afin de formater les données pour l'affichage."""

    def __init__(self, meteo: Meteo):
        self._meteo = meteo

    def get_date(self) -> datetime:
        """Retourne la date de l'objet Meteo décoré."""
        return self._meteo.get_date()

    def get_station(self):
        """Retourne la station de l'objet Meteo décoré."""
        return self._meteo.get_station()

    def get_vent(self):
        """Retourne le vent de l'objet Meteo décoré."""
        return self._meteo.get_vent()

    def get_pluie(self):
        """Retourne la pluie de l'objet Meteo décoré."""
        return self._meteo.get_pluie()

    def get_atmosphere(self):
        """Retourne l'atmosphère de l'objet Meteo décoré."""
        return self._meteo.get_atmosphere()

    def formatted_date(self):
        """Retourne la date formatée pour l'affichage."""
        return self._meteo.get_date().strftime('%d/%m/%Y à %Hh%M')

    def formatted_temp(self):
        """Retourne la température formatée pour l'affichage."""
        return f"{self._meteo.get_atmosphere().get_temperature()} °C"

    def formatted_wind(self):
        """Retourne la force du vent formatée pour l'affichage."""
        return f"{self._meteo.get_vent().get_force_moyenne_du_vecteur_vent()} km/h"

    def formatted_humidity(self):
        """Retourne l'humidité formatée pour l'affichage."""
        return f"{self._meteo.get_atmosphere().get_humidite()} %"

    def formatted_pressure(self):
        """Retourne la pression formatée pour l'affichage."""
        return f"{self._meteo.get_atmosphere().get_pression()} hPa"

    def __repr__(self):
        return f"StationDisplay({self._meteo})"
