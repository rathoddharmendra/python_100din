import os

filename = os.path.join(os.path.dirname(__file__),'my_file.txt')


with open(filename, mode='r') as file:
    contents = file.read()
    print(contents)


with open(filename, mode='a') as file:
    file.write('\nMy name is ' + contents)

with open(filename, mode='r') as file:
    contents = file.read()
    print(contents)