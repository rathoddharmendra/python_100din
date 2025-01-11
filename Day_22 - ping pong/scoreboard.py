#type: ignore

from turtle import Turtle
import asyncio

class Scoreboard(Turtle):
    def __init__(self, initial_position: tuple):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.initial_position: tuple = initial_position
        self.goto(self.initial_position) 
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier New", 24, "bold"))

    def update_score(self):
        self.score += 1
        self.write_score()

    def game_over(self, position):
        self.clear()
        self.goto(position)
        self.write(f"Game Over! : {self.score}", align="center", font=("Courier New", 24, "bold"))
    def win(self, position):
        self.clear()
        self.goto(position)
        self.write(f"You Win! : {self.score}", align="center", font=("Courier New", 24, "bold"))

# async def draw_dotted_line(turtle: Turtle, direction: int, position: tuple, length: int):
def draw_dotted_line(turtle: Turtle, direction: int, position: tuple, length: int):
        turtle.setheading(direction)
        turtle.penup()
        turtle.goto(position)
        for _ in range(1, length):
            if _ % 2 != 0:
                turtle.down()
                turtle.forward(10)
            else:
                turtle.penup()
                turtle.forward(10)

def draw_grid():
    """Draws the grid of the gameboard"""
    lines = []
    for line in range(1,6):
        line = Turtle()
        line.speed('fastest')
        line.hideturtle()
        line.pencolor("white")
        line.penup()
        lines.append(line)
        
    # draws center line
    # asyncio.gather(draw_dotted_line(turtle=lines[0], direction=90, position=(0,-300), length=60),draw_dotted_line(turtle=lines[1], direction=90, position=(400,-300), length= 60))
    draw_dotted_line(turtle=lines[0], direction=90, position=(0,-300), length=60)
    # draws y-edges
    draw_dotted_line(turtle=lines[1], direction=90, position=(400,-300), length= 60)
    draw_dotted_line(turtle=lines[2], direction=90, position=(-400,-300), length= 60)

    # draws x-edges
    draw_dotted_line(turtle=lines[3], direction=0, position=(-400,-300), length= 80)
    draw_dotted_line(turtle=lines[4], direction=0, position=(-400,300), length= 80)
