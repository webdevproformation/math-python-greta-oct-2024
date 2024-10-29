class Personnage : 
    def __init__(self, p_nom , p_pv):
        self.nom = p_nom
        self.pv = p_pv

    def perdre_pv(self , personnage , force):
        # faire perdre de la vie à l'autre personnage 
        personnage.pv -= force

class Magicien(Personnage):
    # lorsque la magicien lance un sort => fait perdre 50 pv à l'autre personnage
    def lancer_sort(self , personnage):
        self.perdre_pv(personnage , 50)

class Guerrier(Personnage):
    def frapper(self , personnage):
        self.perdre_pv(personnage , 20) # Polymorphisme 

m = Magicien("Merlin", 80)
g = Guerrier("Attila", 120)
m.lancer_sort(g)
m.lancer_sort(g)
print(vars(g))
g.frapper(m)
g.frapper(m)
g.frapper(m)
g.frapper(m)
print(vars(m)) # Game Over car les PV du magicien = 0 

"""
créer le fichier 14-exo.py
Exercice : Gestion d’une Bibliothèque
Créez un programme pour gérer une bibliothèque avec les classes suivantes :

Classe Livre :
Attributs : titre, auteur, année_publication
Méthode : afficher_info() qui affiche les informations du livre
Classe LivreEmpruntable (hérite de Livre) :
Attributs supplémentaires : emprunteur, date_emprunt
Méthode : emprunter(l’emprunteur, la date) qui met à jour les informations d’emprunt
Méthode : retourner() qui réinitialise les informations d’emprunt
"""