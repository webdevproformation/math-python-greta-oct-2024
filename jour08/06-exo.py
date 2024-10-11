import requests
from bs4 import BeautifulSoup 
import pprint

reponse = requests.get("https://www.imdb.com/what-to-watch/fan-favorites/?ref_=watch_tpks_tab")
print(reponse.content)
## <html>\r\n<head><title>403 Forbidden</title></head>\r\n<body>\r\n<center><h1>403 Forbidden</h1></center>\r\n</body>\r\n</html>

soup = BeautifulSoup(reponse.content,features="html.parser")

notes = soup.findAll("span", {"class": "ipc-rating-star--rating"})
titres = soup.findAll("span" , {"data-testid" : "title"})

print(notes)
print(titres)


texte = ""
for note, titre in zip(notes,titres):
    txt_note = note.text
    text_titre = titre.text
    texte += f"note : {txt_note} - titre : {text_titre}\n"

# créer un fichier sauvegarde.txt
with open("jour08/favoris.txt", "w",encoding="utf-8") as fichier:
    fichier.write(texte)


"""
cas pratique

réaliser un web scrapping sur la page suivante : https://www.scrapethissite.com/pages/simple/

récupérer le nom du pays et le nom de la capitale

sauvegarder le résultat dans un fichier favoris.txt
"""