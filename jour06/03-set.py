# liste
etudiants = ["Alain", "Benjamin"]

# tuple
etudiants = ("Alain", "Benjamin")

# set 
etudiants = {"Alain", "Benjamin"}
# une variable de liste 
# utiliser des {  } à la place des [ ]

# https://openclassrooms.com/fr/courses/7527306-decouvrez-le-fonctionnement-des-algorithmes

# https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python

etudiants = {"Alain", "Pierre" , "Zorro" , "Céline"}
etudiant_php = {"Alain", "Pierre" , "Zorro"}
etudiant_judo = {"Alain", "Julien" ,"Sophie"}

# pouvez vous me donner le nom des étudiants qui ne VONT PAS au cours de PHP ??? 

# https://webdevpro.net/toutes-les-jointures-sql/

etudiant_non_php = etudiants.difference(etudiant_php)
print(etudiant_non_php)

etudiant_php_judo = etudiants.intersection(etudiant_php , etudiant_judo)
print(etudiant_php_judo)


"""
créer le fichier 04-exo.py

voici 3 set :

employees = {'Corey', 'Jim' , 'Steven' , 'April' , 'Judy' , 'Jenn' , 'John' , 'Jane'}
gym_members = {'April', 'John' , 'Corey'}
developers = {'Judy' , 'Corey' , 'Steven' , 'Jane' , 'April'}

# quels sont les employees qui sont developpers et sont inscrits au club de gym

# quels sont les employees qui ne sont ni developpers ni inscrits au club de gym

# est ce que Steven est inscrit au club de gym ?


"""