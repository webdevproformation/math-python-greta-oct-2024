class Personnage : # class Mère / class Parent
    nom = "perso"
    pv = 200

    def frapper(self):
        print("perso frappe")
# Guerrier est une class Enfant 
# en PHP / Java
# class Guerrier extends Personnage {}
# tout le code écrit dans Personnage est copié dans la class Guerrier
class Guerrier(Personnage):
    pass 

g1 = Guerrier()
print(g1.nom)
print(g1.pv)
g1.frapper()