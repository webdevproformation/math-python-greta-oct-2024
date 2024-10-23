class Meuble:
    _nom = "table"
    _prix = 0

    @property # décorateur
    def nom(self): # méthode getter
        print (self._nom)
    
    @nom.setter # décorateur
    def nom(self, value): # méthode setter
        self._nom = value

    @property
    def prix(self):
        print (self._prix)
    
    @prix.setter
    def prix(self, value):
        self._prix = value

meuble = Meuble()
meuble.nom            # déclencher le getter
meuble.nom = "chaise" # exécuter le setter 
meuble.nom            # déclencher le getter