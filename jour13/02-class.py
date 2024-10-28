class Matiere :
    sujet = "Python"
    duree = 10
    unite = "jours"

    def description(self) : 
        # fonction dans une class => TOUJOURS mettre self en premier paramètre
        # j'ai suivi une formation sur Python pendant 10 jours
        print(f"j'ai suivi une formation sur {self.sujet} pendant {self.duree} {self.unite}")

# QUAND la class est finie => revenir début de ligne (enlever les identations)
# class => modèle qui permet de créer des objet 
# class permet de déclarer le contenu d'un objet 
# à partir de la class => on crée notre objet => créer une INSTANCE 

m = Matiere() # la variable m contient désormais un objet 
              # en PHP / Java / C => m = new Matiere() 

print(m.sujet) 
print(m.unite) # nom_objet.nom_cle (comme en Javascript)

m.description() # pour exécuter une méthode nom_objet.nom_method()
                # la méthode contient juste self ALORS pas besoin de mettre une valeur dans les ()