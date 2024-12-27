"""
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

"""

def square(x):
    cmove(x)
    turn_left()
    cmove(x)
    turn_left()
    cmove(x)
    turn_left()
    cmove(x)
    turn_left()
def turn_right():
    turn_left()    
    turn_left()    
    #turn_left()
    
def cmove(x):
    for _ in range(x):
        move()

cmove(3)
turn_left()
cmove(3)
turn_right()
move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
# Hurdle #1 challenge
def turn_right():
    turn_left()    
    turn_left()    
    turn_left()
    
def cross_hurdle(x):
    for _ in range(x):
        move()
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
        
cross_hurdle(6)
