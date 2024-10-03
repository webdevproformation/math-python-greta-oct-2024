class Maison :
    def __init__(self):
        self.pieces = [Piece(name) for name in ["cuisine", "salon", "chambre"] ]

    def __del__ (self):
        print("maison detruite")

class Piece :
    def __init__(self, name):
        self.name = name
    def __del__ (self):
        print(f"{self.name} detruite")

maison = Maison()
cuisine = maison.pieces[0] 
del maison

print(cuisine)
