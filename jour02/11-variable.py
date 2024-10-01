# START
# END 
# en Python => la première ligne de ton fichier c'est ton start
# la dernière ligne => END 

# commentaire monoligne 

"""
commentaire 
multiligne
avec 
saut de ligne 
"""

# 3 types de base 
# chiffres 
# int
largeur = 22
prix_voiture = 15000
prix_voiture = 15_000
prix_maison = 2_000_000

# float 
prix = 12.5

# réduction 
valeur = -60.3 

# pour la culture générale
# nombre complexe
coordonnee = 2 + 3j 

# Boolean
# attention bien respecter la Majuscule et minuscule 
a = True
b = False 
c = 10 > 3 
print(c)

# le texte => string 

d = "comment allez vous les amis ????"
e = 'je vais bien merci !'

f = """
vous pouvez
écrire du texte
avec saut de ligne
"""

print(f)

g = '''
c'est possible 
avec les apostrophes aussi !!
'''

print(g)

# type complexe 

# tableau et objet 

# en python il existe 4 types de tableau 
# list
# tuple
# set
# dictionnaire

# list
fleurs = ["rose", "jasmin" , "tulipe"]

print(fleurs[2])

# En Python pour créer un objet il faut au préalable créer une class

class Etudiant :
    nom = "Alain"
    age = 22
    competences = ["PHP", "JS"]

# attention à l'indentation 
etudiant = Etudiant()
print(etudiant.age)

"""
créer un le fichier 11-exo.py
1/ créer la variable test qui va contenir 
le résultat de la comparaison suivante : 255 <= 3
2/ créer la variable inconnu de type texte contenant le mot 'bonjour'
3/ créer la variable voiture qui est une liste vide 
4/ afficher ces trois variables dans le terminal de votre IDE

"""