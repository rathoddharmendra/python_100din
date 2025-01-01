# import random

# # Randomly select a word from a file
# # Ask user for a letter guess
# # guess the letter in the chosen word
#   # If Yes, reveal the letter in the word and update the guessed letters 
#          # Check if the player has won 
#   # If No, subtract 1 life from the player
#   # Display the word with unknown letters and the remaining lives

# # check users live 
#     # If lives are 0, display a message and end the game
#     # If lives are not 0, prompt the user to continue playing

# word_list = ["apple", "banana", "cherry", "date", "elderberry"]

# def choose_word():
#     return random.choice(word_list)


# def play_hangman():
#     word = list(choose_word())
#     guessed_letters = []
#     lives = 7

#     while lives > 0:

#         print("Guess the word:")
#         print(" ".join(letter if letter in guessed_letters else "_" for letter in word))
#         guessed_letters_string = " ".join(guessed_letters)
#         print(f"")
#         guess = input("Enter a letter: ").lower()

#         if guess in guessed_letters:
#             print("You've already guessed that letter.")
#         elif guess in word:
#             guessed_letters.append(guess)
#         else:
#             lives -= 1
#             print(f"Incorrect guess. You have {lives} lives left.")

#         if "_" not in word:
#             print("Congratulations! You've guessed the word.")
#             break

#     if lives <= 0:
#         print("You've lost. The word was:", word)


