from matplotlib.style.core import available

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# def insert_coin() -> float:
#     print("Please insert coins now...")
#     total = 0
#     # ask the user for coins
#     quarter = int(input("how many quarters? "))
#     dime = int(input("how many dimes? "))
#     nickel = int(input("how many nickels? "))
#     cents = int(input("how many cents? "))
#     # Convert coin values to cents and add them to total
#     total = quarter * 0.25 + dime * 0.10 + nickel * 0.05 + cents * 0.01
#     return float(total/100)

def take_order():
    machine_powered_on = True
    while machine_powered_on:

        # TODO: 1. TAKE ORDER - PROMPT
        order = input("What would you like to order (latte/espresso/cappuccino/): ").lower()

        if order == "report":
            coffee_maker.report()
            money_machine.report()
            continue

        if order == "off":
            machine_powered_on = False
            print("\n💤💤Turning the coffee machine off...💤💤")
            break

        # TODO: 3. CREATE LOOP TO TAKE VALID ORDER
        menu_order = menu.find_drink(order)
        if menu_order is None:
            print(f"Couldn't find anything with name {order} to in menu. Try again...")
            continue

        # # TODO: 2. CHECK IF THE RESOURCES ARE AVAILABLE - IF NOT, DISPLAY ERROR MESSAGE AND GO TO PROMPT
        # if not coffee_maker.is_resource_sufficient(menu_order):
        #     print("Not enough resources to make this order. Try another drink..")
        #     continue

        # # TODO: 4. INSERT COIN AND PROCESS IT - IF NOT ENOUGH MONEY, DISPLAY ERROR MESSAGE AND GO TO PROMPT
        # if not money_machine.make_payment(menu_order.cost):
        #     print("Not enough money. Money refunded. Try another option...\n")
        #     continue
        # # TODO: 5. MAKE COFFEE AND UPDATE RESOURCES
        # coffee_maker.make_coffee(menu_order)

        # TODO: 2. CHECK IF THE RESOURCES ARE AVAILABLE - IF NOT, DISPLAY ERROR MESSAGE AND GO TO PROMPT
        if coffee_maker.is_resource_sufficient(menu_order) and money_machine.make_payment(menu_order.cost):
        # TODO: 5. MAKE COFFEE AND UPDATE RESOURCES
            coffee_maker.make_coffee(menu_order)


if __name__ == "__main__":
    # initializing classes
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()

    take_order()



