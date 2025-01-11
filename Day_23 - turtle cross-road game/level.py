from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level_number = 1
        self.penup()
        self.hideturtle()
        self.goto((-270, 200))
        self.write(f"Level {self.level_number}", align="center", font=("Courier", 16, "normal"))

    def change_level(self, level_number: int):
        self.clear()
        self.level_number = level_number
        self.write(f"Level {self.level_number}", align="center", font=("Courier", 16, "normal"))
