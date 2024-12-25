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