from typing import Any, Dict

from story_data import rooms

# Text-based game script

# Define the game state
game_state: Dict[str, Any] = {
    "current_room": "locked_room",
    "inventory": [],
    "clues": set(),
}


def check_inventory(item: str) -> bool:
    """
    Check if an item is in the player's inventory.

    Args:
        item (str): The item to check.

    Returns:
        bool: True if the item is in the inventory, False otherwise.
    """
    return item in game_state["inventory"]


def process_command(command: str) -> None:
    """
    Process a player's command.

    Args:
        command (str): The command entered by the player.
    """
    current_room = game_state["current_room"]
    room = rooms[current_room]

    # check if the command is available in this room
    if command in room["options"]:
        # Check if it requires an item
        if command in room["required_items"]:
            # check if the player has the item
            required_item = room["required_items"][command]
            if not check_inventory(required_item):
                print(f"You need {required_item} to do that.")
                return
        # display the results of the command
        print(room["options"][command])
        # Does the command lead to another space? Move there
        if command in room["next_room"]:
            game_state["current_room"] = room["next_room"][command]
    else:
        # not available? invalid command
        print("Invalid command.")


def update_room_description(room: Dict) -> str:
    """
    Update the room description based on items taken.

    Args:
        room (dict): The current room's data.

    Returns:
        str: The updated room description.
    """
    if "description_no_items" in room and all(item in game_state["inventory"]
                                              for item in room["items"]):
        return room["description_no_items"]
    return room["description"]


def list_actions() -> None:
    """
    List the current verbs available for use as commands in the game.
    """
    current_room = game_state["current_room"]
    room = rooms[current_room]

    actions = list(room["options"].keys())
    print("Available commands:")
    for action in actions:
        print(f"- {action}")
    print("- inventory")
    print("- list commands")
    print("- list clues")
    print("- help")


def list_inventory() -> None:
    """
    List the inventory player is holding.
    """

    inventory = game_state["inventory"]

    if not inventory:
        print("You don't have anything.")
        return

    print("You have:")
    for item in inventory:
        print(f"- {item}")


def list_clues() -> None:
    """
    List the clues that have been found.
    """

    clues = game_state["clues"]

    if not clues:
        print("You haven't found anything yet. ")
        return

    print("You found:")
    for _, message in clues:
        print(f"- {message}")


def display_intro() -> None:
    """
    Display the game title and introduction.
    """
    print(r"""
  ______    __                                         
 /_  __/   / /_   ___                                  
  / /     / __ \ / _ \                                 
 / /     / / / //  __/                                 
/_/     /_/ /_/ \___/                                  
                                                       
    ______                                             
   / ____/   _____  _____  ____ _    ____   ___        
  / __/     / ___/ / ___/ / __ `/   / __ \ / _ \       
 / /___    (__  ) / /__  / /_/ /   / /_/ //  __/       
/_____/   /____/  \___/  \__,_/   / .___/ \___/        
                                 /_/                   
    ____                                               
   / __ \  ____   ____    ____ ___                     
  / /_/ / / __ \ / __ \  / __ `__ \                    
 / _, _/ / /_/ // /_/ / / / / / / /                    
/_/ |_|  \____/ \____/ /_/ /_/ /_/                     
                                                       
""")
    print("Welcome to the Text-Based Adventure Game!")
    print("=" * 40)
    print(
        "You find yourself locked in a mysterious room. Your goal is to find a way out."
    )
    print("- Type 'list commands' to see the available commands. ")
    print("- Type 'list clues' to see what you've learned. ")
    print("- Type 'help' to get more instructions. ")
    print("Good luck!\n")


def display_win_game() -> None:
    """
    Display the game win screen.
    """

    count_of_clues = 0
    for room in rooms.values():
        count_of_clues += len(room['clues'])

    print(f"{'*'*19}")
    print("*  You've escaped! *")
    print(f"{'*'*19}")

    clues_found = len(game_state['clues'])
    print(f"You've found {clues_found} out of {count_of_clues} clues.")

    if clues_found == count_of_clues:
        print(
            "As you piece together the clues, you realize that you were a test "
            "subject in an experiment gone awry. The scientists were trying to "
            "erase traumatic memories, but instead, they locked you in a loop "
            "of confusion. With the code in hand, you unlock the front door and "
            "step into the sunlight, free but forever changed by what you "
            "discovered.")


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


def main() -> None:
    """
    Main game loop.
    """
    display_intro()

    while True:
        current_room = game_state["current_room"]
        room = rooms[current_room]

        print(update_room_description(room))

        # did they win? exit
        if current_room == "freedom":
            display_win_game()
            break

        # get command from user
        print('_' * 25)
        command = input("> ").strip().lower()

        # if a take command, check if the item is here,
        # otherwise can't grab it
        if command.startswith("take "):
            item = command.split(" ", 1)[1]
            if item in room["items"]:
                game_state["inventory"].append(item)
                room["items"].remove(item)
                print(f"You take the {item}.")
            else:
                print(f"There is no {item} here.")

        elif command.startswith("inspect "):
            item = command.split(" ", 1)[1]
            if item in room["clues"]:
                game_state["clues"].add((item, room["options"][command]))
                # room["items"].remove(item)
                print(f"You read the {item}.")
                print(room["options"][command])
            else:
                print(f"There is no {item} here.")

        elif command == "list commands":
            list_actions()
        elif command == "list clues":
            list_clues()
        elif command == "inventory":
            list_inventory()
        elif command == "help":
            display_help()
        else:
            # handle other commands
            process_command(command)


if __name__ == "__main__":
    main()
