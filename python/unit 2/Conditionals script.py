"""Mr. Myerscough's Conditional Example:
In this program, we will look at how to write and use conditionals.
Conditional means that for a string of code to be executed, a 
condition must be true (or false)."""

# If example
name = input("Enter your name: ")
if name=="Mr. Myerscough":
    print("You are the teacher!")

# If else example

name = input("Enter your name: ")
if name=="Mr. Myerscough":
    print("You are the teacher!")
else:
    print("You are a student.")

# If else elif example

name = input("Enter your name: ")
if name== "Mr. Myerscough":
    print("You are the teacher!")
elif name == "Mr. Hatzl":
    print("You are the principal!")
elif name == "Mr. Z":
    print("You are the assistant principal!")
else:
    print("You are a student.")

# And in conditionals
correct_username = "myerscough"
correct_password = "riverview"
username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Welcome Mr. Myerscough")
else:
    print("Incorrect username or password!")

# Or in conditionals
age = int(input("Enter age: "))

if age < 15 or age > 18:
    print("You are not in high school")
else:
    print("You are in high school!")

""" Video Points

- Intro

- So far, all programs have been pretty straightforward, just a set of basic instructions. You can almost always tell
what it's going to do. But how do programs make decisions?

- Conditionals are used to run certain code if a specific condition is met, or skip over it if that condition is not met.

- To write conditionals, we check IF something is true. IF it is true, the code below will run. If not, it will be ignored. (Example)

- We can also use the else command. Our condition is checked, and if it is true, it runs the if block. If the condition is false, it runs the 
else block (Example)

- If there are multiple conditions to check, we use the elif command. This stands for elseif. Our program checks the first condition, and if it
is true, it runs that block. If it is false, it checks the elif condition. If that is true, it runs that block. If that is false, it keeps 
checking elif's until they are done. If all are false, it will run the else block. (Example)

- We can also use the "and" logical operator in our conditionals. Here, we will compare if the user's entered username and password match
the correct username and password. We check if username is correct AND password is correct. The condition only returns true if both are true.
(Example)

- The "or" logical operator works the same way. Let's check the users age. If their age is less than 15 OR greater than 18, then they probably
aren't in high school anymore. This condition will return true if either one of the conditions are true. (Example)

- Make sure to SMASH that thumbs up button, leave a comment down below and subscribe for more coding content. Roboman out.

"""