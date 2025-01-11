from turtle import Turtle, Screen
from scoreboard import Scoreboard, draw_center_line
# create initial board setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")

# draw grid
p1_score = Scoreboard((-100, 270))
p2_score = Scoreboard((100, 270))
draw_center_line()


screen.exitonclick()