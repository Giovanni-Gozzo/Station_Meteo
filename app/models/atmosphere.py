"""
Modèle réprésentant les conditions atmosphériques.
"""

class Atmosphere:
    """
    Représente les données atmosphériques (température, humidité, pression).
    """
    def __init__(self, temperature: float, humidite: float, pression: float):
        self.set_temperature(temperature)
        self.set_humidite(humidite)
        self.set_pression(pression)

    def get_temperature(self) -> float:
        """Retourne la température en degrés Celsius."""
        return self.__temperature

    def get_humidite(self) -> float:
        """Retourne le taux d'humidité en pourcentage."""
        return self.__humidite

    def get_pression(self) -> float:
        """Retourne la pression atmosphérique en hPa."""
        return self.__pression

    def set_temperature(self, temperature: float):
        """Définit la température avec validation (-30 à 60°C)."""
        if not isinstance(temperature, float):
            raise ValueError("La température doit être un flottant.")
        if temperature < -30 or temperature > 60:
            raise ValueError("La température doit être comprise entre -30°C et 60°C.")
        self.__temperature = temperature

    def set_humidite(self, humidite: float):
        """Définit l'humidité avec validation (0 à 100%)."""
        if not isinstance(humidite, float):
            raise ValueError("L'humidité doit être un flottant.")
        if humidite < 0 or humidite > 100:
            raise ValueError("L'humidité doit être comprise entre 0% et 100%.")
        self.__humidite = humidite

    def set_pression(self, pression: float):
        """Définit la pression."""
        if not isinstance(pression, float):
            raise ValueError("La pression doit être un flottant.")
        self.__pression = pression

    def __repr__(self):
        return (
            f"Atmosphere(temp={self.__temperature}°C, "
            f"humidite={self.__humidite}%, "
            f"pression={self.__pression}hPa)"
        )
