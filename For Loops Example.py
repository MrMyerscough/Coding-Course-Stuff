"""Mr. Myerscough's For Loop Example:
This program will show you how for loops work in python, and how
to write them. For loops are used when you want to do a task, or 
a set of tasks, a set number of times."""

# For loop print 5 times
for i in range(5):
    print("WAT")

# For loop printing i ten times.
for i in range(10):
    print(i)

# Count from 1 to 10
for i in range(1,11):
    print(i)

# Count odd numbers 1-10
for i in range(1,10,2):
    print(i)

# Operations in for loop
for i in range(1,11):
    print(i+i)

# Writing things in loops
for i in range(11):
    print("Hi!")

""" Video Points

- Intro

- Looping in programs is used to repeat a set of commands multiple times. This keep us from having to write the same code multiple times
to do the same thing

- This creates cleaner, easier to read code, and makes less work than copying and pasting code multiple times. If you find yourself
copying and pasting, try to see if the code can fit into a loop to stop repeated lines of code.

- There are two kinds of loops: for and while. We will learn about while loops in the next lesson.

- For loops are used if you want to repeat a block of code a set number of times. Let's print something five times. (Do example.)

- In this for loop, we create a new variable i. This counts how many times the loop has been run. i always starts at 0, and increases each
time the loop is run. When i = the number in the range, the loop stops. In this case, the loop runs for i = 0, 1, 2, 3, and 4.
The keyword "in" shows what the parameters for the for loop are, followed by range. Range shows for what numbers the loop will run. Here,
it runs for numbers 0, 1, 2, 3, and 4, and stops when i = range number, which in this case is 5.

- i updates every time we run the loop. We can print this value to see how it changes each time. (Example)

- What if I want to count from 1 to 10? Each time I run the for loop, it starts at 0 by default. I can change this by giving it a starting
and ending value in the range parameter. If I give it a starting value or 1, it starts counting at 1. Keep in mind the for loop doesn't run
for the last number in the range, that's where it stops. If I want to print 1-10, I need to end my range at 11. (Example)

- What if I only want each odd number between 1 and 10? I can add another parameter to range, called the step. This tells it what to increase 
i by each time the loop is run. Here, I start at 1 and loop through 11, by I have a step of 2, which increase i by 2 each time. So our program
counts 1, 3, 5, 7, and 9. (Example)

- We can do operations inside of the loop as well. Here, let's add i to itself each time the loop runs. (Example)

- Instead of just printing numbers, we can also print text inside of a loop. Let's print "Hi!" 10 times on the screen. (Example)

- Make sure to SMASH that thumbs up button, leave a comment down below and subscribe for more coding content. Roboman out.

"""