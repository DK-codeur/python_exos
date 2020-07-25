# encodage
# -*- coding:Utf-8 -*-

# import des librairie

from tkinter import *
from tkinter.messagebox import *
import webbrowser

app = Tk()

# app conf
app.title("DK PYapp")
app.geometry("600x300")
# app["bg"] = "grey"
app.iconbitmap("icon.ico")


# msg menu
def funct():
    showinfo("super app", "element clicke avec succes !")


def lien():
    webbrowser.open("http://www.google.fr")


def nvell_fen():
    nvell_fen = Toplevel(app)
    label1 = Label(nvell_fen, text="1- apprendre comment declarer les variable").pack(padx=8, pady=8)
    label2 = Label(nvell_fen, text="2- apprendre comment declarer une fonction", padx=8, pady=8).pack()

# functions msgBox
def messageYesNo():
    if askyesno("Confirmer", "Voulez vous vraiment faite ça ?"):
        showwarning("Confirmation OK", "vous avez appuyez sur oui")

    else: # for NO response
        showinfo("titre 2", "bah jai essayer quand meme")
        showerror("titre 3", "desoler je l'ai perdu")


def messageCancel():
    if askokcancel("titre 4", "veut u ecouter le msg"):
        showinfo("titre 5", "ok info recu")


def messageRetryCancel():
    if askretrycancel("titre 6", "besoin de service svp"):
        showinfo("titre 7", "cest bien de reesayer")

# menu
monMenu = Menu(app)

#menu2
menu1 = Menu(monMenu, tearoff=0)  # tearoff=0 => menu indeplacable
menu1.add_command(label="Creer project", command=funct)
menu1.add_command(label="Ouvrir projet", command=funct)
menu1.add_separator()
menu1.add_command(label="Quitter", command=app.quit)

monMenu.add_cascade(label="Fichier", menu=menu1)

# menu2
menu2 = Menu(monMenu, tearoff=1)
menu2.add_command(label="Copier", command=funct)
menu2.add_command(label="Coller", command=funct)

monMenu.add_cascade(label="Editer", menu=menu2)

# menu 3
menu3 = Menu(monMenu, tearoff=0)
menu3.add_command(label="docs", command=nvell_fen)
menu3.add_command(label="visiter url...", command=lien)

monMenu.add_cascade(label="Aide", menu=menu3)

# ajout de monMenu a mon app
app.config(menu=monMenu)


# les frame conteneur
grFrame = Frame(app, borderwidth=2, relief=RAISED, bg="yellow")
grFrame.pack(side=TOP, padx=20, pady=40)

frame1 = Frame(grFrame, borderwidth=2, relief=RAISED)
frame1.pack(side=LEFT, padx=20, pady=10)

frame2 = Frame(grFrame, borderwidth=2, relief=SUNKEN)
frame2.pack(side=RIGHT, padx=10, pady=10)

btn2 = Button(frame2, text="bouton OUI/NON", command=messageYesNo, cursor="cross").pack(padx=10, pady=10)
btn1 = Button(frame1, text="bouton annuler", command=messageCancel, cursor="pirate").pack(padx=10, pady=10)
btn3 = Button(frame2, text="bouton ESSAYER/ANNULER", command=messageRetryCancel, cursor="pirate").pack(padx=10, pady=10)


app.mainloop()


