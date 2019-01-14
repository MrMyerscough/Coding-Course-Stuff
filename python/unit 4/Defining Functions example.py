"""This is Mr. Myerscough's defining functions example.
In python, functions are an essential part of programming.
A function is a string of code that is given a name, and can be
called upon later to do a specific set of tasks. This is also
called subroutines in other programming languages. Functions 
allow for quick calling upon code that will be reused multiple
times."""

# def = define
def sayHello():
    name = input("What's your name? ")
    print("Hi there!")
    print("Your name is " + name)
    print("I hope you like dogs!")

# To run or 'call' the function, write the name of the 
# function and then a set of parenthesis
sayHello()

"""Functions can also be given some data or values to work with. 
You call these 'parameters.' They are placed inside the 
parenthesis when you are defining your function and then they 
can be used inside of the function like variables."""

# Here, our parameters are the variables 'name' and 'age.'
def areYouOld(name, age):
    if age > 80:
        print("Hey " + name + "! You're old")
    else:
        print("Hey " + name + "! You're not old yet")

# When you call a function with parameters, you have to give it
# the data to work with, again inside the parenthesis.

# Without looking, what will this print?
areYouOld("Isaiah", 16)

"""Functions can be used to calculate a value and then return that 
value. Use the keyword 'return' in the function where you want 
to hand back data. Combined with parameters, you can make 
functions with inputs and an output."""

def findTheSum(firstNumber, secondNumber):
    total = firstNumber + secondNumber
    return total

# without looking, what will this print?
print( findTheSum(12, 18) )

# the return keyword can also be used to make the function stop
# before it has reached the end
def speak():
    answer = input("Are you Isaiah? ")
    # If you answer no, you won't see the image. The return
    # causes it to end before displaying anything. 
    if answer == "no":
        return
    print("/^-----^\\ ")
    print("V  o o  V")
    print(" |  Y  |")
    print("  \\ Q /")
    print("  / - \\ ")
    print("  |    \\ ")
    print("  |     \\     )")
    print("  || (___\\====")
    print("Bark bark!")

speak()

# Challenge: what will the following output?
areYouOld("Jacob", findTheSum(40, findTheSum(23, 32) ) )


"""
in video script mention
-breaking big problems into smaller ones
 -just like a list of instructions can be grouped
  - instructions example
-top down programming
-bottom up programming
"""
