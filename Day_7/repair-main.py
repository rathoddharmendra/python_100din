"""
The Hangman Game

Save the little guy, by guessing the letters of a word before his life runs out.

§ The Hangman Game expects a list of words in a file named 'word.txt'.

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


def get_revealed_letters(chosen_word: list, guessed_letters: list) -> str:
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

def ask_user_input() -> str:
    """
    Ask the user for a letter guess and return it.
    """
    user_input = ""
    while len(user_input) != 1:
        user_input = input("Guess a letter: ").lower()
        if len(user_input) == 1:
            return user_input
        print("Please enter only one letter.")
        
def reveal_match_graphics(res: bool, guessed_letters: str, lives) -> None:
    if res:
        print(f"Correct guess! Keep going!\nYou have guessed: {guessed_letters} and still have {lives} lives left.")
    else:
        print(f"\nIncorrect guess! \n So far, you've guessed: {guessed_letters} and have {lives} lives left.")
    
def restart():
    ask_user_input = input("\nDo you want to play again? (Y/N): ").lower()
    if ask_user_input == 'y':
        main()
    else:
        print("\nThanks for playing!")
        exit()


def check_round(lives, chosen_word, guessed_letters):
    """
    # Check if the player has won or lost the game
    """
    if lives <= 0:
        print("\nYou've lost! The secret word was:", chosen_word)
        print("GAME OVER GRAPHICS!")
        restart()
    elif len(guessed_letters) == len(chosen_word):
        print(f"\nCongratulations! You've guessed the word: {chosen_word}, and saved the little man🧍🏻‍♂️!")
        print("WINNING GRAPHICS!")
        restart()

def main():
    chosen_word = choose_random_word()
    guessed_letters = []
    lives = 7
    greetings(get_revealed_letters(chosen_word, []))

    def check_match(user_input, lives) -> bool:
        """
        Check if the user's input matches any letter in the chosen word, and update the guessed letters list accordingly. If incorrect guess, decrease the lives.

        Args:
            user_input (str): The letter guessed by the player.
        
        Returns:
            match (bool): True if the user's input matches any letter in the chosen word, False otherwise.
        """
        if user_input in chosen_word:
            guessed_letters.add(user_input) # appends here
            return True
        elif user_input not in chosen_word:
            lives -= 1 # takes live here
            return False

    # Game Loop Starts
    while lives > 0:
        user_input = ask_user_input()
        result = check_match(user_input, lives)
        reveal_match_graphics(result, guessed_letters, lives)
        check_round(lives, chosen_word, guessed_letters)

if __name__ == "__main__":
    main()