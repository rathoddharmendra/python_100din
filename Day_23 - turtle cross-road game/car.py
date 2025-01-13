from turtle import Turtle
from generate_random_color import generate_random_rgb_color
from level import HEIGHT, WIDTH, level_number

# Class to represent a car on the road. It moves at a constant speed and checks if it has gone off the screen.

MOVE_SPEED = 10
class Car(Turtle):
    def __init__(self, y_position: int, speed: int):
        super().__init__()
        self.move_speed = speed
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(generate_random_rgb_color())
        self.penup()
        self.goto((int(WIDTH/2), y_position))
        self.move()
        self.setheading(180)
        

    def move(self):
        self.off_screen()
        new_speed = MOVE_SPEED + int(self.move_speed * 0.5)
        self.forward(new_speed)

    def off_screen(self):
        if self.xcor() < (-330):
            self.hideturtle()