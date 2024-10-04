def palindrome (mot):

    # je veux générer le mot avec les lettres inversées
    # transforme mon mot en liste 
    mot_list = list(mot)
    # mettre les lettres de la liste du dernier au premier
    mot_list.reverse()
    # prendre le tableau inversé et mettre chaque valeur comme lettre d'une string
    mot_inverse = "".join(mot_list)
    # je compare mot avec  mot_inverse
    print(mot == mot_inverse)

palindrome("lol")
palindrome("kayak")
palindrome("laos")
palindrome("Table")
