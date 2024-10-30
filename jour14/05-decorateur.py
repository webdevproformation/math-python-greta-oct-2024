# décorateur 

def envoyer_email(fonction):
    def wrapper():
        print("envoyer email")
        fonction()
    return wrapper


@envoyer_email # élargir / étendre une fonction par une autre 
def connexion():
    print("connexion")

connexion() 

# d'abord exécuter la fonction décoratrice envoyer_email
# qui va exécuter fonction connexion
@envoyer_email
class Toto:
    pass 