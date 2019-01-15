""" Unit 3 - While Loops
In this example there will be 4 different tasks to complete using while loops.
Make sure to run your code in between each task to make sure that program is working correctly before moving on."""

# Task 1: Create a program that counts to 27
# Your program should use a while loop, and keep increasing the variable each time the loop runs

i = 1
while(i<28):
    print(i)
    i = i + 1

# Task 2: Create a program that counts backwards from 20 to -10 by twos
# Your program should print 20, 18, 16, 14 ... -6, -8, -10 using a while loop.

i = 20
while(i>-11):
    print(i)
    i = i - 2

# Task 3: Create a program that keeps asking the user if they like dogs until they say yes
# Your program should use a while loops, a conditional statement, and text input

while(True):
    answer = input("Do you like dogs? ")
    if answer == "yes":
        print("Great!")
        break

# Task 4: Create a menu that lets the user pick from 3 options, and only ends when the user selects the end option
# Your program should use an infinite while loops, conditionals, and a break command when exit is entered by the user.

while(True):
    print("Welcome to my menu!")
    print("A = Apple")
    print("B = Banana")
    print("Q = Quit")
    choice = input()
    if choice == "A":
        print("An apple a day keeps the doctor away!")
    elif choice == "B":
        print("Bananas: B A N A N A S!")
    elif choice == "Q":
        break
    else:
        print("That's not a valid choice!")
