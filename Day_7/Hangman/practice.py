import random, time

word_list = ["apple", "banana", "cherry", "date", "elderberry"]

chosen_word = list(random.choice(word_list))
guessed_letters_list = list("_" * len(chosen_word))
lives = 7


while lives > 0:
    user_input = input("Guess a letter: ").lower()
      
    if user_input in chosen_word:
        if user_input in guessed_letters_list:
            print("You've already guessed that letter.")
        else:
            print("Correct! You have guessed it right") # continue
            # update_guessed_letters
            for i in range(len(chosen_word)):
                if chosen_word[i] == user_input:
                    guessed_letters_list[i] = user_input
                #  if won, break game if all letters guessed
            if "_" not in guessed_letters_list:
                    time.sleep(2) # 2 secs sleep
                    print(f"Congratulations! You've guessed the word {" ".join(guessed_letters_list)}.")
                    break

    else:
        print("Incorrect guess!")
        lives -= 1
        if lives == 0:
            print(f"You've lost. The word was {" ".join(guessed_letters_list)}.")
            break

    print(" ".join(guessed_letters_list))
    print(f"Lives left: {lives}")