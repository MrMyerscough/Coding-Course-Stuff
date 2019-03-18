# 1.3 - Operators and Types
# In this practice there will be 5 different tasks to complete using operators.
# Make sure to run your code in between each task to make sure that program is working correctly before moving on.

# Task 1: Solve this problem: What is the output of the difference of (double the sum of 4 and 7) and 7, divided by 5?
# Your program should output 3 if you coded it correctly.

print(((2*(4+7))-7)/5)

# Task 2: What is the sum of 4 to the 6th power and 6 to the 4th power?
# Your program should output 5392 if you coded it correctly.

print((4**6)+(6**4))

# Task 3: A group of 53 people are trying to carpool to a festival. 5 people can fit in each car. How many people will be left
# over in the last car? HINT: Use the modulo operator.

leftover = 53 % 5
print("There will be", leftover, "people in the last car.")

# Task 4: Write a program that takes the users number and adds 5, doubles the previous answer, subtracts 4 from that answer,
# divides that answer by 2, and then subtracts the users entered number. Print the result.
# If you coded it correctly, your program should output 3 no matter what the user enters.

start_num = int(input("Enter a number: "))
num = start_num + 5
num = num * 2
num = num - 4
num = num / 2
num = num - start_num
print(num)

# Task 5: Have the user enter the side length of a square and store it as a variable. Then, find the perimeter of the square.
# If the user enters the square has a side length of 6, the program should output 24 for the perimeter

side = input("What is the side length of the square? ")
perimeter = 4 * int(side)
print("The perimeter of the square is", perimeter, "units.")