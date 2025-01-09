import turtle, time
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')
class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(x=0, y=260)
        self.write_score()
        self.hideturtle()
        

    def update_score(self):
        self.clear()
        self.score += 1
        self.write_score()
        
    def write_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.write(f"Game Over! Final score: {self.score}", align=ALIGNMENT, font=FONT)