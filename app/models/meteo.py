from datetime import datetime
from app.models.station import Station
from app.models.vent import Vent
from app.models.pluie import Pluie
from app.models.atmosphere import Atmosphere

class Meteo:
    def __init__(self, date: datetime, station: Station, vent: Vent, pluie: Pluie, atmosphere: Atmosphere):
        self.set_date(date)
        self.set_station(station)
        self.set_vent(vent)
        self.set_pluie(pluie)
        self.set_atmosphere(atmosphere)

    def get_date(self) -> datetime:
        return self.__date

    def get_station(self) -> Station:
        return self.__station

    def get_vent(self) -> Vent:
        return self.__vent

    def get_pluie(self) -> Pluie:
        return self.__pluie

    def get_atmosphere(self) -> Atmosphere:
        return self.__atmosphere

    def set_date(self, date: datetime):
        if not isinstance(date, datetime):
            raise ValueError("La date doit être un objet datetime.")
        self.__date = date

    def set_station(self, station: Station):
        if not isinstance(station, Station):
            raise ValueError("La station doit être une instance de la classe Station.")
        self.__station = station

    def set_vent(self, vent: Vent):
        if not isinstance(vent, Vent):
            raise ValueError("Le vent doit être une instance de la classe Vent.")
        self.__vent = vent

    def set_pluie(self, pluie: Pluie):
        if not isinstance(pluie, Pluie):
            raise ValueError("La pluie doit être une instance de la classe Pluie.")
        self.__pluie = pluie

    def set_atmosphere(self, atmosphere: Atmosphere):
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
