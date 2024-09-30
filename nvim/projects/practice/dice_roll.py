import random

while True:
    ques=input("do you want to roll the dice?")
    if ques=="y":
        num=random.randint(1,21)
        print(num)
    elif ques=="n":
        break
