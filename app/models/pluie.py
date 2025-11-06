class Pluie:
    def __init__(self, pluie_intensite_max: float, pluie: float):
        self.set_pluie_intensite_max(pluie_intensite_max)
        self.set_pluie(pluie)

    def get_pluie_intensite_max(self) -> float:
        return self.__pluie_intensite_max

    def get_pluie(self) -> float:
        return self.__pluie

    def set_pluie_intensite_max(self, valeur: float):
        if not isinstance(valeur, (int, float)):
            raise ValueError("L'intensité maximale de pluie doit être un nombre.")
        self.__pluie_intensite_max = float(valeur)

    def set_pluie(self, valeur: float):
        if not isinstance(valeur, (int, float)):
            raise ValueError("La quantité de pluie doit être un nombre.")
        self.__pluie = float(valeur)

    def __repr__(self):
        return f"Pluie(intensite_max={self.__pluie_intensite_max} mm/h, cumul={self.__pluie} mm)"
