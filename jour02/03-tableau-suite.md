# tableau suite 

```
START
    # PHP en Python en Javascript 
    # il est possible de stocker des tableaux avec des valeurs de type différents

    etudiant = ["Alain" , 22 , True , [ "PHP", "JS" ] , 10000.3 ]

    # attention si vous faites du C et Java
    # tableaux sont plus contraints (typés) => il n'est possible de stocker QUE un seul type de valeur 

END
```

# les objets 

ça ressemble beaucoup aux tableaux => dans une variable nous allons pouvoir stocker PLUSIEURS valeurs 
MAIS pour chaque valeur on va associer une clé (texte)

```
START
    etudiant = ["Alain" , 22 , True , [ "PHP", "JS" ] , 10000.3 ]

    etudiant[4] # 10000.3

    ## le dernier type de valeur que l'on peut stocker dans une variable => objet 
    etudiant = {
        # clé   : valeur
        prenom : "Alain",
        "age"    : 22 ,
        is_admin : True ,
        competences : [ "PHP", "JS" ],
        paiement_formation : 10000.3
    }

    etudiant = {prenom:"Alain","age":22,is_admin:True,competences:["PHP","JS"],paiement_formation:10000.3}

    etudiant.paiement_formation # objet.clé
    etudiant.age

    etudiant.competences[0]
END
```
- en javascript il est possible de créer de objet (comme on vient de voir)
- en PHP en Python en Java => il faut créer une class pour créer des objets 


# cas pratique 

créer un script en PSEUDO Code qui contient une variable de type objet :
    - qui s'appelle formation 
    - qui contient les clé / valeur suivantes
        - nom DWWM
        - duree 6 mois
        - matieres tableau JS PHP Symfony HTML CSS 
        - lieu tableau présentiel , distanciel
        - prix 10000
        - encours Vrai

comment récupérer la valeur DWWM depuis l'objet
comment récupérer la valeur Symfony depuis l'objet
comment récupérer la valeur distanciel depuis l'objet

```
START
    formation = {
        nom : "DWWM",
        duree : "6 mois",
        matieres : ["JS" , "PHP", "Symfony", "HTML", "CSS" ] ,
        lieu : ["présentiel" , "distanciel"],
        prix : 10000 ,
        encours : True
    }

    formation.nom
    formation.matieres[2]
    formation.lieu[1]
END
```