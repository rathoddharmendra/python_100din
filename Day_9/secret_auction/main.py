import os
from art import logo, rules

bidding_results = {}

def greetings():
    print("Welcome to the Bidding Game!")
    print(logo)
    print(rules)

def clear_screen():
    os.system('clear')

def ask_bid() -> None:
    name = input("Enter your name: ")
    bid_amount = int(input("Enter your bid amount: $"))
    bidding_results[name] = bid_amount

def display_bidding_results(bidding_results: list) -> None:
    bid_amount = 0
    winner_name = ""
    for key, value in bidding_results.items():
        if bid_amount < value:
            winner_name = key
            bid_amount = value
    print(f"The winner is: {winner_name} and has bid ${bid_amount}")
    # highest_bidder = max(bidding_results, key=bidding_results.get)
    # print(f"The winner is: {highest_bidder} and has bid ${bidding_results[highest_bidder]}")

if __name__ == '__main__':
    greetings()
    continue_bidding = True
    while continue_bidding:
        ask_bid()
        is_continue = input("Do you have any more bid? (y/n): ").lower()
        if is_continue != 'y':
            continue_bidding = False
        clear_screen()

    # Display the winner bid
    display_bidding_results(bidding_results)
