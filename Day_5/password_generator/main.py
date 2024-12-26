import elements
import random
from collections import deque 
    
# Declaring deque 
queue = deque(['name','age','DOB'])  

def generate_password(letter_count: int, number_count: int, special_char_count: int) -> str:
    """
    Generates a password with a given number of letters, numbers, and special characters.

    Args:
        letter_count (int): The number of letters in the password.
        number_count (int): The number of numbers in the password.
        special_char_count (int): The number of special characters in the password.
    """
    password_elements = []
    # Randomly chooses elements from parents list
    password_elements.extend(random.sample(elements.letters, len(elements.letters))[:letter_count])
    password_elements.extend(random.sample(elements.numbers, len(elements.numbers))[:number_count])
    # password_elements.extend(random.sample(elements.special_chars, len(elements.special_chars))[:special_char_count])
    password_elements.extend([random.choice(elements.special_chars) for _ in range(0, special_char_count)])
    
    password = (random.sample(password_elements, len(password_elements)))
    # converts chars of list to string
    return ''.join(password)

if __name__ == "__main__":
    letter_count = int(input("Enter the number of letters in the password: "))
    number_count = int(input("Enter the number of numbers in the password: "))
    special_char_count = int(input("Enter the number of special characters in the password: "))

    password = generate_password(letter_count, number_count, special_char_count)
    print("Generated password: ", password)


    