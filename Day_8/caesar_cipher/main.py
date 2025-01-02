from symbols import caesar_cipher
# import keyboard

alphabet = list("abcdefghijklmnopqrstuvwxyz")

def encrypt(msg: str, shift: int) -> str:
    """
    Returns the encrypted message using a Caesar cipher with the given shift.

    Args:
        msg (str): The message to be encrypted.
        shift (int): The number of positions to shift each letter.
    """
    encrypted_msg = ""

    for char in msg.lower():
        if char in alphabet:
            encrypted_char = alphabet[(alphabet.index(char) + shift) % 26]
            encrypted_msg += encrypted_char
        else:
            encrypted_msg += char
    return encrypted_msg

def decrypt(encrypted_msg: str, shift: int) -> str:
    """
    Returns the decrypted message using a Caesar cipher with the given shift.

    Args:
        encrypted_msg (str): The encrypted message to be decrypted.
        shift (int): The number of positions to shift each letter.
    """
    decrypted_msg = ""

    for char in encrypted_msg.lower():
        if char in alphabet:
            decrypted_char = alphabet[(alphabet.index(char) - shift) % 26]
            decrypted_msg += decrypted_char
        else:
            decrypted_msg += char
    return decrypted_msg

def greeting() -> None:
    """
    Prints a greeting message with the Caesar cipher.
    """
    print("Welcome to the Caesar Cipher!")
    print(caesar_cipher)
    print("-" * 40 + "\n")
def play() -> None:
    greeting()
    is_game = True
    while is_game:
        message = input("Enter your message: ").lower()
        shift = int(input("Enter the shift value: "))

        choose_option = input("Do you want to encrypt or decrypt a message? (e/d): ").lower()
        
        if choose_option == "e":
            encrypted_msg = encrypt(message, shift)
            print(f"Encrypted message: {encrypted_msg}")
        elif choose_option == "d":
            decrypted_msg = decrypt(message, shift)
            print(f"Decrypted message: {decrypted_msg}")
        else:
            play()

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            is_game = False # Exit the game loop
        
    print("Thanks for playing!")

if __name__ == "__main__":
    play()
    


    # try:
    #     print("Press 'Escape' to exit or use Ctrl+C to interrupt.")


    #     if keyboard.is_pressed('esc') or keyboard.is_pressed('cmd+c'):
    #         print("Exiting...")
    #         exit()
    # except Exception as e:
    #     print(f"An error occurred: {e}")
    # finally:
    #     print("Thank you for using the Caesar Cipher!")




