""" Unit 3 - For Loops
In this example there will be 4 different tasks to complete using for loops.
Make sure to run your code in between each task to make sure that program is working correctly before moving on."""

# Task 1: Print the string "Hello!" 8 times.
# Your program should use a for loop, not 8 different print statements

for i in range(8):
    print("Hello!")

# Task 2: Count from 1 to 10
# Your program should use a for loop

for i in range (10):
    print(i+1)

# Task 3: Count from 100 to 0 by fives
# Your program should use a for loop with a step

num = 100
for i in range(21):
    print(num)
    num = num - 5

# Task 4: Create a loop that takes a number and increases it by 25% ten times, and prints the output each time.
# Your output should look like this if you start with 10: 12.5, 15.625, 19.53125...
# HINT: Use 1.25 to increase by 25%

num = 10
for i in range(10):
    num = num * 1.25
    print(num)