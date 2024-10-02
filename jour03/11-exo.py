ville = "Marseille"

if ville == "Paris":
    print("vous habitez à Paris")
elif ville == "Boulogne" or ville == "Clamart" or ville == "Montrouge":
    print("vous habitez dans le 92")
elif ville == "Saint-Denis" or ville == "Aubervilliers" or ville == "Pantin" :
    print("vous habitez dans le 93")
else :
    print("vous habitez hors d'Ile de France")

"""
```py
Créer le nouveau fichier 12-exo.py

1 ce fichier contient 3 variables :
premier variable compteur = 30
deuxième variable titre = "titre de l'article"
troisième variable contenu = "lorem ipsum ...."

2 afficher dans le console le texte suivant en utilisant les variables précédentes :
<div>
  <h1 class="title">titre de l'article</h1>
  <p>lorem ipsum .... </p>

  si la variable compteur = 0 alors  
    <p> aucun like</p>
    sinon 
    <p> cet article a 30 likes</p>
</div>
```
"""