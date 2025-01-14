import turtle, time, os
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')
filename = os.path.join(os.path.dirname(__file__), 'high_score.txt')
class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = self.get_high_score()
        self.color('white')
        self.penup()
        self.goto(x=0, y=260)
        self.write_score()
        self.hideturtle()
        
    def set_high_score(self):
        with open(filename, 'w') as file:
            file.write(str(self.score))
        
    def get_high_score(self):
        with open(filename) as file:
            return int(file.read())
                


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
        
        self.set_high_score() if self.score > self.highest_score else None
        self.score = 0
        self.highest_score = self.get_high_score()