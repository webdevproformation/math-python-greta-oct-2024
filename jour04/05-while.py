# autre boucle 

for i in range(0,10):
    print(i)

i = 0  # minimum
while i < 10: # maximum (condition de sortie)
    print(i)
    i += 1    # augmentation 

reponse = input("comment allez aujourd'hui ????")
print(reponse)

"""
cas pratique 

créer le fichier 06-exo.py

ce script vous demande de saisir un chiffre entre 0 et 10 ?

si vous avez saisit une valeur correcte => le terminal affiche le texte merci
si vous avez saisit une valeur incorrecte => le terminal vous dit que ce n'est pas correct ET il vous repose de saisir un chiffre correct 
TANT QUE vous n'avez pas saisit de chiffre correct vous êtes bloqué dans la boucle !

"""
