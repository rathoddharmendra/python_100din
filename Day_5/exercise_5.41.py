# FizzBuzz challenge #5.41

"""
# Solution #6:
# FizzBuzz challenge #

For numbers from 1 to 100, print the number on the console except for the following conditions:
if it is divisible by 3, print "Fizz"
if it is divisible by 5, print "Buzz"
if it is divisible by 3 and 5, print "FizzBuzz"

"""
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)