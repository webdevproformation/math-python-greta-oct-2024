# rappel

# class / objet

why ?? 

- ranger plein d'informations (propriétés) et les traitements qui vont avec (méthodes)

how ?

```py
class NomClass : # PascalCase
    prop = "texte"
    caracteristique = 2
    cle = True 

    # méthodes classiques
    def nom_method(self):
        # traitement dans la méthode

    def nom_method2(self):
        # traitement dans la méthode2

    # méthode magique     
    def __init__ (self):
        # traitement de la méthode constructrice 
```

une fois que la class est créé je peux créer un objet depuis la class => instancier une class

```py
nom_objet = NomClass() # automatiquement la méthode __init__ est exécutée
nom_objet.prop
nom_objet.caracteristique
nom_objet.cle
nom_objet.nom_method()
nom_objet.nom_method2()
```

# portée (scope)

- les propriétés et les méthodes d'une class en plus de les créer 
- on peut leur attribuée une visibilité / disponible 
- Pourquoi ? organisation + sécurisation (=> UTILISER de la manière CORRECTE)

programme pour la gestion des Livres
propriété => disponible OUI / NON => Boolean => PAS d'autres valeurs => int / string / tableau 

- 3 types de portées
    - private
    - public 
    - protected 

```py 
class Toto:
    propriete_public = 10 
    _propriete_protected = 20 
    __propriete_private = 30 # condition OBLIGATOIRE AVANT de lui affecter une valeur 

    # pour donner une valeur à une propriété private => 
    # il faut créer une méthode dédiée à cette propriété setter 

    def set_propriete_private(self, valeur): 
        # condition sur la valeur 
            self.__propriete_private = valeur
        # else
            # raise Exception("message alerte !!!")

```


# héritage polymorphisme

- class 1 => 3 propriétés a b c méthode d et f 
- class 2 => 3 propriétés a b c méthode d et e
- Salle de Réunion / Salle de classe
- Professeur / Etudiant / Personnel 
- AU lieu d'avoir plusieurs class qui contiennent le même code / même propriétés / méthodes 
- créer une classe mère qui contient les propriétés / méthodes communes aux class enfants

```py
class A: # class MERE
    prop1 = 1
    prop2 = 2
    
    def __init__(self):
        # traitement
    
    def method(self):
        # traitement

class B(A):
    def method2(self):
        # traitement

class C(A):
    def method3(self):
        # traitement

```