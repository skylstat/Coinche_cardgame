#Ouvrir le fichier COINCHE.py pour jouer ou le fichier TesterlesIA.py pour voir la perfomance des IA

from carte import *
from jeu_de_cartes import *
from distribution import *
from annonces import *
from joueurs import *



class partie:

#On définit la partie à l'aide des joueurs,du jeu de cartes et de l'atout

    def __init__(self,joueurs,atout):
        self.jeu = jeu_de_cartes().paquet
        self.joueurs = joueurs              #Remarque: joueurs sous la forme d'une liste de classe: [ joueur_humain[0],...,joueur_humain[3] ]
        self.atout=atout

    def valeur_point_carte(self,carte):
        """" On établit la valeur des cartes en fonction de l'atout"""
        self.carte=carte
        self.valeur=0
        if self.carte.couleur == self.atout:                                     # Valeurs pour les cartes atouts
            if self.carte.valeur=='Valet':
                self.valeur=20
            if self.carte.valeur=='9':
                self.valeur=14
            if self.carte.valeur=='As':
                self.valeur=11
            if self.carte.valeur=='10':
                self.valeur=10
            if self.carte.valeur=='Roi':
                self.valeur=4
            if self.carte.valeur=='Dame':
                self.valeur=3
            if self.carte.valeur=='8':
                self.valeur=0
            if self.carte.valeur=='7':
                self.valeur=0

        else :                                                          # Valeurs des cartes non atout
            if self.carte.valeur=='As':
                self.valeur=11
            if self.carte.valeur=='10':
                self.valeur=10
            if self.carte.valeur=='Roi':
                self.valeur=4
            if self.carte.valeur=='Dame':
                self.valeur=3
            if self.carte.valeur=='Valet':
                self.valeur=2
            if self.carte.valeur=='9':
                self.valeur=0
            if self.carte.valeur=='8':
                self.valeur=0
            if self.carte.valeur=='7':
                self.valeur=0

        return self.valeur


class pli:

    def __init__(self, partie, premierjoueur):
        self.partie = partie
        self.joueurs = partie.joueurs
        self.joueurcourant = premierjoueur
        self.cartes_posees = []
        self.atout= partie.atout
        self.cartes_atout_posees=[]             


    def cartes_possibles(self, joueur):

        #On définit la liste des cartes que le joueur a le droit de jouer en examinant une par une les cartes de sa main pour savoir si elles sont jouables
        #Si elle est vide, alors le joueur doit pisser

        a=len(joueur.main)
        cartes_possibles=[]

        if len(self.cartes_posees) == 0 :
            cartes_possibles = joueur.main

        else :
            for i in range(a):
                if self.carte_jouable(joueur.main[i])==1 :
                    if joueur.main[i].couleur==self.atout :     #Boucle pour la montée de l'atout
                        if len(self.cartes_atout_posees)==0:
                            cartes_possibles.append(joueur.main[i])
                        else:
                            if all(self.partie.valeur_point_carte(x) < self.partie.valeur_point_carte(joueur.main[i]) for x in self.cartes_atout_posees): #On compare la carte qui est de la couleur atout, a toutes les autres cartes atouts déposées lors de ce pli pour vérifier la montée de l'atout
                                cartes_possibles.append(joueur.main[i])
                    else:
                        cartes_possibles.append(joueur.main[i])

            if len(cartes_possibles)==0 :     
                for i in range(a):
                    if joueur.main[i].couleur==self.atout :
                        if len(self.cartes_atout_posees)==0:
                            cartes_possibles.append(joueur.main[i])
                        else:
                            if all(self.partie.valeur_point_carte(x) < self.partie.valeur_point_carte(joueur.main[i]) for x in self.cartes_atout_posees): #On compare la carte qui est de la couleur atout, a toutes les autres cartes atouts déposées lors de ce pli pour vérifier la montée de l'atout
                                cartes_possibles.append(joueur.main[i])

            if len(cartes_possibles)==0 :                       #Nouvelle boucle dans le cas pour régler le cas où il ne peut pas monter à l'atout mais qu'il a de l'atout
                for i in range(a):
                    if joueur.main[i].couleur==self.atout :
                        cartes_possibles.append(joueur.main[i])

            if len(cartes_possibles) == 0 :
                print("Vous devez pisser")
                cartes_possibles= joueur.main


        return cartes_possibles



    def carte_jouable(self,carte):

        #On regarde si la carte est jouable, si c'est le cas self.jouable vaut 1, sinon il vaut 0

        self.jouable= 0

        if carte.couleur == self.cartes_posees[0].couleur :
            self.jouable = 1

        return self.jouable


    def vainqueur(self,partie):

        #On calcule qui remporte le pli en fonction des cartes posées et de l'atout de la partie
        k=partie
        a=self.cartes_posees[0]
        b=k.valeur_point_carte(a)
        c=0
        for i in range(1,4):
            if a.couleur == k.atout :
                if self.cartes_posees[i].couleur == k.atout :
                    if k.valeur_point_carte(self.cartes_posees[i]) > b :
                        a=self.cartes_posees[i]
                        b=k.valeur_point_carte(self.cartes_posees[i])
                        c=i
            else :
                if self.cartes_posees[i].couleur == k.atout :
                    a=self.cartes_posees[i]
                    b=k.valeur_point_carte(self.cartes_posees[i])
                    c=i
                else :
                    if k.valeur_point_carte(self.cartes_posees[i]) > b :
                        a=self.cartes_posees[i]
                        b=k.valeur_point_carte(self.cartes_posees[i])
                        c=i
        return c

    def points(self):
                        #Compteur de points pour le pli
        p=0
        for i in range(4):
            p=p+partie(self.joueurs,self.atout).valeur_point_carte(self.cartes_posees[i])
        return p
