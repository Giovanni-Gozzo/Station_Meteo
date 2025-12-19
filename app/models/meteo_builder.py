"""
Module contenant le Builder pour la création d'objets Meteo.
"""
from datetime import datetime
from app.models.meteo import Meteo
from app.models.station import Station
from app.models.vent import Vent
from app.models.pluie import Pluie
from app.models.atmosphere import Atmosphere

class MeteoBuilder:
    """
    Builder Pattern pour la création d'objets Meteo complexes step-by-step.
    """
    def __init__(self):
        self._date = None
        self._station = None
        self._vent = None
        self._pluie = None
        self._atmosphere = None

    def with_date(self, date_val):
        """Définit la date."""
        self._date = date_val
        return self

    def with_station(self, nom, ville, station_id):
        """Définit la station."""
        self._station = Station(station_id, nom, ville)
        return self

    def with_vent(self, dir_vec_max, dir_vec_moyen, dir_rafale_max, force_moy, force_rafale_max):
        """Définit les données de vent."""
        # pylint: disable=too-many-arguments, too-many-positional-arguments
        self._vent = Vent(dir_vec_max, dir_vec_moyen, dir_rafale_max, force_moy, force_rafale_max)
        return self

    def with_pluie(self, intensite_max, cumul):
        """Définit les données de pluie."""
        self._pluie = Pluie(intensite_max, cumul)
        return self

    def with_atmosphere(self, temp, hum, press):
        """Définit les données atmosphériques."""
        self._atmosphere = Atmosphere(temp, hum, press)
        return self

    def build(self) -> Meteo:
        """Construit l'objet Meteo final."""
        # Vérification si des composants sont manquants
        components = [
            self._date,
            self._station,
            self._vent,
            self._pluie,
            self._atmosphere
        ]

        if any(x is None for x in components):
            if not self._station:
                self._station = Station("Inconnu", "Inconnu", "0")
            if not self._vent:
                self._vent = Vent(0, 0, 0, 0, 0)
            if not self._pluie:
                self._pluie = Pluie(0, 0)
            if not self._atmosphere:
                self._atmosphere = Atmosphere(0, 0, 0)
            if not self._date:
                self._date = datetime.now()

        return Meteo(
            date=self._date,
            station=self._station,
            vent=self._vent,
            pluie=self._pluie,
            atmosphere=self._atmosphere
        )
