# épisode précédent

# opération sur les chiffres 

```py
a = 1
b = 2

a + b
a - b
a * b
a / b
a ** b
a % b  # modulo reste entier
a // b # partie entier du la division

# opérateur unaire
c = 10 
c = c + 1
c += 1

d = 30
d = d - 5
d -= 5
```

# opération sur les string (concaténation)

```py
prenom = "Victor"
nom = "Hugo"

# manière classique => + " "
auteur = prenom + " " + nom 

# f string
auteur = f"{prenom} {nom}"

# "".format
auteur = "{} {}".format(prenom , nom)
# en PHP sprintf()

titre = "mon premier article"
elementHtml = f"<h1>{titre}</h1>"
```

# opération sur les boolean

```py
a = 1 > 2 # False
b = 1 < 2 # True

"""
opérateur de comparaison
>
<
>=
<=
!=
==

=> n'existe pas pour faire des comparaisons
=< n'existe pas pour faire des comparaisons

opérateur de calcul boolean

and
or
not

=> voir le tableau des vérités
"""
```

# condition 

```py 
if 10 > 2 and 2 < 5 or 6 > 1 :
    print("coucou")

isAdmin = False

if isAdmin == True :
    print("bienvenue")
else:
    print("vous n'êtes pas autorisé à accéder à cette page")

# if ternaire 

print("bienvenue") if isAdmin == True else print("vous n'êtes pas autorisé à accéder à cette page")

age = 50

if age < 18 :
    print ("mineur")
elif age < 80 :
    print("majeur")
elif age < 120 :
    print ("retraité")
else :
    print("chiffre impossible")
```

# boucle

- itérer ou boucler faire loop => synonyme 