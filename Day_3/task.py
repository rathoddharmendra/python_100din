print("Welcome to rolly! a roller coaster ticket purchasing system for local ride")

height = float(input("What is your height in cm? "))

bill = 0

if height >= 120.00:
    age = int(input("What is your age? "))
    if age <= 12:
        print("Child tickets are $5")
        ticket = 5
    elif age <= 18:
        print("Youth tickets are $7")
        ticket = 7
    elif age >=45 and age <=55:
        print("Your ticket is on the house. You can ride for free!")
        ticket = 0
    else:
        print("Adult tickets are $12")
        ticket = 12

    is_photo_req = input("Do you want additional ride photos taken for $3? (Y/N) ")
    if is_photo_req.lower() == 'y':
        bill = ticket + 3

    print(f"Your total bill is ${bill}\nHave a nice ride-o-rolley!")

else:
    print("As per our policy, people shorter than 120 cm are not allowed due to safety reasons")