
#Ce programme permet de tester la perfomance des intelligences artificielles en comptant le nombre de victoires de chaque équipe sur 10000 matchs
#On sélectionne dans le tableau joueurs (situé juste après la classe joueur_intelligent4) quel type de joueur on veut faire jouer: random, intelligent1,2,3,4
#Puis on exécute


import operator
import random
from carte import *
from jeu_de_cartes import *
from distribution import *

compteur1=0
compteur2=0
from conversion import *

nature_joueurs = ['ordi','ordi','ordi','ordi']

def sort(l):
    l_couleur=[[] for i in range(4)]
    for i in range(len(l)):
        if l[i].couleur=="Carreau":
            l_couleur[0]+=[l[i]]
        if l[i].couleur=="Coeur":
            l_couleur[1]+=[l[i]]
        if l[i].couleur=="Pique":
            l_couleur[2]+=[l[i]]
        if l[i].couleur=="Trefle":
            l_couleur[3]+=[l[i]]
    l=l_couleur[0]+l_couleur[1]+l_couleur[2]+l_couleur[3]
    return l

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
        self.cartes_atout_posees=[]             #Utile pour la montée à l'atout



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
                    if joueur.main[i].couleur==self.atout :     #Boucle pour la montée de l'atout
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
                #print("Vous devez pisser")
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

    
class annonces:



    def __init__(self, main_joueur, jeu_de_cartes, numdealer):        #il n'est peut etre pas la peine de preciser les mains, joueurs peuvent suffire
        self.jeu_de_cartes=jeu_de_cartes
        self.main_joueur=main_joueur
        self.numdealer=numdealer
        self.arefaire = 1



    def distribution_speciale(self):
                #on distribue 3 cartes a chaquee joueur
        for i in range(4):
            for p in range(3):
                carte=self.jeu_de_cartes[0]
                self.main_joueur[(self.numdealer+i+1)%4].append(carte)
                self.jeu_de_cartes.remove(carte)
                
        l=[]
        #print("Le joueur 1 a la main suivante :".format(1))           #On fait apparaître que la main du joueur humain
        for i in range(len(self.main_joueur[0])):
            l.append(self.main_joueur[0][i].nom())
        #print(l)
        #print("\n")
        """for j in range(1,4):
            l=[]
            print("Le joueur {0} a la main suivante :".format(j+1))          #On fait apparaître que la main du joueur humain
            for i in range(len(self.main_joueur[j])):
                l.append(self.main_joueur[j][i].nom())
            print(l)"""

        #time.sleep(2)

        #on distribue 2 cartes a chaque joueur
        for i in range(4):
            for p in range(2):
                carte=self.jeu_de_cartes[0]
                self.main_joueur[(self.numdealer+i+1)%4].append(carte)
                self.jeu_de_cartes.remove(carte)
        l=[]
        #print("Le joueur 1 a désormais la main suivante :".format(self.numdealer%4+1))           #On fait apparaître que la main du joueur humain
        for i in range(len(self.main_joueur[0])):
            l.append(self.main_joueur[0][i].nom())
        #print(l)
        #print("\n")
        #time.sleep(2)

        """for j in range(4):
            l=[]
            print("Le joueur {0} a la main suivante :".format(j+1))
            for i in range(len(self.main_joueur[0])):
                l.append(self.main_joueur[0][i].nom())
            print(l)"""
        
        #on distribue 3 cartes a chaquee joueur
        for i in range(4):
            for p in range(3):
                carte=self.jeu_de_cartes[0]
                self.main_joueur[(self.numdealer+i+1)%4].append(carte)
                self.jeu_de_cartes.remove(carte)
        l=[]
        #print("Le joueur {num} a la main suivante :".format(num=self.numdealer%4+1))           #On fait apparaître que la main du joueur humain
        for i in range(len(self.main_joueur[0])):
            l.append(self.main_joueur[0][i].nom())
        for i in range(4):
            l=self.main_joueur[i]
            self.main_joueur[i]= sort(l)
        #print(self.main_joueur[0])
        #print("/n")
        #time.sleep(1)
        '''for j in range(1,4):
            l=[]
            print("Le joueur {0} a la main suivante :".format(j+1))          #On fait apparaître que la main du joueur humain
            for i in range(len(self.main_joueur[j])):
                l.append(self.main_joueur[j][i].nom())
            print(l)'''
        return self.main_joueur
        
    
    
    def atout(self,liste_joueurs):
        couleur=('Carreau','Coeur','Pique','Trefle')
        a=0
        global l_ann
        l_ann=[]

        #annonce
        passes_succ=0
        while passes_succ<4:
            for j in range(4):
                #print("Au joueur {0} de parler".format((self.numdealer+j)%4+1))
                ann1=liste_joueurs[j].choisis_annonce()
                #print(ann1)
                if (l_ann==[]or ann1[0]>l_ann[-1][0][0])and ann1[0]>0:
                    passes_succ=0
                    #print("Le joueur {0} prend".format((self.numdealer+j+1)%4))
                    #time.sleep(1)
                    
                    if ann1[1] ==0:
                        a=couleur[0]
                        #print("\nL'annonce est %d Carreau\n" %ann1[0])
                    if ann1[1]==1:
                        a=couleur[1]
                        #print("\nL'annonce est %d Coeur\n" %ann1[0])
                    if ann1[1]==2:
                        a=couleur[2]
                        #print("\nL'annonce est %d Pique\n" %ann1[0])
                    if ann1[1]==3:
                        a=couleur[3]
                        #print("\nL'annonce est %d Trefle\n" %ann1[0])
                        #time.sleep(1)
                    l_ann.append((ann1,j))
                else:
                    passes_succ+=1
                    #print("Passe")
                    #time.sleep(1)
        if a==0:
            self.arefaire = 1
        else:
            self.arefaire = 0
        return a


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
                #print(" Mario joue : {0} \n \n".format(self.cartes_jouables_noms[i]))
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
                #print(" Luigi joue : {0} \n \n".format(self.cartes_jouables_noms[i]))
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
                #print(" Daisy : {0} \n \n".format(self.cartes_jouables_noms[i]))
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
                #print(" Toad joue : {0} \n \n".format(self.cartes_jouables_noms[i]))
                self.joue(pli,x)


    def joue(self, pli, i):
        pli.cartes_posees.append(self.cartes_jouables[i])
        if self.cartes_jouables[i].couleur==pli.atout:               #Utile pour effectuer la montée à l'atout
            pli.cartes_atout_posees.append(self.cartes_jouables[i])
        self.main.remove(self.cartes_jouables[i])


    
def Coinche_IA(N):
    JOUER = 1
    global compteur1
    global compteur2
    global l_ann
    Score1,Score2 = 0,0
    while(max(Score1,Score2)<N):
        refaire_distribution = 1
        while(refaire_distribution):
            a=0
            mains=[[] for i in range (4)]
            test=distribution()
            debut=annonces(mains,test.jeu,(a-1)%4)
            jeu_distribué=mains
            jeu_d = debut.distribution_speciale()
            joueurs=[joueur_IA1(jeu_d,0),joueur_IA2(jeu_d,1),joueur_IA1(jeu_d,2),joueur_IA2(jeu_d,3)]        #Compteur pour régler l'ordre du premier joueur
            atout=debut.atout(joueurs)
            refaire_distribution = debut.arefaire
        
        p=partie(joueurs,atout)
        equipe1=0
        equipe2=0

        for j in range (0,8):

                #print("°°°°°°°°°°°°°°°°°°\n°°°°°MANCHE {0}°°°°°\n°°°°°°°°°°°°°°°°°°".format(j+1))
                test=pli(p,joueurs[a])

                for i in range(0,4):
                    b=(a+i)%4
                    k=b+1
                    #print("---------------------------- \n Joueur {0}".format(k))
                    #time.sleep(1.5)
                    joueurs[b].choisis_cartes(test)

                l=(a+test.vainqueur(p))%4+1
                m=test.points()
                #time.sleep(2)

                if l==1 or l==3:
                    equipe1 += m
                    #print(" Le joueur {0} gagne le pli \n L'équipe 1 gagne {1} points \n \n".format(l,m))
                else :
                    equipe2 += m
                    #print(" Le joueur {0} gagne le pli \n L'équipe 2 gagne {1} points \n \n".format(l,m))
                a=(a+test.vainqueur(p))%4
                #time.sleep(2)

        l=(a+test.vainqueur(p))%4+1
        if l==1 or l==3:
            equipe1 += 10
            #print(" L'équipe 1 gagne la 10 de der")
        else :
            equipe2 += 10
            #print(" L'équipe 2 gagne la 10 de der")

        #print("°°°°°°°°°°°°°°°°°°\n°°°°°Fin de la partie°°°°°\n°°°°°°°°°°°°°°°°°°")


        #time.sleep(1)
        #print("SCORE FINALE PARTIE : Equipe1 [ {0} points ]=== Equipe2  [ {1} points ]".format(equipe1,equipe2))
        if l_ann[-1][0][1]==1 or l_ann[-1][0][1]==3:
            if equipe1 > l_ann[-1][0][0]:
                #print("Et les vainqueurs sont :")
                #time.sleep(1)
                #print("...")
                #time.sleep(1)
                #print("L'Equipe 1\n")
                #time.sleep(1)
                #print("Félicitations !\n")
                Score1 += equipe1 + l_ann[-1][0][0]
                Score2 += equipe2
            else:
                #print("Et les vainqueurs sont :")
                #time.sleep(1)
                #print("...")
                #time.sleep(1)
                #print("L'Equipe 2\n")
                #time.sleep(1)
                #print("Félicitations !\n")
                Score2 += 160 + l_ann[-1][0][0]
                    
        else:
            if equipe2 > l_ann[-1][0][0]:
                '''print("Et les vainqueurs sont :")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("L'Equipe 2\n")
                time.sleep(1)
                print("Félicitations !\n")'''
                Score2 += equipe2 + l_ann[-1][0][0]
                Score1 += equipe1
            else:
                    '''print("Et les vainqueurs sont :")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    print("L'Equipe 1\n")
                    time.sleep(1)
                    print("Félicitations !\n")'''
                    Score1 += 160 + l_ann[-1][0][0]

        if Score1 > N:
            compteur1 += 1
        elif Score2 > N:
            compteur2 += 1
        else:
            JOUER=1

        #print("SCORE TOTAL : Equipe1 [ {0} points ]=== Equipe2  [ {1} points ]".format(Score1,Score2))



        #JOUER = int(input("Voulez-vous continuer à jouer ? 1/Oui 0/Non"))



for i in range(1000):
    Coinche_IA(1000)



print("Nombre de victoire pour l'équipe 1: {0}".format(compteur1))
print("Nombre de victoire pour l'équipe 2: {0}".format(compteur2))






