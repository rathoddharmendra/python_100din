from os import path

filename = path.join(path.dirname(__file__), 'name.txt')
print(filename)
try:
    file = open(filename)
except Exception as e:
    print(f'{filename} not found')
    print(f"{e}")
    raise(FileNotFoundError(f'{filename} not found'))
