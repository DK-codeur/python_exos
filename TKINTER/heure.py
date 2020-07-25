#-*- coding:Utf-8 -*-

from tkinter import *
import time

app = Tk()
app.title("my Hour app")
app.geometry("700x300")
app["bg"] = "pink"


# function
def cycle_1s():
    heure.set(time.strftime('Date et Heure : %A %d %B %Y %Hh %Mmin %Ss'))
    app.after(1000, cycle_1s)


Label(app, text="voici la date et l'heur actuelle", font=("mono space", 22, "bold")).pack(padx=10, pady=10)
heure = StringVar()
Label(app, textvariable=heure, font=("arial", 14, "italic")).pack(padx=12, pady=12)


cycle_1s()


app.mainloop()
