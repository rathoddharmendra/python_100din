import os

filename = '/Users/mac_dee/Desktop/my_file.txt'
# filename = os.path.join(os.path.dirname(__file__),'../../../../../../mac_dee/Desktop/my_file.txt')

try:
    with open(filename, mode='r') as file:
        contents = file.read()
        print(contents)


    with open(filename, mode='a') as file:
        file.write('\nMy name is ' + contents)

    with open(filename, mode='r') as file:
        contents = file.read()
        print(contents)
except Exception as e:
    print('File Not Found: ' + filename)
finally:
    print('Task complete. Run again')