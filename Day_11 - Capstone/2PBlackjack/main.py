from art import logo, win, draw, loose
import random, time, os
def greetings():
    print("Welcome to the Bidding Game!")
    print(logo)

def deal_card() -> list:
    """
    Deal a single card to the player and computer.
    """
    card_list = [11,1,2,3,4,5,6,7,8,9,10,10,10,10] # Initialize a list of card values
    return random.choice(card_list)

def checks_total(players_cards: list, computers_cards: list) -> tuple:
    """
    Calculates the total points for both players and computers.
    """
    return sum(players_cards), sum(computers_cards)

def display_cards(players_cards: list, computers_cards: list) -> None:
    """
    Display player's and computer's cards.
    """
    # os.system('clear')
    players_score, computers_score = checks_total(players_cards, computers_cards)
    print(f"Your cards: {players_cards}, current score: {players_score}")
    print(f"Computer's first card: {computers_cards[0]}")
    print("\n")

def player_turn(players_cards: list, computers_cards: list, player_turn: bool = True) -> bool:
    """
    Handles player's turn.
    """
    def is_player_busted() -> bool:
        if sum(players_cards) > 21:
            return True

    while player_turn:
        #checks every turn until player's score is 21 or busts
        if is_player_busted():
            break

        want_to_play = input("Do you want to hit or stand? (h/s): ").lower()
        if want_to_play == 'h':
            players_cards.append(deal_card())
            display_cards(players_cards, computers_cards)
            
        else:
            player_turn = False
            print(f"\nPlayer stands. Now it's Dealer's turn... \n {'*' * 40}")
            time.sleep(2)

    if is_player_busted():
        print("Busted! You lose.")
        return True

def computer_turn(players_cards: list, computers_cards: list) -> None:
    def is_computer_busted() -> bool:
        if sum(computers_cards) > 21:
            return True

    def display_dealers_card():
        # os.system('clear')
        print(f"Your cards: {players_cards}, current score: {sum(players_cards)}")
        print(f"Dealers's cards: {computers_cards}, dealers's current score: {sum(computers_cards)}")
        print("\n")
    # Dealer hits until his score is 17 or more
    while sum(computers_cards) < 17 and not is_computer_busted():
        print(f"Dealer hits...")
        time.sleep(1)  # delay for user to see the dealer's card
        computers_cards.append(deal_card())
        display_dealers_card()
        
    # one more turn to computer based on a random number
    # makes game interesting for user, and increases their chances of winning
    if random.random() > 0.7 and sum(computers_cards) < 19:
        print(f"Dealer takes the risk and hits again...")
        time.sleep(3)  # delay for user to see the dealer's card
        computers_cards.append(deal_card())
        display_dealers_card()

    if is_computer_busted():
        time.sleep(2) # delay for user to see the computer
        print(f"Whoo Hoooo! Dealer Busted! You Win\nDealers's Final card are : {computers_cards}, and dealer went above 21 with final score: {sum(computers_cards)}")
        return True

def main():
    
    computers_cards = []
    players_cards = []
    greetings()

    # Deal initial cards to players
    players_cards.append(deal_card())
    players_cards.append(deal_card())

    computers_cards.append(deal_card())
    computers_cards.append(deal_card())

    # Print initial cards
    display_cards(players_cards, computers_cards)
    # Game loop for player_1:
    if player_turn(players_cards, computers_cards):
        print(loose)
        return
    # Game loop for computer:
    if computer_turn(players_cards, computers_cards):
        print(win)
        return
    # Check if player or computer won
    if sum(players_cards) > sum(computers_cards):
        print(win)
    elif sum(players_cards) == sum(computers_cards):
        print(draw)
    else:  # computer wins
        print(loose)


if __name__ == "__main__":
    # Check if player wants to play
    while input("Do you want to play Blackjack? (y/n): ").lower() == 'y': # new_learnen - using input and game loop, instead of setting a boolean flag
        os.system('clear')  # Clear the terminal before starting a new game
        main()
  
    print("Thanks for playing!")
            

    