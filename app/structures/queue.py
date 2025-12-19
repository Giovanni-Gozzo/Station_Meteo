"""
Implémentation d'une File (Queue).
"""
from app.structures.data_structure import DataStructure

class Queue(DataStructure):
    """Structure de données de type File (FIFO)."""

    def __init__(self):
        self.items = []

    def add(self, data):
        """Enfile un élément (enqueue)."""
        self.items.append(data)

    def remove(self):
        """Défile un élément (dequeue)."""
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def search(self, data):
        """Recherche si un élément est dans la file."""
        return data in self.items

    def delete(self, data):
        """Supprime la première occurrence de data."""
        if data in self.items:
            self.items.remove(data)

    def is_empty(self):
        """Vérifie si la file est vide."""
        return len(self.items) == 0

    def peek(self):
        """Regarde le premier élément sans l'enlever."""
        if not self.is_empty():
            return self.items[0]
        return None

    def __iter__(self):
        """Itérateur sur les éléments de la file."""
        yield from self.items
