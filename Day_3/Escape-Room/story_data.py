from typing import Any, Dict

# Define the rooms and options
rooms: Dict[str, Dict] = {
    "locked_room": {
        "description":
        "You are in a locked room. There is a large table in the middle of the room. "
        "There is a door to the north.",
        "options": {
            "go north": "You need to use the key to open the door.",
            "use key": "You use the key to unlock the door.",
            "examine table": "You take a close look at the table.",
            "look around":
            "You see a large dusty table with some papers on it. "
            "There is a crumped note on the floor. ",
            "inspect note":
            "The note reads 'Find the truth, or be lost forever.'",
        },
        "required_items": {
            "use key": "key"
        },
        "next_room": {
            "use key": "hallway",
            "examine table": "large_table"
        },
        "items": [],
        "clues": ['note']
    },
    "large_table": {
        "description":
        "As you look closer, you notice a key under the papers.",
        "description_no_items": "Large table with yellowed papers.",
        "options": {
            "leave table":
            "You finish examing the table",
            "look around":
            "The dusty table has papers that are so yellowed with age, "
            "they can't be read. ",
            "examine papers":
            "The papers are orders for medical and office supplies. ",
        },
        "required_items": {},
        "next_room": {
            "leave table": "locked_room"
        },
        "items": ["key"],
        "clues": []
    },
    "hallway": {
        "description":
        "You are in a hallway. There is a door to the north, south, east and west. ",
        "options": {
            "go north":
            "You go through the door to the north.",
            "go west":
            "You go through the door to the west.",
            "go south":
            "You go through the door to the south. The door locks again.",
            "go east":
            "You go through the door to the east.",
            "examine table":
            "There is a secret drawer under the side table.",
            "look around":
            "A side table sits on the east wall of the room. "
            "There is a photograph hanging on the west wall.",
            "inspect photograph":
            "A photograph shows you shaking hands with a "
            "man in a lab coat, with the caption, 'Project Genesis - 2023.'",
        },
        "required_items": {},
        "next_room": {
            "go north": "office",
            "go west": "storage_room",
            "go south": "locked_room",
            "go east": "break_room",
            "examine table": "side_table"
        },
        "items": [],
        "clues": ['photograph'],
    },
    "side_table": {
        "description": "You pry open the secret drawer and see a flashlight.",
        "description_no_items": "The secret drawer is empty.",
        "options": {
            "leave table": "Closing the drawer. You stand up.",
            "look around": "The side table is well worn.",
        },
        "required_items": {},
        "next_room": {
            "leave table": "hallway"
        },
        "items": ['flashlight'],
        "clues": []
    },
    "break_room": {
        "description":
        "What looks like a breakroom. "
        "It's bright room with some tables and chairs. "
        "There is a coffee machine, fridge and sink. "
        "The doors are to the west and east. ",
        "options": {
            "go east":
            "You go through the door to the east.",
            "go west":
            "You go through the door to the west.",
            "look around":
            "A bulletin board on the wall has various notices pinned to it. ",
            "inspect bulletin":
            "One notice reads, 'Staff Meeting - Discussing the ethical "
            "implications of Project Genesis.' ",
            "examine coffee machine":
            "There is a little cold coffee left. ",
            "examine fridge":
            "It's mostly empty except for a half eaten sandwich. ",
            "examine sink":
            "A dirty coffee mug is waiting to be washed. "
        },
        "required_items": {},
        "next_room": {
            "go east": "lab",
            "go west": "hallway"
        },
        "items": [],
        "clues": ['bulletin'],
    },
    "storage_room": {
        "description":
        "You are in a storage room. There is a door to the east. ",
        "options": {
            "go east":
            "You leave the storage room and return to the hallway.",
            "examine cabinet":
            "You turn the flashlight on and open the cabinet.",
            "examine bookshelf":
            "You take a close look at the bookshelf. ",
            "look around":
            "You see various items scattered around. "
            "There is a tall cabinet against the wall. "
            "A filled bookshelf is standing next to the door. ",
        },
        "required_items": {
            "examine cabinet": "flashlight"
        },
        "next_room": {
            "go east": "hallway",
            "examine cabinet": "file_cabinet",
            "examine bookshelf": "storage_bookshelf",
        },
        "items": ["vest"],
        "clues": []
    },
    "file_cabinet": {
        "description": "There are 2 drawers filled with folders.",
        "options": {
            "look around": "The papers are old and yellowed. "
            "Most of these papers mention a Doctor H.",
            "leave cabinet":
            "Turning the flashlight off, you close the cabinet."
        },
        "required_items": {},
        "next_room": {
            "leave cabinet": "storage_room"
        },
        "items": [],
        "clues": []
    },
    "storage_bookshelf": {
        "description": "The shelves are filled with neurology books. ",
        "options": {
            "look around":
            "Besides the many books on neurology, there is a handwritten journal. ",
            "leave bookshelf":
            "Maybe there's more information in other rooms.",
            "inspect journal":
            "A journal on the bookshelf details experiments on "
            "memory manipulation, with entries signed by 'Dr. H.'",
        },
        "required_items": {},
        "next_room": {
            "leave bookshelf": "storage_room",
        },
        "items": [],
        "clues": ['journal'],
    },
    "office": {
        "description": "A cluttered office with papers strewn everywhere. "
        "There is a door to the east and south.",
        "options": {
            "look around":
            "A computer screen flickers with an unfinished email. ",
            "go east":
            "You go through the door on the east.",
            "go south":
            "You go through the door on the south.",
            "inspect email":
            "The email reads, 'We must keep the subject contained "
            "until we can reverse the process. The memories are too dangerous.' ",
        },
        "required_items": {},
        "next_room": {
            "go east": "front_office",
            "go south": "hallway"
        },
        "items": [],
        "clues": ['email']
    },
    "front_office": {
        "description":
        "There is a door to west behind the counter. "
        "A metal door is to the south. "
        "And a double door to the east with a keypad. ",
        "options": {
            "go west":
            "You need the keycard to open the door.",
            "go east":
            "You go through the door on the west.",
            "go south":
            "You go through the door on the south.",
            "look around":
            "This is a big room with a long counter. "
            "On the counter is a computer, and a phone. "
            "There is a single drawer. ",
            "examine phone":
            "The line is dead. ",
            "examine computer":
            "The computer is locked. ",
            "examine drawer":
            "You open the drawer. ",
            "use keycard":
            "You swipe the keycard on the panel.",
        },
        "required_items": {
            "use code": 'code',
        },
        "next_room": {
            "examine drawer": "front_office_drawer",
            "go west": "office",
            "go south": "lab",
            "use keycard": "freedom",
        },
        "items": [],
        "clues": []
    },
    "front_office_drawer": {
        "description": "The drawer has a keycard.",
        "description_no_items":
        "The drawer is filled with regular office supplies. ",
        "options": {
            "look around": "Plenty of office supplies. ",
            'leave drawer': 'You close the drawer. ',
        },
        "required_items": {},
        "next_room": {
            'leave drawer': 'front_office'
        },
        "items": ['keycard'],
        "clues": []
    },
    "lab": {
        "description":
        "A sterile lab with various scientific instruments and vials."
        "A whiteboard has a complex diagram of the human brain."
        "There is a door to the north and west.",
        "options": {
            "go north":
            "You go through the door on the north.",
            "go west":
            "You go through the door on the west.",
            "look around":
            "A whiteboard has a complex diagram of the human brain."
            "On the lab table is a clipboard with documents. ",
            "inspect clipboard":
            "A document on the clipboard reveals that you were "
            "part of an experiment to erase traumatic memories, but something "
            "went wrong. "
        },
        "required_items": {},
        "next_room": {
            "go north": "front_office",
            "go west": "break_room",
        },
        "items": [],
        "clues": ['clipboard'],
    },
    "freedom": {
        "description": "Hurray! You made it, and you are outside. You are free!",
        "options": {},
        "required_items": {},
        "next_room": {},
        "items": [],
        "clues": []
    },
}
