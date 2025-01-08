import turtle, random
from generate_random_color import generate_random_rgb_color
def draw_next_circles(turtle: turtle.Turtle, gap: int) -> None:
    counter = 0
    rounds = int(360 / gap)
    for degree in range(rounds):
        turtle.pencolor(generate_random_rgb_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + gap)

t = turtle.Turtle()
ts = t.getscreen()
t.speed("fastest")
ts.colormode(cmode=255)

draw_next_circles(t, 5)

screen = turtle.Screen()
screen.exitonclick()