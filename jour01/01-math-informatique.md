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


# cas pratique 

pour ceux qui ont compris  voici un cas traiter  , vous avez un nouveau labyrinthe :

<https://user.oc-static.com/upload/2022/03/24/16481140439378_FR_4366701_ALGO_STATICS_P1C3-2.jpg>

- attention aux obstacles au milieu / attention au monstre
- attention il y a deux solutions possible pour atteindre le trésor

- écrire le pseudo code pour faire en sorte que le perso arrive sur la case du trésor