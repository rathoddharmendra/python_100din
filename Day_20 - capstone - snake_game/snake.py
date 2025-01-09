# type: ignore

from turtle import Turtle, Screen
import random
from generate_random_color import generate_random_rgb_color

MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.possible_directions = [90, 270]
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        for i in range(5):
            new_snake = Turtle(shape="square")
            new_snake.color(generate_random_rgb_color())
            # new_snake.color('white')
            new_snake.penup()
            x_position = new_snake.xcor() - (i * 20)
            new_snake.goto(x=x_position, y=0)
            new_snake.speed(0)
            self.snakes.append(new_snake)

    def move(self):

        # make the body follow first snake
        for snake_index in range(len(self.snakes) -1, 0, -1): # 2
            x_pos = self.snakes[snake_index - 1].xcor()
            y_pos = self.snakes[snake_index - 1].ycor()
            self.snakes[snake_index].goto(x_pos, y_pos)
            
        
        self.snakes[0].forward(MOVE_DISTANCE)
        # self.snakes[0].left(self.direction)
    
        
    def up(self):
        self.snakes[0].setheading(90)

    def down(self):
        self.snakes[0].setheading(270)

    def left(self):
        self.snakes[0].setheading(180)

    def right(self):
        self.snakes[0].setheading(0)
        # check for collision with border