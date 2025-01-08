import turtle, random
from generate_random_color import generate_random_rgb_color

t = turtle.Turtle("turtle")
ts = t.getscreen()

ts.colormode(cmode=255)
t.speed(10)
t.pensize(10)

def random_walk(turtle: turtle.Turtle, steps: int) -> None:
    directions = [0, 90, 270, 90]
    # directions = [random.randint(90,180)]

    colors  = ['red', 'green', 'blue', 'gray', 'brown', 'gold', 'orange', 'hotpink']

    for _ in range(steps):
        # turtle.pencolor(random.choice(colors))
        turtle.pencolor(generate_random_rgb_color())
        turtle.forward(30)
        turtle.right(random.choice(directions))
    # turtle.home() # ends at home of turtle

random_walk(t, 100)

screen = turtle.Screen()
screen.exitonclick()
