"""
Implémentez la fonction diff_max_min, qui prend une liste d'entiers positifs en entrée, et retourne la différence entre le plus grand entier de la liste et le plus petit.

Votre fonction sera testée sur plusieurs listes de test différentes, et chaque liste sera composée de 2 à 100 entiers positifs.

Par exemple : diff_max_min([1, 1, 5, 4]) devrait retourner 4 (5-1)
"""

liste = [1, 1, -1, 4] ; 

# minimun avec la fonction builtins  
minimun = min(liste)
print(minimun)

minimun = liste[0] 
for i in liste: 
    if i < minimun :
        minimun = i

print(minimun)


# max
maximum = max(liste)
print(maximum)

maximum = liste[0]
for i in liste:
    if i > maximum :
        maximum = i

print(maximum)

## solution 1
def diff_max_min(liste) :
    minimun = min(liste)
    maximum = max(liste)
    return maximum - minimun

## solution 2
def diff_max_min(liste) :
    minimun = liste[0] 
    for i in liste: 
        if i < minimun :
            minimun = i
    maximum = liste[0]
    for i in liste:
        if i > maximum :
            maximum = i
    return maximum - minimun

## solution 3
def diff_max_min(liste) :
    sorted_liste = sorted(liste)
    minimun = sorted_liste[0]
    maximum = sorted_liste[len(sorted_liste)-1]
    return maximum - minimun

print(diff_max_min([1, 1, 0, 40]) )