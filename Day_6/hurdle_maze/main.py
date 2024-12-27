"""
ESCAPE THE MAZE
Write a program using an if/elif/else statement so Reeborg can find the exit. The secret is to have Reeborg follow along the right edge of the maze, turning right if it can, going straight ahead if it can’t turn right, or turning left as a last resort.

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

What you need to know
The functions move() and turn_left().
Either the test front_is_clear() or wall_in_front(), right_is_clear() or wall_on_right(), and at_goal().
How to use a while loop and if/elif/else statements.
It might be useful to know how to use the negation of a test (not in Python).

"""


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def find_a_wall():
    while not is_facing_north():
        turn_left()
        
# one time to align the robot north, then start the main loop
while front_is_clear():
    move()
turn_left()

while not at_goal():
    #checks at every move
    if right_is_clear():
        turn_right()
        move()
    elif wall_on_right and front_is_clear():
        move()
    else:
        turn_left()  

        