from turtle import Turtle
from generate_random_color import generate_random_rgb_color
from level import HEIGHT, WIDTH

# Class to represent a car on the road. It moves at a constant speed and checks if it has gone off the screen.

class Car(Turtle):
    def __init__(self, y_position: int, speed: int):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color(generate_random_rgb_color())
        self.penup()
        self.goto((int(WIDTH/2), y_position))
        self.speed(speed)
        self.move()
        self.setheading(180)
        

    def move(self):
        self.off_screen()
        self.forward(20)

    def off_screen(self):
        if self.xcor() < (-330):
            self.hideturtle()