from tkinter import Frame

from tkinter import Frame, Label, Scale, LEFT, HORIZONTAL

class MaFenetre(Frame):

    def __init__(self, master = None) -> None:
        super(MaFenetre, self).__init__(master, width=320, height=240)
        self.master.title("Mon application")
        self.pack()

    def initWidgets(self):
        self.FTexte = Label(self, text="F")
        self.FCurseur = Scale(self , orient= HORIZONTAL , from_= -148, to =212 , command=self.convertirFEnC)

        self.CTexte = Label(self, text="C")
        self.CCurseur = Scale(self , orient= HORIZONTAL , from_= -100, to =100, command=self.convertirCEnF)

        for widget in [self.CTexte, self.CCurseur , self.FTexte, self.FCurseur ]:
            widget.pack(side=LEFT)

    def convertirCEnF(self, valeur):
        C = float(valeur)
        F = C * 9/5 +32
        self.FCurseur.set(F)

    def convertirFEnC(self , valeur):
        F = float(valeur)
        C = ( F -32 ) * 5/9
        self.CCurseur.set(C)

ma_fenetre = MaFenetre()
ma_fenetre.initWidgets()
ma_fenetre.mainloop()