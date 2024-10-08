# Rappel 

## condition 

```py
if condition :
    # traitement 

if condition1 :
    # traitement
elif condition2 :
    # traitement
elif condition3 :
    # traitement
else :
    # traitement final
```


### condition ternaire (if ternaire)

- au lieu d'avoir à faire des sauts de ligne, on va faire un if else en UNE SEULE LIGNE 

```py
if condition :
    # traitement 1
else :
    # traitement 2

# traitement 1 if condition else # traitement 2
```


## boucle 

```py
min = 0
maxNonInclu = 100
pas = 1
for i in range(min, maxNonInclu, pas) :
    # traitement

i = 0
while i < 100 :
    # traitement
    i += 1
```

## fonction builtin 

- les fonctions built in (fonction tombe du ciel)
- mot clé du langage Python 

```py
# exemple 1 print()
a = 12
print(a) # 

# exemple 2 len()

texte = "bonjour"
len(texte) # compter le nombre de lettres dans la variable texte (string)
           # 7

fleurs = ["rose", "jasmin", "tulipe", "lilas"]
len(fleurs) # compter le nombre de valeurs dans la variable fleurs (list)
         # 4

# exemple 3 input()

# permet de bloquer le terminal pour poser une question 

reponse = input("quel est votre budget ?")

# bonus
# range()
# str()
# int()
```


## fonction (def)

- permet de stocker des traitements dans une "variable"
- permet de ne pas se répéter

```py
# créer une fonction
def nom_fonction ( param1, param2 ) :
    # traitement

# exécuter / appeler la fonction 
nom_fonction ( 1 , 2 )

nom_fonction ( param1 = 1 , param2 = 2 )

nom_fonction ( param2 = 2 , param1 = 1 )

# créer une fonction avec un nombre inconnu de parametre

def nom_fonction ( *param ) :
    # traitement

nom_fonction()
nom_fonction(1,2)
nom_fonction(1,2,3)
nom_fonction(1,2,3,4)


def nom_fonction ( **option ) :
    # traitement

nom_fonction()
nom_fonction(a = 1, b = 2)
nom_fonction(a = 1, b = 2, c = 3)
nom_fonction(a = 1, b = 2, c = 3, d = 4)
```


## tableau => list

- tableau / data structure (synonyme)

- CRUD Create (ajouter) / Read (lire) / Update (modifier) / Delete (supprimer)

```py
liste = [1,2]

# Create
# ajouter le chiffre 3 à la fin 
liste.append(3)
# ajouter le chiffre 0 au début
liste.insert(0,0) 

# Read 
liste[0] # récupérer la première valeur
liste[-3:] # récupérer les 3 dernières valeurs
liste[:2]  # récupérer les 2 premières valeurs

# Update 
# tranformer le chiffre 3 en 10
liste[2] = 10 

# Delete
liste.remove(3) # supprimer la valeur qui a la position 3 
del(liste[2])  # supprimer la valeur qui a la position 2
liste.clear()  # supprimer toutes les valeurs 

# autre
liste.sort() # trier les valeurs du plus petit au plus grand
liste.sort(reverse = True) # trier les valeurs du plus grand au plus petit
liste.reverse() # mettre dans l'autre sens 
```