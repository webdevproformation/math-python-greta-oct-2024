# solution AVEC FONCTION


```txt
FONCTION
    # fonction = variable qui stocke des traitements
    # il faut créer les fonctions AVANT de les appeler / exécuter
    aller_a_droite  
        x = x + 1
        score = score + 10

    aller_en_haut
        y = y + 1
        score = score + 20  
START
    x = 0
    y = 0
    score = 0

    aller_a_droite 
    aller_a_droite
    aller_en_haut
    aller_en_haut
END
``` 


# solution AVEC FONCTION AVEC PARAMETRE



```txt
FONCTION
    # la fonction aller_a_droite dispose d'un parametre =>  nb_fois
    # ce paramètre c'est une VARIABLE LOCALE A LA FONCTION
    # existe QUE DANS LE BLOC de la fonction 

    aller_a_droite ( nb_fois )
        x = x + 1 * nb_fois
        score = score + 10 * nb_fois

    aller_en_haut ( nb_fois )
        y = y + 1 * nb_fois
        score = score + 20 * nb_fois
START
    x = 0
    y = 0
    score = 0

    aller_a_droite (2)
    aller_en_haut(2)
END
``` 

# cas pratique 

en utilisant l'image 05-exo.png, créer un programme qui permet au personnage d'atteindre le trésor sans passer les pierres / les monstres

![](https://github.com/webdevproformation/math-python-greta-oct-2024/blob/main/jour01/05-exo.png)

créer des fonctions qui permettent de se déplacer vers le haut et vers la droite

si le personnage se déplace horizontalement son score augmente de + 1
si le personnage se déplace verticalement  son score augmente de + 2


# les symboles 

- en informatique vous pouvez :
    - additionner des chiffres avec le symbole `+`
    - soustraire des chiffres avec le symbole `-`
    - multiplier des chiffres avec le symbole `*`
    - diviser des chiffres avec le symbole `/`
    - puissance d'un chiffre sur un autre des chiffres avec le symbole `**`


# Solution 1

```
FONCTION
    aller_a_droite (nb_fois)
        x = x + 1 * nb_fois
        score = score + 1 * nb_fois

    aller_en_haut (nb_fois)
        y = y + 1 * nb_fois
        score = score + 2 * nb_fois
START
    x = 0
    y = 0 
    score = 0
    aller_a_droite(2)
    aller_en_haut(3)
END
```


# Solution 2

```
FONCTION
    aller_a_droite (nb_fois)
        x = x + 1 * nb_fois
        score = score + 1 * nb_fois

    aller_en_haut (nb_fois)
        y = y + 1 * nb_fois
        score = score + 2 * nb_fois
START
    x = 0
    y = 0 
    score = 0
    aller_en_haut(3)
    aller_a_droite(2)
END
```

# Solution 3

```
FONCTION
    aller_a_droite (nb_fois)
        x = x + 1 * nb_fois
        score = score + 1 * nb_fois

    aller_en_haut (nb_fois)
        y = y + 1 * nb_fois
        score = score + 2 * nb_fois

    aller_a_gauche (nb_fois)
        x = x - 1 * nb_fois
        score = score + 1 * nb_fois
START
    x = 0
    y = 0 
    score = 0
    aller_a_droite(2)
    aller_en_haut(2)
    aller_a_droite(1)
    aller_en_haut(1)
    aller_a_gauche(1)
END
```