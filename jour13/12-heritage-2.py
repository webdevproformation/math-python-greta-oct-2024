class Personnage : 
    def __init__(self, p_nom , p_pv):
        self.nom = p_nom
        self.pv = p_pv

    def frapper(self):
        print(f"le personnage {self.nom} vient de frapper")

class Magicien(Personnage):
    pass

class Guerrier(Personnage):
    pass 

m = Magicien("Merlin", 100) # exécuter le __init__ de Personnage
m.frapper()
g = Guerrier("Attila", 1000)
g.frapper()