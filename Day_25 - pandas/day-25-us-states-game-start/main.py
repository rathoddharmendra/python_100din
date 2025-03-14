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


while len(states.guessed_states) < 50:
    user_guess = screen.textinput(title='Guess a State', 
                                  prompt='Enter the name of a state:').title()
    if user_guess == 'Exit':
        is_game_on = False
        turtle.write('Click anywhere to exit', align='center', font=('Courier', 24, 'normal'))
        break
    elif states.find_state_by_name(user_guess):
            scoreboard.update_scoreboard()
            print('found a state')
            time.sleep(1)
    else:
         turtle.write('State not found!', align='center', font=('Courier', 24, 'normal'))
         time.sleep(1)
         turtle.clear()

print(states.create_unguessed_states_csv())

screen.mainloop()


