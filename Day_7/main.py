"""
The Hangman Game

Save the little guy, by guessing the letters of a word before his life runs out.

"""
import random, os

import random
import os

def choose_random_word() -> str:
    """
    Import the words list from a separate file, and return a random word.
    
    Raises:
        FileNotFoundError: If 'word.txt' does not exist.
        ValueError: If 'word.txt' is empty.
    
    Returns:
        str: A randomly selected word from the file.
    """
    file_path = os.path.join(os.path.dirname(__file__), "word.txt")

    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError("The file 'word.txt' does not exist.")
        
        with open(file_path, "r") as file:
            words = file.read().splitlines()
        
        if not words:
            raise ValueError("The file 'word.txt' is empty.")
        
        return random.choice(words)
    
    except Exception as e:
        raise RuntimeError(f"Error selecting a random word: {e}")

def greetings(word: str) -> None:
    """
    Greet the player and ask them to start the game.
    """
    print("Welcome to Hangman!")
    print("Guess the secret word by guessing letters.")
    print("You have 7 lives.")
    print("Good luck!")

    print(f"The secret word has {word} letters.")

def revealed_letters(chosen_word: list, guessed_letters: list) -> str:
    """
    Reveal the word by replacing unknown letters with underscores.

    Args:
        word (str): The secret word to be guessed.
        guessed_letters (set): The set of letters guessed by the player.

    Returns:
        str: The word with the unknown letters replaced by underscores.
    """
    revealed_word = ""
    for letter in chosen_word:
        if letter in guessed_letters:
            revealed_word += letter
        else:
            revealed_word += "-"
    return revealed_word

if __name__ == "__main__":
    chosen_word = choose_random_word()
    guessed_letters = []
    
    lives = 7

    greetings(revealed_letters(chosen_word, []))
    while lives > 0:
        user_input = input("Guess a letter: ").lower()
        if len(user_input) != 1:
            print("Please enter only one letter.")
            continue
        else:
            guessed_letters.append(user_input)
        if user_input not in chosen_word:
            lives -= 1
            print(f"Sorry, '{user_input}' is not in the word.")
        else:
            print("Correct!")

        print(revealed_letters(chosen_word, guessed_letters))
        print(f"\nYou have {lives} lives left.")
        if lives == 0:
            print("\nYou're out of lives! Game over.")
            break