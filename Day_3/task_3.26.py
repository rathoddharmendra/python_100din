#Pizza Order Automation

size = input("Choose the size of your pizza? S, M or L ")
is_pepperoni = input("Do you want to add pepperoni? Y/N ")
is_cheese = input("Do you want additional cheese? Y/N ")

bill = 0

if size.lower() == "s" and is_pepperoni:
    bill += 15
elif size.lower() == "m":
    bill += 20
else:
    bill += 25

# checks pepperoni's especial condition - If pepperoni is selected, and for a smaller pizza, add +2$ else +3$
if is_pepperoni.lower() == "y":
    if size.lower() == "s":
        bill += 2
    else:
        bill += 3

if is_cheese.lower() == "y":
    bill += 1

print(f"Your total bill for the pizza is {bill}")





