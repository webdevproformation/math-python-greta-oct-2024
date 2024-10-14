# crée une fonction
def f1(): 
    print("je suis f1")
# exécute
f1()

# créer une fonction qui retourne une fonction 
def f2():
    return f1

f2()
f2()() # première () exécuter f2 => f1 
       # deuxieme () exécuter f1

    # pour exécuter la fonction qui est retournée par f2 il faut
    # enchainer deux fois des () ()

# ----------------

# fonction décoratrice
def traitement(f):
    def inner():
        print("je suis une fonction décoratrice")
        f()
    return inner

# décorer la fonction calcul avec la fonction décoratrice traitement
@traitement
def calcul():
    print("je suis la fonction calcul")

calcul()
# fonction qui exécuter (modifier) une autre fonction
# fonction décoratrice avec un @
# calcul() => exécuter traitement qui exécuter calcul


def envoiEmail(f):
    def inner():
        print("envoyer email")
        f()
    return inner

def verifBdd(f):
    def inner():
        print("verification en base de données")
        f()
    return inner

@envoiEmail
@verifBdd
def connexion():
    print("connexion")

connexion()
# intérêt des decorateurs => ajouter des traitements en + sur une fonction existante sans avoir à modifier l'appel de la fonction
# fonction qui modifie une fonction 