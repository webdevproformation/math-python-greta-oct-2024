# plus de variable 

![](https://user.oc-static.com/upload/2022/03/24/16481137434451_FR_4366701_ALGO_STATICS_P1C3-1.jpg)

- nous allons compliquer le jeu car on va ajouter en plus du suivi des variables x et y 
- nous allons ajouter une troisième variable score 
- par défaut le score est de 0 quand on commence le jeu
- si on se déplace horizontalement augmenter (automatiquement) le score de + 10
- si on se déplace verticalement augmente le score de + 20 


```txt
START
    x = 0
    y = 0
    score = 0 

    déplacer à droite   =>  x = 1 y = 0 score = 10 
    x = x + 1
    score = score + 10 
    
    monte de 1 case    =>  x = 1 y = 1 score = 30
    y = y + 1
    score = score + 20 
    
    déplacer à droite  => x = 2 y = 1 score = 40
    x = x + 1
    score = score + 10

    monte 1 case       => x = 2 y = 2 score = 60
    y = y + 1
    score = score + 20
END 
```

# cas pratique 

## énoncé

![](https://user.oc-static.com/upload/2022/03/24/16481140439378_FR_4366701_ALGO_STATICS_P1C3-2.jpg)

1. reprendre le 2ème labyrinthe et faire en sorte que le perso arrive au trésor SANS toucher les arbres / pierres et le monstre
1. vous devez suivre sa position x et y ainsi que son score
1. si le personnage se déplace vers la droite le score augmente de + 15  
1. si le personnage se déplace vers le haute le score augmente de + 5

## Objectif 

1. Ecrire le code pour résoudre ce problème 
1. Quel est le score final ? 


# solution 1

```
START
    x = 0
    y = 0
    score = 0

    aller à droite
    x = x + 1
    score = score + 15
    
    aller à droite
    x = x + 1
    score = score + 15

    aller à droite
    x = x + 1
    score = score + 15

    aller en haut
    y = y + 1
    score = score + 5

    aller en haut
    y = y + 1
    score = score + 5

    aller en haut
    y = y + 1
    score = score + 5
    

    le score final est de 60 
END
```


# solution 2

```
START
    x = 0
    y = 0
    score = 0

    aller à droite 3 fois
    x = x + 1 * 3
    score = score + 15 * 3

    aller en haut 3 fois
    y = y + 1 * 3
    score = score + 5 * 3
    
    le score final est de 60 
END
```


# solution 3

```
START
    x = 0
    y = 0
    score = 0

    aller en haut
    y = y + 1 
    score = score + 5 
    
    aller en haut
    y = y + 1 
    score = score + 5 
    
    aller à droite
    x = x + 1 
    score = score + 15 

    aller en haut
    y = y + 1 
    score = score + 5 
    
    aller à droite
    x = x + 1 
    score = score + 15 

    aller à droite
    x = x + 1 
    score = score + 15 


    le score final est de 60 
END
```


# solution 4

```
START
    x = 0
    y = 0
    score = 0

    aller en haut
    y = y + 1  * 2
    score = score + 5  * 2
    
    aller à droite
    x = x + 1 
    score = score + 15 

    aller en haut
    y = y + 1 
    score = score + 5 
    
    aller à droite
    x = x + 1 * 2
    score = score + 15  * 2

    le score final est de 60 
END
```