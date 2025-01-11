#type: ignore

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position: tuple):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.position: tuple = position
        self.goto(self.position) 
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier New", 24, "bold"))



def draw_center_line():
    center_line = Turtle()
    center_line.speed('fastest')
    center_line.hideturtle()
    center_line.pencolor("white")
    center_line.penup()
    center_line.goto((0,-500))
    center_line.setheading(90)

    for _ in range(1, 100):
        if _ % 2 != 0:
            center_line.down()
            center_line.forward(10)
        else:
            center_line.penup()
            center_line.forward(10)