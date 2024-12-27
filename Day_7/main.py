"""
The Hangman Game

Save the little guy, by guessing the letters of a word before his life runs out.

"""
import random
import os
import graphics

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
    print("=" * 40)
    print("Welcome to Hangman!")
    print(f"{graphics.hangman}\n")
    print("YOUR GOAL IS TO SAVE THE LITTLE MAN BY GUESSING THE RIGHT LETTERS OF THE SECRET WORD BEFORE HIS 7 LIVES RUN OUT")
    print(f"The secret word {word} has total {len(word)} letters.")
    print("GOOD LUCK!")
    print("=" * 40)


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
        if len(guessed_letters) == len(chosen_word):
            print(f"\nCongratulations! You've guessed the word: {chosen_word}, and saved the little man🧍🏻‍♂️!")
            break

        user_input = input("Guess a letter: ").lower()
        if len(user_input) != 1:
            print("Please enter only one letter.")
            continue
        elif user_input in chosen_word:
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
            print(f"The secret word was: {chosen_word}")
            break