# condition 

- les fonctions variables vont stocker des traitements 
- les fonctions sont aussi appelées des structures 

- il existe deux autres structures : 
    - les conditions (que l'on va voir)
    - les boucles 


```txt
START
    
    age = 20 

    si la personne est mineur (0 et 18) alors je veux affiche le texte "je suis mineur"

    si la personne est majeur (18 à 100 ) alors je afficher le texte "je suis majeur"

    SI age > 0 ET age <= 18
    #   20 > 0 ET 20 <= 18
    #   True   ET  False 
        ECRIRE "je suis mineur"
    SI age > 18 ET age <= 100
    #  20  > 18 ET 20 <= 100
    #   True    ET True 
    # True 
        ECRIRE "je suis majeur"

END
```

# cas pratique 

créer un script qui contient les instructions suivantes 

créer une variable qui s'appelle langue qui contient le texte "fr"


si la variable langue contient la valeur "en" écrire "Hello"
si la variable langue contient la valeur "es" écrire "Hola"
si la variable langue contient la valeur "gr" écrire "Hallo"
si la variable langue contient la valeur "fr" écrire "Bonjour"

```txt
START
    langue = "english"

    SI langue == "english
        ECRIRE "Hello"
    SI langue == "espagnol"
        ECRIRE "Hola"
    SI langue == "germany"
        ECRIRE "Hallo"
    SI langue == "français"
        ECRIRE "Bonjour"
END
```



```
START
        verif = 1 == 1
                TRUE
        verif2 = 10 == 10 
                TRUE
        verif3 = "Hello" == "Hello"
                True 

        text = "Hello"

        verif4 = text == "Hello"
        #        "Hello" == "Hello"

END
```


# cas pratique 