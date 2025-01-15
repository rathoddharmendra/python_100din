import tkinter, os

window = tkinter.Tk('Dee')
window.title('Dee Tkinter')
window.minsize(width=600, height=200)

# img_path = os.path.join(os.path.dirname(__file__), 'blank_states_img.gif')
# img = tkinter.PhotoImage(file=img_path)


# Label
label = tkinter.Label(window, text='Hello, Dee!', font=('Arial', 24, 'bold'))
label.grid(column=0,row=0)
# label.pack()
# label.place(x=0,y=0)

# image_label = tkinter.Label(window, image=img).pack()
button_1 = tkinter.Button(window, text='Button')
button_1.grid(column=2, row=2)

button_2 = tkinter.Button(window, text='New Button')
button_2.grid(column=3, row=1)

# Entry
entry = tkinter.Entry(window, width=10 )
entry.grid(column=4, row=3)

# import turtle 

# turtle = turtle.Turtle()
# turtle.write(arg='Hello,')
window.mainloop()