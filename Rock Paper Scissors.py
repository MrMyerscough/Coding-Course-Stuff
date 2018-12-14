import random

""" This program will have the user play rock paper scissors against
a computer opponent. They will select a choice: either rock, paper, or
scissors. Then, the bot will randomly generate a choice and the program
will compare what the bot threw and the user and determine who won. It 
will play best of 5."""

# This sets the values of wins and losses at the start of the program.
wins = 0
losses = 0
print("Let's play rock paper scissors! Best of five wins!")

# This loop ends when either the user has 3 wins or 3 losses, which would be the best three out of five.
while (wins < 3) and (losses < 3):
    # User enters their choice here
    choice = input("What will you throw: Rock, Paper, or Scissors? ")
    
    # This is where the bot generates it's choice
    bot = random.randint(1,3)
     # This changes the value from a number to a string so they can compare to the user choice.
    if bot==1:
         botchoice = "Rock"
    elif bot==2:
        botchoice="Paper"
    elif bot==3:
        botchoice="Scissors"
    if choice == "Rock" or choice == "rock":
        
        # This is where the user choice is compared to the bot choice.
        if botchoice == "Rock":
            print("You tied! You both threw rock.")
        elif botchoice == "Paper":
            print("You lose! Your opponent threw paper.")
            losses = losses+1
        elif botchoice == "Scissors":
            print("You win! Your opponent threw scissors.")
            wins = wins+1

    elif choice == "Paper" or choice == "paper":
        # This is where the user choice is compared to the bot choice.
        if botchoice == "Rock":
            print("You win! You both threw rock.")
            wins = wins+1
        elif botchoice == "Paper":
            print("You tied! Your opponent threw paper.")
        elif botchoice == "Scissors":
            print("You lose! Your opponent threw scissors.")
            losses = losses+1
    
    elif choice == "Scissors" or choice == "scissors":
        # This is where the user choice is compared to the bot choice.
        if botchoice == "Rock":
            print("You lose! You both threw rock.")
            losses = losses+1
        elif botchoice == "Paper":
            print("You win! Your opponent threw paper.")
            wins = wins+1
        elif botchoice == "Scissors":
            print("You tied! Your opponent threw scissors.")
    
    # An easter egg for users who try to play Rock Paper Scissors Lizard Spock
    elif choice == "Lizard" or choice == "lizard":
        print("Good try, but we aren't playing Rock Paper Scissors Lizard Spock")
    
    elif choice == "Spock" or choice == "spock":
        print("Good try, but we aren't playing Rock Paper Scissors Lizard Spock")
    
    # This tells the user they didn't enter their choice correctly.
    else:
        print("That's not a valid choice!")

# This is where the user is told their score and if they won the best three out of five.
if wins == 3:
    print("You won " + str(wins) + " times and lost " + str(losses) + " times. You won!")
else:
    print("You won " + str(wins) + " times and lost " + str(losses) + " times. You lost.")