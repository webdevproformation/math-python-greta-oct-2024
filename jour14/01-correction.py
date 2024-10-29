"""
Livre
    titre, auteur, année_publication

    def __init__(self , titre, auteur, année_publication)


LivreEmpruntable(Livre)
    emprunteur, date_emprunt

    def __init__(self , titre, auteur, année_publication, emprunteur, date_emprunt)
        # initiation emprunteur, date_emprunt
        # ET initialiser les propriétés titre, auteur, année_publication VIA le constructeur de la class parent / class supérieure

"""

class Livre :
    def __init__(self, p_titre, p_auteur, p_annee_publication) :
        self.titre = p_titre
        self.auteur = p_auteur
        self.annee_publication = p_annee_publication
    
    def afficher_info(self):
        print(f"{self.p_titre} {self.auteur} publié le {self.annee_publication}")

class LivreEmpruntable(Livre):
    def __init__(self,p_titre, p_auteur, p_annee_publication ):
        # super().__init__(p_titre, p_auteur, p_annee_publication)
        Livre.__init__( self ,p_titre, p_auteur, p_annee_publication)

    def emprunter(self , nom , date):
        self.emprunteur = nom
        self.date_emprunt = date

    def retourner(self):
        self.emprunteur = None
        self.date_emprunt = None

livre = LivreEmpruntable("20000 lieux sous les mers", "Jules Vernes" ,1870)
print(vars(livre))
livre.emprunter("moi", "01/01/2024")
print(vars(livre))
livre.retourner()
print(vars(livre))
