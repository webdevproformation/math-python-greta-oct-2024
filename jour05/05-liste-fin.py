# update => mis à jour
# modifier la valeur 1 par la valeur 10
liste = [1,2, 3, "a", "b", "c", "d"]
#        0,1, 2,  3 ,

liste[0] = 10 

print(liste) # [10, 2, 3, 'a', 'b', 'c', 'd']

# delete => supprimer des valeurs dans une liste existante

# pour supprimer la lettre "a" juste lui dire 
liste.remove("a")
print(liste)

# vide intégralement les valeurs de la list
liste.clear()
print(liste) # []


# opération en +

liste = [10, 20 , 5 , 30]
liste.sort()
print(liste)
liste.sort(reverse=True)
print(liste)

# string => "bonjour" => prendre les lettres et les mettre dans l'ordre 

texte = "bonjour"
tableau = list(texte) # list() une fonction native (builtins) de Python comme range()
print(tableau) # ['b', 'o', 'n', 'j', 'o', 'u', 'r']
tableau.sort()
print(tableau)
print ("".join(tableau)) # bjnooru


# faire une boucle / parcourir une liste 

for i in range(0,10):
    print(i)
    # 0 1 2 3 4 5 6 7 8 9 

jours = ["lundi", "mardi", "mercredi", "jeudi"]

for i in jours:
    print(i)
    #  "lundi" "mardi" "mercredi" "jeudi"

"""
Créer un nouveau fichier 06-exo.py

- créer une fonction nommée voyelle et qui prend pour paramètre une chaine de caractère
- cette fonction retourne le nombre de voyelles contenu dans la chaine de caractère donnée en argument

exemples :

voyelle('hello') // => 2
voyelle('why') // => 1
"""