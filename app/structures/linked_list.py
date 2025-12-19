"""
Implémentation d'une Liste Chaînée.
"""
from app.structures.data_structure import DataStructure

class Node:
    """Représente un nœud dans la liste chaînée."""
    # pylint: disable=too-few-public-methods

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(DataStructure):
    """Implémentation d'une liste chaînée simple."""
    def __init__(self):
        self.head = None

    def add(self, data):
        """Ajoute un élément à la fin de la liste."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def search(self, data):
        """Vérifie si un élément est présent."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def delete(self, data):
        """Supprime la première occurrence d'un élément."""
        current = self.head
        if current and current.data == data:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next
        current = None

    def __iter__(self):
        """Itérateur sur les données des nœuds."""
        current = self.head
        while current:
            yield current.data
            current = current.next
