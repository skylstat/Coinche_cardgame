
#6 types de joueur avec un système de jeu différent: humain,random, IA1, IA2,IA3,IA4.
#Le fichier TesterlesIA.py permet d'évaluer les différentes performances des IA.

import operator

from carte import *
from jeu_de_cartes import *
from distribution import *
from annonces import *
from valeurs_essentielles import*
from conversion import *


class joueur_humain:


    def __init__(self,jeu,i):
        self.main = jeu[i]

            
    def choisis_cartes(self,pli):
        l=[]
        self.cartes_jouables=[]
        self.cartes_jouables_noms=[]
        a=pli.cartes_possibles(self)

        for i in range(len(self.main)) :
            l.append(self.main[i].nom())
        print("Voici votre main : {0} \n ".format(l))

        for i in range(len(a)):
            self.cartes_jouables_noms.append(a[i].nom())
            self.cartes_jouables.append(a[i])
        print("Voici les cartes que vous pouvez jouer : {0} \n ".format(self.cartes_jouables_noms))
        x = int(input(("Quel carte voulez-vous jouer? (Taper 0 pour la 1ere, 1 pour 2eme, 2 pour la 3eme, 3 pour la 4eme, ..., 7 pour la 8eme) ")))                 #interaction du joueur et de la console

        while x >= len(self.cartes_jouables) :                                      #Boucle while pour empêcher les fausses manipulations : mauvais type ou mauvaise indexation
            print("Vous ne pouvez jouer cela ! Selectionnez à nouveau une carte dans celles qui sont proposées")
            x = int(input(("Quel carte voulez-vous jouer? (Taper 0 pour la 1ere, 1 pour 2eme, 2 pour la 3eme, 3 pour la 4eme, ..., 7 pour la 8eme) ")))


        for i in range(len(self.cartes_jouables)) :                                #Action du joueur
            if x==i:
                print(" Vous jouez : {0} \n \n".format(self.cartes_jouables_noms[i]))
                self.joue(pli,x)

    def joue(self, pli, i):
        pli.cartes_posees.append(self.cartes_jouables[i])
        if self.cartes_jouables[i].couleur==pli.atout:               #Utile pour effectuer la montée à l'atout
            pli.cartes_atout_posees.append(self.cartes_jouables[i])
        self.main.remove(self.cartes_jouables[i])


class joueur_random:        #Ordinateur qui choisit au hasard la carte qu'il joue parmi les cartes qui lui sont possibles


    def __init__(self,jeu,i):
        self.main = jeu[i]



    def choisis_cartes(self,pli):
        l=[]
        m=[]
        self.cartes_jouables=[]
        self.cartes_jouables_noms=[]
        a=pli.cartes_possibles(self)

        for i in range(len(self.main)) :
            l.append(self.main[i].nom())

        for i in range(len(a)):
            self.cartes_jouables_noms.append(a[i].nom())
            self.cartes_jouables.append(a[i])

        for i in range(len(self.cartes_jouables)) :
            m.append(i)
        x=random.choice(m)

        for i in range(len(self.cartes_jouables)) :                                #Action du joueur
            if x==i:
                print(" King Kong joue : {0} \n \n".format(self.cartes_jouables_noms[i]))
                self.joue(pli,x)


    def joue(self, pli, i):
        pli.cartes_posees.append(self.cartes_jouables[i])
        if self.cartes_jouables[i].couleur==pli.atout:               #Utile pour effectuer la montée à l'atout
            pli.cartes_atout_posees.append(self.cartes_jouables[i])
        self.main.remove(self.cartes_jouables[i])
        """del(self.main[i])"""

class joueur_IA1:

    # Joue toujours sa carte la plus forte possible

    def __init__(self,jeu,i):
        self.main = jeu[i]

    def choisis_annonce(self):
        ann=0
        main=self.main
        l=[(0,0) for i in range(4)]
        for i in range(8):
            if main[i].couleur == 'Carreau':
                v0=valeur_point_cartes(main[i])
                l[0]=tuple(map(operator.add, l[0] , (1,v0)))
                #print(valeur_point_cartes(main[i]))
            if main[i].couleur == 'Coeur':
                v1=valeur_point_cartes(main[i])
                l[1]=tuple(map(operator.add, l[1] , (1,v1)))
                #print(valeur_point_cartes(main[i]))
            if main[i].couleur == 'Pique':
                v2=valeur_point_cartes(main[i])
                l[2]=tuple(map(operator.add, l[2] , (1,v2)))
                #print(valeur_point_cartes(main[i]))
            if main[i].couleur == 'Trefle':
                v3=valeur_point_cartes(main[i])
                l[3]=tuple(map(operator.add, l[3] , (1,v3)))
                #print(valeur_point_cartes(main[i]))
        maxi=(0,0)
        pos=0
        for j in range(4):
            if l[j]>maxi:                       
                maxi=l[j]
                pos=j
        if maxi[1]>=27 and l[j][0]>=3:
                ann=90
        if maxi[1]>=37:
                ann=100
        if maxi[1]>=45:
                ann=110
        if maxi[1]>=55:
                ann=120
        return (ann,pos)
            
            

    def choisis_cartes(self,pli):
        m=0
        b=0
        l=[]
        m=[]
        self.cartes_jouables=[]
        self.cartes_jouables_noms=[]
        self.point_carte=[]
        a=pli.cartes_possibles(self)

        for i in range(len(self.main)) :
            l.append(self.main[i].nom())



        for i in range(len(a)):
            self.cartes_jouables_noms.append(a[i].nom())
            self.cartes_jouables.append(a[i])
            self.point_carte.append(pli.partie.valeur_point_carte(a[i]))

        m=max(self.point_carte)
        for i in range(len(self.point_carte)):
            if self.point_carte[i]==m:
                b=i

        x=b

        for i in range(len(self.cartes_jouables)) :                                
            if x==i:
                print(" Mario joue : {0} \n \n".format(self.cartes_jouables_noms[i]))
                self.joue(pli,x)


    def joue(self, pli, i):
        pli.cartes_posees.append(self.cartes_jouables[i])
        if self.cartes_jouables[i].couleur==pli.atout:               #Utile pour effectuer la montée à l'atout
            pli.cartes_atout_posees.append(self.cartes_jouables[i])
        self.main.remove(self.cartes_jouables[i])


class joueur_IA2:

        #Si le joueur a des chances de gagner le pli alors il jouera sa carte la plus forte,sinon il jouera sa plus faible carte possible.

    def __init__(self,jeu,i):
        self.main = jeu[i]

    def choisis_annonce(self):
        ann=0
        main=self.main
        l=[(0,0) for i in range(4)]
        for i in range(8):
            if main[i].couleur == 'Carreau':
                v0=valeur_point_cartes(main[i])
                l[0]=tuple(map(operator.add, l[0] , (1,v0)))
                #print(valeur_point_cartes(main[i]))
            if main[i].couleur == 'Coeur':
                v1=valeur_point_cartes(main[i])
                l[1]=tuple(map(operator.add, l[1] , (1,v1)))
                #print(valeur_point_cartes(main[i]))
            if main[i].couleur == 'Pique':
                v2=valeur_point_cartes(main[i])
                l[2]=tuple(map(operator.add, l[2] , (1,v2)))
                #print(valeur_point_cartes(main[i]))
            if main[i].couleur == 'Trefle':
                v3=valeur_point_cartes(main[i])
                l[3]=tuple(map(operator.add, l[3] , (1,v3)))
                #print(valeur_point_cartes(main[i]))
        maxi=(0,0)
        pos=0
        for j in range(4):
            if l[j]>maxi:                       
                maxi=l[j]
                pos=j
        if maxi[1]>=27 and l[j][0]>=3:
                ann=90
        if maxi[1]>=37:
                ann=100
        if maxi[1]>=45:
                ann=110
        if maxi[1]>=55:
                ann=120
        return (ann,pos)
            

    def choisis_cartes(self,pli):
        m=0
        b=0
        l=[]
        m=[]
        self.cartes_jouables=[]                        #On affiche la main du joueur et également les cartes qu'il peut jouer pour pouvoir vérifier si les règles sont bien respectés
        self.cartes_jouables_noms=[]
        self.point_carte=[]
        a=pli.cartes_possibles(self)

        for i in range(len(self.main)) :
            l.append(self.main[i].nom())



        for i in range(len(a)):
            self.cartes_jouables_noms.append(a[i].nom())
            self.cartes_jouables.append(a[i])
            self.point_carte.append(pli.partie.valeur_point_carte(a[i]))

        m=max(self.point_carte)

        if len(pli.cartes_posees)==0:                                       #Si c'est le premier joueur du pli, il joue sa carte la plus forte
                for i in range(len(self.point_carte)):                          #Boucle qui permet de trouver la position de la carte de la plus grande valeur dans la liste des valeurs des cartes jouables
                    if self.point_carte[i]==m:
                        b=i
        else:                                                               #Si ce n'est pas le premier joueur, il joue sa carte la plus forte si il peut gagner le pli, sinon sa plus faible
            n=[]
            for i in range(len(pli.cartes_posees)):
                n.append(pli.partie.valeur_point_carte(pli.cartes_posees[i]))
            q=max(n)
            if m > q :
                for i in range(len(self.point_carte)):
                    if self.point_carte[i]==m:
                        b=i
            else:
                for i in range(len(self.point_carte)):
                    if self.point_carte[i]==min(self.point_carte):
                        b=i

        x=b

        for i in range(len(self.cartes_jouables)) :                                #Action du joueur
            if x==i:
                print(" Luigi joue : {0} \n \n".format(self.cartes_jouables_noms[i]))
                self.joue(pli,x)


    def joue(self, pli, i):
        pli.cartes_posees.append(self.cartes_jouables[i])
        if self.cartes_jouables[i].couleur==pli.atout:               #Utile pour effectuer la montée à l'atout
            pli.cartes_atout_posees.append(self.cartes_jouables[i])
        self.main.remove(self.cartes_jouables[i])



class joueur_IA3:

    #Joue toujours sa carte la plus forte possible sauf s'il commence le tour, il jouera alors une carte aléatoirement


    def __init__(self,jeu,i):
        self.main = jeu[i]

    def choisis_annonce(self):
        ann=0
        main=self.main
        l=[(0,0) for i in range(4)]
        for i in range(8):
            if main[i].couleur == 'Carreau':
                v0=valeur_point_cartes(main[i])
                l[0]=tuple(map(operator.add, l[0] , (1,v0)))
                #print(valeur_point_cartes(main[i]))
            if main[i].couleur == 'Coeur':
                v1=valeur_point_cartes(main[i])
                l[1]=tuple(map(operator.add, l[1] , (1,v1)))
                #print(valeur_point_cartes(main[i]))
            if main[i].couleur == 'Pique':
                v2=valeur_point_cartes(main[i])
                l[2]=tuple(map(operator.add, l[2] , (1,v2)))
                #print(valeur_point_cartes(main[i]))
            if main[i].couleur == 'Trefle':
                v3=valeur_point_cartes(main[i])
                l[3]=tuple(map(operator.add, l[3] , (1,v3)))
                #print(valeur_point_cartes(main[i]))
        maxi=(0,0)
        pos=0
        for j in range(4):
            if l[j]>maxi:                       
                maxi=l[j]
                pos=j
        if maxi[1]>=27 and l[j][0]>=3:
                ann=90
        if maxi[1]>=37:
                ann=100
        if maxi[1]>=45:
                ann=110
        if maxi[1]>=55:
                ann=120
        return (ann,pos)

    def choisis_cartes(self,pli):
        m=0
        b=0
        l=[]
        m=[]
        self.cartes_jouables=[]
        self.cartes_jouables_noms=[]
        self.point_carte=[]
        a=pli.cartes_possibles(self)

        for i in range(len(self.main)) :
            l.append(self.main[i].nom())



        for i in range(len(a)):
            self.cartes_jouables_noms.append(a[i].nom())
            self.cartes_jouables.append(a[i])
            self.point_carte.append(pli.partie.valeur_point_carte(a[i]))

        m=max(self.point_carte)

        if len(pli.cartes_posees)==0:
            r=[]
            for i in range(len(self.cartes_jouables)):
                r.append(i)
                b=random.choice(r)
        else:
            for i in range(len(self.point_carte)):
                if self.point_carte[i]==m:
                    b=i

        x=b

        for i in range(len(self.cartes_jouables)) :                                #Action du joueur
            if x==i:
                print(" Daisy : {0} \n \n".format(self.cartes_jouables_noms[i]))
                self.joue(pli,x)


    def joue(self, pli, i):
        pli.cartes_posees.append(self.cartes_jouables[i])
        if self.cartes_jouables[i].couleur==pli.atout:               #Utile pour effectuer la montée à l'atout
            pli.cartes_atout_posees.append(self.cartes_jouables[i])
        self.main.remove(self.cartes_jouables[i])

class joueur_IA4:

    #Si il peut gagner le pli, il jouera sa carte la plus forte, sinon il joue sa plus faible. Joue une carte au hasard si il doit commencer le plie

    def __init__(self,jeu,i):
        self.main = jeu[i]

    def choisis_annonce(self):
        ann=0
        main=self.main
        l=[(0,0) for i in range(4)]
        for i in range(8):
            if main[i].couleur == 'Carreau':
                v0=valeur_point_cartes(main[i])
                l[0]=tuple(map(operator.add, l[0] , (1,v0)))
                #print(valeur_point_cartes(main[i]))
            if main[i].couleur == 'Coeur':
                v1=valeur_point_cartes(main[i])
                l[1]=tuple(map(operator.add, l[1] , (1,v1)))
                #print(valeur_point_cartes(main[i]))
            if main[i].couleur == 'Pique':
                v2=valeur_point_cartes(main[i])
                l[2]=tuple(map(operator.add, l[2] , (1,v2)))
                #print(valeur_point_cartes(main[i]))
            if main[i].couleur == 'Trefle':
                v3=valeur_point_cartes(main[i])
                l[3]=tuple(map(operator.add, l[3] , (1,v3)))
                #print(valeur_point_cartes(main[i]))
        maxi=(0,0)
        pos=0
        for j in range(4):
            if l[j]>maxi:                       
                maxi=l[j]
                pos=j
        if maxi[1]>=27 and l[j][0]>=3:
                ann=90
        if maxi[1]>=37:
                ann=100
        if maxi[1]>=45:
                ann=110
        if maxi[1]>=55:
                ann=120
        return (ann,pos)
        
    def choisis_cartes(self,pli):
        m=0
        b=0
        l=[]
        m=[]
        self.cartes_jouables=[]
        self.cartes_jouables_noms=[]
        self.point_carte=[]
        a=pli.cartes_possibles(self)

        for i in range(len(self.main)) :
            l.append(self.main[i].nom())



        for i in range(len(a)):
            self.cartes_jouables_noms.append(a[i].nom())
            self.cartes_jouables.append(a[i])
            self.point_carte.append(pli.partie.valeur_point_carte(a[i]))

        m=max(self.point_carte)

        if len(pli.cartes_posees)==0:
            r=[]
            for i in range(len(self.cartes_jouables)):
                r.append(i)
                b=random.choice(r)

        else:                                                               #Si ce n'est pas le premier joueur, il joue sa carte la plus forte si il peut gagner le pli, sinon sa plus faible
            n=[]
            for i in range(len(pli.cartes_posees)):
                n.append(pli.partie.valeur_point_carte(pli.cartes_posees[i]))
            q=max(n)
            if m > q :
                for i in range(len(self.point_carte)):
                    if self.point_carte[i]==m:
                        b=i
            else:
                for i in range(len(self.point_carte)):
                    if self.point_carte[i]==min(self.point_carte):
                        b=i

        x=b

        for i in range(len(self.cartes_jouables)) :                                #Action du joueur
            if x==i:
                print(" Toad joue : {0} \n \n".format(self.cartes_jouables_noms[i]))
                self.joue(pli,x)


    def joue(self, pli, i):
        pli.cartes_posees.append(self.cartes_jouables[i])
        if self.cartes_jouables[i].couleur==pli.atout:               #Utile pour effectuer la montée à l'atout
            pli.cartes_atout_posees.append(self.cartes_jouables[i])
        self.main.remove(self.cartes_jouables[i])
