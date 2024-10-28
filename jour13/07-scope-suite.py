class CompteBancaire :
    def __init__(self, p_password) :
        self.set_password (p_password)
    # fonction que l'on appelle un setter
    # son role est de vérifier QUE la valeur est conforme AVANT de l'affecter dans une propriété 
    def set_password (self, valeur) :
        if(type(valeur) == str and len(valeur) > 7) :
            self.__password = valeur
        else :
            raise Exception("mot de passe incorrect")

c1 = CompteBancaire("azerty123456")
try:
    c1.set_password("qwerty")
    print(vars(c1))
except Exception as e:
    print(f"erreur remarquée lors de la création du compte {type(e)}, {e}")

# cas pratique
# créer le fichier 08-exo.py
# créer une class Salaire 
# contient 3 propriétés
# montant => private
# mois => publique
# annee => publique
# créer une fonction constructrice qui va initialiser les 3 propriétés
# pour la propriété privée (montant) il faut que ce montant soit un chiffre positif 
# si le montant est négatif => une exception doit être levée lors de l'exécution du code 
# écrire le code de cette class !! 


