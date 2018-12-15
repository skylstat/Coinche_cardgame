from carte import *
from jeu_de_cartes import *
import random

class distribution:
    """On distribue les cartes"""
    def __init__(self):
        """On incrémente directement à self.jeu le jeu MELANGE"""
        self.jeu= random.sample(jeu_de_cartes().paquet,32)
    def distribuer(self):
        self.j= [ [],[],[],[] ]
        for i in range(4):
            for p in range(8):
                carte=self.jeu[0]
                self.j[i].append(carte)
                self.jeu.remove(carte)

        return self.j
