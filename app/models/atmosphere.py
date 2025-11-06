class Atmosphere:
    def __init__(self, temperature: int, humidite: int, pression: int):
        self.set_temperature(temperature)
        self.set_humidite(humidite)
        self.set_pression(pression)

    def get_temperature(self) -> int:
        return self.__temperature

    def get_humidite(self) -> int:
        return self.__humidite

    def get_pression(self) -> int:
        return self.__pression

    def set_temperature(self, temperature: int):
        if not isinstance(temperature, int):
            raise ValueError("La température doit être un entier.")
        if temperature < -30 or temperature > 60:
            raise ValueError("La température doit être comprise entre -30°C et 60°C.")
        self.__temperature = temperature

    def set_humidite(self, humidite: int):
        if not isinstance(humidite, int):
            raise ValueError("L'humidité doit être un entier.")
        if humidite < 0 or humidite > 100:
            raise ValueError("L'humidité doit être comprise entre 0% et 100%.")
        self.__humidite = humidite

    def set_pression(self, pression: int):
        if not isinstance(pression, int):
            raise ValueError("La pression doit être un entier.")
        self.__pression = pression

    def __repr__(self):
        return (
            f"Atmosphere(temp={self.__temperature}°C, "
            f"humidite={self.__humidite}%, "
            f"pression={self.__pression}hPa)"
        )
