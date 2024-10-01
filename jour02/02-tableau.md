# tableau 

```
START

    # je suis dans une classe ET j'ai face à moi plusieurs étudiants
    
    # je suis obligé de créer AUTANT de VARIABLE que J'AI d'étudiants

    etudiant1 = "Alain"
    etudiant2 = "Benoit"
    etudiant3 = "Céline"
    etudiant4 = "Zorro"

    # j'aimerai créer UNE SEULE variable qui permet de stocker TOUS les étudiants 
    
    # pour faire ça => créer une variable 

    etudiants = [ "Alain" , "Benoit" , "Céline" , "Zorro"  ]

    # la variable étudiants contient un tableau qui contient 4 string 
END
```

## cas pratique

créer un script en PSEUDO Code qui contient une variable  :
    - qui s'appelle recette 
    - qui contient les string suivantes : "Carotte", pomme de terre , riz , sel , poivre  
   <!--  - 
    - céleri -->

```txt
START
    recette = [ "Carotte" , "pomme de terre"  , "riz"  , "sel" , "poivre"]
    recette=["Carotte","pomme de terre","riz","sel","poivre"]
    recette = [
                "Carotte",
                "pomme de terre",
                "riz",
                "sel",
                "poivre"
    ]
END
```

## comment utiliser les valeurs qui sont stockées dans le tableau  ????

```txt
START
    fleurs = ["rose", "jasmin", "tulipes"]
    #           0         1         2 

    # je veux récupérer la première valeur qui est stockée dans la variable fleurs qui est un tableau
    # pour récupérer "rose" qui est stockée dans la variable fleurs nous allons utiliser la POSITION de la valeur dans le tableau 
    # utiliser l'INDEX

    fleurs[0] # récupére moi la valeur qui est stockée à la position (index) 0 dans la variable fleurs (qui est tableau) 

    etudiants = [ "Alain" , "Benoit" , "Céline" , "Zorro"  ]
    #                0         1          2          3

    # je veux récupérer la valeur "Céline" ??

    etudiants[2]

    # je veux récupérer la valeur "Benoit" ??

    etudiants[1]
END
```


## cas pratique


