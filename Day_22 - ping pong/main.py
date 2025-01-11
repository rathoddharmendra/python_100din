from turtle import Turtle, Screen
from scoreboard import Scoreboard, draw_grid
from paddle import Paddle
from ball import Ball
# create initial board setup
screen = Screen()
screen.setup(width=830, height=630)
screen.bgcolor("black")
screen.title("Dee's Ping-Pong")
screen.tracer(0)

# create players
player_1 = Paddle((-390, 200))
player_2 = Paddle((390, -200))

# create ball
ball = Ball()

# draw grid
p1_score = Scoreboard((-100, 265))
p2_score = Scoreboard((100, 265))
draw_grid()
screen.update()

# move paddle
screen.listen()
screen.onkeypress(player_1.move_up, "w")
screen.onkeypress(player_1.move_down, "s")
screen.onkeypress(player_2.move_up, "Up")
screen.onkeypress(player_2.move_down, "Down")

# game loop
is_game_over = False
while not is_game_over:
    screen.update()
    ball.move()

    # checks player_1
    if ball.xcor() < -390:
        if ball.distance(player_1) < 30:
            ball.bounce()
            p1_score.update_score()
        else:
            is_game_over = True
            p1_score.game_over((-150,0))
            p2_score.win((150,0))

    # checks player_2
    if ball.xcor() > 390:
        if ball.distance(player_2) < 30:
            ball.bounce()
            p2_score.update_score()
        else:
            is_game_over = True
            p2_score.game_over((150,0))
            p1_score.win((-150, 0)) 

    # # detect collision with paddles
    # if ball.distance(player_1) < 50 and ball.xcor() > -390:
    #     ball.bounce_x()
    # if ball.distance(player_2) < 50 and ball.xcor() < 390:
    #     ball.bounce_x()

    # # detect score
    # if ball.xcor() > 390:
    #     ball.reset_position()
    #     p1_score.increase_score()
    # if ball.xcor() < -390:
    #     ball.reset_position()
    #     p2_score.increase_score()


screen.exitonclick()