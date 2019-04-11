# 2.2 - More with conditionals
# In this practice there will be 4 different tasks to complete using 
# conditionals. Make sure to run your code in between each task 
# to make sure that the program is working correctly before moving on.


# Task 1: Ask the user if they are in high school. If they enter yes, ask them for 
# their grade level. If they enter 9, print "You're a freshman", if they enter 10 
# print "You're a sophomore", if they enter 11 print "You're a junior", and if they 
# enter 12 print "You're a senior". If they enter in a number that is not 9-12, 
# print that they have entered an invalid value. If they say no to the first question,
#  print "You're not in high school."

# Task 2: Create a menu with 4 options: add, subtract, multiply and divide. You 
# can make the option to type in anything you want (ex, 'add', '+' or '1'). Then
# ask the user for two numbers. Depending on what the user chose, print either 
# the sum, difference, product, or quotient of the two numbers. Your program
# should output "4 plus 5 is 9!" if the user chose to add and then typed '4' and '5'.

# Task 3: Ask the user the random math problem a + b and store their answer as a
# variable. Then, compare their entered answer to the variable correct_answer. If 
# they match, print "Correct!". If they don't match, print "Incorrect! The correct 
# answer is " followed by the value of the correct_answer variable.
import random
a = random.randint(0, 20)
b = random.randint(0, 20)
correct_answer = a + b

# Task 4: Ask the user if they would like to flip a coin. If they say yes, randomly
# print either 'heads!' or 'tails!' using random numbers. If they say no, print 
# out 'okay.'

