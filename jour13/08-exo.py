class Salaire :
    def __init__(self, p_montant, p_mois, p_annee):
        self.set_montant( p_montant )
        self.annee = p_annee
        self.mois = p_mois

    def set_montant(self,valeur) :
        if(type(valeur) is int and valeur > 0) :
            self.__montant = valeur
        else :
            raise Exception("montant invalide")
        
s1 = Salaire(10, 1 , 2024)
print(vars(s1))
# {'_Salaire__montant': 10, 'annee': 2024, 'mois': 1}

s2 = Salaire(10,2, 2024)
