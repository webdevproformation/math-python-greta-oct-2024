"""
5 x 10 = 50
5 x 8 = 40
5 x 6 = 30
5 x 4 = 20
5 x 2 = 10
5 x 0 = 0
5 x -2 = -10
5 x -4 = -20
depart 10
fin   -4 -1 = -5
pas diminution -2
"""

for i in range(10, -5,-2):
    # 5 x 10 = 50
    # 5 x 8 = 40
    # 5 x i = i * 5
    solution = f"5 x {i} = {i * 5}"
    print(solution)

"""
créer le fichier 03-exo.py
boucle qui contient une condition

boucle 1 => 100 augmente de +1
    si i multiple de 3 => fizz
    si i multiple de 5 => buzz
    si i multiple de 5 et 3 => fizzbuzz
    sinon écrire le chiffre

1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14 
fizzbuzz
...
buzz
"""