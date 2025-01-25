import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

def speed_calc_decorator(func):
    def wrapper():
      start_time = time.time()
      func()
      end_time = time.time()
      print(f'The time difference {end_time - start_time} seconds')
    return wrapper

@speed_calc_decorator
def fast_function():
    for i in range(10):
        i * i
        
@speed_calc_decorator
def slow_function():
    for i in range(10):
        i * i


fast_function() 
slow_function()