fleurs = ["rose" , "lilas" , "muguet" , "jasmin" , "tulipe" ]

print(fleurs[0])

# 4 afficher dans la console les 4 derniers éléments de la variable fleurs
print(fleurs[1:5])
print(fleurs[-4:])

# supprimer muguet
fleurs.remove("muguet")
print(fleurs)

# 6 ajouter après rose la valeur "fleur rouge"
fleurs.insert(1,"fleur rouge")
print(fleurs)

# 7 compteur le nombre de fleurs
print(len(fleurs)) # 5

# 8 modifier tulipe par "fleur rose"
# tulipe est à la position 4
fleurs[4] = "fleur rose"
print(fleurs)

# afficher la valeur du milieu
print(fleurs[2])

# quelle est la valeur du milieu (bonus)
nb_element_tableau = len(fleurs)
milieu = round(nb_element_tableau/2)
print(milieu)
print(fleurs[milieu])