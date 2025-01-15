from tkinter import *
import os, time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 1 # 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
tick_mark = '✅'
reps = 7

# ---------------------------- TIMER RESET ------------------------------- # 
def resetTimer():
    pass
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer():
    global reps
    if reps % 2 == 0:
        countdown(text_id=canvas_text, secs=60, min=WORK_MIN - 1)
        reps += 1
    elif reps % 2 == 1:
        countdown(text_id=canvas_text, secs=60, min=SHORT_BREAK_MIN - 1)
        reps += 1
    elif reps == 7:
        countdown(text_id=canvas_text, secs=60, min=LONG_BREAK_MIN - 1)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# freq: secs
def countdown(text_id: int, min: int, secs: int):
    if secs <= 0:
        min -= 1
        secs = 60
    if min < 0:
        update_canvas_text(text_id, f"DONE")
        return # end the countdown
        # todo - add a sound
        # todo - add a break point with reset click
    secs -= 1
    update_canvas_text(text_id, f"{min:02d}:{secs:02d}")
    canvas.after(1000,countdown,text_id, min, secs)
    # todo - set break point with reset click

# Update the text
def update_canvas_text(text_id: int, update_text: str):
    canvas.itemconfig(text_id, text=update_text)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.minsize(width=250, height=250)
window.config(padx=25, pady=25, bg=YELLOW)

header = Label(window, text="Timer", font=(FONT_NAME, 36), fg=GREEN, bg=YELLOW)
header.grid(row=0, column=1)

# create background tomato and put a timer widget on top of it
# new_learnen - canvas for background
canvas = Canvas(window, width=220, height=250, bg=YELLOW, highlightthickness=0) # bg=transparent
bg_image = PhotoImage(file=os.path.join(os.path.dirname(__file__), "tomato.png"))
canvas.create_image(103, 125,image=bg_image)

canvas_text = canvas.create_text(100,140,text=f'{WORK_MIN:02d}:{0:02d}', font=(FONT_NAME, 28, 'bold'), fill=YELLOW )
canvas.grid(row=1, column=1)

print(canvas_text)


# create buttons - start and reset timer

start = Button(
    window, 
    text="Start", 
    command=startTimer, 
    fg=GREEN, 
    highlightbackground=YELLOW, 
    font=(FONT_NAME, 16, 'bold'), 
    highlightthickness=0,
    padx=10,
    pady=10, 
    )
start.grid(row=2, column=0)



reset = Button(
    window,
    text="Reset", 
    command=resetTimer, 
    fg=PINK, 
    highlightbackground=YELLOW, 
    font=(FONT_NAME, 16, 'bold'), 
    highlightthickness=0,
    padx=10,
    pady=10, 
    )
reset.grid(row=2, column=2)

# create labels for work, short and long breaks


# create checkmarks for each completed break
check_mark_name = Label(
        window,
        text=tick_mark + "   " + tick_mark+ "   " + tick_mark+ "   " + tick_mark,
        bg=YELLOW,
        highlightbackground=YELLOW,
        highlightthickness=0,
        )
check_mark_name.grid(row=3, column= 1)

window.mainloop()

