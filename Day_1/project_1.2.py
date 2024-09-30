"""
Wanderly Project - Insipered by Yara from the community to use ASCII art to create a simple game

"""

import random

print("Hello " + input("Hey Howdy, Welcome to the exciting game of Wanderly. How do I call you?\n") + ", Good day!")
print("""

 __      __                    .___           .__         
/  \    /  \_____    ____    __| _/___________|  | ___.__.
\   \/\/   /\__  \  /    \  / __ |/ __ \_  __ \  |<   |  |
 \        /  / __ \|   |  \/ /_/ \  ___/|  | \/  |_\___  |
  \__/\  /  (____  /___|  /\____ |\___  >__|  |____/ ____|
       \/        \/     \/      \/    \/           \/     

""")

res_1 = input("Would you like to know you lucky number for today [Y/N]?")
if (res_1.lower() == "y"):
    random_number = random.randint(0, 9)
    print(f"Your lucky number is: {random_number}")

else:
    print("Okay, no lucky number for you today.")
    print("\n")
print(f'Thanks for playing Wanderly.\nHave a good day')