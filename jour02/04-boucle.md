# boucle (loop)

- c'est une structure comme les fonctions (FONCTION) et les conditions (SI)
- structure essentielle 
- 3ème et dernière structure 
- permet de répéter du code plusieurs fois 

```
START
    
    BOUCLE 0 .. 10 AUGMENTE +1
         ECRIRE "bonjour"
    
    # boucle a un nombre de départ => 0
    # boucle a un nombre maximum de fin  => 10
    # à chaque tout de boucle on augmente le chiffre de +1

END
```

# créer programme de recherche


```
START
    etudiants = [ "Alain" , "Benoit" , "Céline" , "Zorro"  ]

    # est ce que dans la variable etudiants il y a un etudiant qui s'appelle Zorro ?? 

    SI etudiants[0] == "Zorro" => False
    SI etudiants[1] == "Zorro" => False
    SI etudiants[2] == "Zorro"  => False 
    SI etudiants[3] == "Zorro"  => True 

    BOUCLE i 0 .. 3 AUGMENTE +1   # incrément
        SI etudiants[i] == "Zorro"
            ECRIRE True 

END
```


# cas pratique

créer un script en PSEUDO Code qui contient une variable de type tableau :
    - qui s'appelle produits 
    - elle contient les prix suivants
        - 22
        - 44
        - 11
        - 10
        - 3
        - 200

pouvez vous me dire si tableau contient un chiffre supérieur à 50 ??

bonus
pouvez vous dire quelle est le nombre qui est le plus petit ??
