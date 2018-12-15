#Distribution de 3 cartes à chaque joueur, puis 2 cartes et enfin 3 cartes
#La fonction atout effectu le tour d'annonce et permet déterminer l'atout
#Ouvrir le fichier COINCHE.py pour jouer ou le fichier TesterlesIA.py pour voir la perfomance des IA

from joueurs import *
from carte import *
from jeu_de_cartes import *
from distribution import *
import time

nature_joueurs = ['humain','ordi','ordi','ordi']
l_ann=[]
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

class annonces:



    def __init__(self, main_joueur, jeu_de_cartes, numdealer):      
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

        time.sleep(2)

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
        time.sleep(2)

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
        print("Le joueur {num} a la main suivante :".format(num=self.numdealer%4+1))           #On fait apparaître que la main du joueur humain
        for i in range(len(self.main_joueur[0])):
            l.append(self.main_joueur[0][i].nom())
        for i in range(4):
            l=self.main_joueur[i]
            self.main_joueur[i]= sort(l)
        print(self.main_joueur[0])
        print("\n")
        time.sleep(1)
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

        #annonce
        passes_succ=0
        while passes_succ<4:
            for j in range(4):
                print("Au joueur {0} de parler".format((self.numdealer+j)%4+1))
                if nature_joueurs[j]=='humain':

                    y = int(input(("Le joueur {0} veut-il annoncer? (Tapez 0 pour non, 1 pour oui )").format((self.numdealer+j)%4+1)))
                    if y ==1:
                        passes_succ=0
                        print("Le joueur {0} annonce".format((self.numdealer+j)%4+1))
                        time.sleep(1)
                        q =int(input(("Quelle couleur souhaitez-vous pour l'atout? Tapez 0 pour Carreau, 1 pour Coeur, 2 pour Pique, 3 pour Trefle")))
                        v =int(input(("Combien souhaitez-vous annoncer? Tapez une dizaine entre 80 et 160")))
                        l_ann.append(((v,q),j))
                        if q ==0:
                            a=couleur[0]
                            print("\nLe joueur {num} annonce {d} à Carreau\n" .format(num=(self.numdealer+j+1)%4,d=v))
                        if q==1:
                            a=couleur[1]
                            print("\nLe joueur {num} annonce {d} à Coeur\n".format(num=(self.numdealer+j+1)%4,d=v))
                        if q==2:
                            a=couleur[2]
                            print("\nLe joueur {num} annonce {d} à Pique\n".format(num=(self.numdealer+j+1)%4,d=v))
                        if q==3:
                            a=couleur[3]
                            print("\nLe joueur {num} annonce {d} à Trefle\n".format(num=(self.numdealer+j+1)%4,d=v))
                            time.sleep(1)
                    else:
                        passes_succ+=1
                        print("Passe")
                        time.sleep(1)
                else:
                    ann1=liste_joueurs[j].choisis_annonce()
                    #print(ann1)
                    if (l_ann==[]or ann1[0]>l_ann[-1][0][0])and ann1[0]>0:
                        passes_succ=0
                        print("Le joueur {0} prend".format((self.numdealer+j+1)%4))
                        time.sleep(1)
                        
                        if ann1[1] ==0:
                            a=couleur[0]
                            print("\nL'annonce est %d Carreau\n" %ann1[0])
                        if ann1[1]==1:
                            a=couleur[1]
                            print("\nL'annonce est %d Coeur\n" %ann1[0])
                        if ann1[1]==2:
                            a=couleur[2]
                            print("\nL'annonce est %d Pique\n" %ann1[0])
                        if ann1[1]==3:
                            a=couleur[3]
                            print("\nL'annonce est %d Trefle\n" %ann1[0])
                            time.sleep(1)
                        l_ann.append((ann1,j))
                    else:
                        passes_succ+=1
                        print("Passe")
                        time.sleep(1)
        if a==0:
            print("Personne ne prend, on redistribue les cartes")
        else:
            self.arefaire = 0
        return a
