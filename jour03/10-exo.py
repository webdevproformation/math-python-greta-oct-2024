a = 30
b = 40
c = 12 * 4 < 44/3

#1/ vérifier est ce que a supérieur ou égal à b
#si c'est vrai écrire dans la console "verif 1 ok"

verif1 = a >= b
       # 30 >= 40 
        #False
if verif1 :
    print("verif 1 ok") # ne doit pas s'afficher


#2/ vérifier est ce que c supérieur ou égal à b
#si c'est vrai écrire dans la console "verif 2 ok"

verif2 = c >= b
""" c = 12 * 4 < 44/3 
c = 48 < 14.67 
c = False  

b = 40

Ensuite 

c >= b
False >= 40
0     >= 40
False 
"""
if verif2 :
    print("verif 2 ok") # ne doit pas s'afficher

#3/vérifier est ce que c supérieur ou égal à b OU a inférieur à b
#si c'est vrai écrire dans la console "verif 3 ok"

verif3 = c >= b or a < b
""" False >= 40 or 30 < 40 
      0 >= 40   or  True 
     True
"""
if verif3 :
    print("verif 3 ok") # ne doit s'afficher


"""
```py
# créer un nouveau fichier 11-exo.py contenant une variable ville
# initialiser la variable ville = "Marseille"

# si ville a pour valeur Paris 
# alors afficher dans la console "vous habitez à Paris"

# si ville a pour valeur Boulogne ou Clamart ou Montrouge 
# alors afficher dans la console "vous habitez dans le 92"

# si ville a pour valeur Saint-Denis ou Aubervilliers ou Pantin
#  alors afficher dans la console "vous habitez dans le 93"

# sinon
# afficher dans la console "vous habitez hors d'Ile de France"
```
"""