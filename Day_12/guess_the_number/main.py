from art import logo, rules
import random, os
# pseudo code:

def greetings():
    print(logo)
    print(rules)

def decide_level() -> int:
    # This function will return the number of attempts based on the difficulty level chosen by the player
    level = input("Choose a difficulty level (easy, medium, hard): ").lower()
    if level == "easy":
        attempts = 10
    elif level == "medium":
        attempts = 5
    else:
        attempts = 3
    return attempts

def decide_win(secret_number: int, guess: int) -> int: 
    # This function will return True if the player wins, False otherwise
    # You can implement the logic here
    if secret_number == guess:
        return 0
    elif guess > secret_number:
        return 1
    else:
        return -1
        
def play():
    greetings()
    # initialize secret_number
    secret_number = random.randint(1, 100)

    # sets the attempts based on the chosen difficulty level
    attempts = decide_level()

    while attempts > 0:
        print(f"You have {attempts} attempts left to guess the number.")
        guess = int(input("Make a guess: "))
        attempts -= 1
        res = decide_win(secret_number, guess)
        if res == 0:
            print("Congratulations! You've guessed the right number.")
            return
        elif res == 1:
            print("Too high! Try again.")
            continue
        else:
            print("Too low! Try again.")

        if attempts == 0:
            print("Sorry, you've run out of attempts. The number was:", secret_number)
            return


    
if __name__ == "__main__":
    # new_learnen - best setup for the game loop and clears the screen before each game
    while input("Do you want to play the Number Guess Game? (y/n): ").lower() == 'y':
        os.system('clear')  # Clear the terminal before starting a new game
        play()
    print("Thanks for playing! \n Good bye! 😊")