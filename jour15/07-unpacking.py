a = 10
b = 40 

print(a,b)
# (10,40)

# tuple unpacking 

(a,b) = (10,40)
print(a,b)

a,b = 10 , 40
print(a,b)

# variable du tuple unpacking AVEC LISTE 

T = [2,4,5,6,1]

T[0], T[3] = T[2], T[4]
# T[0], T[3] = 5, 1

# [5,4,5,1,1]
print(T)

for i in range(2): # [0,1]
    T[i], T[T[i -1]] = T[i], T[T[i -1]]


# en Python parenthèse ()
def f():
    pass 

f()

tupl = (1,2)

class A:
    def __init__(self, x):
        self.x = x

a = A(1)

tuple2 = (1,) # tuple Avec 1 seul élément
pas_un_tuple = (1) # chiffre !!! 

tuple_vide = ()
tuple_vide = tuple()