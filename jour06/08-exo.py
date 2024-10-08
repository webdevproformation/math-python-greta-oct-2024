matieres = {
    "domaine" : ["HTML" , "CSS" ],
    "duree" : 2,
    "montant" : 5 ,
    "unite" : ["semaines" , "jours"]
}

# je suis une formation en HTML d'une durée de 5 jours
s1 = f"je suis une formation en {matieres['domaine'][0]} d'une durée de {matieres['montant']} {matieres['unite'][1]}"
print(s1)

# il m'a fallu 2 semaines pour comprendre en détail CSS
s2 = f"il m'a fallu {matieres['duree']} {matieres['unite'][0]} pour comprendre en détail {matieres['domaine'][1]}"
print(s2)

# 2 x 5 = 10
s3 = f"{matieres['duree']} x {matieres['montant']} = {matieres['duree'] * matieres['montant']}"
print(s3)

# HTML et CSS sont des langages clients
s4 = f"{matieres['domaine'][0]} et {matieres['domaine'][1]} sont des langages clients"
print(s4)