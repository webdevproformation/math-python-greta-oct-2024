class Phrase :
    def __init__(self, texte) :
        self.texte = texte

    """def nb_lettres(self) :
        print(len(self.texte)) """
    
    def __len__ (self) :
        return len(self.texte)
    
    def __add__ (self, other) :
        return len(self.texte) + len(other.texte)
    
    def __str__(self):
        return str(vars(self))

    def presentation():
        print(f".....")

    def __contains__ (self, lettre) :
        return lettre in self.texte

phrase = Phrase("lorem ipsum")
# phrase.nb_lettres()

print("e" in phrase)

# combien j'ai de lettre dans ma phrase
print(len(phrase)) # via la méthode magique __len__ (qui est la class)

phrase2 = Phrase("comment allez vous aujourd'hui ????")

print(len(phrase2))
total_lettre = phrase + phrase2

print(total_lettre)

print(phrase2)

# chercher est ce que le texte "bonjour" contient la lettre x ??

cherche = "x" in "bonjour"

print(cherche)

"""
créer le fichier 04-exo.py

dans ce fichier vous allez créer une class qui s'appelle Point
cette class dispose de deux propriétés 
    - x
    - y 

vous devez créer une méthode qui va permettre de pouvoir additionner deux points 
qui va donner la position d'un nouveau point qui va avoir comme position
la valeur du x du 1er point + x du 2eme point => x point 3
la valeur du y du 1er point + y du 2eme point => y point 3

premier_point = {  x : 2 , y : 3 }
deuxieme_point = {  x : 4 , y : 5 }
pt_trois = premier_point + deuxiement_point => { x : 6 , y : 8 }

"""