#On définit une classe carte pour faciliter la manipulation des cartes

#Ouvrir le fichier COINCHE.py pour jouer ou le fichier TesterlesIA.py pour voir la perfomance des IA


class carte:        #carte.couleur, carte.valeur, carte.nom()
    """On crée pour chaque carte une classe avec pour attribut sa valeur et son motif"""
    couleur=('Carreau','Coeur','Pique','Trefle')    #COULEUR donne le motif de la carte
    valeur=('7','8','9','10','Valet','Dame','Roi','As')   #VALEUR donne la valeur de la carte
    def __init__(self, couleur, valeur):
        self.couleur = couleur
        self.valeur = valeur
    def nom(self):                                  #nom permet d'afficher la carte
        return self.valeur + " de " + self.couleur
    def __repr__(self):
        return "(%s,%s)"%(self.valeur,self.couleur)
