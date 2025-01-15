from tkinter import *
import os

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30


# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.minsize(width=250, height=250)
window.config(padx=25, pady=25, bg=YELLOW)

# create background tomato and put a timer widget on top of it
# new_learnen - canvas for background
canvas = Canvas(window, width=200, height=250) # bg=transparent
bg_image = PhotoImage(file=os.path.join(os.path.dirname(__file__), "tomato.png"))
canvas.create_image(103, 125,image=bg_image)
h = 00
m = 0
s = 0
canvas.create_text(100,140,text=f'0{h}:0{m:0.2f}', font=(FONT_NAME, 24, 'bold'), fill=YELLOW )
canvas.grid(row=1, column=1)


# create buttons - start and reset timer
def startTimer():
    pass
start = Button(window, text="Start", command=startTimer)
start.grid(row=2, column=0)

def resetTimer():
    pass

reset = Button(window, text="Reset", command=resetTimer)
reset.grid(row=2, column=2)

window.mainloop()

