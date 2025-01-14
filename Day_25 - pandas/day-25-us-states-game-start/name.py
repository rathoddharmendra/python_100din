from turtle import Turtle

class Name(Turtle):
    def __init__(self, x: int, y: int, name: str):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(name, align='center', font=(("Arial", 16, "normal")))