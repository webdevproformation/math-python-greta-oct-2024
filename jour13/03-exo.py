class Voiture :
    nom = "Peugeot 206"
    prix = 3000

    def information(self):
        print(f"j'ai acheté une {self.nom} en occasion à {self.prix} euros")

# creation de l'objet
v = Voiture()
v.information()