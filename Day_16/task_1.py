### Tkinter code snippet

from tkinter import *
from turtle import *

root=Tk()

def print_name(event=None):
    print('hi my name is Dee')

button_1 = Button(root, text="Dee" )
button_1.bind("<Control-Button-1>",print_name)
button_1.pack()

root.mainloop()
