class Personnage:
    def __init__(self, p_nom , p_pv):
        self.nom = p_nom
        self.pv = p_pv
        self.is_vivant = True # par défaut un Personnage est vivant

    def presentation(self):
        if(self.is_vivant):
            print(f"{self.nom} a {self.pv} points de vie")
        else:
            print(f"{self.nom} n'est plus vivant")

    def kill(self):
        self.is_vivant = False 

class Magicien(Personnage):
    def __init__(self, p_nom , p_pv):
        super().__init__(p_nom , p_pv)
        # Personnage.__init__(self , p_nom , p_pv)
        self.mana = 100 

    def lancer_sort(self):
        self.mana -= 20

m = Magicien("Merlin" , 200)
m.lancer_sort()
m.lancer_sort()
print(m.mana) # afficher la quantité de mana du magicien => # 60