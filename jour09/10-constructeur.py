""" class Personne: 
    nom = "Jéremy"
    _age = 30
    __competences = ["html" , "php" , "javascript"] """

# lorsque je crée un personne personne = Personne()
# je voudrai pouvoir définir son nom / age / competence de manière à les distinguer
# pour pouvoir réaliser cette distinction => méthode magique 
# méthode qui ont un nom spécial => bien respecter les noms à utiliser 
# fonction qui ont un sens particulier pour le langage Python 

class Personne :
    def __init__(self, nom, age , competences): 
        # fonction magique 
        # constructeur 
        self.nom = nom
        self._age = age
        self.__competences = competences

personne1 = Personne("Alain" , 22 , ["php","css"])

print(personne1.nom)
print(personne1._age)
print(personne1._Personne__competences)

personne2 = Personne("Zorro" , 44 , ["html"])

print(personne2.nom)
print(personne2._age)
print(personne2._Personne__competences)

# via le constructeur il va être possible de créer des objets ayant les mêmes propriétés MAIS dont les valeurs sont différentes  