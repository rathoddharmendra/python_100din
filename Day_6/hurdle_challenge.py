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
#### Hurdle #1 challenge
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


#### Hurdle #2 challenge

def turn_right():
    turn_left()    
    turn_left()    
    turn_left()
    
def cross_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
        
# number_of_hurdles = 6

# while number_of_hurdles > 0:
#     if at_goal() > 0:
#         break
#     cross_hurdle()
#     number_of_hurdles -= 1


# new_learnen - I like this syntax. It's clear and concise to be used with Boolean conditions.
while not at_goal():
    cross_hurdle()

        
# Hurdle #3 challenge

def turn_right():
    turn_left()    
    turn_left()    
    turn_left()
    
def cross_one_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


# def check_move():
# # front_is_clear() or, at_goal()
#     while front_is_clear() and not at_goal():
#         move()
            
# while not at_goal():
#     check_move()
#     if wall_in_front() and not at_goal():
#         cross_one_hurdle()
    
# much shortened code, but same functionality.
# new_learnen - The main condition check happens primarily, and other conditions are nested below it.
while not at_goal():
    if wall_in_front():
        cross_one_hurdle()
    else:
        move()


# Hurdle #4 challenge
# The position, the height and the number of hurdles changes each time this world is reloaded.

def turn_right():
    turn_left()    
    turn_left()    
    turn_left()
    
def cross_hurdle():
    turn_left()
    while wall_on_right(): 
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        cross_hurdle()
    else:
        move()

    

    

    


    

    
