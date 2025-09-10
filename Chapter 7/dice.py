import random
import time

def roll_dice(n):
    dice = []
    for i in range(n):
        dice.append(random.randint(1,6))
    return dice

def find_winner(cdice_list, udice_list):
    computer_total = sum(cdice_list)
    user_total = sum(udice_list)
    print("Computer total",computer_total)
    print("User total", user_total)

    if user_total < computer_total:
        print("Computer wins")
    else:
        print("Its a tie")

def roll_again(choices, dice_list):
    print("Rolling again...")
    time.sleep(3)
    for i in range(len(choices)):
        if choices[i] == "r":
            dice_list[i] = random.randint(1,5)
    time.sleep(3)

def computer_strategy(n):
    print("Computer is thinking.....")
    time.sleep(3)
    choices = ""
    for i in range(n):
        choices = choices + "r"
    return choices

def computer_strategy2(n):
    print("Computer is thinking.....")
    time.sleep(3)
    choices = "" 
    for i in range(n):
        if computer_rolls[i] < 5:
            choices = choices + "r"
        else:
            choices = choices + "-"
    return choices

number_dice = int(input("Enter number of dice:"))
ready = input("Ready to start hit any key to continue")

user_rolls = roll_dice(number_dice)
print("User first roll:", user_rolls)

user_choices = input("Enter - to hold or r to \ roll again:")

while len(user_choices) != number_dice:
