"""Unit 2 - Conditionals - Comparissons
In this example there will be 4 different tasks to complete using conditionals and comparing different variables.
Make sure to run your code in between each task to make sure that program is working correctly before moving on."""

# Task 1: Ask the user to guess the magic number. If they enter the same value as the magic_number variable, print "You guessed it!"
# If they enter anything else, print "That isn't it! The magic number is 21."

magic_number = 21
guess = input("Guess the magic number!")
if int(guess) == magic_number:
    print("You guessed it!")
else:
    print("Nope! It was 21")


# Task 2: Ask the user if they like dogs and store their response as a variable. If they enter "yes", print "I'm glad you like dogs!"
# If they enter "no", print "What's wrong with you??". If they enter anything else, print "That's not an answer! Enter yes or no."

answer = input("Do you like dogs? ")
if answer == "yes":
    print("I'm glad you like dogs!")
elif answer == "no":
    print("What's wrong with you???????????????")
else:
    print("That's not a valid answer!")

# Task 3: Ask the user the random math problem a + b and store their answer as a variable. Then, compare their entered answer to the
# variable correct_answer. If they match, print "Correct!". If they don't match, print "Incorrect! The correct answer is " followed by
# the value of the correct_answer variable.
import random
a = random.randint(0, 20)
b = random.randint(0, 20)
correct_answer = a + b

answer = input("What is " + str(a) + "+" + str(b) + "?")
if int(answer) == correct_answer:
    print("Correct!")
else:
    print("Incorrect! The correct answer is", correct_answer)

# Task 4: Ask the user if they are in high school. If they enter yes, ask them for their grade level. If they enter 9, print 
# "You're a freshman", if they enter 10 print "You're a sophomore", if they enter 11 print "You're a junior", and if they enter 12
# print "You're a senior". If they say no to the first question, print "You're not in high school."

age = input("Are you in high school? ")
if age == "yes":
    grade = int(input("What is your grade level? "))
    if grade == 9:
        print("You are a freshmen")
    elif grade == 10:
        print("You are a sophomore")
    elif grade == 11:
        print("You are a junior")
    elif grade == 12:
        print("You are a senior")
    else:
        print("That's not a grade level in high school!")
else:
    print("You are not in high school")
