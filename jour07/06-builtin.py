# from builtins import range, len, str , sorted
# importé automatiquement 
# Python va ajouter l'import AUTOMATIQUEMENT 
# ce qui permet de les utiliser dans n'importe quel fichier 

# builtins => module NATIF et autoimporté 

# Python est livré avec d'autres modules Natif MAIS qu'il faudra importer nous même

""" import math
https://docs.python.org/3/py-modindex.html
 """
from random import random , randint
import pprint # pretty print 

# 0 et 1
# 0.25....
# 0.75

print(int(random() * 100))
print(randint(0,100))

fleurs = ["rose", "fleur 2", "fleur 3", "fleur 4"]

index_aleatoire = randint(0,len(fleurs)-1)
print(fleurs[index_aleatoire])


fleurs = [{ "nom" : "Rose" , "prix" : 200, "tva" : 1.2 }, "fleur 2", "fleur 3", "fleur 4"]

pprint.pp(fleurs, indent = 2 ,compact= False , width=20) 


""" range(1,2)

len([])

str()

set()

sorted()  """