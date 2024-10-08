employees = {'Corey', 'Jim' , 'Steven' , 'April' , 'Judy' , 'Jenn' , 'John' , 'Jane'}
gym_members = {'April', 'John' , 'Corey'}
developers = {'Judy' , 'Corey' , 'Steven' , 'Jane' , 'April'}

# quels sont les employees qui sont developpers et sont inscrits au club de gym
# il faut que les noms soient présents dans les 3 set

employees_dev_gym = employees.intersection(gym_members , developers)
print(employees_dev_gym) # {'Corey', 'April'}

# quels sont les employees qui ne sont ni developpers ni inscrits au club de gym
# les employées qui sont uniquement dans le set employee et pas dans les autres set 

employees_notdev_notgym = employees.difference(gym_members , developers)
print(employees_notdev_notgym)

# est ce que Steven est inscrit au club de gym ?

is_steven_gym = "Steven" in gym_members
print(is_steven_gym) # False

"""

Créer le fichier 05-exo.py

- écrire une fonction nommée anagramme qui vérifie si deux chaînes fournies sont des anagrammes l'une de l'autre; 

Voici quelques exemples :
anagramme('finder', 'friend')  => True
anagramme('hello', 'bye') => False
anagramme('mary', 'army') => True
anagramme('nectar', 'carnet') => True

"""