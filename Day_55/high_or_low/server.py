from flask import Flask
from random import randint

app = Flask(__name__)

CHOSEN_NUMBER = randint(1,10)

HOME_IMAGE = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'
HIGH_IMAGE = 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'
LOW_IMAGE = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'
CORRECT_IMAGE = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'



# def make_heading(func):
#     def wrapper(*args, **kwargs):
#         return f"<h1 style='text-align: center'>{func(*args, **kwargs)}</h1>"
#     return wrapper


# def make_bold(func):
#     def wrapper(*args, **kwargs):
#         return f"<b>{func(*args, **kwargs)}</b>"
#     return wrapper

# def make_italics(func):
#     def wrapper(*args, **kwargs):
#         return f"<i>{func(*args, **kwargs)}</i>"
#     return wrapper

# def make_underline(func):
#     def wrapper(*args, **kwargs):
#         return f"<u>{func(*args, **kwargs)}</u>"
#     return wrapper

def add_style(func):
    def wrapper(*args):
        return f"""<head>
        <style>
        body {{
            text-align: center;
            background-color: black;
            justify-content: center;
            align-items: center;
        }}

        img {{
            width: 400;
            height: auto;
        }}
        
        </style>
        </head>
        <body>
        {func(*args)}
        </body>
        """
    return wrapper

@app.route("/")
@add_style
def home():
    return f'<h1>Guess a number betweeen 1 and 10</h1><img src={HOME_IMAGE} alt="correct-image">'
 
@app.route('/<int:number>')
@add_style
def display(number: int):
    if number == CHOSEN_NUMBER:
        return f'<h1>You guessed it right!</h1><img src={CORRECT_IMAGE} alt="correct-image">'
    elif number < CHOSEN_NUMBER:
        return f'<h1>Your guess {number} is bit lower than the secret number!</h1><img src={LOW_IMAGE} alt="low-image">'
    elif number > CHOSEN_NUMBER:
        return f'<h1>Your guess {number} is bit higher than the secret number!  </h1><img src={HIGH_IMAGE} alt="low-image">'
    
if __name__ == "__main__":
    app.run(debug=True, port=8080)

