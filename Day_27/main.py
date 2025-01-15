import tkinter, os

window = tkinter.Tk('Dee')
window.title('Dee Tkinter')
window.minsize(width=600, height=600)

img_path = os.path.join(os.path.dirname(__file__), 'blank_states_img.gif')
img = tkinter.PhotoImage(file=img_path)

# Label
label = tkinter.Label(window, text='Hello, Dee!', font=('Arial', 24, 'bold'))
label_1 = tkinter.Label(window, text='Have A Nice Day!', font=('Arial', 16, 'bold'))
label.pack()
label_1.pack(side='top')
image_label = tkinter.Label(window, image=img).pack()


# import turtle 

# turtle = turtle.Turtle()
# turtle.write(arg='Hello,')
window.mainloop()