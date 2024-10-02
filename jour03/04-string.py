texte = "Bonjour"
autre_texte = "comment allez vous ??"
texte_final = "ça va !!"

# quand on a des variables qui contient chaines de caractères 
# on va pouvoir réaliser => concaténation 
# addition de texte les uns avec les autres 

# écrire la phrase "Bonjour comment allez vous ??" 
# en utilisant les variables précédentes 

# première manière de faire de la concaténation en Python
# méthode classique (dans tous les langages)
phrase = texte + " " + autre_texte 
print(phrase)

# autre manière de faire de la concaténation en Python
# méthode 2 => f string 
phrase2 = f"{texte} {autre_texte}"
print(phrase2)

# méthode 3 
phrase3 = "{} {}".format(texte , autre_texte)
print(phrase3)


"""
1 créer le fichier 05-exo.py
2 ce fichier contient trois variables
titre = "M"
prenom = "John"
nom = "Doe"

3 écrire la phrase suivante dans la console en utilisant les 3 variables de 2 manières possibles :

Je m'appelle Monsieur John Doe

"""