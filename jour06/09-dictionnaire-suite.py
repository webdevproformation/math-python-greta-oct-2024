# dictionaire

voiture = {
    "id" : 1,
    "modele" : 206,
    "marque" : "Peugeot"
}

# CRUD
# ajouter une nouvelle clé / valeur à mon dictionnaire 

# ajouter une clé valeur comme un tableau 
voiture["prix"] = 20_000
print(voiture)
# permet d'ajouter un ou plusieurs clé valeur à un dictionnaire existant
voiture.update({"proprietaire" : "Alain" , "adresse" : "20 rue de Paris"})

print(voiture)

# Read 

print(voiture["id"])
print(voiture.get("id", "valeur par défaut"))

# Update

voiture["modele"] = 208
print(voiture)

voiture.update({"proprietaire" : "Zorro"})
print(voiture)

# Delete 
# supprimer une clé / valeur existant

del voiture["marque"] 
print(voiture)

voiture.pop("id") # supprimer la clé id et sa valeur existante
print(voiture)

"""

créer le fichier 10-exo.py

dans de fichier vous avez un dictionnaire :
- qcm
- contient les valeurs suivantes
    question1 contient un dictionnaire 
        question : "comment écrire une variable"
        reponses : liste [A, B, C, D]
        solution : [A,D]
    question2 contient un dictionnaire 
        question : "comment écrire une fonction"
        reponses : liste [A, B, C, D]
        solution : [A,B]


écrire dans la console le texte suivant 
pour la question1 les bonnes réponses sont A et D

changer la valeur de la question 2 : remplacer "comment écrire une fonction" par "comment écrire une fonction avec des arguments ???"
        

"""