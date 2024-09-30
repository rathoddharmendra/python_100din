'''
BMI Calculator
The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is the formula used to calculate it:

bmi is equal to the person's weight divided by the person's height squared.

Convert this sentence into code on line 6.

'''
import math
height = 1.65 # in meters
weight = 84 # in kgs

# Write your code here.
bmi = (weight/height**2)


print(math.floor(bmi))


