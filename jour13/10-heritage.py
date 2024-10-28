class Magicien :
    nom = "m1"
    pv = 10
    def frapper(self):
        print("magicien frappe")

class Guerrier :
    nom = "g1"
    pv = 20
    def frapper(self):
        print("guerrier frappe")

# si on a plusieurs class qui ont les mêmes propriétés 
# les même mathodes 
# créer une class parent (Personnage)
# class Guerrier et Magicien qui vont copier le contenu de la class Parent => héritage 