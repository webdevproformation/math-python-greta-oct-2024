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
