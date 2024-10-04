"""
# dans ce fichier vous devez créer une fonction qui s'appelle verif qui verifie si un mot 
# se finit par s ou x 
# et commence par a ou b 

# créer le script qui contient cette fonction

# vous devez verifier que la retourne True si
# verif("abeilles") => True
# verif("abeille") => False
# verif("bijoux") => True
# verif("bijou") => False
"""

def verif ( mot ): 
    premier_lettre_mot = mot[0]
    nb_lettre_mot = len(mot)
    dernier_lettre_mot = mot[nb_lettre_mot - 1]

    if (premier_lettre_mot == "a" or premier_lettre_mot == "b") and (dernier_lettre_mot == "x" or dernier_lettre_mot == "s") :
        print(True)
    else:
        print(False)

verif("abeilles")
verif("abeille") 
verif("bijoux") 
verif("bijou") 

reponse = input("saisir un mot : ")
verif(reponse) 