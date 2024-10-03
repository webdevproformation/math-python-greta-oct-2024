# il est possible d'ajouter après les paramètres de la fonction une annotation
# rayon : bool
# rayon : str
# rayon : float
# rayon : int 
# Documentation du code 


def aireCercle (rayon : float ) -> None:
    """
    cette fonction permet de calculer l'aire d'un cercle  
    rayon = doit être un nombre supérieur à 0 
    """
    resultat = 3.14 * rayon ** 2
    """
    calcul du resultat
    """
    print(f"un cercle de rayon {rayon} a une aire de {int(resultat)}")


print(help(range))

# annotation !!!!!!!!!

"""
cas pratique :

créer le 13-exo.py 
1 dans ce fichier vous avez une fonction qui permet de convertif les temparatures en degrès celsus EN degrès farenheite 

exécuter votre fonction avec la valeur 

celsus   Farenheite
0      => 32
40     => 104
60     =>  140

https://formation.webdevpro.net/python-initiation/img/04/javascript-centigrade-to-fahrenheit-exercise-11.png

"""