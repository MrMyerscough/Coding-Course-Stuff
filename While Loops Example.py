"""Mr. Myerscough's While Loop Example:
This program will show you how while loops work in python, and how
to write them. While loops are used when you want to do a task, or 
a set of tasks, continuously until some condition is not true."""

# While loop example
condition=0

while condition<5:
    print(condition)
    
    condition=condition+1

# Larger while loop
condition=0

while condition<100:
    print(condition)
    
    condition=condition+1

# Truth in while loops
condition=True

while condition:
    magic_number=5
    
    guess=int(input("Guess my number! "))
    
    if guess == magic_number:
        print("You got it!")
        condition=False
    
    else:
        print("Guess again!")

# Infinite loop example
while True:
    print("Is this annoying yet?")

# Break in while loops
hello=0

while True:
    print("Hello!")
    hello=hello+1
    
    if hello == 5:
        break

""" Video Script

- Intro

- While loops are also a way to repeat blocks of code. While loops use a condition to tell it when to stop.

- Here, we'll set out variable condition to 0. Notice how our while loop doesn't use a variable like our for loop did. This means the loop
does NOT automatically increase the value of our variable every time. This is something we have to change in the code inside our loop.
Here, we set our condition on the while loop to be while condition is less that 5. We print what condition is, then we increase it by 1 each
time the loop runs (Example)

- Let's make a larger while loop. Instead of 5, let's make the condition 100. (Example)

- While loops work by checking the truth value of the condition. This means that it takes our variable condition, and checks if it is 
less than 5. The loop runs every time this condition returns True. If it returns False, the loop stops.

- We can use truth values to help us write loops as well. Let's set condition to True. Remember that the loop runs whenever the condition
is true. Here, it is always true, so it keeps running until the value of condition is changed to False. Let's make a game to guess my number. 
I'll use some conditionals inside of the loop here to check if the user input matches the number I want them to guess. If they get it right,
the value of condition is changed to false, which ends the loop. Otherwise, it keeps asking for guesses. (Example)

- Be careful when using truth values in while loops. If you aren't careful, you can create an infinite loop. (Example)

- If you want a loop to run indefinitely until a certain condition is met, you could use the keyword break. This keyword ends the loop 
immediately, regardless of if it was done running or not. Here, let's make what would be an infinite loop, but we will add a conditional that
will break the loop if a condition is met. (Example) 

- Make sure to SMASH that thumbs up button, leave a comment down below and subscribe for more coding content. Roboman out.

"""