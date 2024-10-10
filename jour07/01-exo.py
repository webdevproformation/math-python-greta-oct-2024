# cas pratique

# créer un script python qui retourne toutes les valeurs uniques d'une liste 

# [1,2,3,5,2,1,4,3] => [4,5]
# le chiffre 5 et le chiffre 4 sont uniques

chiffres = [1,2,3,5,2,1,4,3]
# créer une liste contenir les resultats 
resultat = []
# créer une variable de type set qui contient les valeurs de chiffres SANS DOUBLON
chiffres_uniques = set(chiffres) # {1,2,3,4,5}
# parcourir la liste de chiffres sans doublon
for chiffre in chiffres_uniques:
    compteur = 0
    # parcourir la liste de chiffre Avec doublon
    for i in chiffres:
        # combien de fois j'ai le chiffre SANS doublon dans la liste AVEC doublon
        if chiffre == i:
            compteur += 1
    # si le compteur == 1 alors ajouter dans la liste resultat
    if compteur == 1:
        resultat.append(chiffre)

print(resultat)
    

# solution 2 => méthode count() des listes 

chiffres = [1,2,3,5,2,1,4,3]

print(chiffres.count(5))
resultat = []
for chiffre in chiffres :
    if chiffres.count(chiffre) == 1: 
        # compte le nombre de fois que chiffres contient la valeur chiffre 
        # if et for en même temps et le compteur 
        resultat.append(chiffre)

print(resultat)

# solution 3

liste = [1,2,3]

# créer une liste [2,4,6] 
# je prends chaque élément de la liste * 2 

resultat = []
for i in liste :
    resultat.append(i * 2)

print(resultat)

# compréhension de liste 
# []
# [ for i in liste ]
# [ i * 2 for i in liste ]
resultat = [ i * 2 for i in liste ] 
print(resultat)


prix_ht = [10,12,20]

prix_ttc = [ i * 1.2 for i in prix_ht ]

prix_ttc = []
for i in prix_ht :
    prix_ttc.append(i * 1.2)

print(prix_ttc)

