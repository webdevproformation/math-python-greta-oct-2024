class Etudiant:
    nom = "Alain"
    age = 32

    def saluation(self):
        print("bonjour")

# je transforme ma class en objet

etudiant = Etudiant()

# utiliser la méthode saluation
etudiant.saluation()
# afficher les propriétés de l'objet 
print(etudiant.nom)
print(etudiant.age)