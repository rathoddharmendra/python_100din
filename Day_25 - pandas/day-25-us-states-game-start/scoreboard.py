import turtle 

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=-290, y=280)
        self.hideturtle()
        self.score = -1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}/50", align='center', font=(("Arial", 16, "normal")))