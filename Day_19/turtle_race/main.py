# type: ignore

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

# ASK TO CHOOSE A BET: TURTLE
user_bet = screen.textinput(title="Make your bet", prompt="Choose a turtle (red','blue','green','pink','black','purple', 'yellow'): ")
players = ['red','blue','green','pink','black','purple', 'yellow']
turtles = []
# create six players and set penup
for player in players:
    color = player
    player = Turtle(shape="turtle")
    player.color(color)
    player.penup()
    player.speed(0)
    # set them at the start
    y_coordinate = -150 + players.index(color) * 50 # sets y coordinate from -150 to 150
    player.goto(x = -230, y = y_coordinate)
    turtles.append(player)

# RUN RACE AND DECLARE THE WINNER

def run(turtle):
    turtle.forward(random.randint(0,10))

if user_bet:
    is_race_on = True


while is_race_on:
    winner = ""
    for turtle in turtles:
        run(turtle)
        # check for a winner
        if turtle.xcor() >= 230:
            winner = turtle.pencolor()
            is_race_on = False
            break

# Declare winner
if winner == user_bet:
    print(f"You litle turtle - the {winner} won the race !")
else:
    print(f"You lost your bet! The {winner} turtle beat your race! ")




screen.exitonclick()