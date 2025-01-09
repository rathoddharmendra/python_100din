# type: ignore
from color import extract_colors
import os, random
import turtle

image_path = os.path.join(os.path.dirname(__file__), "image.jpg")
colors = extract_colors(image_path, num_of_colors=10)[1:] # removing first color white

t = turtle.Turtle()

#
turtle.colormode(255)
# or
ts = t.getscreen()
ts.colormode(cmode=255)

# t.pensize(20)
t.speed(10)
t.penup()
t.goto(-200, -200)
# print first line
# make a dot

def draw_hirst(t: turtle.Turtle, colors: list) -> None:
    """
    Draws a hirst square from any given color list
    Args:
        t (turtle.Turtle): The turtle object to draw on.
        colors (list): A list of RGB color tuples.
    """
    gap = 40
    size = 10
    for y in range(size):
        t.goto(-200, y * gap)
        for _ in range(size):
            t.dot(20, random.choice(colors))
            t.forward(gap)
    t.hideturtle()
      
# calling draw_hirst(t, colors)
draw_hirst(t, colors)

screen = turtle.Screen()
screen.exitonclick()