"""
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

for i in range (1,101):
    if i % 3 == 0 and i % 5 == 0 :
        print("fizzbuzz") 
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0 :
        print("buzz")
    else:
        print(i)

"""
...x...
"""

for j in range(0,4):
    ligne = ""
    for i in range(0, 7):
        if i >= 3 -j and i <= 3 +j :
            ligne += "x"
        else :
            ligne += "."
    print (ligne)