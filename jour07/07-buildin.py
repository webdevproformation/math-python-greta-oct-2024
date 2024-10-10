# les lignes d'entête du fichier va 
# contenir toutes les imports

import random

chiffre_aleatoire = random.randint(0, 1000)

print(chiffre_aleatoire)

#--------

import time

start = time.time()
## verif =  "i" in range(0, 100_000_000)
end = time.time() 
duree = f"duree = {end - start} secondes"
print(duree)

#--------
import builtins
import pprint 

pprint.pp(builtins.__dict__)

#--------

import importlib

lib = importlib.import_module("06-builtin")

pprint.pp(lib.__dict__)

#--------

import datetime

print(datetime.datetime.now()) 
# 2024-10-10 16:35:25.651798

maintenant = datetime.datetime.now()

# afficher la date au format français
## JJ/MM/AAAA
## MM/JJ/AAAA

# https://www.w3schools.com/python/python_datetime.asp
maintenant_fr = maintenant.strftime("%d/%m/%Y")
print(maintenant_fr)

#--------

# csv / json / xml => permet à Python de travailler et communiquer avec des fichiers de type tableur 