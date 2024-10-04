# variable de base / simple 
# variable qui contient 1 valeur 

mot = "abeille"
position = 0
isVoyelle = True

# variable complexe
# une variable contient PLUSIEURS VALEURS 
# tableau 

panier1 = "pomme"
panier2 = "poire"
panier3 = "abricot"

# une seule variable qui contient toutes ces string
panier = [ "pomme" , "poire" , "abricot" ]

print(panier[0])

# panier est une liste (un type de tableau, il en existe 4 en tout dans Python)

# opérateur in  => opérateur d'appartenance 

# est ce que j'ai "poire" dans la list panier

poire_dans_panier = "poire" in panier 
print(poire_dans_panier) # True

banane_dans_panier = "banane" in panier 
print(banane_dans_panier) # False 

# CRUD 

# Create => est il possible d'ajouter une nouvelle string dans ma liste
# Read => récupérer un ou plusieurs valeurs stockées dans ma liste
# Update => modifier une valeur existante dans la liste 
# Delete  => supprimer une valeur dans ma liste 
 
# Create

fleurs = ["rose", "jasmin" ]

# ajouter dans la liste fleurs la valeur "tulipe"

fleurs.append("tulipe") # ajouter à la fin 
print(fleurs)

# ["rose", "jasmin" , "tulipe" ]

# ajouter "lilas" entre "rose" et "jasmin" (et les valeurs après lilas vont être poussées automatiquement)
fleurs.insert(2, "lilas")
print(fleurs)

# bonjour => ["b","o", "n", "j", "o" , "u", "r"]

# read

jours = ["lundi", "mardi", "mercredi"]
#           0        1         2
#           -3       -2        -1 
print(jours[0])

nb_valeur_liste = len(jours) # 3
print(jours[nb_valeur_liste - 1])

print(jours[-1])

# prendre une "slice" / partie d'une liste 

villes = ["Lyon", "Paris" , "Lille" , "Marseille" , "Grenoble"]

print(villes[1:3])
# [Paris" , "Lille"]


print(villes[2:5])
print(villes[2:]) # si le deuxieme chiffre est omis => automatiquement python va écrire len(ville) ici 5
# ["Lille" , "Marseille" , "Grenoble"]

print(villes[0:2])
print(villes[:2])
# ["Lyon", "Paris"]
""" import pprint 

pprint.pp(jours) """

"""
créer le fichier 04-exo.py

ce fichier contient une liste exos qui est vide 

1 ajouter les valeurs suivantes : "PHP", "JS" et "CSS"
2 ajouter après la valeur "PHP" le texte "Git"
3 récupérer les deux premières valeurs de la liste
4 récupérer les trois dernières valeurs de la liste
5 déterminer si la valeur "Symfony" est présente dans la liste ?
6 récupérer l'avant dernière valeur de la liste 

"""