exo = []

exo.append("PHP")
exo.append("JS")
exo.append("CSS")

print(exo)
# ['PHP', 'JS', 'CSS']

exo.insert(1, "Git")

# 3 récupérer les deux premières valeurs de la liste

print(exo[0 : 2]) # ['PHP', 'Git']
print(exo[: 2])   # ['PHP', 'Git']

# ['PHP', "Git", 'JS', 'CSS']

# 4 récupérer les trois dernières valeurs de la liste

print(exo[1: 4]) # ['Git', 'JS', 'CSS']
print(exo[1: ]) # ['Git', 'JS', 'CSS']
print(exo[-3: ]) # ['Git', 'JS', 'CSS']

# 5 déterminer si la valeur "Symfony" est présente dans la liste ?

symfony_in_liste = "Symfony" in exo
print(symfony_in_liste) # False

# 6 récupérer l'avant dernière valeur de la liste 

print(exo[2])   # JS
print(exo[-2])  # JS


tableau = ["a", "b", "c", "d","e", "d"]
print(tableau.index("d"))