class Voiture :
    nom = "Peugeot 206"
    prix = 3000

    def information(self):
        print(f"j'ai acheté une {self.nom} en occasion à {self.prix} euros")

    def information2(self):
        return f"j'ai acheté une {self.nom} en occasion à {self.prix} euros"

# creation de l'objet
v = Voiture()
v.information()
print(v.information)
# méthode 
# <bound method Voiture.information of <__main__.Voiture object at 0x000001FA58796A50>>
print(v.information2())