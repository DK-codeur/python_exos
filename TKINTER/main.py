# encodage
# -*- coding:Utf-8 -*-

# import de la librairie tkinter
from tkinter import *
from tkinter.messagebox import *

monapp = Tk()

# monapp conf
monapp.title("DK PYapp")
monapp.geometry("1200x700")
monapp["bg"] = "grey"
monapp.iconbitmap("icon.ico")

hello = Label(monapp, text="Hello i'm DK-codeur, there my first python program !")
hello.pack()

# labelFrame
titreCadre = LabelFrame(monapp, text='mon super titre', padx="20", pady=40, )
titreCadre.pack(fill="both", expand="no")

Label(titreCadre, text="text dans mon cadre").pack()

# button quit
quitter = Button(monapp, text="fermer cette fenetre", fg="white", bg="blue", command=monapp.quit)
quitter.pack()

quitter2 = Button(monapp, text="autre bouton pour fermer", relief="sunken", command=monapp.quit).pack()

# un label avec bg
montext = Label(monapp, text="un texte avec un background", bg="#40E0D0")
montext.pack()

# les input
moninput = StringVar()
moninput.set("texte par default")
entrer = Entry(monapp, textvariable=moninput, width=70).pack()

# les case a cocher
myCheck1 = Checkbutton(monapp, text="premier element a cocher").pack()
myCheck1 = Checkbutton(monapp, text="deuxieme element a cocher").pack()

# les radio
# resutl = StringVar()
# myRadio1 = Radiobutton(monapp, text="oange", textvariable=resutl, value=1).pack()
# myRadio2 = Radiobutton(monapp, text="mandarine", textvariable=resutl, value=2).pack()

# les listes
myList = Listbox(monapp)
myList.insert(1, "python")
myList.insert(2, "php")
myList.insert(3, "laravel")

myList.pack()

# les scroll
scrolle = DoubleVar()
myscroll = Scale(monapp, variable=scrolle, orient="horizontal", from_=0, to=100, resolution=1, tickinterval=5,
                 length=900, label="scale from 0 to 100")
myscroll.pack()

# frame
frame1 = Frame(monapp, bg="green", borderwidth=1)
frame1.pack(padx=15, pady=10)
Label(frame1, text="ici zone de text").pack(padx=4, pady=2)

monapp.mainloop()
