"""
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
min => 2
max => 7 = 6 + 1
augmentation de +1
"""
for i in range (2,7) :
    # 4 x 2 = 8
    # 4 x 3 = 12
    # 4 x 4 = 16
    # 4 x i = i * 4
    solution = f"4 x {i} = {i * 4}"
    print(solution)

for i in range (8,25, 4) :
    # 4 x 2 = 8
    # 4 x 3 = 12
    # 4 x 4 = 16
    # 4 x i = i 
    solution = f"4 x {int(i / 4)} = {i}"
    print(solution)

for i in range (2,7) :
    # 4 x 2 = 8
    # 4 x 3 = 12
    # 4 x 4 = 16
    # 4 x i = i * 4
    # TypeError: can only concatenate str (not "int") to str
    solution = "4 x " + str(i) + " = " + str(i * 4)
    print(solution)

for i in range (2,7) :
    # 4 x 2 = 8
    # 4 x 3 = 12
    # 4 x 4 = 16
    # 4 x i = i * 4
    # TypeError: can only concatenate str (not "int") to str
    print("4 x" , str(i) , "=" , str(i * 4))


"""
Créer un nouveau fichier 02-exo.py

en utilisant une boucle, afficher dans la console les string suivants :
5 x 10 = 50
5 x 8 = 40
5 x 6 = 30
5 x 4 = 20
5 x 2 = 10
5 x 0 = 0
5 x -2 = -10
5 x -4 = -20
"""