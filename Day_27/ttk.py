from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Hello World!")
root.minsize(width=600, height=600)

frm = ttk.Frame(root, padding=10)
frm.grid()
# frm.grid_location(x: 300, y: 300)
ttk.Label(frm, text="Hello World!").grid(column=100, row=0)
ttk.Label(frm, text="Hello World1!").grid(column=40, row=10)
ttk.Label(frm, text="Hello World2!").grid(column=30, row=20)
ttk.Label(frm, text="Hello World3!").grid(column=100, row=30)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=10, row=10)

# root.geometry("600x600")
root.mainloop()