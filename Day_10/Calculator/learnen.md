
<!-- new_learnen -->
### inner function

```python
def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)
```

### storing function as a variable

```python
def add_function(n1, n2):
    return n1 + n2

new_function = add_function
new_function(5, 10)
```

### validated inputs 

```python

def get_valid_input(prompt: str, validation_fn):
    while True:
        user_input = input(prompt)
        if validation_fn(user_input):
            return user_input
        print("Invalid input. Please try again.")

def operator_validation_fn(value: str) -> bool:
    if value in ["+", "-", "*", "/"]:
        return True
    else:
        return False

def number_validation_fn(value: str) -> bool:
    try:
        if value.isnumeric():
            return True
    except ValueError:
        return False
    else:
        return False

def ask_for_input(num):
    """
    Returns a tuple of two numbers and an operator.
    """
    num1 = num if num else get_valid_input("Enter the first number: ", number_validation_fn)
    num2 = get_valid_input("Enter the next number: ", number_validation_fn)
    operator = get_valid_input("Enter an operator (+, -, *, /): ", operator_validation_fn)
    
    return (float(num1), float(num2), operator)

```

### os.system('clear')