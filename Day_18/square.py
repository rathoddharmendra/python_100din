from turtle import Turtle, Screen

def draw_square(turtle: Turtle) -> None:
    """Draws a square"""
    for _ in range(4):
        print(turtle.pos())
        turtle.forward(100)
        turtle.right(90)
        

turtle_1 = Turtle("turtle")

# sets the right screen and color
turtle_1.color('bisque')
turtle_1_screen = turtle_1.getscreen()
turtle_1_screen.bgcolor('#800080')
turtle_1.speed(1)

draw_square(turtle_1)


# to run by default, at the end of the game
screen = Screen()
screen.exitonclick()
