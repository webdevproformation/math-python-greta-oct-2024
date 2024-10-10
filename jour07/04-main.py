# import lib => importer TOUTES les fonctions disponibles dans le fichier lib.py

# si vous voulez importer UNIQUEMENT la fonction soustraction 
from lib import soustraction 

soustraction(1,2) # attention ne pas mettre lib.soustraction(1,2)


"""
cas pratique créer les fichier 
- fonctions.py
une fonction genererArticle 
- prend comme paramètre une string (titre)
    print("je viens d'écrire l'titre")

- data.py

créer une liste qui contient articles qui contient les valeurs suivantes
[ "article1" , "article2", "article3" ]

- 05-exo.py

import fonction et importer data

utiliser la fonction genererArticle sur toutes les valeurs da la liste 

"""