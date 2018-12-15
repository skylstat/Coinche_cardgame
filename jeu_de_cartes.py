
from carte import *

class jeu_de_cartes:
    """Création d'un jeu de 32 cartes (chaque carte étant une classe) de belote"""
    def __init__(self):
        "Construction du paquet de 32 cartes"
        couleur=('Carreau','Coeur','Pique','Trefle')
        valeur=('7','8','9','10','Valet','Dame','Roi','As')
        self.paquet = []            #paquet contient le jeu de cartes
        for i in range(4):
            for j in range(8):
                self.paquet.append(carte(couleur[i],valeur[j]))
    def jeregarde(self):       #On vérifie que le paquet est bien créé
        return self.paquet
