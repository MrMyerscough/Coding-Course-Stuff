"""Mr. Myerscough's variables example:
This program will show how to write variables, define them,
and call for them. It will also show what types of variables
you can use in python."""

#To define a variable, you must give it a name and a value
#This is a variable with type int (integer, or whole number)
variable = 1
print(type(variable))

#This is a variable with type float (numbers with decimals)
variable = 1.0
print(type(variable))

#This is a variable with type str (string, which is any text)
variable = "One"
print(type(variable))

#This is a variable with type bool (boolean, which means either 
#True or False. Make sure you write True or False with a capital)
variable = True
variable = False
print(type(variable))

#For str type, it may be useful to call a certain character in the
#string. To do this, you use the following command.
x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(x[3])

#Keep in mind that the characters in a string start at value 0.
#If I wanted to call the letter 'C', I would have to call the
#2nd character.
print(x[2])

#To print only a section of the string, you use a colon to seperate
#the range of string you want repeated. Below is letters H-P
print(x[7:16])

#If I want to print from K through the end, it looks like this
print(x[10:])

#You can also make it print the same message multiple times!
z = "*Knock*"
print(z*3)

"""Be careful if you try and print a string with another type.
All variables have to be type str to be printed if you are
printing another string. To remedy this, you have to cast the
variable as a string."""

x = "I am "
y = 16
z = " years old."
print(x + str(y) + z)
#By writing str(variable), you make that variable type str, which
#allows it to be printed.