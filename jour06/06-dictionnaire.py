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