# fonctions en Python subtilités

def prixTTC(prixHT : float, unite : str) -> None:
    resultat = f"{prixHT * 1.2} {unite}"
    print(resultat)

# au moment de l'exécution de la fonction
# mis les valeurs dans le même ordre QUE dans la définition de la fonction 
prixTTC(10, "€")

# au moment de l'appel de la fonction
# vous pouvez rappeler le nom du paramètre et la valeur à lui associer 
prixTTC(prixHT=20 , unite="$")

# enfin il est possible de mettre les arguments DANS l'ordre que l'on veut SI on écrit le nom du paramètre avant la valeur
prixTTC(unite="£" , prixHT=40 )


# fonction qui fait une addition ET on ne sait pas combien de paramètre on peut lui passer 
# nombre illimité d'arguments à passer à la fonction

def addition ( *chiffres ):
    print(chiffres)
    resultat = 0 
    for i in chiffres:
        resultat += i
    print(resultat)

addition()
addition(1)
addition(1,2)
addition(1,2,3)
addition(1,2,3,4)
addition(1,2,3,4,5)

print(1)
print(1,"a")
print(1,"a" ,"toto")
print(1,"a" ,"toto", [])

# si vous avez une fonction qui contient un paramètre avec ** 
# la fonction peut être appelée avec autant d'argument que l'on veut 

def genererPdf( **options ): # keywordargument => kwarg
    print(options)

genererPdf(nom = "Victor Hugo" , dt = "janvier 2024" , isAvailable = True )
genererPdf(nom = "Arthur Rimbault")
genererPdf(nom = "Albert Camus" , dt = "1960" , description ="il est largement considéré comme l’un des plus grands écrivains français de tous les temps.")

"""
créer le fichier 15-exo.py

1/ déclarer une fonction min 

2/ cette fonction dispose de deux arguments a et b

3/ cette fonction contient 3 instructions :
- si a est supérieur à b afficher la valeur de b dans la console
- si a est inferieur à b afficher la valeur de a dans la console
- si a est égal à b afficher la valeur de a dans la console
"""