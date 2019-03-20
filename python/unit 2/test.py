# imports
import random

# get user choice
print("let's play rock-paper-scissors!")
user_choice = input('what will you play? ')

# generate computer's choice from a random number
random_number = random.randint(1,3)
if random_number == 1:
    computer_choice = 'rock'
elif random_number == 2:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'

# print who won or lost!
if user_choice == 'rock':

    if computer_choice == 'rock':
        print('computer chose rock! DRAW!')
    elif computer_choice == 'paper':
        print('computer chose paper! you LOSE!')
    else:
        print('computer chose scissors! you WIN!')

elif user_choice == 'paper':

    if computer_choice == 'rock':
        print('computer chose rock! you WIN!')
    elif computer_choice == 'paper':
        print('computer chose paper! DRAW!')
    else:
        print('computer chose scissors! you LOSE!')

elif user_choice == 'scissors':

    if computer_choice == 'rock':
        print('computer chose rock! you LOSE!')
    elif computer_choice == 'paper':
        print('computer chose paper! you WIN!')
    else:
        print('computer chose scissors! DRAW!')

else:
    print("hey! that's not a valid option. choose rock paper or scissors.")