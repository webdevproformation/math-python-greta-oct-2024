# print(1/0)
# print(1/"a")


class MonException(Exception): # héritage
    pass

def verifier_liste(liste):
    if len(liste) != 2 :
        raise MonException("la liste doit contenir 2 éléments exactement")
    
verifier_liste([1,2])