# type: ignore
import turtle

# create turtle
t = turtle.Turtle()
screen = turtle.Screen()

def handle_click(key: str) -> None:
    if key == 'w':
        t.forward(10)
    elif key == 's':
        t.backward(10)
    elif key == 'a':
        t.setheading(t.heading() + 10)
    elif key == 'd':
        t.setheading(t.heading() - 10)
    elif key == 'c':
        t.home()
        t.clear()


# Define wrapper functions to pass key to handle_click
def move_forward():
    handle_click('w')

def move_backward():
    handle_click('s')

def turn_left():
    handle_click('a')

def turn_right():
    handle_click('d')

def clear_screen():
    handle_click('c')

# Bind keys to wrapper functions
# Set focus on the screen to capture key presses
screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=clear_screen, key="c")

screen.exitonclick()
