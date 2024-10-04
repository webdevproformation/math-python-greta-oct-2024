# rappels 



## fonction 

- variable qui contient des instructions 


```py 
# créer une fonction 
def nom_fonction (a, b) :
    # traitement
    # calcul
    # créer une variable
    # concaténation ...
    pass

# appeler la fonction
nom_fonction(1 , 2 )

# appeler la fonction en reprenant les parametres
nom_fonction( a = 1 , b = 2 )

# appeler la fonction en reprenant les parametres dans un autre ordre
nom_fonction(  b = 2 , a = 1  )

# si vous avez une fonction dont vous ne savez pas le nombre de paramètres
# solution 1
def nom_fonction( *options ) : # attention au * devant le paramètre
    pass

nom_fonction()
nom_fonction(1)
nom_fonction(1,2)
nom_fonction(1,2,3)

# solution 2
def nom_fonction ( **options ):
    pass

nom_fonction()
nom_fonction(a = 1)
nom_fonction(a = 1 , b = 2)

# facultatif => lorsque l'on crée une fonction on peut ajouter des annotations FACULTATIVES 

def calcul ( a : str , b : int ) -> None :
    """
    écrire un texte qui décrit à quoi ça sert, comment ça marche ...
    """
    pass
```

## boucle

```py 
# boucle for 
start = 0
end = 10
pas = 2

for i in range(start, end, pas) :
    # traitement

# boucle while

i = 0
while i < 10 :
    # traitement
    i += 2
```


## norme de nommage fonction et variable (class)

```

# régles de nommage

premier_eleve # snake_case 
premierEleve  # camelCase 
PremierEleve  # PascalCase
premier-eleve # kebab-case
```

```

créer le fichier 01-exo.py

dans ce fichier vous allez créer une fonction qui dit si ou ou non un mot contient une voyelle 

- la fonction s'appelle isVoyelle
- elle a un paramètre qui est une chaine de caractère 
- cette fonction contient plusieurs instructions
    - première instruction qui parcours chaque lettre du mot (paramètre)
    - deuxieme block si la lettre == a e i o u y 
        - la fonction print True
    - sinon print False 

isVoyelle("manger") True
isVoyelle("bnp") False 

```
