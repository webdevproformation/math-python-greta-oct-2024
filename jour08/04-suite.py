# installer le module => requests
# https://pypi.org/project/requests/

# pip install requests
# sudo apt install python3-requests
# python3 -3.12 -m pip requests

import requests
from bs4 import BeautifulSoup 
import pprint

reponse = requests.get("https://webdevpro.net/")
## print(reponse.content)

soup = BeautifulSoup(reponse.content,features="html.parser")

titres = soup.findAll("h2")
dates = soup.findAll("time")

for date, titre in zip(dates,titres):
    txt_date = date.text
    text_titre = titre.text
    print(f"publié le {txt_date} - {text_titre}")
    

