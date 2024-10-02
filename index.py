# coding: utf-8

import cgi 

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

print(form.getvalue("name"))

auteur = "je change le texte"
dt_creation = "01/01/2024"
description = "je suis un texte de description"

html = f"""<!DOCTYPE html>
<head>
    <title>Mon programme</title>
</head>
<body>
    <h1>{auteur} <small>{dt_creation}</small></h1>
    <p>{description}</p>
    <form action="/index.py" method="post">
        <input type="text" name="name" value="Votre nom" />
        <input type="submit" name="send" value="Envoyer information au serveur">
    </form> 
</body>
</html>
"""

print(html)