# dernier concept de la journée
# portée des variables 



def f():
    chiffre = 10
    # la variable chiffre est stockée DANS la fonction f
    # on dit que la variable chiffre est LOCALE à la fonction 
    # je ne peux UTILISER cette variable QUE dans la fonction 


# print(chiffre) 
# NameError: name 'chiffre' is not defined


largeur = 10
# la variable largeur a une portée GLOBALE
# cette variable est disponible AVANT et APRES la fonction 
# MAIS elle peut être aussi utilisée DANS la fonction  

def f2():
    print(largeur +2)

def f3():
    print(largeur -1)

def f4():
    print(largeur + 5)

f2()

