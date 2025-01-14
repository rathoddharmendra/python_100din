import turtle
import os
from states import States

screen = turtle.Screen()
screen.title('U.S States Game')
bg_image = os.path.join(os.path.dirname(__file__), 'blank_states_img.gif')
screen.register_shape(bg_image)
turtle.shape(bg_image)

states = States()

is_game_on = True
while is_game_on:
    user_guess = screen.textinput(title='Guess a State', prompt='Enter the name of a state:')

    if user_guess == 'exit':
        is_game_on = False
    elif states.find_state_by_name(user_guess):
            found_state = turtle.Turtle()
            found_state.hideturtle()
            found_state.penup()
            found_state.goto(-200, 300)
            found_state.write(user_guess, align='center', font=('Arial', 16, 'normal'))
    else:
         turtle.write('State not found!', align='center', font=('Arial', 16, 'normal'))


screen.mainloop()


