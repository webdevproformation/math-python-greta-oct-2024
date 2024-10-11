# rappel 

## module 

- projet compliqué => découper le projet en plusieurs fichiers 
- donc vous allez devoir importer le contenu d'un fichier dans un autre 

## syntaxe 

```py
# fonctions.py
# stocker des fonctions qui contiennnent des traitements / calcul 
def f1():
    pass

def f2():
    pass 
```

### syntaxe 1 : import <nom_module>

```py
# principal.py
import fonctions # le nom du fichier 
                 # ne écrire "fonctions"
                 # il faut QUE les fichiers principal.py ET fonctions.py dans le même dossier
fonctions.f1() # ne pas oublier le nom du fichier . fonction à utiliser ()
```

### syntaxe 2 : from <nom_module> import <fonction1>, <fonction2>

```py
from fonctions import f1, f2
# import où on précise QUELLES FONCTIONS SONT à UTILISER 
f2()
```

## module natif 

- builtin => print() / range() / len() / str() / list()  / int() / float() / set()
- ...
- liste complète => https://docs.python.org/3/py-modindex.html

## module créé par le développeur 

- vous créez un fichier => importer dans un autre 

## module créé par la communauté => télécharger 

- pypi.org (dépôt => site internet qui stocke du code)
- plein de module / de code / package => qui vont répondre à un besoin 
- ET que l'on va pouvoir utiliser 
- il faudra au préalable les télécharger => via la commande `pip`