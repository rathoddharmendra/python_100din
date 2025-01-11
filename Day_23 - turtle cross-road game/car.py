from turtle import Turtle
from generate_random_color import generate_random_rgb_color
class Car(Turtle):
    def __init__(self, y_position: int, speed: int):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color(generate_random_rgb_color())
        self.penup()
        self.goto((310, y_position))
        self.speed(speed)
        self.move()

    def move(self):
        while True:
            self.off_screen()
            self.forward(20)

    def off_screen(self):
        if self.ycor() < (-280):
            self.__del__()