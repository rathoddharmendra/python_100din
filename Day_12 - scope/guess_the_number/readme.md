## Define the problem - USE CASES to solve the problem

## create flow chart
![alt text](image.png)

## Create Todo or pseduo code

<!-- greetings -->
print("Welcome to the Number guessing game!")
print("Choose a number between 1 and 100")

<!-- set difficulty level -->
level = input("Set difficulty level easy/hard?")
if level == easy:
    attempts = 10
else:
    attempts = 5
def play():
<!-- set secret number -->
secret_number = random.randint(1,100)

while attempts > 0:
<!-- make guess,  -->
guess = input("Choose a number between 1 and 100")
<!-- check the number and  -->
if guess == secret_number: 
    then win
    break
elif guess < secret_number: too low
else: too high

<!-- reduce attempts by one  -->
attempts -= 1

if __name__ == "__main__":
    while input("Do you want to play y/n?") == "y":
        play()
    print("Thanks for playing")

