import random

# This sets the bot to a random choice, either rock, paper, or scissors
bot = random.randint(1,3)

if bot == 1:
    bot = "rock"
elif bot == 2:
    bot = "paper"
else:
    bot = "scissors"

# This gets the users choice
user = input("What will you throw: rock, paper, or scissors? ")

if user.lower() == "rock":
    # Write your code here for what happens if the user throws rock
elif user.lower() == "paper":
    # Write your code here for what happens if the user throws paper
elif user.lower() == "scissors":
    # Write your code here for what happens if the user throws scissors
else:
    print("That's not a valid option!")