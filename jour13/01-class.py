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

