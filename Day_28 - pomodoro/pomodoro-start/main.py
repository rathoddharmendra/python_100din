from tkinter import *
import os, time

# todo:
# add pause button
# Lift window when min is less than 1
# add playsounds

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 20 # 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
tick_mark = '✅'
reps = 0
timer = None



# ---------------------------- TIMER RESET ------------------------------- # 
def resetTimer():
    global reps
    window.after_cancel(timer)
    update_canvas_text(text_id=canvas_text, update_text="00:00")
    header.config(text="Timer", fg=GREEN)
    check_mark_name.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer():

    global reps
    if reps % 2 == 0:
        header.config(text=f'Working...', fg=GREEN)
        if reps > 0:
            check_mark_name.config(text=f'{check_mark_name.cget('text')}  {tick_mark}')

        countdown(text_id=canvas_text, min=WORK_MIN - 1)

    elif reps == 7:
        header.config(text=f'LONG BREAK', fg=RED)
        countdown(text_id=canvas_text, min=LONG_BREAK_MIN - 1)
        update_canvas_text(text_id=canvas_text, update_text=f"DONE")

        reps = 0
        return
    elif reps % 2 == 1:
        header.config(text=f'SHORT BREAK', fg=PINK)
        countdown(text_id=canvas_text, min=SHORT_BREAK_MIN - 1)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# freq: secs
def countdown(text_id: int, min: int, secs: int = 60):
    '''
    Once Countdown method is called, it continues to run for 4 work sesssions, 4 short breaks and 1 long break
    Countdown, depends on start_timer() function to complete interal loops with global reps variable
    '''
    global reps
    global timer
    if min == 0:
        window.lift()
    if secs <= 0: # every minute to reset secs and decrease 1 min
        min -= 1
        secs = 60
    # if min == 0: # pop out window when timer is less than 1 min
    #     window.attributes['topmost'] = True
    if min < 0:
        reps += 1
        startTimer()
        return # end the countdown
        # todo - add a sound
        # todo - add a break point with reset click
    secs -= 1
    update_canvas_text(text_id, f"{min:02d}:{secs:02d}")
    timer = canvas.after(1000,countdown,text_id, min, secs)
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
        text='',
        bg=YELLOW,
        highlightbackground=YELLOW,
        highlightthickness=0,
        )
check_mark_name.grid(row=3, column= 1)

window.lift()
window.attributes("-topmost", True)
window.after_idle(window.attributes, "-topmost", False)

window.mainloop()

