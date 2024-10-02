nombre_like = 10

if nombre_like > 0 :
    print(f"vous avez {nombre_like} likes")
else :
    print("vous avez aucun like")

# dans ce cas de figure si on a un if 
# qui a un seul ligne 
# puis un else
# puis une seule ligne 

# il existe une autre manière de l'écrire => if ternaire 

print(f"vous avez {nombre_like} likes") if nombre_like > 0 else print("vous avez aucun like")

# if ternaire !!! et il s'écrit en 1 SEULE LIGNE 