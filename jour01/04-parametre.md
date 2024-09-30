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