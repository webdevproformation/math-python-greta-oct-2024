# cas pratique complet 

créer un script contient un tableau 

- qui s'appelle anniversaires = 
- et qui contient les 4 valeurs suivantes  "sept 2024", oct 2024, janv 2025,  nov 2025

1. créer un script qui permet d'afficher le nombre de valeurs stockées dans la variable anniversaires
2. script qui permet de savoir si il y a une date d'anniversaire en fev 2024 dans la variable anniversaires
3.  script qui permet de savoir si il y a une date d'anniversaire en janv 2025 dans la variable anniversaires
4. un script qui permet d'ajouter la valeur "déc 2024" entre la valeur oct 2024, janv 2025


```
FONCTION 
    anniversaire_existe(valeur_recherchee)
        BOUCLE i 0 .. 3 AUGMENTE +1
            SI anniversaires[i] == valeur_recherchee
                ECRIRE True

START
    anniversaires = [ "sept 2024", "oct 2024", "janv 2025",  "nov 2025" ]
    
    # question 1
    compteur = 0 
    BOUCLE i 0 .. 3 AUGMENTE +1
        compteur = compteur + 1
    ECRIRE compteur
    
    # question 2 

    valeur_recherchee = "fev 2024"
    
    BOUCLE i 0 .. 3 AUGMENTE +1
        SI anniversaires[i] == valeur_recherchee
            ECRIRE True

    # question 3 

    anniversaire_existe("janv 2025")

    # question 4 

    # trouver la position de "oct 2024" dans le tableau anniversaires

    anniversaire = ["a" , "b" , "c" , "d"]

    position = 0 
    
    BOUCLE i 0 .. 3 AUGMENTE +1
        SI anniversaires[i] == "b"
            position = i 

    resultat = []
    
    BOUCLE i 0 .. position AUGMENTE +1
        resultat[i] = anniversaires[i]

    resultat[position + 1] = "x"

    BOUCLE i position + 1 .. 3 AUGMENTE +1
        resultat[i + 1] = anniversaires[i]


END 
```