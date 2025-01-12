from turtle import Turtle, Screen
import os, sys, time
# from ..timmy import Timmy
# from ..level import Level

file_path = os.path.join(os.path.dirname(__file__), '')
# sets the screen
screen = Screen()
screen.setup(width=630, height=450)
screen.bgcolor('white')
screen.title('Dee\'s Turtle Cross-road Game')
screen.tracer(0)
screen.colormode(255)

t = Turtle()
t.shape('square')
t.shapesize(stretch_wid=1, stretch_len=3)
t.color("red")
t.penup()
t.goto((int(630/2), 0))
t.speed(0)
t.setheading(180)

timmy = Turtle('turtle')
# screen.listen()
# screen.onkey(timmy.move_up, 'Up')
# screen.onkey(timmy.move_down, 'Down')

is_game_on = True


while is_game_on:
    screen.update()
    # play the game here
    time.sleep(0.5)
    t.forward(20)
    print(t.distance(timmy))
    if t.xcor() < -280:
        is_game_on = not is_game_on
        t.hideturtle()


    # detect car collision with the turtle
    
    # create the finish line

screen.update()
screen.exitonclick()