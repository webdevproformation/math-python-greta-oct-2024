"""
s'appelle formation
il contient les valeurs suivantes :
    nom => DWWM
    duree = 6
    unite => mois
    matieres une liste [ Python; js PHP MySQL ]
"""

formation = {
    "nom" : "DWWM",
    "duree" : 6 ,
    "unite" : "mois" ,
    "matieres" : [ "Python", "js", "PHP" ,"MySQL" ]
}

"""
-  je suis une formation en DWWM dans laquelle je vais suivre du PHP et du MySQL

- La formation dure 6 mois 

- il y a 4 matières principales
"""
# -  je suis une formation en DWWM dans laquelle je vais suivre du PHP et du MySQL
solution1 = f"je suis une formation en {formation["nom"]} dans laquelle je vais suivre du {formation["matieres"][2]} et du {formation["matieres"][3]}"
print(solution1)

solution2 = f"je suis une formation en {formation.get("nom")} dans laquelle je vais suivre du {formation.get("matieres")[2]} et du {formation.get("matieres")[3]}"
print(solution2)

# - La formation dure 6 mois 
solution3 = f"La formation dure {formation["duree"]} {formation["unite"]} "
print(solution3)

solution4 = f"La formation dure {formation.get("duree")} {formation.get("unite")} "
print(solution4)

# - il y a 4 matières principales
solution5 = f"il y a {len( formation["matieres"] )} matières principales"
print(solution5)


"""
1/ créer le fichier  08-exo.py

2/ le fichier contient une variable de type dictionnaire :
- le nom de la variable est matiere
- cette variable contient les valeurs suivantes :
  - domaine => liste de  HTML et CSS
  - duree => 2
  - montant => 5
  - unite qui contient une liste => semaines et jours
  - 

3/ afficher dans la console la phrase suivante 
je suis une formation en HTML d'une durée de 5 jours

4/ afficher dans la console la phrase suivante 
il m'a fallu 2 semaines pour comprendre en détail CSS

5/ afficher dans la console la phrase suivante
2 x 5 = 10

6/ afficher dans la console la phrase suivante
HTML et CSS sont des langages clients
"""

toto = {
    "domaine" : ["tutu", "titi"]
}

# "je fais tutu"
solution = f"je fais {toto['domaine'][0]}"
print(solution)
