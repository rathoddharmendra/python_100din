# Bugs: When app crashes or doesn't work as expected to do

# Describe the problem
'''
Describe the problem: write the answers below in YAML format.

1. what is the for loop doing?
> It's incremeting the counter, aka 'i' from 1 to 19.

1.1 What is the purpose of the if statement?
> It's checking if 'i' equals 20 to execute a print statement.

2. When if the function meant to print "You got it!"
> When i equals 20. (assumption? Why? Can I get more context?)
3. What are your assumptions about the value of i?
wrong assumption on purpose:
> I will hit 20, and finally print "You got it!"
'''
def my_function():
    for i in range(1, 20):
        # if i == 20:
        if i == 19:
            print("You got it!")

# my_function()


'''
Reproduce Bug: the given erroneous code and explain the mistake.
'''
'''
Explanation of Bug:
1. Describe the problem:
> List Index out of range: 
$dice_num can sometimes give value/index value out of range on $dice_images list.

'''
from random import randint
dice_images = ['1', '2', '3', '4', '5', '6']

dice_num = randint(1, len(dice_images))

# print(f"You rolled a {dice_images[dice_num - 1]}!")



'''
debugging code for bugs
'''
try:
    year = int(input("What's your year of birth? "))
except ValueError as e:
    print(f"Invalid input with error {e}. Please enter a valid year such as 1994.")
finally:
    year = int(input("What's your year of birth? "))

if year <= 1980:
    print("You are from a Greatest Generation")
elif year > 1980 and year <= 1994:
    print("You are a millenial")
elif year > 1994 and year <= 2000:
    print("You are a Gen Z")
elif year > 2000:
    print("You are a Baby Boomer")

    

