# rappel hier qu'est ce que l'on a vu ensemble ??? 

# Math (PSEUDO CODE)

## condition

```txt
START
    # SI est un mot clé (de tous les langages informatique)
    # suivi d'une 
    # condition / comparaison / opération boolean
    SI 10 > 2
        True
        Executer les instructions du SI 

    SI 10 > 2 OU 2 < 5 ET 5 > 3 ET ...
        False
END
```

# tableau 

- variable que contient PLUSIEURS VALEURS
- ça permet d'éviter de créer autant de variable que j'ai de valeurs à stocker 

```txt
START
    # 3 variables qui contient 1 string chacune
    adresse1 = "75 rue de Lille"
    adresse2 = "80 rue de Marseille"
    adresse3 = "22 rue de Paris"

    # au lieu d'avoir 3 variables => grâce au tableau je n'ai QUE UNE SEULE VARIABLE qui contient 3 valeurs de type string 
    
    # version en 1 ligne
    adresses = [ "75 rue de Lille" , "80 rue de Marseille" ,  "22 rue de Paris" ]

    # version avec saut de ligne après chaque valeur 

    # square bracket  []
    # crochet []
    adresses = [ 
            "75 rue de Lille" ,       # 0
            "80 rue de Marseille" ,   # 1
            "22 rue de Paris"         # 2
    ]

    # pour utiliser les valeurs stockées DANS un tableau il faut utiliser leur position (index)
    
    # pour récupérer la valeur "80 rue de Marseille" qui est stockée dans le tableau 
    adresses[1]  
END
```

# objet 

- variable qui contient PLUSIEURS VALEURS
- curly bracket  { } 
- clé : valeur

```txt
START    
    # curly bracket  { } 
    # accolade { }
    # objet qui contient 6 clés 
    voiture = {
        "clé" : "valeur", # dans certain langage il faut mettre des "" sur la clé
        modele : 206,     # dans d'autres langages pas la peine 
        marque : "Peugeot"
        annee : 2020,
        prix : 10_250.3
        proprietaire : {
            nom : "Alain"
        },
        enCirculation : True
    }

    # je veux récupérer la valeur 2020 qui est stockée dans l'objet comment faire ?

    voiture.annee 

    # je veux récupérer la valeur "Alain" qui est stockée dans l'objet comment faire ?

    voiture.proprietaire.nom
END
```

# fonction 

- variable dans laquelle vous allez stocker des instructions 

```txt
FONCTION
    # créer / déclarer une fonction
    addition()
        a = 1
        b = 2
        c = a + b 
START
    # appeler / exécuter une fonction 
    addition()
END
```

# boucle 

- permet de faire répéter des instructions
- variable => i (incrément)
- valeur de départ 0
- valeur maximum  10
- augmentation + 1 (à chaque tour de boucle)

```txt
START
    
    BOUCLE i 0 .. 10 AUGMENTER + 1

END
```

# algorithme 

- mixer boucle / condition / variable / fonction 
- trier un tableau du plus petit au plus grand => https://fr.wikipedia.org/wiki/Tri_%C3%A0_bulles
- prendre un tableau et insérer dedans une valeur qui va pousser vers la droite les autres valeurs 

```txt
START
    anniversaires = ["a" , "b" , "c" , "d"]

    position = 0 
    
    BOUCLE i 0 .. 3 AUGMENTE +1
        SI anniversaires[i] == "b"
            position = i 

    resultat = []
    
    BOUCLE i 0 .. position AUGMENTE +1
        resultat[i] = anniversaires[i]

    resultat[position + 1] = "x"

    BOUCLE i position + 1 .. 3 AUGMENTE +1
        resultat[i + 1] = anniversaires[i]
END
```

# Python

- langage très utilisé en 2024 (notamment dans le domaine de l'IA)
- nous allons utiliser la version 3.12

## commentaire en Python

```py
# commentaire monoligne

"""
commentaire
multiligne
"""
```

## variable en Python

```py
# chiffre
# chiffre entier
distance = 200

# chiffre à virgule
# https://docs.python.org/fr/3/tutorial/floatingpoint.html
remise = 0.5
remise = 1/3 => 0.33333333333333333333333333333333333333....
remise = 1/3 => 0.3333333333333333333334

# chiffre complex
coordonnees = 2 + 3j

# les textes

```