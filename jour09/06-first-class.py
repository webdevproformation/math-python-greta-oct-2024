"""
vehicule = {
    "nom" : "Peugeot 206",
    "prix" : 10_000,
    "en_circulation" : False
}

def mise_en_circulation(v):
    v["en_circulation"] = True

def prixTTC(v):
    print(v["prix"]* 1.2)
# 1 seule variable qui contient à la fois les 3 valeurs (propriété)
    ET les deux fonctions (méthode)
"""

class Vehicule:
    # la class Vehicule contient 3 propriétés
    nom = "Peugeot 206"
    prix = 10_000
    en_circulation = False

    def mise_en_circulation(self): 
        # méthode => fonction qui est dans une class
        # la méthode on OBLIGATOIREMENT comme premier paramètre la variable self 
        # self permet d'accéder au propriété de la class 
        # accède à la propriété en_circulation et modifie sa valeur à True
        self.en_circulation = True

    def prixTTC(self):
        #self.prix = self.prix * 1.2
        self.prix *= 1.2

# à partir de la class je crée un objet 
vehicule = Vehicule() # appel la class (j'exécute la class )

vehicule.nom 
vehicule.prix
vehicule.en_circulation
vehicule.prixTTC()
vehicule.mise_en_circulation()

# cas pratique
# créer le fichier 07-exo.py

# dans ce fichier vous allez créer une class qui s'appelle Etudiant
# cette class contient 2 propriétés 
# nom => "Alain"
# age => 32
# ajouter dans cette class 1 méthode qui s'appelle saluation
# cette méthode contient 1 traitement print("bonjour")

# une fois la class créé, créer un objet et exécuter la méthode salutation
# afficher aussi dans la console le nom et l'age de l'étudiant