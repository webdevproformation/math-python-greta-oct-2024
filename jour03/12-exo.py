# variable
compteur = 30
titre = "lorem ipsum avec beaucoup beaucoup beauoupc de texte"
contenu = "lorem ipsum ...."
# condition 
paragrapheFinal = ""
if compteur == 0 :
    paragrapheFinal = "<p>aucun like</p>"
else :
    paragrapheFinal = f"<p>cet article a {compteur} likes</p>"
# concaténation 
resultatConcatenation = f"""
<div>
    <h1 class="title">{titre}</h1>
    <p>{contenu}</p>
    { paragrapheFinal }
</div>
"""
# afficher le resultat dans la console 
print(resultatConcatenation)


# exemple 1
prenom = "Victor"
nom =  "Hugo"

prenom + nom    # méthode 1
f"{prenom}{nom}" # méthode 2
"{}{}".format(prenom , nom) # méthode 3