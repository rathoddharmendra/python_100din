# type: ignore
from turtle import Turtle, Screen
import random, time
# from Day_18.generate_random_color import generate_random_rgb_color
from generate_random_color import generate_random_rgb_color
screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(cmode=255)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# store snakes body
snakes = []
def make_snake():
    pass
def move_snake():
    pass

for i in range(3):
    new_snake = Turtle(shape="square")
    new_snake.color(generate_random_rgb_color())
    # new_snake.color('white')
    new_snake.penup()
    x_position = new_snake.xcor() - (i * 20)
    new_snake.goto(x=x_position, y=0)
    new_snake.speed(0)
    snakes.append(new_snake)

# move the snake
is_game = True
possible_directions = [90, 270]

# listen for keypresses
while is_game:
    screen.update()
    time.sleep(0.1)
   
    # make the body follow first snake
    for snake_index in range(len(snakes) -1, 0, -1): # 2
        x_pos = snakes[snake_index - 1].xcor()
        y_pos = snakes[snake_index - 1].ycor()
        snakes[snake_index].goto(x_pos, y_pos)
        screen.update()
    # direction = random.choice(possible_directions) # set by user's keystroke
    snakes[0].forward(20)
    snakes[0].left(random.choice(possible_directions))
    
    # check for collision with border

screen.listen()
screen.exitonclick()