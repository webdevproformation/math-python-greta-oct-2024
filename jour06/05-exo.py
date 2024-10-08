def anagramme( mot1 , mot2 ):
    mot1_tri = sorted(mot1)  # sorted('finder') => 'd', 'e', 'f', 'i', 'n', 'r'   
    mot2_tri = sorted(mot2)  # sorted('friend') => 'd', 'e', 'f', 'i', 'n', 'r'
    if mot1_tri == mot2_tri:
        print(True)
    else :
        print(False)

anagramme('finder', 'friend')  
anagramme('hello', 'bye')
anagramme('mary', 'army') 
anagramme('nectar', 'carnet') 

# fonction QUASI correcte (mais pas correct )
def anagramme( mot1 , mot2 ):
    # vérifier SI mot1 et mot2 ont le même nombre de lettre 
    if(len(mot1) !=  len(mot2)) :
        print(False)
        return 
    mot1_set = set(mot1) # set("hello") => {"h","e","l", "o"}
    mot2_set = set(mot2)
    resultat = mot1_set.difference(mot2_set)
    if len(resultat) == 0:
        print(True)
    else:
        print(False)

# attention les set ne prennent pas de doublon 
anagramme('feff', 'fefe')  
anagramme('finder', 'friend')  
anagramme('hello', 'bye')
anagramme('mary', 'army') 
anagramme('nectar', 'carnet') 

set1 = { 1, 2 , 3 }
set2 = { 3, 4 , 5 }
print(set1.difference(set2))
print(set1.symmetric_difference(set2))