# les conditions en PSEUDO CODE 
# SI 

# en Python => SI => se traduit par if (en minuscule !!!)

if 10 > 2 :
    # True
    # alors on exécute les instructions dans le block indenté sous le if 
    print("la condition est respectée")

if 10 < 2 :
    # False 
    print("la condition est respectée peut être ????")


# SI ET aussi SINON

age = 10

# verifier que l'age de la personne si < 18 => affiche le texte vous êtes mineur
# sinon affiche le texte vous êtes adulte

if age < 18 :
    print("vous êtes mineur")
else :
    print("vous êtes adulte")

# verifier que l'age de la personne si < 18 => affiche le texte vous êtes mineur
# verifier que l'age de la personne si entre 18 et 80 => affiche le texte vous êtes adulte
# verifier que l'age de la personne si entre 81 et 120 => affiche le texte vous êtes retraité
# sinon affiche le texte age impossible 


age = 200

if age < 18 :
    print("vous êtes mineur")
elif age < 80  :
    print("vous êtes adulte")
elif age < 120 :
    print ("vous êtes retraité")
else:
    print("age impossible")

# attention à l'ordre des if elif 
# dès qu'une condition est True => toutes les suivants sont ignorés
# si toutes les conditions sont False => else 

"""
# créer le fichier 10-exo.py
# ce fichier contient trois variables
# a = 30
# b = 40
# c = 12 * 4 < 44/3
# 1/ vérifier est ce que a supérieur ou égal à b
# si c'est vrai écrire dans la console "verif 1 ok"

# 2/ vérifier est ce que c supérieur ou égal à b
# si c'est vrai écrire dans la console "verif 2 ok"

# 3/vérifier est ce que c supérieur ou égal à b OU a inférieur à b
# si c'est vrai écrire dans la console "verif 3 ok"
"""