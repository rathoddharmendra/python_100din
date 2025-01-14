# type: ignore
from turtle import Turtle, Screen
import random, time
import snake
from food import Food
from scoreboard import Scoreboard
from generate_random_color import generate_random_rgb_color

screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(cmode=255)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.delay(2000)

# store snakes body
snake = snake.Snake()
food = Food()
score = Scoreboard()

# control snake
screen.listen()
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
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_score()
    # Detect collisions with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # is_game = False
        score.game_over()
        snake.reset_snake()


    # Detect collision with tail
    for snake_segment in snake.snakes[1:]:
        if snake_segment.distance(snake.head) < 10:
            # is_game = False§
            score.game_over()
            snake.reset_snake()

screen.exitonclick()