"""
Play RPS game in retro mode

uses play_rps function to take user's choice and decides the winner
"""
import random
import rps_ascii
def play_rps():
    """
    Function to play Rock, Paper, Scissors game.
    Uses user's choice and computer's random choice to determine the winner.
    Logic submitted from ![https://wrpsa.com/](WRPSA)
    Args:
        None 
    """
    print("Welcome to Rock, Paper, Scissors!")

    user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor \n")
    user_choice = int(user_input)
    if user_choice < 0 or user_choice > 2:
        print("Invalid choice. Please choose again.")
        return play_rps() #new_learnen - using return to restart function to play again

    computer_choice = random.randint(0, 2)

    print("\n##########Game Begins!##########")
    print(f"You chose: {user_choice}\n\n {rps_ascii.rps_dict[user_choice]}")
    print(f"Computer chose: {computer_choice}\n\n {rps_ascii.rps_dict[computer_choice]}")

    if (user_choice == 0 and computer_choice == 2 or user_choice == 1 and computer_choice == 0 or user_choice == 2 and computer_choice == 0):
        print(rps_ascii.win)
    elif(user_choice == computer_choice):
        print(rps_ascii.draw)
    else:
        print(rps_ascii.loose)


if __name__ == "__main__":
    play_rps()




