import turtle

# Create a new turtle object
t = turtle.Turtle("turtle")
ts = turtle.getscreen()
# ts.bgcolor('grey')
# t.speed(1)

def draw_multi_shape(turtle: turtle.Turtle) -> None:
    """Draws a multi-colored triangle, square, and circle"""
    colors  = ['red', 'green', 'blue', 'gray', 'brown', 'gold', 'orange', 'hotpink']

    for num_sides in range(3, 11):
        turtle.home()
        turtle.pencolor(colors[num_sides - 3])
        angle = 360 / num_sides
        for _ in range(num_sides):
            turtle.forward(100)
            turtle.right(angle)

draw_multi_shape(t)

# Create a screen object and set the background color to orange
screen = turtle.Screen()
screen.exitonclick()