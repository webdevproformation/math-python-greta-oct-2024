qcm = {
    "question1" : {
        "question" : "comment écrire une variable",
        "reponses" : ["A", "B", "C", "D"],
        "solution" : ["A","D"]
    },
    "question2" : {
        "question" : "comment écrire une fonction",
        "reponses" : ["A", "B", "C", "D"],
        "solution" : ["A","B"]
    }
}

# pour la question1 les bonnes réponses sont A et D
s1 = f"pour la question1 les bonnes réponses sont {qcm["question1"]["solution"][0]} et {qcm["question1"]["solution"][1]}"
print(s1)

s2 = f"pour la question1 les bonnes réponses sont {qcm.get("question1").get("solution")[0]} et {qcm.get("question1").get("solution")[1]}"
print(s2)

# update une valeur pour une clé existante

qcm["question2"]["question"] = "comment écrire une fonction avec des arguments ???"
print(qcm)

# modifier la réponse pour la question 2 
# Bonus ! 
qcm.update({"question2" :{ **qcm["question2"] , "solution" : ["C"] }}) 
print(qcm)