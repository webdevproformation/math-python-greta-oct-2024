# fonction 

- en informatique il y a deux éléments de base qui composent les programmes :

1.  variable (x, y score) => permet de stocker des valeurs 
2.  fonction => permet de stocker des plusieurs traitements / plusieurs calculs

# solution SANS FONCTION

```txt
START
    x = 0
    y = 0
    score = 0

    à droite 
    x = x + 1
    score = score + 10    

    à droite 
    x = x + 1
    score = score + 10   

    en haut 
    y = y + 1
    score = score + 20  

    en haut 
    y = y + 1
    score = score + 20 
END
``` 


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

# coucou Nada
