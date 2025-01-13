from turtle import Turtle, Screen
from timmy import Timmy
from level import Level, HEIGHT, WIDTH, level_number
from traffic import Traffic
import time

# sets the screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('white')
screen.title('Dee\'s Turtle Cross-road Game')
screen.tracer(0)
screen.colormode(255)
screen.delay(1000)

level = Level()
traffic = Traffic()
# create a turtle
timmy = Timmy()

screen.listen()
screen.onkey(timmy.move_up, 'Up')
screen.onkey(timmy.move_down, 'Down')

is_game_on = True
counter = 10 - traffic.level
def reset_car_counter():
    global counter
    counter = 10 - traffic.level
    
def increase_level():
    if timmy.ycor() > 180:
        level.increase_level()
        traffic.increase_level()
        timmy.reset_position()

while is_game_on:
    screen.update()
    # play the game here
    time.sleep(0.1)
    # every 5th loop, create 1 car
    if counter < 0:
        traffic.create_traffic()
        reset_car_counter()
    else:
        counter -= 1
    
    traffic.move_cars()
    # detect car collision with the turtle
    for car in traffic.cars:
        # if car.ycor() + 60 < timmy.ycor() and car.ycor() - 20 > timmy.ycor() :
        distance = car.distance(timmy)
        timmy_y = timmy.ycor()
        car_y = car.ycor()
        buffer = 5
        # measure the distance
        if distance < 30:
            is_game_on = False
            level.game_over()
            break
    # change level
    increase_level()
    # Declare winner
    if traffic.level > 5:
        is_game_on = False
        level.declare_win()
    
    # create the finish line

screen.update()
screen.exitonclick()