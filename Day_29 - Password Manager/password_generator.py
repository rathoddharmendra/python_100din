# type: ignore
import random, math, clipboard
ALPHABETS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                       'A', 'B', 'C', 'D', 'E', 'F,', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
SPECIAL_CHARACTERS = ['!', '@', ':'';','#','$','|','%', '&', '*', '+', '-', '_']

NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
class PasswordGenerator:
    def __init__(self):
        pass

    def generate_password(self, pass_length: int):
        password_list = []
        alphabets = random.sample(ALPHABETS, math.floor(pass_length/2))
        special_characters = random.sample(SPECIAL_CHARACTERS, math.ceil(pass_length/4))
        numbers = random.sample(NUMBERS, math.floor(pass_length/4))
        password_list.extend(alphabets)
        password_list.extend(special_characters)
        password_list.extend(numbers)
        password = ''.join(random.sample(password_list, pass_length))
        self.copy_to_clipboard(password)
        return password
    
    def copy_to_clipboard(self, password: str):
        clipboard.copy(password)




