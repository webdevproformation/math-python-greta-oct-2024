class Exo :
    def __init__(self, p_duree, p_enonce , p_note) :
        self.enonce = p_enonce
        self.note = p_note
        self.duree = p_duree

exo1 = Exo(5 , "créer une class" , 3)
# Exo(5 , "créer une class" , 3) de manière automatique Python va rechercher SI il y a une méthode __init__ dans la class 
# si elle existe bien il l'exécute 
exo2 = Exo(4 , "instancier une class" , 2)

print(exo1.note) # 3
print(exo2.note) # 2

"""
créer le fichier 12-exo.py

# class Article
# 4 propriétés publiques
# auteur = string
# contenu = string
# like = chiffre entier
# titre = string 

# cette class dispose d'une fonction constructrice __init__() ayant autant de paramètre que l'on a de propriétés dans la class  + self

# va initialiser les propriétés de la class

# ajouter une méthode pour cette class => render 
# print concatenation via les  propriétés de la class du texte suivant
/*
<h1>titre</h1>
<p>contenu</p>
<ul>
    <li>écrit par : auteur</li>
    <li>like : like </li>
</ul>
*/
# générer deux articles => 
# article1  => valeurs des paramètres = "moi" / "lorem ipsum" / 10 / "mon premier article" 
# article2  => valeurs des paramètres = "un étudiants" / "exemple article" / 15 / "utiliser une class au quotidien" 

exécuter la méthode render pour l'article1 et l'article2
"""