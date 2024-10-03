""" 
def addition ():
    a = 20
    b = 30
    print (b + a) """

# je viens de mettre les variables a et b comme paramètres de la fonction 
# le fait de mettre des paramètres de fonction 
# les variables EXISTES MAIS elles n'ont pas de VALEUR
def addition (a, b): # paramètres
    print (b + a)

# c'est au moment de l'exécution de la fonction addition QUE je vais donner une valeur a l'argument a et b 

addition(10,30)   # 40 # argument 
addition(35 , 22) # 57

"""
Créer un nouveau fichier 11-exo.py

1/ déclarer une fonction aireCercle 

2/ cette fonction dispose d'un paramètre rayon

3/ cette fonction dispose de deux instructions :
- déclarer la variable resultat = 3,14 * rayon * rayon
- afficher dans la console la phrase suivante :
l'aire d'un cercle de rayon rayon a une aire de resultat

4/ exécuter la fonction aireCercle pour le rayon
44,5
70,43
"""