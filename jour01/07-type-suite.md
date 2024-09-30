# type 

```txt
START
    entier = 1
    prix = 12.5

    texte = "bonjour les amis"

    logique = True
    logique2 = False
END
```

# chiffre int / float

```txt
START
    # addition / soustraction / multiplication / division / puissance

    prix_ht = 20 
    tva = 1.2
    # multiplication
    prix_ttc = prix_ht * tva 

    remise = 5
    # soustraction
    prix_ttc_avec_remise = prix_ttc - remise

    prix_produit1 = 1
    prix_produit2 = 3

    # addition 
    total_panier = prix_produit1 + prix_produit2
    
    distance = 200
    # division 
    moitie = distance / 2 

END
```

## chaine de caractère / string 

```txt
START
    formation = "DWWM"
    adresse = "75 rue de Paris"

    # je suis une formation DWWM au 75 rue de Paris
    # concaténation => addition de chaine de caractère 

    phrase = "je suis une formation " + formation + " au " + adresse

END
```

## Boolean 

- <https://fr.wikipedia.org/wiki/George_Boole>

=>  raisonnements logiques peuvent être présenté sous forme de lois mathématiques 
=> 1 (True)
=> 0 (False)

chiffre 

1    [ 0  0 ]
2    [ 0  1 ]
3    [ 1  0 ]
4    [ 1  1 ]

- <https://fr.wikipedia.org/wiki/Table_de_v%C3%A9rit%C3%A9>

opérations que l'on peut réaliser via des valeurs boolean

True ET True => True
False ET True => False
True ET False => False
False ET False => False 

= opérateur ET (opérateur Boolean => comment + pour les chiffres)
=> il faut que les conditions autour du ET soit simulténanement TRUE pour que le calcul retourne True 

True OU True => True
True OU False => True
False OU True => True
False OU False => False 

=> si une condition auteur de l'opérateur OU est True => renvoie true sinon ça retourne false 


```txt
START

    variable = 12 > 10 # True

    variable2 = 30 > 40 # False

    variable3 = 30 > 40 OU 12 > 10
                 False   OU  True
                    True 


    variable4 = 30 < 40 ET 12 < 10
                TRUE    ET  False
                  False 
END
```

# cas pratique 

pour chaque comparaison opérationn boolean dire SI c'est True ou False ??

```txt
2 >= 2
"a" == "ab"
2 != 3 ET 10 < 33
(2 != 5 ET  3 > 4 ) OU 2 <= 14 
2 != 5 ET  ( 3 > 4  OU 2 <= 14 ) 
2 != 5 ET  3 > 4  OU 2 <= 14  
```
