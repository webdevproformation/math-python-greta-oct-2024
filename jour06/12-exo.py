etudiant = {
    "q1" : 10,
    "q2" : 13,
    "q3" : 9,
    "q4" : 15
}

total = 0
for i in etudiant.values():
    total += i 

moyenne = total / len(etudiant)

print(moyenne) # 11.75