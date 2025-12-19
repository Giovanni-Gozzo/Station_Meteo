"""
Module définissant l'interface Command.
"""
from abc import ABC, abstractmethod

class Command(ABC):
    """Interface abstraite pour le pattern Command."""
    # pylint: disable=too-few-public-methods

    @abstractmethod
    def execute(self):
        """Exécute la commande."""
