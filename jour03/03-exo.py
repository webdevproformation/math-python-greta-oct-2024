a = 12
b = 0
c = -2.5

print(a / c)        # -4.8
print(a * c + a)    # -18.0
print(a * (c + a))  # 114.0
# solution 1
# print(a / b)

# solution 2 
try:
    print(a / b) 
except ZeroDivisionError:
    print("attention division par 0")

# solution 2 : entourer la division par un try except
# si la division entraine une erreur de type ZeroDivisionError
# affiche le texte "attention division par 0" au lieu d'afficher le message d'erreur par défaut de Python 

"""
12 / 0 => infini / impossible
Traceback (most recent call last):
  File "c:\\Users\\harri\\Desktop\\math\\jour03\\03-exo.py", line 8, in <module>
    print(a / b)
          ~~^~~
ZeroDivisionError: division by zero
erreur => python STOP l'exécution !!! 
solution 1 => bloquer l'instruction en la commentant 
"""

#print(c / b)
try:
    print(c / b)
except ZeroDivisionError:
    print("attention division par 0")

