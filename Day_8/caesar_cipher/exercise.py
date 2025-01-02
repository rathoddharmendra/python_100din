import operator

alphabet = list("abcdefghijklmnopqrstuvwxyz")

# def encrypt(msg: str, shift: int) -> str:
#     encrypted_msg = ""
#     for letter in msg:
#         if letter in alphabet:
#             encrypted_msg += alphabet[(alphabet.index(letter) + shift) % 26] #tests : z, x, y
#         else:
#             encrypted_msg += letter
#     return encrypted_msg

# def decrypt(msg: str, shift: int) -> str:
#     decrypted_msg = ""
#     for letter in msg:
#         if letter in alphabet:
#             decrypted_msg += alphabet[(alphabet.index(letter) - shift) % 26] #tests : z, x, y
#         else:
#             decrypted_msg += letter
#     return decrypted_msg

def caesar_cipher(encode_or_decode: str, message: str, shift: int) -> None:
    cipher_msg = ""

    if encode_or_decode == "e":
        shifted_index = operator.add(alphabet.index(letter), shift) % 26
    elif encode_or_decode == "d":
        shifted_index = operator.subtract(alphabet.index(letter), shift) % 26
    else:
        print("Invalid direction. Please enter either 'encode' or 'decode'.")
        play()

    for letter in message:
        if letter in alphabet:
            cipher_msg += alphabet[shifted_index] #tests : z, x, y
        else:
            cipher_msg += letter

    return cipher_msg


def play() -> None:
    try:
        message = input("Enter the message: ").lower()
        shift = int(input("Enter the shift value: "))
        direction = input("Do you want to decrypt or encrypt (d/e)? ").lower()
    except Exception as e:
        print(f"An error occurred: {e}. Try again.")
        play()

    caesar_cipher(direction, message, shift)

if __name__ == "__main__":
    is_game = True
    while is_game:
        play()
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again!= "y":
            print("Thanks for playing!")
            is_game = False # Exit the game loop



# # Test the program
# message = "Hello, World!"
# shift = 3
# direction = "encode"
# play()

# # Test the program with different messages and shifts
# message = "Python is awesome!"
# shift = 5
# direction = "decode"
# play()

# # Test the program with non-alphabet characters
# message = "Hello, 123!"
# shift = 3
# direction = "encode"
# play()
