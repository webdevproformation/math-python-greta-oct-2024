def voyelle (mot) :
    compteur = 0
    index_premier_lettre = 0
    nb_lettre_mot = len(mot)

    for i in range (index_premier_lettre , nb_lettre_mot):
        lettre = mot[i]
        if lettre == "a" or lettre == "e"  or lettre == "i" or lettre == "o" or lettre == "u"  or lettre == "y":
            compteur += 1
    print(compteur)

voyelle ("bonjour") # 3

def voyelle2 (mot) :
    compteur = 0 
    mot_liste = list(mot) # ['b', 'o', 'n', 'j', 'o', 'u', 'r']
    # print(mot_liste)
    for lettre in mot_liste :
        if lettre in ["a", "e", "i","u","o","y"]:
            compteur += 1
    print(compteur)

voyelle2 ("bonjour")

"""
Créer un nouveau fichier 07-exo.py

créer une fonction dont le nom est palindrome et prenant un paramètre nommé mot

- cette fonction doit retourner True si mot est un palindrome 
- si mot n'est pas un palydrome alors la fonction retourne False

exemples :
print(palindrome("lol")) # => True
print(palindrome("kayak")) # => True
print(palindrome("laos")) # => False
print(palindrome("table")) # => False

"""