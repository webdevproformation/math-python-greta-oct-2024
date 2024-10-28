class Personnage :
    def __init__(self, p_nom, p_pv, p_faction):
        self.nom = p_nom
        self.pv = p_pv
        self.faction = p_faction
    
    def presentation(self):
        print(f"je m'appelle {self.nom} je suis {self.faction} et j'ai {self.pv} points de vie")

magicien = Personnage("Merlin", 100, "mage" )
magicien.presentation()

guerrier = Personnage("Attila", 1000, "général")
guerrier.presentation()

nom_1 = "Merlin"
pv_1 = 100
faction_1 = "marge"

nom_2 = "Attila"
pv_2 = 1000
faction_2 = "Général"

def presentation(nom, pv, faction):
    print(f"je m'appelle {nom} je suis {faction} et j'ai {pv} points de vie")

presentation(nom_1, pv_1, faction_1)
presentation(nom_2, pv_2, faction_2)

# https://formation.webdevpro.net/python-poo/
# login : python
# password : poo