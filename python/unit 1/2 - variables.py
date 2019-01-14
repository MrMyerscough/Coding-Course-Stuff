"""Mr. Myerscough's variables example:
This program will show how to write variables, define them,
and call for them. It will also show what types of variables
you can use in python."""

# Types examples
variable = 1
print(type(variable))

variable = 1.0
print(type(variable))

variable = "One"
print(type(variable))

variable = True
variable = False
print(type(variable))

# Ways to name variables
variable = 1
myVariable = 3

# Variable storage errors
1 = var
my variable = 3

# Manipulating variables
variable = 1
variable = 2
variable = variable + 4

# Print operation example
x = 5
y = 10
print(x+y)

# Print str with int example

x = "I am"
y = 16
z = "years old."
print(x + y + z)
print(x + " " + str(y) + " " + z)
print(x, y, z)

""" Video Points

- Intro

- Variables are one of the most useful tools a programmer has.

- There are three main things you can do with variables: define, assign, recall

- The four basic types of variables are int, float, string, and bool.

- [explain variable types, and how they are not compatible, cause errors and stuff]

- To check the type of a variable, you can use the type command. Invoke it with parenthesis and enter your variable as a parameter.

- Int stands for integer, and works with whole number values that can be used in computations

- Float stands for floating point number, which is a number with a decimal

- Str stands for string, which is a series of characters and letters

- Bool stands for boolean, which is a truth value. It can either be true or false. These are used to evaluate a condition
which we will learn about in a later lesson

- Naming variables and naming errors

- You can print variables by using the print command we learned about in the last lesson (show how to do it)

- You can also print the result of an operation on two variables (show print(x+y))

- Be careful if you are trying to print a string and an int at the same time. Python only lets you print type string
with other type strings. (Show that). To fix this error it will give you, cast the int as type str to let it be printed (show this)

- Make sure to SMASH that thumbs up button, leave a comment down below and subscribe for more coding content. Roboman out.

"""