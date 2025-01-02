# def greetings(word: str) -> None:
#     """
#     Print a greeting message with the given word.

#     Args:
#         word (str): The word to be used in the greeting.
#     """
#     print(f"Hello, {word}! Good day!")

# if __name__ == "__main__":
#     greetings("Dee")


def greet_with(name: str, location: str = "No-Where") -> None:
    """
    Print a greeting message with the given name and location.

    Args:
        name (str): The name of the person to greet.
        location (str): The location where the greeting will be made.
    """
    print(f"Greetings, {name}! How is like to live in {location}?")


if __name__ == "__main__":
    greet_with("Alice", "New York") # positional arguments
    greet_with(name="Bob") # keyword arguments