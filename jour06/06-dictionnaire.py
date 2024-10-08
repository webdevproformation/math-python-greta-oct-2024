# liste 

l = [1,2]

# tuple

t = (1,2)

# set

s = {1,2}

# pour ces 3 types tableaux, pour accéder à une valeur stockée 

print(l[0]) 
print(t[0]) 
# print(s[0]) # pour info les set sont utilisés QUE pour faire des comparaisons entre des tableaux 

# crée un tableau et stocke des valeurs MAIS les valeurs sockées SANS signification

# il existe un dernier type de tableau => dictionnaire 
# dans tableau on va stocker la valeur ET clé (key)

# variable etudiant qui stocke un dictionnaire
# qui est entouré de { }
# "clé" : valeur 
etudiant = {
   "prenom" : "Alain",
   "age"  : 22,
   "is_admin" : True 
}

# pour les dictionnaires => pour récupérer une valeur 

# manière comme les tableaux précédents
print(etudiant["prenom"]) # la même syntaxe pour que les tableaux précédents

print(etudiant.get("prenom")) # méthode get()

# je veux récupérer le nom de l'étudiant (clé qui n'existe pas)
try :
    print(etudiant["nom"])
except KeyError :
    print("la clé nom n'existe pas")

# la même chose avec get()
print(etudiant.get("nom" , "la clé nom n'existe pas"))

"""
créer le fichier 07-exo.py

dans ce fichier vous avez un dictionnaire
s'appelle formation
il contient les valeurs suivantes :
    nom => DWWM
    duree = 6
    unite => mois
    matieres une liste [ Python; js PHP MySQL ]

à partir de cette variable, écrire dans la console le texte suivant 

-  je suis une formation en DWWM dans laquelle je vais suivre du PHP et du MySQL

- La formation dure 6 mois 

- il y a 4 matières principales


"""