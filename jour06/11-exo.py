# parcourir une liste 
# exactement comme une boucle classique

dico = {
    "a" : 1 ,
    "b" : 2
}

# parcourir les clé du dictionnaire
for i in dico :
    print(i) # "a" et "b"

# parcourir les valeurs du dictionnaire
for i in dico.values():
    print(i) # 1 et 2

# parcourir les clé et valeurs du dictionnaire

for cle, valeur in dico.items():
    print(cle, valeur)

"""
créer le fichier 02-exo.py

il contient un dictionnaire 
qui s'appelle etudiant
qui contient les valeurs suivantes 
    "q1" : 10
    "q2" : 13
    "q3" : 9
    "q4" : 15

me donner la moyenne de l'étudiant ? 

"""