import os
filename = os.path.join(os.path.dirname(__file__),'../Input/Letters/starting_letter.txt')
with open(filename) as file:
    lines = [line.rstrip() for line in file.readlines()]

print(lines)