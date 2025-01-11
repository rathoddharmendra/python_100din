from turtle import Turtle, Screen
from timmy import Timmy
from level import Level
from road import Road

# sets the screen
screen = Screen()
screen.setup(width=630, height=450)
screen.bgcolor('white')
screen.title('Dee\'s Turtle Cross-road Game')
screen.tracer(0)
screen.colormode(255)

level = Level()
road = Road()

# create a turtle
timmy = Timmy()

screen.listen()
screen.onkey(timmy.move_up, 'Up')
screen.onkey(timmy.move_down, 'Down')

is_game_on = True


while is_game_on:
    screen.update()
    road.create_random_cars()
    # create the obstacles
    
    # check for collisions
    # if timmy.distance(level.obstacle) < 20:
    #     is_game_on = False
    #     level.game_over()

    

# create the finish line

screen.update()
screen.exitonclick()