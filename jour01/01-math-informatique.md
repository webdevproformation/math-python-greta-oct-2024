# math et informatique 

- j'ai basé cette présentation sur le support de cours suivant : 
- <https://openclassrooms.com/fr/courses/7527306-decouvrez-le-fonctionnement-des-algorithmes>

question Charlène : 

```bash
git init
git add .
git commit -m "foiezhfiuze"
git remote ...
```

# avant les math 

- pour créer un programme informatique => découper son problème en brique de base
- comment organiser notre programme 
- attention ici l'objectif n'est pas de code => PSEUDO CODE (ressemble à du code ET du français)

```txt 
START
    instruction
    instruction
    instruction
END 
```

# deux intructions

- variable => stocker des informations 
- fonction => stocker des traitements 
 
# cas fil rouge 

=> jeu de type labyrinthe
=> le but du jeu c'est de faire en sorte que le personnage arrive au trésor 

![](https://user.oc-static.com/upload/2022/03/24/16481137434451_FR_4366701_ALGO_STATICS_P1C3-1.jpg)


# abstraction 

```txt
START
    x = 0 # position horizontale du perso sur le damier 
    y = 0 # position verticale du perso sur le damier 

    .... ????? 
    je déplace le personnage à droite d'une case 
    attention le symbole = n'a pas le même sens en mathématique QUE en informatique
    = en mathématique COMPARAISON
    = en informatique AFFECTATION 
    D'abord le programme va effectuer le calcul à DROITE du = 
    une fois que la calcul est fini alors STOCKE la valeur calculé à la variable à GAUCHE du = 
    x = x + 1 


    objectif => le perso arrive à la case du trésor
    x = 2
    y = 2
END 
```

# solution du premier jeu 

```
START
    x = 0
    y = 0

    déplacer à droite d'une case 
    x = x + 1   
    dans ma tête et dans la RAM de l'ordinateur x = 1 y = 0

    déplacer vers le haute d'une case 
    y = y + 1
    dans ma tête et dans la RAM de l'ordinateur x = 1 y = 1

    déplacer à droite d'une case 
    x = x + 1   
    dans ma tête et dans la RAM de l'ordinateur x = 2 y = 1

    déplacer vers le haute d'une case 
    y = y + 1
    dans ma tête et dans la RAM de l'ordinateur x = 2 y = 2

    etant donné que x = 2 y = 2 => j'ai gagné !!!!!!!!!
END 
```


# cas pratique 

pour ceux qui ont compris  voici un cas traiter  , vous avez un nouveau labyrinthe :

<https://user.oc-static.com/upload/2022/03/24/16481140439378_FR_4366701_ALGO_STATICS_P1C3-2.jpg>

- attention aux obstacles au milieu / attention au monstre
- attention il y a deux solutions possible pour atteindre le trésor

- écrire le pseudo code pour faire en sorte que le perso arrive sur la case du trésor

# bientôt la correction 

## solution 1

```txt
START
    x = 0
    y = 0

    aller à droite  x  1 et y  0
    x = x + 1

    aller à droite  x  2 et y  0
    x = x + 1

    aller à droite  x  3 et y  0
    x = x + 1

    aller en haut   x  3 et y  1
    y = y + 1

    aller en haut   x  3 et y  2
    y = y + 1

    aller en haut   x  3 et y  3
    y = y + 1

END
```

## solution 2

```txt
START
    x = 0
    y = 0

    x = x + 3
    y = y + 3

END
```

## solution 3

```txt
START
    x = 0
    y = 0
    
    aller en haut x 0 y 1
    y = y + 1

    aller en haut x 0 y 2
    y = y + 1

    aller à droite  x 1 y 2
    x = x + 1

    aller en haut  x 1 y 3
    y = y + 1

    aller à droite  x 2 y 3
    x = x + 1

    aller à droite  x 3 y 3
    x = x + 1
END
```


## solution 4

```txt
START
    x = 0
    y = 0
    
    aller en haut x 0 y 2
    y = y + 2

    aller à droite  x 1 y 2
    x = x + 1

    aller en haut  x 1 y 3
    y = y + 1

    aller à droite  x 3 y 3
    x = x + 2
END
```