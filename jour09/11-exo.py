class Exo :
    def __init__(self, p_duree, p_enonce , p_note) :
        self.enonce = p_enonce
        self.note = p_note
        self.duree = p_duree

exo1 = Exo(5 , "créer une class" , 3)
exo2 = Exo(4 , "instancier une class" , 2)

print(exo1.note) # 3
print(exo2.note) # 2