
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from quiz_brain import QuizBrain
import time

THEME_COLOR = '#375362'
FONT = ('Arial', 20, 'italic')
PADDING = 20

after = ''

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize(width=300, height=300)
        self.window.config(padx=PADDING, pady=PADDING, bg=THEME_COLOR)

        # create images
        right_button_image_path = os.path.join(os.path.dirname(__file__),'./images/right.png')
        wrong_button_image_path = os.path.join(os.path.dirname(__file__),'./images/wrong.png')

        try:
            right_button_image = Image.open(right_button_image_path)  # Open the image
            right_button_image = right_button_image.resize((60, 60))  # Resize if needed
            right_button_image = ImageTk.PhotoImage(right_button_image)  # Convert to PhotoImage

            wrong_button_image = Image.open(wrong_button_image_path)  # Open the image
            wrong_button_image = wrong_button_image.resize((60, 60))  # Resize if needed
            wrong_button_image = ImageTk.PhotoImage(wrong_button_image)  # Convert to PhotoImage
        except Exception as e:
            print(f"Error loading image: {e}")
        
        self.score = 0
        # score label
        self.score_label = Label(self.window, text=f'Score: {self.score}', 
                                 bg=THEME_COLOR, fg='white', pady=5, justify='left', 
                                 font=('Arial', 16, 'bold'))
        self.score_label.grid(row=0, column=1)
        
        self.canvas = Canvas(self.window, width=300, height=250)
        # self.canvas.create_image(150, 150, image=card_front_image)
        self.text = self.canvas.create_text(150, 125, 
                                            text='Start the Quizz App', 
                                            font=FONT, fill=THEME_COLOR, width=280)
        self.canvas.configure(bg='beige', highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        common_button_attributes = {
            'bg': THEME_COLOR,
            'highlightthickness': 0,
            'activebackground': THEME_COLOR,
            'activeforeground': 'white',
            'fg': THEME_COLOR,
        }
        self.right = Button(self.window, image=right_button_image, command=self.say_yes)
        self.right.grid(row=2, column=0)

        self.wrong = Button(self.window, image=wrong_button_image, command=self.say_no)
        self.wrong.grid(row=2, column=1)

        # result
        self.result = Label(self.window, text='', font=('Arial', 12, 'italic'), bg=THEME_COLOR, fg='pink')
        self.result.grid(row=3, column=0, columnspan=2)

        self.show_next_question()
        self.window.mainloop()

    def say_yes(self):
        self.check_answer('True')
    
    def say_no(self):
        self.check_answer('False')

    def show_next_question(self):
        self.canvas.configure(bg='beige')
        self.canvas.itemconfig(self.text, fill=THEME_COLOR)

        if self.quiz_brain.still_has_questions():
            self.canvas.itemconfig(self.text, text=self.quiz_brain.next_question())
        else:
            self.canvas.itemconfig(self.text, text=f'Quiz Over! Final Score: {self.score} / {self.quiz_brain.question_nr}')

            self.right.config(state=DISABLED)
            self.wrong.config(state=DISABLED)
        
    def show_result(self, result: str):
        global after
        self.result.config(text=result)
        after = self.window.after(1500, self.hide_result)

    def hide_result(self):
        self.result.config(text='')
        self.window.after_cancel(after)
    def update_score(self):
        self.score_label.config(text=f'Score: {self.score} / {self.quiz_brain.question_nr}')

    def check_answer(self, response: str):
        if self.quiz_brain.check_answer(response):
            self.score += 1
            self.update_score()
            # self.show_result('Correct')
            self.change_background(True)
        else:
            # self.show_result('Incorrect')
            self.update_score()
            self.change_background(False)

    def change_background(self, is_right: bool):
        if is_right:
            self.canvas.config(bg='green')
            self.canvas.itemconfig(self.text, fill='white')
        else:
            self.canvas.config(bg='red')
            self.canvas.itemconfig(self.text, fill='white')

        self.window.after(1000, self.show_next_question)

# get the create_text to fetch questions from the question bank