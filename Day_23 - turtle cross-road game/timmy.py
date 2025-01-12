from turtle import Turtle

class Timmy(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('blue')
        self.penup()
        self.speed(0)
        self.goto((0, -200))
        self.setheading(90)


    def move_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)

    def reset_position(self):
        self.goto((0, -200))