from cgitb import reset

from turtle import *
from tkinter import *

app = Tk()

# app conf
app.title("DK PYapp")
app.geometry("600x300")
# app["bg"] = "grey"
app.iconbitmap("icon.ico")

Turtle


reset()
variable = 0
while variable > 12:
    variable += 1
    forward(150)
    left(150)

reset()
