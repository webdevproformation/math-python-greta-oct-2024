# ajouter la lettre x après la valeur b dans une liste
# et pousser les autres données d'un cran
# sans utiliser les méthodes append() et insert() des listes

anniversaires = ["a" , "b" , "c" , "d"]

position = 0 

# recharcher la lettre b dans la list anniversaire
for i in range(0, len(anniversaires)) :
    if anniversaires[i] == "b" :
        position = i 
        break

print(position)

# créer une liste vide ayant une size de anniversaire + 1
resultat = [None] * (len(anniversaires) + 1)

# remplir jusqu'à position le resultat
for i in range(0, position + 1) :
    resultat[i] = anniversaires[i]

resultat[position + 1]= "x"

for i in range(position + 2, len(anniversaires) + 1) :
    resultat[i] = anniversaires[i -1]

print(resultat)