"""
Modèle représentant une ville.
"""

class Ville:
    """
    Représente une ville.
    """
    def __init__(self, nom: str):
        self.__nom = nom

    def get_nom(self) -> str:
        """Retourne le nom de la ville."""
        return self.__nom

    def set_nom(self, nom: str):
        """Définit le nom de la ville."""
        if not isinstance(nom, str):
            raise ValueError("Le nom de la ville doit être une chaîne de caractères.")
        self.__nom = nom

    def __repr__(self):
        return f"La villle est {self.__nom}"
