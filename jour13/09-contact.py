import re
class Contact :
    def __init__(self, p_tel) :
        self.set_tel(p_tel)

    def set_tel(self, valeur) :
        # "^[0-9]{10}$" => PATTERN (FORME)
        # ^ commence 
        # [0-9] un chiffre entre 0 et 9
        # {10} répéter exactement 10 fois
        # $ fini
        resultat = re.search("^0[1-7][0-9]{8}$", valeur)
        if resultat :
            self.__tel = valeur 
        else:
            raise Exception("téléphone fr valide attendu")

contact = Contact("0002031405")

