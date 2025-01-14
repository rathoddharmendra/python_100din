import turtle
import os, time
from states import States
from scoreboard import Scoreboard
screen = turtle.Screen()
screen.title('U.S States Game')
bg_image = os.path.join(os.path.dirname(__file__), 'blank_states_img.gif')
screen.register_shape(bg_image)
turtle.shape(bg_image)

states = States()
scoreboard = Scoreboard()

is_game_on = True
while is_game_on:
    user_guess = screen.textinput(title='Guess a State', prompt='Enter the name of a state:').lower()

    if user_guess == 'exit':
        is_game_on = False
        turtle.write('Click anywhere to exit', align='center', font=('Courier', 24, 'normal'))
        screen.exitonclick()
    elif states.find_state_by_name(user_guess):
            scoreboard.update_scoreboard()
            print('found a state')
            time.sleep(1)

    else:
         turtle.write('State not found!', align='center', font=('Courier', 24, 'normal'))
         time.sleep(1)
         turtle.clear()


screen.mainloop()


