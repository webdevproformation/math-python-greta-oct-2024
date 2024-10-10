# tableau 

en Python il y a 4 types de tableau 

## list

```py
heures = ["10h00", "11h00"]

# CRUD 

# Create (ajouter)
heures.append("12h00") # ajout à la fin
heures.insert(0,"9h00") # ajouter en position 0 (et pousser les autres)

# Read 
heures[0] 
heures[0:2] # prendre une slice (part) de le premier et le 2ème 

# Update 
heures[0] = "8h00" # changer la valeur de l'item qui se trouve en position 0

# Delete 
del heures[1] # supprimer l'item qui se trouve en position 1
heures.clear() # vide à 100% la liste 
```

## tuple

```py
prix = (10.5,12.2,14)

# SI vous avez un GROS tableau (1 000 000) de valeurs ET que vous devez faire une recherche 

prix_recherche = 20 in prix
# le temps de recherche ne dépend pas de la taille du tableau 
# create
# update
# delete
# ne sont pas possibles avec un tuple => IMMUTABLE 
# une fois créé plus possible de les modifier 

# read fonctionne COMME une liste 
prix[0]
prix[0:2]

def f(a,b):
    pass
f(1,2)
# tuple SONT présents lorsque l'on verra les Base de données 
```

## set

```py
etudiants = {"Alain", "Pierre" ,"Céline"}
php = { "Alain" , "Zorro" }
js = { "Alain" , "Céline" , "Charles" }

# parmis les étudiants lesquels font du js et php ??? 
# les deux en même temps 

etudiants.intersection(php, js)

# CRUD 

# Create
etudiants.add()
etudiants.update() # méthode update sur un set AJOUTE 

# Read => ne fonctionne PAS 

# update => ne fonctionne PAS DIRECTEMENT
# etudiants[0] = "Charles" => ça ne fonctionne PAS
# la solution remove puis un add 

# Delete 
etudiants.remove("Alain")
```

## dictionnaire


```py
vehicule = {
    "nom" : "avion",
    "prix" : 1_000_000,
    "en_service" : True
}
# au lieu d'utiliser un chiffre on va utiliser la clé pour accéder à la valeur 

# Create (ajouter une clé valeur au dictionnaire)
vehicule["nouvelle clé"] = "nouvelle valeur"
vehicule.update({"nouveau" : "valeur"})

# Read 
vehicule["prix"]
vehicule.get("inconnue", "une valeur par défaut")

# Update => modifier une valeur
vehicule["prix"] = 2_000_000
vehicule.update({"prix" : 3_000_000})

# Delete
# supprimer la clé et valeur associée
del vehicule["en_service"]
```

```py
# cas pratique

# créer un script python qui retourne toutes les valeurs uniques d'une liste 

# [1,2,3,5,2,1,4,3] => [4,5]
# le chiffre 5 et le chiffre 4 sont uniques
```