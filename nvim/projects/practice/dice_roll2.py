import random

dice_question=print("Do you want to roll the dice?")


while True:
    dice_question=input("1. yes    2.no\n")
    if dice_question=="yes":
        dice_roll=random.randint(1,100)
        print(dice_roll)
    elif dice_question=="no":
        break
