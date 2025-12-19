from app.structures.data_structure import DataStructure

class Queue(DataStructure):
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
        return len(self.items) == 0

    def peek(self):
        """Regarde le premier élément sans l'enlever."""
        if not self.is_empty():
            return self.items[0]
        return None

    def __iter__(self):
        for item in self.items:
            yield item
