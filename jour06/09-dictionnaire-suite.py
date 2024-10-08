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

