import os

# TODO: 7. Declare drink options
drinks = {
    "espresso" : {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "sugar": 0,
            "cream": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
            "sugar": 6,
            "cream": 10,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
            "sugar": 12,
            "cream": 8,
        },
        "cost": 3.0,
    },
}  

# TODO: 6. Declare coffee resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "sugar": 150,
    "cream": 50,
    "money": 0
}

def check_resources(user_prompt) -> bool:
    drink = drinks[user_prompt]
    for ingredient, required in drink["ingredients"].items():
        if resources[ingredient] < required:
            return False
    return True

def insert_coin() -> float:
    print("Please insert coins now...")
    total = 0
    quarter = int(input("how many quarters? "))
    dime = int(input("how many dime? "))
    nickel = int(input("how many nickel? "))
    cents = int(input("how many cents? "))
    total = quarter * 25 + dime * 10 + nickel * 5 + cents * 1
    return float(total/100)

def process_coin(user_prompt) -> float:
    coins = insert_coin()
    change = 0
    # checks against the cost
    if coins >= drinks[user_prompt]["cost"]:
        change = coins - drinks[user_prompt]["cost"]
        print(f"Here is ${change} in change..")
    else:
        print("Sorry that's not enough money. Money refunded. Try another option...\n")
    return change

# TODO: 8. Deduct coffee resources
# TODO: 5. Make coffee
def make_coffee(user_prompt) -> None:
    for ingredient, required in drinks[user_prompt]["ingredients"].items():
        resources[ingredient] -= required
    
    print(f"Here is your {user_prompt} ☕️. Enjoy!")
    # TODO: 10. Update profit
    resources["money"] += drinks[user_prompt]["cost"] 

# TODO: 1. Print report of all coffee resources
def print_report():
    print("Coffee resources report:")
    print("-------------------------")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Sugar: {resources['sugar']}g")
    print(f"Cream: {resources['cream']}g")
    print(f"Money: ${resources['money']}")
    print("-------------")

# TODO: 4. Ask for user prompt

if __name__ == "__main__":
    is_continue = True
    os.system("clear")
    while is_continue:
        
        user_prompt = input("​What would you like? (espresso/latte/cappuccino): ​")
        if user_prompt in [drink for drink in drinks]:
            # TODO: 3. Check resources
            if check_resources(user_prompt):
                # TODO: 2. Insert coin and process them
                change = process_coin(user_prompt)
                if change == 0:
                    continue
                else:
                    make_coffee(user_prompt)
            else:
                print(f"Sorry there is not enough resources for {user_prompt}. Try another option..")
        elif user_prompt.lower() == "report":
            print_report()
        elif user_prompt.lower() == "off":
            print("Turning off the coffee machine..")
            is_continue = False
        else:
            print("Invalid option. Please try again.")