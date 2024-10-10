import lib 
# il FAUT OBLIGATOIREMENT QUE lib.py soit dans le même dossier QUE 03-main.py

print(lib)
## <module 'lib' from 'c:\\Users\\harri\\Desktop\\math\\jour07\\lib.py'> 
# créer une variable qui a le nom du fichier 
# toutes les variables / fonction / class => associer comme un dictionnaire

# utiliser la fonction addition écrite dans le fichier lib.py

lib.addition( 1 , 2 ) # 3
# dès que vous utilisez le mot clé import qui appelle un module externe il y a un dossier qui se crée automatiquement
# __pycache__ => créé AUTOMATIQUEMENT 
# qui contient un fichier .pyc
# python va créer un fichier .pyc qui regroupe tous les imports dans un seul fichier en format BINAIRE
# ne pas toucher à ce fichier  .pyc (il faut juste savoir qu'il existe !)

print(lib.__dict__)

"""
print(lib.__dict__)
lib = {
    "addition" : ....,
    "soustraction" : ....
}
"""

# importer les fonctions addition et soustraction (écrite dans le fichier 03-lib.py)

