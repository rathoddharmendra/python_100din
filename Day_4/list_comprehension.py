
square = lambda x: x**2
new_square = [map(lambda x: x**2, range(10))] 
# new_learn: difference in using list and [] conversion
# list(): Converts any iterable (e.g., strings, tuples, sets, generators) to a list.
# []: Cannot be used directly for conversion. You would need a comprehension or similar construct.

squares = [x**2 for x in range(10)]
# print(square(3))
# print(squares)
# print(new_square)

# Nested-Conditional List Comprehension
new_list_comprehension = [(x, y, 0) for x in [1,2,3] for y in [3,1,4] if x != y]
print(new_list_comprehension)

# Traditional for loop
result = {}
for x in range(5):
    result[x] = x * x

# Dictionary comprehension
result = {x: x * x for x in range(5)}

# Traditional for loop
result = set()
for x in range(5):
    result.add(x * x)

# Set comprehension
result = {x * x for x in range(5)}

# Traditional for loop with yield
def generator():
    for x in range(5):
        yield x * x

# Generator expression
result = (x * x for x in range(5))
