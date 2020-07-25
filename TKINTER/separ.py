# encodage
# -*- coding:Utf-8 -*-

# import de la librairie tkinter
from tkinter import *
from tkinter.messagebox import *

app = Tk()

# monapp conf
app.title("DK PYapp")
app.geometry("600x300")
app["bg"] = "grey"
app.iconbitmap("icon.ico")

#separateur
sep = PanedWindow(app, orient=HORIZONTAL, relief=RAISED)
sep.pack(side=TOP, expand=Y, fill=BOTH, padx=10, pady=10)

sep.add(Label(sep, text="partie 1", bg="cyan", anchor=CENTER))
sep.add(Label(sep, text="partie 2", bg="orange", anchor=CENTER))
sep.add(Label(sep, text="partie 3", bg="pink", anchor=CENTER))

sep.pack()

app.mainloop()
