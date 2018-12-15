from carte import *

def valeur_point_cartes(carte):
        """" On établit la valeur des cartes en fonction de l'atout"""
        p=0
        if carte.valeur=='Valet':
                p=20
        if carte.valeur=='9':
                p=14
        if carte.valeur=='As':
                p=11
        if carte.valeur=='10':
                p=10
        if carte.valeur=='Roi':
                p=4
        if carte.valeur=='Dame':
                p=3
        if carte.valeur=='8':
                p=0
        if carte.valeur=='7':
                p=0

        return p
