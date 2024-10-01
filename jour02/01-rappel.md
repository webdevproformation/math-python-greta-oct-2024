# Rappel

## variable

- element de base de tous les programmes
- stocker une VALEUR => avec 3 types de base 
                - chiffre = > int / float
                - texte => string
                - boolean => boolean

```txt
START
    # stocker un chiffre entier
    age = 22 
    # stocker chiffre à virgule flottante
    prix = 1.2
    # stocker du texte
    text = "bonjour"
    largeur = "20px"

    # stocker un boolean
    isAdmin = True
    verification = False
END
```

## fonction

- deuxième élément de base de tout programme informatique
- stocker de stocker des instructions (traitements)
- ça permet de regrouper des instructions (éviter de se répéter)
- attention il faut créer / déclarer une fonction AVANT de l'utiliser 
- conseil = une fonction contient au maximum 30 traitements 

```txt
FONCTION
    addition
        a = 1
        b = 2
        c = a + b

START
    addition
    addition
    addition
END
```

## fonction avec paramètre

```txt
FONCTION
    # créer la fonction
    addition (a, b)
        c = a + b

START
    # appel la fonction / exécuter la fonction
    addition(1,2)
    addition(3,4)
    addition(10,1000)
END
```

## type

- int / float
- string
- boolean
- tableau (aujourd'hui) => DataStructure 
- objet  (aujourd'hui)

## opération sur les chiffres et sur les string 

- addition  +
- soustraction  -
- division   /
- multiplication *
- puissance  **
- modulo (aujourd'hui) %


```txt
START
    rue = "75 rue de Paris"
    ville = "Lyon"
    # addition de 2 textes => concaténation
    adresse_complete = rue + ville
END
```


## calcul boolean

```
START
    
    # comparaison 
    a = 20 > 10  # True
    b = 20 < 10  # False
    c = 20 >= 10 # True 
    d = 20 <= 10 # False
    e = 20 == 10 # False
    f = 20 != 10 # True

    # opérateur  boolean

    g = 20 > 10 ET 30 < 12   
        True    ET False
        False
    
    g = 20 > 10 OU 30 < 12 
        True   OU   False
        True 

END
```

True ET True => True
True ET False => False
False ET True => False
False ET False => False

True OU True => True
True OU False => True
False OU True => True
False OU False => False


## conditions

- SI est un mot clé du langage (de tous les langages)
- le mot clé SI est suivi d'un calcul boolean 

```
START

    SI 2 > 3 OU 10 < 30
       False OU  True
            True 
       ECRIRE "bonjour" 

    SI 2 != 2 ET 10 < 30
       False  ET True
            False  
       ECRIRE "bonjour 2" 

END
```