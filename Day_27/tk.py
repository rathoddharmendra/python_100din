import tkinter
import tkinter.font

window = tkinter.Tk()
window.title("Hello, Dee!")
window.minsize(width=600, height=600)

new_text = 'Sheral'
def change_label():
    new_text = entry.get()
    label.config(text=f'Hello, {new_text.strip("'")}')

font = tkinter.font._FontDescription = ('Courier', 16, 'bold')
label = tkinter.Label(window, text="Hello, Dee!",font=font)
label.pack()


# buttons
button = tkinter.Button(window, text='change', command=change_label)
button.pack()


# 
entry = tkinter.Entry(window, width=40, bg='gray', name="entry" )
entry.pack()


window.mainloop()