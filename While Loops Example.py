"""Mr. Myerscough's While Loop Example:
This program will show you how while loops work in python, and how
to write them. While loops are used when you want to do a task, or 
a set of tasks, continuously until some condition is not true."""

#This is to give our variable a starting value
condition=0

#This is the basic format of a while loop: 
#while(Condition that is true):
while condition<5:
    print(condition)
    
    #This increases the value of our variable every time the loop runs
    condition=condition+1

print("")
condition=0

#Let's change the condition on our loop to make it work more times.
while condition<100:
    print(condition)
    condition=condition+1

print("")
condition=True

#While loops are useful if you want to ask the user to input something
#until they get some question right as well.
while condition:
    """By setting the condition variable to True, the loop will run 
    the value of condition is changed to False. This creates an
    infinate loop."""
    magic_number=5
    guess=int(input("Guess my number! "))
    if guess == magic_number:
        print("You got it!")
        condition=False
    else:
        print("Guess again!")

#Be careful about making infinite loops. Uncomment the loop below
#and see what happens.
while True:
    print("Is this annoying yet?")

hello=0

#You can use a break if you want the loop to end at a certain point.
while True:
    print("Hello!")
    hello=hello+1
    if hello == 5:
        #By using the break command, it stops the loop when the
        #variable hello gets to 5, instead of being infinite.
        break

