"""Mr. Myerscough's For Loop Example:
This program will show you how for loops work in python, and how
to write them. For loops are used when you want to do a task, or 
a set of tasks, a set number of times."""

#This is the basic format of a for loop: 
#for (variable) in range(How many times you want the loop to run).
for i in range(10):
    """After the loop, you place a colon, and python should auto-indent
    Anything indented after the loop will be done in the loop.
    This program counts from 0-9. This is because the range
    specified is the value at which the loop stops. Your variable
    always starts at 0, so ten times counts 0,1,2,3,4,5,6,7,8,9."""
    print(i)

#This just makes a space between the loops when they print.
print("")

#How do we count from 1 to 10 then? Let's take a look.
for i in range(1,11):
    """Above, I gave the range a starting value and an ending
    value. This lets the loop know to start at 1, and end at i=11,
    which will display all numbers 1-10.""" 
    print(i)

print("")

#We can also count by more than one at a time.
for i in range(2,11,2):
    """This counts all even numbers 2-10. The first two numbers set
    the range for the loop, and the final number is called the step.
    This tells the loop what to count by. In this case, I wrote
    step 2, which counts every other number."""
    print(i)

print("")

#You can also do operations inside of for loops.
for i in range(1,11):
    #Here, we add i to itself every time the loop runs
    print(i+i)

print("")

#We can also write things using loops.
for i in range(11):
    #This prints "Hi!"" 10 times on the screen.
    print("Hi!")