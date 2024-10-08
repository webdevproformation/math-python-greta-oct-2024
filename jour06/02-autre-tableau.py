# les autres tableaux 
# Liste => utilise le plus
# tuple
# set

# dictionnaire 

# liste
etudiants = ["Alain", "Benjamin"]

# tuple
etudiants = ("Alain", "Benjamin")
# au lieu d'utiliser des [] utiliser des ()

# permet d'effectuer des recherches dans ce type de tableau 
# la recherche va durer autant de temps quelquesoit son nomnbre de valeur 
# 
# pour les listes plus il y a de valeurs et plus la recherche est lente 

## ------------------

import time # time => permet de mettre en place un minuteur 

# test d'appartenance sur une séquence de 100 éléments
tic = time.perf_counter() # lance le chronomètre 
"x" in range(0,1_000) # recherche "x" dans une liste de 0 - 99
tac = time.perf_counter() # stop de chronometre 
print(f"duree exécution {tac - tic:0.4f} seconds") # 0.0000
