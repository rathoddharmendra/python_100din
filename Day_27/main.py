import tkinter

window = tkinter.Tk('Dee')
window.title('Dee Tkinter')
window.minsize(width=600, height=600)

# Label
label = tkinter.Label(window, text='Hello, Dee!', font=('Arial', 24, 'bold'))
label_1 = tkinter.Label(window, text='Have A Nice Day!', font=('Arial', 16, 'bold'))
label.pack()
label_1.pack(side='right')

window.mainloop()