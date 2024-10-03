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
