def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    if n2 == 0:
        raise ValueError("Cannot divide by zero")
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

operations = {
    '+': add,
    '-': subtract,
    '/': divide,
    '*': multiply
}

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


def greetings():
    print("Welcome to the Calculator!")
    print("This program will perform basic arithmetic operations on two numbers.")


def main():
    greetings()
    is_continue = True
    use_previous_result = False
    while is_continue:
        num1, num2, operator = ask_for_input(use_previous_result)
        result = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {result}")

        play_again = input("Type 'y' to use previous result, type 'n' to start fresh, or type anything else to stop the game").lower()
        if play_again == "y":
            use_previous_result = result
        elif play_again == "n":
            use_previous_result = False
        else:
            is_continue = False

if __name__ == "__main__":
    main()