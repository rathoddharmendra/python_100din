import turtle, random
from generate_random_color import generate_random_rgb_color
def draw_next_circles(turtle: turtle.Turtle) -> None:
    counter = 0
    for degree in range(361):
        turtle.pencolor(generate_random_rgb_color())
        turtle.circle(100)
        turtle.left(counter + 1)
        # turtle.tilt(degree)
        # turtle.setposition(x=degree, y=degree)
        # draw spirograph



t = turtle.Turtle()
ts = t.getscreen()
t.speed("fastest")
ts.colormode(cmode=255)

draw_next_circles(t)

screen = turtle.Screen()
screen.exitonclick()