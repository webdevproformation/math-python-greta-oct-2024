

# scope / portée des propriétés 

class Etudiant:
    __nom = "Alain"
    age = 22
    _is_admin = True
# par défaut toutes les propriétés des class en Python sont PUBLIQUES
# permet de PROTEGER LE CODE => AU SENS de BIEN L'UTILISER 

# en Python => convention de nommage
# propriete => public
# _propriete => protected
# __propriété => private 

etudiant = Etudiant()

print(etudiant.age) # 22
print(etudiant._is_admin) # True
# print(etudiant.__nom) # 'Etudiant' object has no attribute '__nom'
print(etudiant._Etudiant__nom) # Alain => name mangling (bidouiller )

"""
cas pratique 

créer le fichier 09-exo.py

# créer une class Personne
# Cette class dispose de 3 propriétés :
# => nom = "Jéremy" (publique)
# => age = 30   (protected)
# => competences = liste contenant 3 valeurs  => html / php / javascript  (private)


une fois que la class est créée

créer un objet personne et affiche dans la console les nom age et competences de cet objet 

"""