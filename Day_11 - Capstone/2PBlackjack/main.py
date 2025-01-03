from art import logo
import random
def greetings():
    print("Welcome to the Bidding Game!")
    print(logo)

def deal_card() -> list:
    """
    Deal a single card to the player and computer.
    """
    card_list = [11,1,2,3,4,5,6,7,8,9,10,10,10,10] # Initialize a list of card values
    return random.choice(card_list)

def check_next_move(players_cards: list, computers_cards: list) -> str:
    """
    Recommends next move based on the player's and computer's cards.
    """
    pass


def main():
    computers_cards = []
    players_cards = []
    greetings()
