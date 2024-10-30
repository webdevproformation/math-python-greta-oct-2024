from collections import Counter

# LinkedList
# Queue Stack 

# je veux savoir combien de lettre j'ai de fois la lettre o dans le texte
# bonjour les amigos 

texte = "bonjour les amigos"

compte1 = Counter(texte)
print(compte1)
print(compte1.get("o"))

liste = [1,2,3,1,3,4,2,2]
compte = Counter(liste)
print(compte) # Counter({2: 3, 1: 2, 3: 2, 4: 1})

# utilisable sur dictionnaire // set // tuple 

texte2 = "lorem ipsum" 
compte2 = Counter(texte2)
compte3 = compte1 + compte2 # __add__


# https://apprendrepython.com/compter-les-elements-dune-liste-avec-collections-counter-en-python/


texte2 = "bonjour les amigos"

print(texte2.count("o"))