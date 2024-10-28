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

nom = "Merlin"
pv = 100
faction = "marge"

def presentation(nom, pv, faction):
    print(f"je m'appelle {nom} je suis {faction} et j'ai {pv} points de vie")

presentation(nom, pv, faction)