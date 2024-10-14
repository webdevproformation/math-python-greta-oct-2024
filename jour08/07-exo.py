from requests import get
from bs4 import BeautifulSoup

reponse = get("https://www.scrapethissite.com/pages/simple/")

soup = BeautifulSoup(reponse.content, features="html.parser")

pays = soup.findAll("h3",{"class":"country-name"})
capitals = soup.findAll("span",{"class":"country-capital"})

# compréhension de list 
texte = [ f"super - pays : {p.text.strip()} - capital : {c.text.strip()}\n" for p, c in zip(pays , capitals) ]

with open("favoris.txt", "w" , encoding="utf8") as fichier:
    fichier.write("".join(texte))