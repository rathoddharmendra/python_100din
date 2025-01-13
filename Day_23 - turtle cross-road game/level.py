from turtle import Turtle

HEIGHT = 450
WIDTH = 630

# global level variables
level_number = 1
class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto((-260, 200))
        self.write(f"Level {level_number}", align="center", font=("Courier", 16, "normal"))
    
    def increase_level(self):
        global level_number
        self.clear()
        level_number += 1
        self.write(f"Level {level_number}", align="center", font=("Courier", 16, "normal"))

    def make_finish_line(self):
        pass

    def game_over(self):
        self.clear()
        self.goto((0, 0))
        self.write(f"Game Over!", align="center", font=("Courier", 24, "normal"))

    def declare_win(self):
        self.clear()
        self.goto((0, 160))
        self.write(f"You Won! 🎉 ", align="center", font=("Courier", 36, "normal"))
