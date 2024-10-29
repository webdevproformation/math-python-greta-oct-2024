"""
Livre
    titre, auteur, année_publication

    def __init__(self , titre, auteur, année_publication)


LivreEmpruntable(Livre)
    emprunteur, date_emprunt

    def __init__(self , titre, auteur, année_publication, emprunteur, date_emprunt)
        # initiation emprunteur, date_emprunt
        # ET initialiser les propriétés titre, auteur, année_publication VIA le constructeur de la class parent / class supérieure

"""

class Livre :
    def __init__(self, p_titre, p_auteur, p_annee_publication) :
        self.titre = p_titre
        self.auteur = p_auteur
        self.annee_publication = p_annee_publication
    
    def afficher_info(self):
        print(f"{self.p_titre} {self.auteur} publié le {self.annee_publication}")

class LivreEmpruntable(Livre):
    def __init__(self,p_titre, p_auteur, p_annee_publication ):
        # super().__init__(p_titre, p_auteur, p_annee_publication)
        Livre.__init__( self ,p_titre, p_auteur, p_annee_publication)

    def emprunter(self , nom , date):
        self.emprunteur = nom
        self.date_emprunt = date

    def retourner(self):
        self.emprunteur = None
        self.date_emprunt = None

livre = LivreEmpruntable("20000 lieux sous les mers", "Jules Vernes" ,1870)
print(vars(livre))
livre.emprunter("moi", "01/01/2024")
print(vars(livre))
livre.retourner()
print(vars(livre))


## créer le fichier 02-exo.py
## class Personnage 
# 3 propriétés :  
# nom  
# pv 
# is_vivant ( par défaut => True) 
# créer une méthode qui permet d'afficher toutes les informations du personnage
# créer une méthode qui va tuer le personnage  is_vivant => False

# class Magicien qui est une class enfant de Personnage 
# mana par défaut = 100
# méthode lancer_un_sort qui consomme 20 de mana à chaque lancer de sort

# créer un objet m qui va initialiser le magicien
# lancer deux sorts
# vérifier que le mana du magicien est désormais de 60 
