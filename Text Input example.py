"""Mr. Myerscough's text input example:
This program will show you how to let the user input information
and use it again in other parts of your program."""

# Input example
user_input = input("Enter your name: ")
print(type(user_input))
print(user_input)

# Casting an input
user_age = int(input("Enter your age: "))
print(type(user_age))

pi = float(input("Enter the value of pi: "))
print(type(pi))
print(type(pi) == float)

radius = float(input("Enter the radius of the circle: "))
circle_circumference = 2 * pi * radius

print("The circle circumference is", circle_circumference)

""" Video Script

- Intro

- Input is a type of command like print, invoked using parenthesis. The input command waits until you hit enter to continue the program

- Input allows the user to enter text or numbers to be used by the program later

- ALL INPUTS NEED TO BE STORED IN A VARIABLE OR THEY ARE USELESS

- Any text entered inside of the parenthesis will be shown before the input is asked for 

- Input stores all entered information as a string type by default

- If you want the user to enter a number to be used in some calculation, you should cast it to the number type you need for that calculation
(int or float). (Show example)

- If you just want to print the number after it was entered, you don't need to cast it. It will stay a string

- Make sure to SMASH that thumbs up button, leave a comment down below and subscribe for more coding content. Roboman out.

"""