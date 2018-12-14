"""Mr. Myerscough's Conditional Example:
In this program, we will look at how to write and use conditionals.
Conditional means that for a string of code to be executed, a 
condition must be true (or false)."""

#To write a conditional, we use an "if" statement.
name = input("Enter your name: ")
"""In the below statement, if the name entered is "Mr. Myerscough"
It will display the first message. If anything else is entered,
It will display the other message."""
if name=="Mr. Myerscough":
    print("You are the teacher!")
else:
    print("You are a student.")

"""When writing conditionals, there are three different conditions:
if, elif, and else. If is used to lay out what the first condition
is. If there is more than one condition, you follow the if with an
elif, which is shorthand for elseif, which checks this condition
following the if. Lastly, the else command is used for any condition
that is not specified in any of the if or elif commands."""

#This program checks the age of the user and tells them if they are
#in elementary, middle, or high school, or if they're out of school.
age = int(input("Enter your age: "))
if age <= 11:
    print("You're in elementary school!")
elif age <= 14:
    print("You're in middle school!")
elif age <= 18:
    print("You're in high school!")
else:
    print("You're out of school! Hooray!")

"""When using conditionals, there are a few different operators 
used to evaluate the truth of the condition. You may have noticed
them above. "==" checks to see if the value of the variable is the
same as the value put after the double equals. Be careful, if you
are comparing strings, you have to have the string in quotations.
You can also use ">", "<", "<=" (less than or equal to), and ">=" 
(greater than or equal to). When using these, make sure your
variable type is an int. If not, you can cast it as an int by 
writing int(variable)."""

"""You can also use operators inside of your conditional statements.
These operators are "and" and "or". "and" checks to see if both of
the conditions are true to do whatever is below, and or checks that
just one of the conditions is true."""

correct_username = "myerscough"
correct_password = "riverview"
username = input("Enter username: ")
password = input("Enter password: ")

#The "and" checks that BOTH the entered username and password match
#the BOTH correct username and password.
if username == correct_username and password == correct_password:
    print("Welcome Mr. Myerscough")
else:
    print("Incorrect username or password!")

#The "or" checks that either the users age is less than 11 OR 
#greater than 14. If one of those is true, it prints the message
#below. Otherwise, it prints the other message.
age = int(input("Enter age: "))
if age < 15 or age > 18:
    print("You are not in high school")
else:
    print("You are in high school!")


    
    