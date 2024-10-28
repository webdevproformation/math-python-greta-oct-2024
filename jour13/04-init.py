# j'ai besoin dans mon programme de pouvoir créer 
# vehicules qui ont de nom / prix différent les uns des autres

""" class Voiture :
    nom = 206
    prix = 2000 """

class Voiture :
    # ajouter dans cette class une fonction magique
    # sens particulier pour Python 
    # elle va réaliser / excuter de manière SPECIAL 
    def __init__(self, p_nom, p_prix):
        self.nom = p_nom
        self.prix = p_prix

    def info(self):
        print(f"j'ai acheté une {self.nom} en occasion à {self.prix} euros")


# si j'ai besoin de créer un véhicule 
voiture1 = Voiture("BMW", 5000) 
voiture1.info()

voiture2 = Voiture("206" , 4000)
voiture2.info()
# lorsque je crée un objet depuis une class 
# la méthode __init__ est AUTOMATIQUEMENT exécuter lorsque l'on crée l'objet
# la méthode __init__ contient 3 paramètres et lors de la création de l'objet 
# dans le nom de la class il ne FAUT METTRE QUE 2 paramètres
# nom de cette méthode magique => constructeur

# créer le fichier 05-exo.py
# dans ce fichier vous avez une class Personnage
# contient 3 propriétés 
# nom
# pv
# faction
# initialiser ces 3 propriétés dans un constructeur
# créer enfin une méthode qui réaliser une concaténation => presentation
# "je m'appelle {nom} je suis {faction} et j'ai {pv} points de vie"

# créer un objet qui s'appelle magicien 
# nom => Merlin
# pv 100
# faction => mage

# créer un objet qui s'appelle guerrier
# nom Attila
# pv 1000
# faction => général 

# exécuter la méthode presentation pour le guerrier et le magicien