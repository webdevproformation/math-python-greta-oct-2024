class Etudiant :
    # et cette class contient uniquement un nom  comme attribut
    def __init__(self, p_nom):
        self.nom = p_nom

class Etudiant :
    # et cette class contient uniquement un nom  comme attribut
    # qui est privé
    def __init__(self, p_nom):
        self.__nom = p_nom

    def set_nom(self, p_nom):
        # condition 
        self.__nom = p_nom

    def get_nom(self):
        return self.__nom
    
e = Etudiant("nom")
e.set_nom("nouveau nom") # e.nom = "nouveau nom"


class Etudiant :
    @property # getter
    def nom(self):
        return self.__nom
    
    @nom.setter # setter
    def nom (self, valeur):
        if(len(valeur) > 2 ):
            self.__nom = valeur
        else:
            raise Exception("nom invalide")
        
e2 = Etudiant()
e2.nom = "Alain" # exécuter le setter de la class 
print(e2.nom)
# permet d'utiliser la syntaxe d'une propriété publique sur une propriété private 
# facilité d'écrire d'une propriété public ET EN même temps la sécurité du code d'une propriété private 



class Etudiant:
    largeur = 20 

    @staticmethod
    def presentation():
        print("je m'appelle Alain")

""" e = Etudiant()
e.presentation() """

Etudiant.presentation()
Etudiant.largeur = 30 

print(Etudiant.largeur)


etudiant = ["Alain", 22 , "75 rue de Paris"]

class Etudiant:
    def __init__(self, nom, age , adresse):
        self.nom = nom
        self.age = age
        self.adresse = adresse

e = Etudiant(etudiant[0] , etudiant[1] , etudiant[2])


# ------------------

from dataclasses import dataclass

@dataclass
class Etudiant:
    nom : str
    age : int
    adresse : str

e = Etudiant(adresse = "30 rue de Lille" , nom = "Zorro",age = 22)
print(vars(e))