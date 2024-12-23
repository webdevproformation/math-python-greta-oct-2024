# commentaire en Python 
# en Python on peut écrire DIRECTEMENT le code 
# pas besoin page html => mettre le contenu > mettre un script

# variable
# type => string / chiffre (int / float / complex)
#      => boolean 
#      => tableau (data structure)
#             - list
#             - tuple
#             - set
#             - dictionnaire

# j'ai besoin de code un projet sur la gestion d'une école 
# concept => planning / etudiant / professeurs / salle ...
# ce n'est pas une bonne idée de créer autant de variable que j'ai de date dans mon planning 
# comment gérer (en informatique) ces concepts => objet 

# MAIS en Python pour pouvoir créer un objet IL FAUT OBLIGATOIREMENT créer D'ABORD un class 

toto_titi_toutou = 2

# <p class="first-element-intro">

largeurEcran = 10 

## créer une class qui a 3 propriétés 
class Etudiant : # PascalCase 
    # dans la class il FAUT mettre une identation 
    prenom = "Alain"
    competences = ["PHP", "JS"]
    age = 22

    # et une méthode 
    def presentation(self): # variable qui va permettre d'accéder aux propriétés de l'objet 
        print(f"je suis la méthode présentation de {self.prenom}")



def calcul( *chiffres ) :
    pass ; 

calcul()
calcul(1)
calcul(1,2)
calcul(1,2,3)


def calcul( **chiffres ) :
    print(chiffres.get("a"))
    pass ; 

calcul()
calcul(a = 1)
calcul(a = 1, b = 2)
calcul(a = 1,b = 2,c = 3)

""" print()
sorted() # fonction builtins """

[1,2,3].sort()

# "coucou".sort()
a = sorted("coucou")
print(a)

a = sorted([1,10,30,2,5])
print(a)

a = [1,10,30,2,44]
a.sort()
print(a)