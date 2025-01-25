def calculate(func):
    def wrapper(num1, num2):
        print(f'Before calling function: {num1} {func.__name__} {num2}')
        result = func(num1, num2)
        print(f'After calling function: {num1} {func.__name__} {num2} = {result}')
        return result
    
# Concept: Functions as first-order functions
@calculate
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        raise ValueError("Cannot divide by zero")
    return n1 / n2


calculate(add)

# Nested functions
# def outer_function(x):
#     def inner_function(y):
#         return x + y
#     return inner_function

# add_two = outer_function(2)

# def outer_function():
#     print('Called outer function')
#     def inner_function():
#         print('Called inner function')
#     return inner_function

# inner_func = outer_function()
# inner_func()


def logger(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[{level.upper()}] {func.__name__} is being called with arguments {args} {f'"," {kwargs}' if kwargs != {} else ''}")
            result = func(*args, **kwargs)
            print(f"[{level.upper()}] {func.__name__} returned {result}")
            return result
        return wrapper
    return decorator

# Using the decorator
@logger("info")
def add(a, b):
    return a + b

@logger("debug")
def multiply(a, b):
    return a * b

# Call the functions
print(add(3, 5))
print(multiply(4, 6))

import time
def delay_decorator(func):
    def wrapper():
        time.sleep(2)
        print("Inside decorator")
        func()
        print("After decorator")
    return wrapper

@delay_decorator # -> it expects func to return some kind of output - pre set
def say_hello():
    print("Hello, World!")


def say_bye():
    print("Bye, Bye!")
# decorators are used to add additional functionality 

say_hello()

# equivalent to sugar syntax @delay_decorator on say_bye function
bye_decorator = delay_decorator(say_bye)
bye_decorator()

# # Decorators with arguments
# def app(num_times):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 print(f"Inside decorator: {func.__name__}")
#                 result = func(*args, **kwargs)
#                 print(f"After decorator: {func.__name__}")
#                 return result
#         return wrapper
#     return decorator