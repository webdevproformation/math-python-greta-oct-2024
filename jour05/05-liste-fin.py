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