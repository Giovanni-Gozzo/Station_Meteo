"""
Modèle représentant les données de vent.
"""

class Vent:
    """
    Représente les informations de vent (direction et force).
    """
    # pylint: disable=unknown-option-value, too-many-positional-arguments, too-many-arguments

    def __init__(
        self,
        direction_du_vecteur_de_vent_max: float,
        direction_du_vecteur_vent_moyen: float,
        direction_du_vecteur_de_rafale_de_vent_max: float,
        force_moyenne_du_vecteur_vent: float,
        force_rafale_max: float
    ):
        self.set_direction_du_vecteur_de_vent_max(direction_du_vecteur_de_vent_max)
        self.set_direction_du_vecteur_vent_moyen(direction_du_vecteur_vent_moyen)
        self.set_direction_du_vecteur_de_rafale_de_vent_max(
            direction_du_vecteur_de_rafale_de_vent_max
        )
        self.set_force_moyenne_du_vecteur_vent(force_moyenne_du_vecteur_vent)
        self.set_force_rafale_max(force_rafale_max)

    def get_direction_du_vecteur_de_vent_max(self) -> float:
        """Retourne la direction du vent maximum."""
        return self.__direction_du_vecteur_de_vent_max

    def get_direction_du_vecteur_vent_moyen(self) -> float:
        """Retourne la direction du vent moyen."""
        return self.__direction_du_vecteur_vent_moyen

    def get_direction_du_vecteur_de_rafale_de_vent_max(self) -> float:
        """Retourne la direction de la rafale maximale."""
        return self.__direction_du_vecteur_de_rafale_de_vent_max

    def get_force_moyenne_du_vecteur_vent(self) -> float:
        """Retourne la force moyenne du vent."""
        return self.__force_moyenne_du_vecteur_vent

    def get_force_rafale_max(self) -> float:
        """Retourne la force de la rafale maximale."""
        return self.__force_rafale_max

    def set_direction_du_vecteur_de_vent_max(self, valeur: float):
        """Définit la direction du vent maximum."""
        if not isinstance(valeur, float):
            raise ValueError("La direction du vent max doit être un entier (degrés).")
        if valeur < 0 or valeur > 360:
            raise ValueError("La direction du vent max doit être comprise entre 0 et 360°.")
        self.__direction_du_vecteur_de_vent_max = valeur

    def set_direction_du_vecteur_vent_moyen(self, valeur: float):
        """Définit la direction du vent moyen."""
        if not isinstance(valeur, float):
            raise ValueError("La direction du vent moyen doit être un entier (degrés).")
        if valeur < 0 or valeur > 360:
            raise ValueError("La direction du vent moyen doit être comprise entre 0 et 360°.")
        self.__direction_du_vecteur_vent_moyen = valeur

    def set_direction_du_vecteur_de_rafale_de_vent_max(self, valeur: float):
        """Définit la direction de la rafale maximale."""
        if not isinstance(valeur, float):
            raise ValueError("La direction de la rafale max doit être un entier (degrés).")
        if valeur < 0 or valeur > 360:
            raise ValueError("La direction de la rafale max doit être comprise entre 0 et 360°.")
        self.__direction_du_vecteur_de_rafale_de_vent_max = valeur

    def set_force_moyenne_du_vecteur_vent(self, valeur: float):
        """Définit la force moyenne du vent."""
        if not isinstance(valeur, float):
            raise ValueError("La force moyenne du vent doit être un entier (km/h).")
        if valeur < 0 or valeur > 400:
            raise ValueError("La force moyenne du vent doit être comprise entre 0 et 400 km/h.")
        self.__force_moyenne_du_vecteur_vent = valeur

    def set_force_rafale_max(self, valeur: float):
        """Définit la force de la rafale maximale."""
        if not isinstance(valeur, float):
            raise ValueError("La force de la rafale max doit être un entier (km/h).")
        if valeur < 0 or valeur > 400:
            raise ValueError("La force de la rafale max doit être comprise entre 0 et 400 km/h.")
        self.__force_rafale_max = valeur

    def __repr__(self):
        return (
            f"Vent("
            f"dir_max={self.__direction_du_vecteur_de_vent_max}°, "
            f"dir_moy={self.__direction_du_vecteur_vent_moyen}°, "
            f"dir_rafale_max={self.__direction_du_vecteur_de_rafale_de_vent_max}°, "
            f"force_moy={self.__force_moyenne_du_vecteur_vent}km/h, "
            f"force_rafale_max={self.__force_rafale_max}km/h)"
        )
