"""
Modèle principal représentant un relevé météo complet.
Agrège les données de Station, Vent, Pluie et Atmosphère.
"""
from datetime import datetime
from app.models.station import Station
from app.models.vent import Vent
from app.models.pluie import Pluie
from app.models.atmosphere import Atmosphere

class Meteo:
    """
    Classe composite regroupant toutes les informations d'un relevé météo.
    """
    # pylint: disable=too-many-arguments, too-many-positional-arguments, unknown-option-value

    def __init__(self, date: datetime,
                 station: Station,
                 vent: Vent,
                 pluie: Pluie,
                 atmosphere: Atmosphere):
        self.set_date(date)
        self.set_station(station)
        self.set_vent(vent)
        self.set_pluie(pluie)
        self.set_atmosphere(atmosphere)

    def get_date(self) -> datetime:
        """Retourne la date et l'heure du relevé."""
        return self.__date

    def get_station(self) -> Station:
        """Retourne l'objet Station associé."""
        return self.__station

    def get_vent(self) -> Vent:
        """Retourne l'objet Vent associé."""
        return self.__vent

    def get_pluie(self) -> Pluie:
        """Retourne l'objet Pluie associé."""
        return self.__pluie

    def get_atmosphere(self) -> Atmosphere:
        """Retourne l'objet Atmosphere associé."""
        return self.__atmosphere

    def set_date(self, date: datetime):
        """Définit la date du relevé."""
        if not isinstance(date, datetime):
            raise ValueError("La date doit être un objet datetime.")
        self.__date = date

    def set_station(self, station: Station):
        """Définit la station du relevé."""
        if not isinstance(station, Station):
            raise ValueError("La station doit être une instance de la classe Station.")
        self.__station = station

    def set_vent(self, vent: Vent):
        """Définit les données de vent."""
        if not isinstance(vent, Vent):
            raise ValueError("Le vent doit être une instance de la classe Vent.")
        self.__vent = vent

    def set_pluie(self, pluie: Pluie):
        """Définit les données de pluie."""
        if not isinstance(pluie, Pluie):
            raise ValueError("La pluie doit être une instance de la classe Pluie.")
        self.__pluie = pluie

    def set_atmosphere(self, atmosphere: Atmosphere):
        """Définit les données atmosphériques."""
        if not isinstance(atmosphere, Atmosphere):
            raise ValueError("L'atmosphère doit être une instance de la classe Atmosphere.")
        self.__atmosphere = atmosphere

    def __repr__(self):
        return (
            f"Meteo("
            f"date={self.__date.strftime('%Y-%m-%d %H:%M:%S')}, "
            f"station={self.__station}, "
            f"vent={self.__vent}, "
            f"pluie={self.__pluie}, "
            f"atmosphere={self.__atmosphere})"
        )
