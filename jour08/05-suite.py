import requests
from bs4 import BeautifulSoup 
import pprint

reponse = requests.get("https://fr.yahoo.com/")
## print(reponse.content)

soup = BeautifulSoup(reponse.content,features="html.parser")

titres = soup.findAll("h3", {"class": "stream-item-title"})
categories = soup.findAll("strong" , {"data-test-locator" : "stream-item-category-label"})
texte = ""
for categorie, titre in zip(categories,titres):
    txt_categorie = categorie.text
    text_titre = titre.text
    texte += f"catégorie : {txt_categorie} - titre : {text_titre}\n"

# créer un fichier sauvegarde.txt
with open("jour08/sauvegarde.txt", "w",encoding="utf-8") as fichier:
    fichier.write(texte)