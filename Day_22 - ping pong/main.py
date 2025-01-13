# type: ignore
from turtle import Turtle, Screen
from scoreboard import Scoreboard, draw_grid
from paddle import Paddle
from ball import Ball
import time

PADDLE_CONTACT = 378
X_WALL_CONTACT = 400
PADDLE_DISTANCE = 50
# create initial board setup
screen = Screen()
screen.setup(width=830, height=630)
screen.bgcolor("black")
screen.title("Dee's Ping-Pong")
screen.tracer(0)

# create players
player_1 = Paddle((-390, 200))
player_1.color("pink")
player_2 = Paddle((390, -200))
player_2.color("blue")

# create ball
ball = Ball()

# draw grid
p1_score = Scoreboard((-100, 265))
p1_score.color('pink')
p2_score = Scoreboard((100, 265))
p2_score.color('blue')
draw_grid()
screen.update()

# move paddle
screen.listen()
screen.onkeypress(player_1.move_up, "w")
screen.onkeypress(player_1.move_down, "s")
screen.onkeypress(player_2.move_up, "Up")
screen.onkeypress(player_2.move_down, "Down")

def detect_miss():
    global is_game_over
    if ball.xcor() < (-1 * X_WALL_CONTACT):
        is_game_over = True
        p1_score.game_over((-150,0))
        p2_score.win((150,0))

    if ball.xcor() > X_WALL_CONTACT:
        is_game_over = True
        p2_score.game_over((150,0))
        p1_score.win((-150, 0)) 

def detect_paddle_contact():
    # checks player_1
    if ball.xcor() < (-1 * PADDLE_CONTACT):
        if ball.distance(player_1) < PADDLE_DISTANCE:
            ball.bounce()
            p1_score.update_score()
            ball.increase_speed()
    # checks player_2
    if ball.xcor() > PADDLE_CONTACT:
        if ball.distance(player_2) < PADDLE_DISTANCE:
            ball.bounce()
            p2_score.update_score()
            ball.increase_speed()

# game loop
is_game_over = False
while not is_game_over:
    screen.update()
    # time.sleep(0.1)
    ball.move()
    detect_paddle_contact()
    detect_miss()

screen.exitonclick()