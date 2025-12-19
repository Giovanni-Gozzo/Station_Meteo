"""
Modèle représentant une station météo.
"""

class Station:
    """
    Représente une station météo (identifiant, nom, ville).
    """
    def __init__(self, station_id: str, nom: str, ville: str):
        self.set_station_id(station_id)
        self.set_nom(nom)
        self.set_ville(ville)

    def get_station_id(self) -> str:
        """Retourne l'identifiant unique de la station."""
        return self.__station_id

    def get_nom(self) -> str:
        """Retourne le nom de la station."""
        return self.__nom

    def get_ville(self) -> str:
        """Retourne la ville de localisation."""
        return self.__ville

    def set_station_id(self, valeur: str):
        """Définit l'identifiant de la station."""
        if not isinstance(valeur, str):
            raise ValueError("L'ID de la station doit être une chaîne de caractères.")
        self.__station_id = valeur

    def set_nom(self, valeur: str):
        """Définit le nom de la station."""
        if not isinstance(valeur, str):
            raise ValueError("Le nom de la station doit être une chaîne de caractères.")
        self.__nom = valeur

    def set_ville(self, valeur: str):
        """Définit la ville."""
        if not isinstance(valeur, str):
            raise ValueError("Le nom de la ville doit être une chaîne de caractères.")
        self.__ville = valeur

    def __repr__(self):
        return f"Station(id={self.__station_id}, nom='{self.__nom}', ville='{self.__ville}')"
