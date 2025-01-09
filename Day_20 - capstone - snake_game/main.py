# type: ignore
from turtle import Turtle, Screen
import random, time
import snake
from food import Food
from generate_random_color import generate_random_rgb_color

screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(cmode=255)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.delay(500)

# store snakes body
snake = snake.Snake()
food = Food()

# control snake
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# move the snake
is_game = True

# listen for keypresses
while is_game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # food.show_next_food()


screen.listen()
screen.exitonclick()