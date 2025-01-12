from turtle import Turtle, Screen
from timmy import Timmy
from level import Level, HEIGHT, WIDTH
from traffic import Traffic

# sets the screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('white')
screen.title('Dee\'s Turtle Cross-road Game')
screen.tracer(0)
screen.colormode(255)

level = Level()

# create a turtle
timmy = Timmy()

screen.listen()
screen.onkey(timmy.move_up, 'Up')
screen.onkey(timmy.move_down, 'Down')

is_game_on = True


while is_game_on:
    screen.update()
    # play the game here


    # detect car collision with the turtle
    
    # create the finish line

screen.update()
screen.exitonclick()