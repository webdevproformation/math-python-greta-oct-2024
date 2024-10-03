condition = True 

while condition == True:
    reponse = input("saisir un nombre entre 0 et 10 : ")
    try :
        chiffre = int(reponse)
        if chiffre >= 0 and chiffre <=10 :
            print("bravo")
            condition = False
    except ValueError :
        print("attention il faut saisir un chiffre !!")