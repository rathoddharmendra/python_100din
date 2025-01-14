import turtle, time
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')
class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = 0
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
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.store_high_score()
        # self.write(f"Game Over! Final score: {self.score}", align=ALIGNMENT, font=FONT)
        self.write_score()

    def store_high_score(self):
        self.highest_score = self.score if self.score > self.highest_score else self.highest_score
        self.score = 0