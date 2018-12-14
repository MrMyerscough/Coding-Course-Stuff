"""Mr. Myerscough's text input example:
This program will show you how to let the user input information
and use it again in other parts of your program."""

# To code a text input command, you need to store the input as a
# variable. Write it as follows:
user_input = input("Enter your name: ")
print(type(user_input))

"""userinput is the variable that the input is stored under. 
input("Text") is the command that calls for the text input from
the user. Whatever is written inside the parenthesis in quotations
is shown before the input is requested. You can then take what was
entered and use it like a normal variable. Keep in mind that all
entered text is stored as type str."""

print(user_input)
# This prints whatever was entered above.

"""Sometimes what you want the user to enter is a number, not a 
string. But python automatically stores it as a string. To remedy 
this, we can cast the input as an int so it gets stored as an int
instead of a string. You want to do this if you use the input in
any type of mathematics after they have inputted a number."""

user_age = int(input("Enter your age: "))
print(type(user_age))

# Keep in mind that if you want to repeat back a number, it has
# to be cast as a str. If you won't be doing a calculation with
# the number, you don't need to cast it as an int.

# You can also cast an input as a float if needed.
pi = float(input("Enter the value of pi: "))
print(type(pi))