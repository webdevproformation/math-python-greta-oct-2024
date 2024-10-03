import re

condition = True 

while condition == True:
    reponse = input("saisir un nombre de 4 caractères : ")

    if re.search( "^[0-9]{4}$" , reponse) :
        print("bravo")
        condition = False