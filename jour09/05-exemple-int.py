a = 2

print(a.is_integer()) # True 

# variable . quelquechose 
# variable est un OBJET 

# texte

texte = "bonjour"

texte.capitalize() # méthode ajouter AUTOMATIQUEMENT par Python 
print(texte.capitalize()) # Bonjour
print(texte.upper()) # BONJOUR
print(len(texte)) # 7
print(texte.__len__()) # 7 

# liste 

fleurs = ["rose"]

#CRUD 
fleurs.append("tulipe") # append méthode du type List 
fleurs.remove("rose") # remove méthode du type List
print(len(fleurs))  # compter le nombre d'élément d'une liste 
print(fleurs.__len__()) # il est possible d'utiliser la méthode __len__()

# même les fonctions sont des objets en Python
def calcul():
    pass 

calcul.__dict__()

# str float int complexe tuple list dictionnary set => type par défaut 
# def 

# comment pouvons nous créer nos propres types
# vehicule 
# le véhicule va avoir plusieurs caracteristiques 
# nom  => texte (utiliser le type par défaut string)
# prix_achat => chiffre entier le type par défaut int
# en_circulation => boolean => type par défaut 

vehicule_nom = "Peugeot 206"
vehicule_prix = 10_000
vehicule_en_circulation = False 

# 3 variables => pour 1 seul concept géré dans votre logiciel 

# au lieu d'avoir 3 variables => 1 seule qui regroupe ces 3 valeurs 

# solution 1 dictionnaire

vehicule = {
    "nom" : "Peugeot 206",
    "prix" : 10_000,
    "en_circulation" : False
}

def mise_en_circulation(v):
    v["en_circulation"] = True

def prixTTC(v):
    print(v["prix"]* 1.2)

# => regrouper un dictionnaire ET des fonctions => class / objet 