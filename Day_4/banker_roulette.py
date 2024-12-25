'''
This script generates a random friend's name and greets them with a randomly selected greeting.

Extensively uses random.choice() to randomly select an item from a list.
The function pick_a_friend() returns a randomly selected friend from the list of available friends.
The function greet_friend() prints a randomly selected greeting along with the friend's name.

To run this script, you can save it in a file named "random_greeting.py" and run it using Python:

This script will output something like:
Hey, David! You are lucky and can our bills today ��!
'''
import random

def pick_a_friend() -> str:
    """
    Pick a random friend from the list of available friends.
    """

    friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
    return random.choice(friends)


def greet_friend(friend_name: str) -> None:
    """
    Greet a friend with a randomly selected greeting.
    """

    greetings = ["Hello", "Hi", "Hey", "Greetings", "Salutations"]
    print(f"{random.choice(greetings)}, {friend_name}! You are lucky and can our bills today 😂!",)
    
if __name__ == "__main__":
    friend_name = pick_a_friend()
    greet_friend(friend_name)