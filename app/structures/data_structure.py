from abc import ABC, abstractmethod

class DataStructure(ABC):
    @abstractmethod
    def add(self, data):
        """Ajoute un élément à la structure."""
        pass

    @abstractmethod
    def search(self, data):
        """Recherche un élément dans la structure."""
        pass

    @abstractmethod
    def delete(self, data):
        """Supprime un élément de la structure."""
        pass

    @abstractmethod
    def __iter__(self):
        """Permet d'itérer sur les éléments de la structure."""
        pass
