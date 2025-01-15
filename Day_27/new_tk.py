from tkinter import ttk, Tk, StringVar, scrolledtext

window = Tk()
window.title("Hello, Dee!")
window.minsize(width=600, height=600)

# Creating a Frame
frame = ttk.Frame(window, padding=10)
frame.grid()

# Adding a Label widget
label = ttk.Label(frame, text="Hello, Dee!")
label.grid(column=0, row=0)

# Adding a Button widget
button = ttk.Button(frame, text="Quit", command=window.quit)
button.grid(column=1, row=0)

# Adding a Checkbutton widget
checkbutton = ttk.Checkbutton(frame, text="Check me")
checkbutton.grid(column=0, row=1)

# Adding a Radiobutton widget
radiobutton_var = StringVar()
radiobutton_var.set("Option 1")
radiobutton_var.set("Option 2")

radiobutton_1 = ttk.Radiobutton(frame, text="Option 1", variable=radiobutton_var, value="Option 1")
radiobutton_1.grid(column=0, row=2)

radiobutton_2 = ttk.Radiobutton(frame, text="Option 2", variable=radiobutton_var, value="Option 2")
radiobutton_2.grid(column=1, row=2)

# Adding a Combobox widget
combobox_var = StringVar()
combobox_options = ["Option 1", "Option 2", "Option 3"]
combobox = ttk.Combobox(frame, textvariable=combobox_var, values=combobox_options)
combobox.current(0)
combobox.grid(column=0, row=3)

# Adding a Entry widget or INPUT
entry = ttk.Entry(frame, width=10)
entry.grid(column=1, row=3)

# Adding a ScrolledText widget
scrolledtext = scrolledtext.ScrolledText(frame, width=20, height=5)
scrolledtext.grid(column=0, row=4, columnspan=2)

window.mainloop()
