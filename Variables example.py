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
my_variable = 3

# Variable storage errors
1 = var
my variable = 3

# Print operation example
x = 5
y = 10
print(x+y)

# Print str with int example

x = "I am "
y = 16
z = " years old."
print(x + str(y) + z)

""" Video Points

- Intro

- Variables are one of the most useful tools a programmer has.

- There are three main things you can do with variables: define, assign, and (I forget what you said)

- The four main types of variables are int, float, string, and bool.

- Int stands for integer, and works with whole number values that can be used in computations

- Float stands for floating point number, which is a number with a decimal

- Str stands for string, which is a series of characters and letters

- Bool stands for boolean, which is a truth value. It can either be true or false. These are used to evaluate a condition
which we will learn about in a later lesson

- Naming variables and naming errors

- You can print variables by using the print command we learned about in the last lesson (show how to do it)

- You can also print the result of an operation on two variables (show print(x+y))

- Be careful if you are trying to print a string and an int at the same time. Python only lets you print type string
with other type strings. To fix this error it will give you, cast the int as type str to let it be printed (show this)

- Maybe something else?

- Make sure to SMASH that thumbs up button, leave a comment down below and subscribe for more coding content. Roboman out.

"""

# Maybe take this part out?
x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(x[3])

#Keep in mind that the characters in a string start at value 0.
#If I wanted to call the letter 'C', I would have to call the
#2nd index.
print(x[2])

#To print only a section of the string, you use a colon to seperate
#the range of string you want repeated. Below is letters H-P
print(x[7:16])

#If I want to print from K through the end, it looks like this
print(x[10:])

#You can also make it print the same message multiple times!
z = "*Knock*"
print(z*3)