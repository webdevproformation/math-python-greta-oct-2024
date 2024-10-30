"""
mplémentez la fonction diff_max_min, qui prend une liste d'entiers positifs en entrée, et retourne la différence entre le plus grand entier de la liste et le plus petit.

Votre fonction sera testée sur plusieurs listes de test différentes, et chaque liste sera composée de 2 à 100 entiers positifs.

Par exemple : diff_max_min([1, 1, 5, 4]) devrait retourner 4 (5-1)
"""

def diff_max_min(liste) :
    minimun = min(liste)
    maximun = max(liste)
    return maximun - minimun


diff_max_min([1, 1, 5, 4])

"""
Quel est le but des décorateurs de mise en cache comme functools.lru_cache ou functools.cache ?
https://docs.python.org/3/library/functools.html


Optimiser le nettoyage de mémoire (garbage collector).

Cacher aux utilisateurs des données sensibles à l'intérieur des fonctions en utilisant des "datacaches".

Diminuer l'utilisation de la RAM en utilisant la mémoire cache.

xxxxxxxx Accélérer la vitesse d'exécution en stockant les résultats des fonctions déjà calculées.

"""

from functools import cache

@cache
def factorial(n):
    return n * factorial(n-1) if n else 1

factorial(10)      # no previously cached result, makes 11 recursive calls
factorial(5)       # just looks up cached value result
factorial(12)      # makes two new recursive calls, the other 10 are cached
479001600


"""
Les affirmations suivantes concernent la classe Counter du module collections. Laquelle d'entre elles n'est PAS vraie ?

https://apprendrepython.com/compter-les-elements-dune-liste-avec-collections-counter-en-python/

Les instances de Counter sont mutables, ce qui signifie que vous pouvez modifier le compte après avoir créé une instance de Counter.

Non seulement vous pouvez faire un Counter d'une liste, mais aussi de tuples et de chaînes de caractères.

Counter peut être utilisé pour compter combien de fois les éléments d'une liste apparaissent.

Counter ne supporte pas les opérations arithmétiques. Vous ne pouvez pas additionner deux Counter par exemple.

"""

from collections import Counter

text = "bonjour"

t = Counter(text)
print(t)
print(t.most_common())

liste = [1,2,3,4,3]
t = Counter(liste)


liste2 = [1,2,3,4,3,3]
t2 = Counter(liste2)

t3 = t + t2 

print(t, t2 , t3)

print(t)
print(t.most_common())
print(t.most_common()[0])

tuple = (1,2,3,4,3)
t = Counter(tuple)
print(t)
print(t.most_common())

set = {1,2,3,4,3}
t = Counter(set)
print(t)
print(t.most_common())


dictionnaire = {
    "a" : 1,
    "b" : 1,
    "c" : 2
}

t = Counter(dictionnaire)
print(t)


# --------------

text = "bonjour"
print(text[::1])


"""
La variable __all__ est souvent vue dans les fichiers __init__.py. Laquelle des affirmations suivantes est vraie ? Par convention, elle devrait être :


https://www.geeksforgeeks.org/what-is-__init__-py-file-in-python/
"""