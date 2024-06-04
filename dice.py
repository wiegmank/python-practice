import random

def dice_roll(): 
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_total

def main():
    roll1 = dice_roll()
    roll2 = dice_roll()

    print("player 1 rolled", roll1)
    print("player 2 rolled", roll2)

    if roll1 > roll2:
        print("Player ONE wins!")
    elif roll2 > roll1:
        print("Player TWO wins!")
    else:
        print("TIE!")

main()