# TODO: Create the logging_decorator() function 👇

def logging_decorator(func):
    def wrapper(*args):
        result = func(*args)
        print(func.__name__)
        print(*args)
        return result
    return wrapper

# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)
    
print(a_function(1,2,3))