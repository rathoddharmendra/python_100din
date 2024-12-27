# Design Document:

## Requirements:
1. When the game starts, it displays greetings, rules, and other relevant information for the user.  
2. The actual game starts by asking the user for input.  
3. The system displays whether the input is correct or not by comparing it against the random word.  
4. If the user provides a wrong input, one life is deducted; if the input is correct, the life count remains the same.  
5. If the user guesses all the correct letters in the word before running out of lives, they win.  
6. Otherwise, they lose, and the game asks if they want to play again.  

#### Rules:
1. If the input is correct, the system displays the partial answer using dashes and the revealed letters.  
2. If the input is wrong, one life is deducted from the life count.  
3. If the user guesses all the correct letters in the word before running out of lives, they win.  

---

## Design steps:
1. The user starts the game.  
2. The system displays greetings, the rules of the game, and hints such as the number of letters in the chosen word.  
   - **Pre-requisite:** The system generates a random word.  
3. The system asks the user to enter a letter and waits for the input.  
4. The system checks the user’s input against the chosen word.  
   - **If correct:** display correct   
   - **If incorrect:** Deducts one life and display wrong
5.  Display live left and reveal the opened letters (e.g., `---x---`).
6. The system checks the life count:  
   - **If won:** Ends the game with a WIN message and offers the option to play again or quit.  
   - **If lives > 0:** Displays the current number of lives.  
   - **If lives = 0:** Ends the game with a LOSS message and offers the option to play again or quit.  



---

#### Pre-requisite Materials:
1. Icons to display during the game.  
2. Messages to display for specific conditions.  

---

### Backend Steps - Required Functions:
1. **Greetings Function**  
   - Greets the user, explains the rules, displays the current life count, and provides hints (e.g., the number of letters in the word).  

2. **Word Generator**  
   - Generates a random word.  

3. **User Input**  
   - Takes user input and validates it.  

4. **Check Function**  
   - Compares the input with the word:  
     - If matched, displays "Correct."  
     - If incorrect, deducts one life and displays "Incorrect guess."  

5. **Display Function**  
   - Reveals the letters guessed so far, and life count


6. **Check Round**  
   - Determines the game status:  
     - **If won:** Ends the game with a WIN message.  
     - **If lives > 0:** Continues the game.  
     - **If lives = 0:** Ends the game with a LOSS message.  
---
### Flow Chart

![alt text](image-1.png)

### Pseudo Code
```
def generate_random_word:
    - try:
      - read a list from from the file
    - exception:
    - randomly choose one
    - return chosen_word

def greetings():
    print "banner"
    print how to play -- search online
    show live count
    show --- letters , and letter count

def user_input:
    user_input = input("Enter a letter: ")
    if len(user_input) != 1:
       try again
    if user_input not in alphabet:
        try again

    return user_input

check_match(user_letter):
    if letter in chosen_word:
        print corrent 
    else print incorrect
variable: letter

def display_function():
    if guessed_word_list in chosen_word:
        print "letter"
    else:
        print --
    print(live count)
    
check_round(lives, won_or_not_status):
    if won_or_not_status == True:
        display won
        break
    elif lives < 0:
        display lost
        break
    else:
        continue

def continue():
    ask_user = input("Do you want to continue? (y/n): ")
    if ask_user.lower() == y:
        main()
    else:
        quit()
```


