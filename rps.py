import random


bot_choice = random.choice(["rock", "paper", "scissors"])
user_choice = input("Select rock, paper, or scissors: \n")

print("Bot choice: " + bot_choice)
if bot_choice == user_choice:
    print("TIE!")
elif user_choice == "rock" and bot_choice == "scissors":
    print("YOU WIN!")
elif user_choice == "paper" and bot_choice == "rock":
    print("YOU WIN!")
elif user_choice == "scissors" and bot_choice == "paper":
    print("YOU WIN!")
else:
    print("YOU LOSE! ")