class Station:
    def __init__(self, station_id: str, nom: str, ville: str):
        self.set_station_id(station_id)
        self.set_nom(nom)
        self.set_ville(ville)

    def get_station_id(self) -> str:
        return self.__station_id

    def get_nom(self) -> str:
        return self.__nom

    def get_ville(self) -> str:
        return self.__ville

    def set_station_id(self, valeur: str):
        if not isinstance(valeur, str):
            raise ValueError("L'ID de la station doit être une chaîne de caractères.")
        self.__station_id = valeur

    def set_nom(self, valeur: str):
        if not isinstance(valeur, str):
            raise ValueError("Le nom de la station doit être une chaîne de caractères.")
        self.__nom = valeur

    def set_ville(self, valeur: str):
        if not isinstance(valeur, str):
            raise ValueError("Le nom de la ville doit être une chaîne de caractères.")
        self.__ville = valeur

    def __repr__(self):
        return f"Station(id={self.__station_id}, nom='{self.__nom}', ville='{self.__ville}')"
