# https://appbrewery.github.io/python-day3-demo/

flag = False
commands = ['left', 'right', 'padel', 'knife', 'row', 'swim', 'stay', 'leave', 'follow her address', 'follow on your own']

def display_intro() -> None:
    """
    Display the game title and introduction.
    """
    print("""
        ___________.__            .___    _____          
        \_   _____/|__| ____    __| _/   /     \ ___.__. 
        |    __)  |  |/    \  / __ |   /  \ /  <   |  | 
        |     \   |  |   |  \/ /_/ |  /    Y    \___  | 
        \___  /   |__|___|  /\____ |  \____|__  / ____| 
            \/            \/      \/          \/\/      
        ___ ___                                        
        /   |   \  ____   _____   ____                  
        /    ~    \/  _ \ /     \_/ __ \                 
        \    Y    (  <_> )  Y Y  \  ___/                 
        \___|_  / \____/|__|_|  /\___  >                
            \/              \/     \/                 

    """)
    print(
    '''
            )
        (  (              .^.
            \) )           .'.^.'.
            (/          .'.'---'.'.
            _\)_       .'.'-------'.'.
        (__)()    .'.'-,=======.-'.'.
        (_)__)  .'.'---|   |   |---'.'.
        (__)_),'.'-----|   |   |-----'.'.
        ()__.'.'-------|___|___|-------'.'.
        (_.'.'---------------------------'.'.
        .'.'-------------------------------'.'.
        """""|====..====.=======.====..====|"""""
        ()_)|    ||    |.-----.|    ||    |
        (_)_|    ||    ||     ||    ||    |
        (...|____||____||_____||____||____|
        (_)_(|----------| _____o|----------|            ,,
        (_)(_|----------||     ||----------|           <' \ ____
        (__)(|----------||_____||----------|            "(  ( -_-<
        (_)(_|---------|"""""""""|---------|              \  _- /
        ()()(|--------|"""""""""""|--------|               )/ )/
    ||||||||||||||||||||||||||||||||||||||||||||||        -'--'-

''')
    print("Welcome to Dee's Adventure Game - FIND MY HOME!")
    print("=" * 40)
    print(
        "You find yourself lost in a mystical forest. Your goal is to reach your home back before sunset."
    )
    # print("- Type 'list commands' to see the available commands. ")
    # print("- Type 'list clues' to see what you've learned. ")
    # print("- Type 'help' to get more instructions. ")
    # print("Good luck!\n")
    # print("=" * 40)

def display_help() -> None:
    """
    Display the help information.
    """

    print("**** Help *****")
    print("Most commands are two parts, a verb and noun. Common verbs are:")
    print(" - examine  - use")
    print(" - take     - leave")
    print(" - go       - inspect")
    print("When examining something, use 'leave' to stop.")
    print("'inspect' things that might be clues. ")
    print(" * * * * ")

def display_game_over() -> None:
    """
    Displays Game Over logo
    """
    print('''
    
                                                         
        _________    _____   ____     _______  __ ___________ 
        / ___\__  \  /     \_/ __ \   /  _ \  \/ // __ \_  __ 
        / /_/  > __ \|  Y Y  \  ___/  (  <_> )   /\  ___/|  | \/
        \___  (____  /__|_|  /\___  >  \____/ \_/  \___  >__|   
        /_____/     \/      \/     \/                   \/       

''')

questions = [
    "You are walking in jungle, and see the road ahead is diverging ahead.\nYou can either go 'left' or 'right' to reach home. \nWhich one do you choose? ",

    "After walking a while, you find an old platform overlooking a lake.\nYou decide to check it out.\nHere you find two objects lying around wooden 'padel' and a 'knife'.\nWhich one do you pick? ",

    "The platform broke and you barely made it to the ground below.\nIn front of you, there is a lake. You find a small boat near the shore.\nDo you decide to 'row' the boat or 'swim' across the lake? ",

    "You crossed the lake and met a witch on the other side.She invites you to her home and asks to stay for the night.\nWould you 'stay' or 'leave' her home? ",

    "She tells you a scary story from the past and both of you go to sleep.\nNext morning, she offers to give you a map to lead to your home and laughs madly at you.You take the map, and leave the hut to not insult the witch.\nWould you 'follow her address' on the map or 'follow on your own' as you don't trust the wicked map? "
]
def ask_question(question : str) -> str:
    """
    Asks a question, checks against pre-defined answers and returns the choice selected by user.

    Args:
        question (string): current question to ask at the prompt

    Returns:
        response (string): response selected by the user
    """
    while True:
        response = input(question)
        if response in commands:
            break
        print("\nThat's doesn't work! Re-enter your choice again\n")
    print("*" * 40)
    return response


def main() -> None:
    """
    Main game loop
    """
    display_intro()
    
    response_1 = ask_question(questions[0])
    if response_1 == "right":
        print("You fell into kingdom of shadow. Game Over!")
        display_game_over()
        exit()
    else:
        clue_1 = ask_question(questions[1])
        print('''
                                        .__     
                ________________    _____|  |__  
                _/ ___\_  __ \__  \  /  ___/  |  \ 
                \  \___|  | \// __ \_\___ \|   Y  
                \___  >__|  (____  /____  >___|  /
                    \/           \/     \/     \/ 

        
        ''')
        while True:
            response_2 = ask_question(questions[2])
            if (clue_1 == "knife" and response_2 == "row"):
                print("You cannot row boat with a knife")

            elif not (clue_1 == "knife" and response_2 == "row"):
                break

        if response_2 == "swim":
            print("Lake is infested with crocodiles. You went straight into their tummy. Game Over!")
            display_game_over()
            exit()
        else:
            response_3 = ask_question(questions[3])
            if response_3 == "leave":
                print("It's dark outside and you fell in some trap. Game Over!")
                display_game_over()
                exit()
            else:
                response_4 = ask_question(questions[4])
                if response_4 == "follow on your own":
                    print("After troddding for while, you met a hungry lion. Game Over!")
                    display_game_over()
                    exit()
                else:
                    print('''
                    

            __  ______  __  __  ___   ___  ____  __ ______  __  _______  
            \ \/ / __ \/ / / / / _ | / _ \/ __/ / // / __ \/  |/  / __/  
            \  / /_/ / /_/ / / __ |/ , _/ _/  / _  / /_/ / /|_/ / _/    
            /_/\____/\____/ /_/ |_/_/|_/___/ /_//_/\____/_/  /_/___/    
                                                                        
                                                 
                                                                    
You walked following the map and finally see the known trodden path to your home.\nYou are filled with ecstacy and promise your self to visit the old lady to give your thanks.\nFor now, you are safe. This adventure can take another day. 

 __  __                   _    
 \ \/ /__  __ __  _    __(_)__ 
  \  / _ \/ // / | |/|/ / / _ 
  /_/\___/\_,_/  |__,__/_/_//_/
                               



                    ''')

        









if __name__ == "__main__":
    main()