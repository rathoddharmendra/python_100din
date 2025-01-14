# type: ignore

from turtle import Turtle, Screen
import random, time
from generate_random_color import generate_random_rgb_color

# class enum Values (
INITIAL_SNAKE_LENGTH = 4
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snakes = []
        self.current_positions = []
        self.create_snake()
        self.head = self.snakes[0]

    def reset_snake(self):
        time.sleep(1)
        for snake in self.snakes:
            snake.goto(1000,1000)

        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for i in range(INITIAL_SNAKE_LENGTH):
            new_snake = Turtle(shape="square")
            new_snake.color(generate_random_rgb_color())
            # new_snake.color('white')
            new_snake.penup()
            x_position = new_snake.xcor() - (i * 20)
            new_snake.goto(x=x_position, y=0)
            new_snake.speed(0)
            self.snakes.append(new_snake)

    def _add_snake(self, position: tuple):
        new_snake = Turtle(shape="square")
        new_snake.color(generate_random_rgb_color())
        # new_snake.color('white')
        new_snake.penup()
        new_snake.speed(0)
        new_snake.goto(position)
        self.snakes.append(new_snake)

    def extend(self):
        self._add_snake(self.snakes[-1].position())

    def move(self):
        self.current_positions = []
        # make the body follow first snake
        for snake_index in range(len(self.snakes) -1, 0, -1): # 2
            x_pos = self.snakes[snake_index - 1].xcor()
            y_pos = self.snakes[snake_index - 1].ycor()
            self.current_positions.append((x_pos, y_pos))
            self.snakes[snake_index].goto(x_pos, y_pos)

        self.head.forward(MOVE_DISTANCE)
    
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        # check for collision with border