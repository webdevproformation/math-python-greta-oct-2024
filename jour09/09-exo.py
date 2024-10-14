class Personne: # bien mettre la première lettre de la class avec un P Majuscule
                # PascalCase
    nom = "Jéremy"
    _age = 30
    __competences = ["html" , "php" , "javascript"]

# créer l'objet
personne = Personne()

print(personne.nom)
print(personne._age)
print(personne._Personne__competences) # propriété privée accessible depuis l'extérieur

# si je veux créer une Personne avec la class que j'ai créée qui aurai des valeurs différentes pour les propriétés => ce n'est pas simple de les modifier