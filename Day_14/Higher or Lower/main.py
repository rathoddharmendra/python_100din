
import random, os
from game_data import data
from art import logo, vs, rules

def greetings():
    print(logo)
    print(rules)

def select_random_name() -> dict:
    return random.choice(data)


def select_accounts(name_one:dict) -> tuple:
    if name_one:
        name_one = name_one.copy()
    else:
        name_one = select_random_name()

    name_two = select_random_name()
    if name_two["name"] == name_one["name"]:
        name_two = select_random_name()

    return name_one, name_two

def play_round(name_one:dict) -> tuple: 
    name_one, name_two = select_accounts(name_one)
    
    print(f"\n\nCompare A: {name_one["name"]}, a {name_one["description"]}, from {name_one["country"]}")
    print(vs)
    print(f"Against B: {name_two["name"]}, a {name_two["description"]}, from {name_two["country"]}\n")

    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    #check winner 

    round_winner = name_one if name_one["follower_count"] > name_two["follower_count"] else name_two

    # print(f"Round Result: A - {name_one["name"]} has {name_one["follower_count"]} millions followers vs B - {name_two["name"]} who has {name_two["follower_count"]} millions followers\n")
        
    if user_choice == 'a' and round_winner["name"] == name_one["name"] or user_choice == 'b' and round_winner["name"] == name_two["name"]:
        result = True
        return round_winner, result
    else:
        result = False
        return None, result

def play():
    score = 0
    is_game = True
    name_one = None

    greetings()

    while is_game:
        round_winner, result = play_round(name_one)
        if result:
            score += 1
            name_one = round_winner
            print(f"\nCongratulations! You've won this round. Your  score is {score}\n")
        else:
            print(f"\nYou loose, and your final score is {score}\n")
            return
            

if __name__ == "__main__":
    while input("Do you want to play? y/n ").lower() == "y":
        os.system("clear")
        play()
    print("Thanks for playing")
            






