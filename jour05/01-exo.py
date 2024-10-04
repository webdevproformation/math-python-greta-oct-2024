"""
- la fonction s'appelle isVoyelle
- elle a un paramètre qui est une chaine de caractère 
- cette fonction contient plusieurs instructions
    - première instruction qui parcours chaque lettre du mot (paramètre)
    - deuxieme block si la lettre == a e i o u y 
        - la fonction print True
    - sinon print False 

isVoyelle("manger") True
isVoyelle("bnp") False 
"""

# pour le paramètre choisir un mot qui n'est pas str

def isVoyelle (  mot  ):
    # je veux parcourir chaque lettre du mot 
    # la première lettre du mot => mot[0] => m
    # la deuxieme lettre du mot => mot[1] => a
    # la dernière  lettre du mot => mot[5]  => r mot[len(mot)]   len(mot) = 6
    resultat = False 
    position_premiere_lettre = 0
    nombre_lettre_mot = len(mot) # 6
    for i in range(position_premiere_lettre, nombre_lettre_mot) :
        lettre = mot[i]
        # pour chaque lettre du mot je veux savoir si c'est une voyelle 
        if lettre == "a" or lettre == "e" or lettre == "i" or lettre == "o" or lettre == "u" or lettre == "y":
            # print(True)
            resultat = True
    
    print(resultat)

#          012345    
print("exemple1")

isVoyelle("manger")

print("exemple2")

isVoyelle("bnp")


# créer le fichier 02-exo.py
# dans ce fichier vous devez créer une fonction qui s'appelle verif qui verifie si un mot 
# se finit par s ou x 
# et commence par a ou b 

# créer le script qui contient cette fonction

# vous devez verifier que la retourne True si
# verif("abeilles") => True
# verif("abeille") => False
# verif("bijoux") => True
# verif("bijou") => False
