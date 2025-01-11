# type: ignore
from turtle import Turtle

MOVE_SPEED = 30
UP = 90
DOWN = 270
SCREEN_LIMIT = 255
class Paddle(Turtle):
    def __init__(self, initial_position: tuple):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.speed(0)
        self.shapesize(stretch_len=0.5, stretch_wid=3)
        self.resizemode("user")
        self.initial_position = initial_position
        self.goto(self.initial_position) 
        
    def move_up(self):
        x, y = self.position()
        if y < (SCREEN_LIMIT):
            self.goto(x, y + MOVE_SPEED)
        # self.setheading(UP)
        # self.forward(MOVE_SPEED)
        # self.shapesize(stretch_len=0.5, stretch_wid=3)


    def move_down(self):
        x, y = self.position()
        if y > (SCREEN_LIMIT * -1):
            self.goto(x, y - MOVE_SPEED)
        # self.setheading(DOWN)
        # self.forward(MOVE_SPEED)
        # self.shapesize(stretch_len=0.5, stretch_wid=3)


