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