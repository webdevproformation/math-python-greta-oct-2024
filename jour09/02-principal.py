# installer le module requests 
# et je veux l'installer QUE pour ce projet 
# donc je souhaite l'installer en Local 

# Python => Virtual Environnement => Environnement Virtuel 
# créer un dossier "...." dans ce dossier on va télécharger les dépendances UNIQUEMENT POUR CE PROJET 

"""
# étant donné QUE l'on est sur le python par défaut 
# afficher l'ensemble des modules globaux 
pip list
"""

"""
# créer un environnement virtuel Windows
python -m venv .env
# python interpréteur de code 
# -m venv => créer un environnement virtuel (dossier)
# .env nom du dossier 

# créer un environnement virtuel Linux
sudo apt install python3.12-venv
python3 -m venv .env
"""


## une fois créé => activer 

"""
# créer un environnement virtuel Windows

.env\Scripts\activate.bat
deactivate 

# créer un environnement virtuel Linux

source .env/bin/activate 
"""

"""
installer une librairie depuis internet => requests 

pip install requests 
"""

import requests 

reponse = requests.get("https://lemonde.fr")
print(reponse)

# url : https://formation.webdevpro.net/python-poo/
# login : python
# password : poo