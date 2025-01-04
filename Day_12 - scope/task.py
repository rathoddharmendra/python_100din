enemies = 1
pi = 3.14
def print_pi():
    print(f"Value of PI: {pi}") # read or reference global variable is alright

def increases_enemies(enemy) -> None:
    global enemies # global counter - to define global within the function to change the global value
    enemies += 1
    print(f"Enemies inside function to {enemies}")

# increases_enemies(enemies)
# print(f"Enemies outside function to {enemies}")

print_pi()