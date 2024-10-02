# opération chiffre 
# opéation sur les string 
# opération sur les boolean (tableau des vérités)

a = 10 > 2
print(a) # True

b = 10 < 3
print(b) # False

# opérateur de comparaison entre les deux valeurs 

# > strictement supérieur
# < strictement inférieur
# >= supérieur ou égal
# <= inférieur ou égal
# != différent
# == égal

# attention l'opérateur de comparaison === n'existe pas en Python
# attention l'opérateur de comparaison !== n'existe pas en Python

# il est possible d'avoir des comparaisons séparés par ET OU opérateur boolean

# SI 10 > 2 OU 2 < 10

c = 10 > 3 and 10 < 11
#    True  and  True
#         True
print(c)
# && n'existe pas en Python
# AND n'existe pas en Python

d = 25 > 2 or 25 > 30
#    True or  False
#      True
print(d)

# dernier opérateur à connaitre pour les calcul boolean

e = not 23 > 2 
#   not  True  => False
#     False
print(e)
f = not 23 < 2
#   not False => True
print(f)

"""
créer le fichier 07-exo.py
dans ce fichier vous allez créer des variables qui vont stocker les opérations boolean suivantes
2 >= 2
 "a" == "ab"
 2 != 3 and 10 < 33
 "hello" > "bonjour" 
 2 ==  "2"
 "2" == "2"
 (2 != 5 and 3 > 4 ) or 2 <= 14 
 2 != 5 and ( 3 > 4  or 2 <= 14 ) 
 2 != 5 and 3 > 4  or 2 <= 14  

 pour chacune dire si c'est True ou False => expliquer pourquoi ??
"""
