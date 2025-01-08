"""
Draw a dashed line of 10 paces each
"""

import turtle as t
import random
# from square import draw_square

turtle_1 = t.Turtle("turtle")
# turtle_1.shapetransform(10, -1, 0, 2)
turtle_1.speed(10)
turtle_1.pensize(3)
turtle_1.pencolor("red")

ts_1 = turtle_1.getscreen()
ts_1.screensize(canvwidth=1000, canvheight=1000, bg="pink")
ts_1.delay(300)

def draw_dashed_line(turtle: t.Turtle, step_length: int, steps: int) -> None: 
    for _ in range(steps):
        turtle.forward(step_length)
        turtle.pu() if turtle.isdown() else turtle.pd()

        # if _ % 2 == 0:
        #     turtle.pendown()
        # else:   
        #     turtle.penup()


draw_dashed_line(turtle_1, 10, 50)

screen = t.Screen()
screen.window_height()
screen.exitonclick()
