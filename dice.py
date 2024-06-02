import random

roll = random.randint(1,6)
user_guess = int(input("Guess dice roll: "))

if user_guess == roll:
    print("That's correct - they rolled a " + str(roll))
else:
    print("WRONG - they rolled a " + str(roll))