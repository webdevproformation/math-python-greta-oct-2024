class Formation :
    # constructeur de la class 
    def __init__(self, p_nom, p_prix) :
        self.nom = p_nom
        self.prix = p_prix

f = Formation("DWWM", 5000) 

# en Python les propriétés d'une class SONT PUBLIQUES 
# je vais accéder à la propriété nom depuis l'objet 
# 
print(f.nom) 

# modifier la valeur stockée dans la propriété depuis l'extérieur de class 
f.nom = "Intégrateur Web" # modifier la valeur stockée dans la propriété 
print(f.nom)
# la propriété nom est PUBLIQUE !!! 

# par rapport à d'autres langages => en Python les propriétés (et les méthodes) sont PUBLIQUES 
# la convention => si une propriété est (pour le codeur) par CONVENTION
# privée __nom_propriete
# protected _nom_propriete


class CompteBancaire:
    def __init__(self,p_nom, p_adresse , p_password) :
        self.nom = p_nom               # Publique
        self._adresse = p_adresse      # Protected
        self.__password = p_password   # Private 

compte = CompteBancaire("Alain" , "75 rue de Paris" , "azerty")

print(compte.nom)
compte.nom = "Alain DUPONT"
print(compte.nom)

print(compte._adresse)
compte._adresse = "80 rue de Lille"
print(compte._adresse)

# print(compte.__password)

compte.__password = "toto" # essayer de modifier la propriété privée depuis l'objet

print(vars(compte))
"""
{
    'nom': 'Alain DUPONT', 
    '_adresse': '80 rue de Lille', 
    '_CompteBancaire__password': 'azerty', 
    '__password': 'toto'
}
"""

# print(compte.__password)