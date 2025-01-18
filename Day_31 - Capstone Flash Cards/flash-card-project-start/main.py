from tkinter import *
import os
from PIL import Image, ImageTk
from word import WordListGenerator, LANG

BACKGROUND_COLOR = "#B1DDC6"


# create a word list generator
word_list_generator = WordListGenerator()
card = {}
flip = ''

# create the window
window = Tk()
window.title("Flashy")
window.minsize(width=400, height=400)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

button_config = {
    "width": 40,
    "height": 40,
}

# create images
card_front_image_path = os.path.join(os.path.dirname(__file__),'./images/card_front.png')
card_back_image_path = os.path.join(os.path.dirname(__file__),'./images/card_back.png')

right_button_image_path = os.path.join(os.path.dirname(__file__),'./images/right.png')
wrong_button_image_path = os.path.join(os.path.dirname(__file__),'./images/wrong.png')

try:

    card_front_image = Image.open(card_front_image_path)  # Open the image
    card_front_image = card_front_image.resize((400, 260))  # Resize if needed
    card_front_image = ImageTk.PhotoImage(card_front_image)  # Convert to PhotoImage

    card_back_image = Image.open(card_back_image_path)  # Open the image
    card_back_image = card_back_image.resize((400, 260))  # Resize if needed
    card_back_image = ImageTk.PhotoImage(card_back_image)  # Convert to PhotoImage

    right_button_image = Image.open(right_button_image_path)  # Open the image
    right_button_image = right_button_image.resize((60, 60))  # Resize if needed
    right_button_image = ImageTk.PhotoImage(right_button_image)  # Convert to PhotoImage

    wrong_button_image = Image.open(wrong_button_image_path)  # Open the image
    wrong_button_image = wrong_button_image.resize((60, 60))  # Resize if needed
    wrong_button_image = ImageTk.PhotoImage(wrong_button_image)  # Convert to PhotoImage
except Exception as e:
    print(f"Error loading image: {e}")
    raise FileNotFoundError('Couldn\'t load image files')

# create design
canvas = Canvas(width=400, height=260)
canvas.config(bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(202, 130, image=card_front_image)
canvas_title = canvas.create_text(200, 50, text='Let\'s Begin', font=('Arial', 20, 'italic'), fill='green')
canvas_word = canvas.create_text(200, 150, text='Click Start', font=('Courier', 42, 'bold'), fill='black')
canvas.grid(row=0, column=0, columnspan=2)


# create buttons

def show_next_card():
    global flip, card

    card = word_list_generator.send_row()
    if card is None:
        canvas.itemconfig(canvas_word, text="Deck Over")
        canvas.itemconfig(canvas_title, text='FINISH')
        return
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(canvas_word, text=card['German'], fill='black')
    canvas.itemconfig(canvas_title, text=LANG, fill='red')
    flip = window.after(3000, flip_card, card['English'])
def flip_card(english_word: str):
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(canvas_word, text=english_word, fill='white')
    canvas.itemconfig(canvas_title, text='English', fill='white')

def right():
    try:
        window.after_cancel(flip)
        word_list_generator.remove_row(card)  # remove the word from the list
    except ValueError:
        print('First Card - There was an error - valueerror')
    except KeyError:
        print('There was an error - keyerror')
    
    print(card)
    show_next_card()

def wrong():
    try:
        window.after_cancel(flip)
    except ValueError:
        print('First Card - There was an error - valueerror')

    show_next_card()



right_button = Button(window, button_config, image=right_button_image, command=right, 
                      bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR, 
                      highlightthickness=0,
                      fg=BACKGROUND_COLOR,     
                      width=55,
                      height=50
                      )
right_button.grid(row=1, column=1)


wrong_button = Button(window, button_config, image=wrong_button_image, command=wrong, 
                      bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR, 
                      highlightthickness=0,
                            width=55,
                      height=50)
wrong_button.grid(row=1, column=0)

window.mainloop()