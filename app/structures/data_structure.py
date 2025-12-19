"""
Module définissant l'interface pour les structures de données.
"""
from abc import ABC, abstractmethod

class DataStructure(ABC):
    """Interface abstraite pour les structures de données personnalisées."""

    @abstractmethod
    def add(self, data):
        """Ajoute un élément à la structure."""

    @abstractmethod
    def search(self, data):
        """Recherche un élément dans la structure."""

    @abstractmethod
    def delete(self, data):
        """Supprime un élément de la structure."""

    @abstractmethod
    def __iter__(self):
        """Permet d'itérer sur les éléments de la structure."""
