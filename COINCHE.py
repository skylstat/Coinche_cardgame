

#Ce programme permet de lancer le jeu de coinche pour un humain contre des intelligences artificielles
#Il suffit juste de suivre les instructions de la console pour jouer
#Pour modifier le niveau de l'ordinateur, il faut aller modifier le tableau des joueurs qui se situe dans le fichier partie_pli.py
#Par défaut on a mis joueurs=[joueur_humain(0),joueur_IA1(1),joueur_IA1(2),joueur_IA1(3)]



import random
import time                 #pour le design du jeu, marquer un temps d'arrêt le rend plus réaliste et surtout plus facile à lire pour le joueur humain
from carte import *
from jeu_de_cartes import *
from distribution import *
from annonces import *
from joueurs import *
from partie_pli import *
from conversion import *

"""DEROULEMENT PARTI AVEC UN HUMAIN ET 3 ORDIS QUI JOUENT ALEATOIREMENT EN RESPECTANT LES REGLES"""


def Coinche(N):
    global l_ann
    JOUER = 1
    Score1,Score2 = 0,0
    while(JOUER or max(Score1,Score2)<N):
        refaire_distribution = 1
        while(refaire_distribution):
            a=0
            mains=[[] for i in range (4)]
            test=distribution()
            debut=annonces(mains,test.jeu,(a-1)%4)
            jeu_distribué=mains
            jeu_d = debut.distribution_speciale()
            joueurs=[joueur_humain(jeu_d,0),joueur_IA1(jeu_d,1),joueur_IA1(jeu_d,2),joueur_IA1(jeu_d,3)]        #Compteur pour régler l'ordre du premier joueur
            atout=debut.atout(joueurs)
            refaire_distribution = debut.arefaire
            
        p=partie(joueurs,atout)
        equipe1=0
        equipe2=0

        for j in range (0,8):

                print("°°°°°°°°°°°°°°°°°°\n°°°°°MANCHE {0}°°°°°\n°°°°°°°°°°°°°°°°°°".format(j+1))
                test=pli(p,joueurs[a])

                for i in range(0,4):
                    b=(a+i)%4
                    k=b+1
                    print("---------------------------- \n Joueur {0}".format(k))
                    time.sleep(1.5)
                    joueurs[b].choisis_cartes(test)

                l=(a+test.vainqueur(p))%4+1
                m=test.points()
                time.sleep(2)

                if l==1 or l==3:
                    equipe1 += m
                    print(" Le joueur {0} gagne le pli \n L'équipe 1 gagne {1} points \n \n".format(l,m))
                else :
                    equipe2 += m
                    print(" Le joueur {0} gagne le pli \n L'équipe 2 gagne {1} points \n \n".format(l,m))
                a=(a+test.vainqueur(p))%4
                time.sleep(2)

        l=(a+test.vainqueur(p))%4+1
        if l==1 or l==3:
            equipe1 += 10
            print(" L'équipe 1 gagne la 10 de der")
        else :
            equipe2 += 10
            print(" L'équipe 2 gagne la 10 de der")

        print("°°°°°°°°°°°°°°°°°°\n°°°°°Fin de la partie°°°°°\n°°°°°°°°°°°°°°°°°°")



        if l_ann[-1][0][1]==1 or l_ann[-1][0][1]==3:
            if equipe1 > l_ann[-1][0][0]:
                print("Et les vainqueurs sont :")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("L'Equipe 1\n")
                time.sleep(1)
                print("Félicitations !\n")
                Score1 += equipe1 + l_ann[-1][0][0]
                Score2 += equipe2
            else:
                print("Et les vainqueurs sont :")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("L'Equipe 2\n")
                time.sleep(1)
                print("Félicitations !\n")
                Score2 += 160 + l_ann[-1][0][0]
                
        else:
            if equipe2 > l_ann[-1][0][0]:
                print("Et les vainqueurs sont :")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("L'Equipe 2\n")
                time.sleep(1)
                print("Félicitations !\n")
                Score2 += equipe2 + l_ann[-1][0][0]
                Score1 += equipe1
            else:
                print("Et les vainqueurs sont :")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("L'Equipe 1\n")
                time.sleep(1)
                print("Félicitations !\n")
                Score1 += 160 + l_ann[-1][0][0]


        time.sleep(1)
        print("SCORE FINALE PARTIE : Equipe1 [ {0} points ]=== Equipe2  [ {1} points ]".format(equipe1,equipe2))

        print("SCORE TOTAL : Equipe1 [ {0} points ]=== Equipe2  [ {1} points ]".format(Score1,Score2))



        JOUER = int(input("Voulez-vous continuer à jouer ? 1/Oui 0/Non"))
