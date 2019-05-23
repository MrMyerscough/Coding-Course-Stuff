# 3.4 - File I/O
# In this example there will be 3 different tasks to complete using 
# File I/O. Make sure to run your code in between each task 
# to make sure that program is working correctly before moving on.


# Task 1: Create a text file from the following lines. Then access
# that text file and read its contents. Print out every number in the 
# file to the terminal with 14 added to it. 

# ===
12
55
23
44
27
# === 

with open('data1.txt') as my_file:
    for line in my_file:
        number = int(line)
        print(number + 14)

# your output should look like:

26
69
37
58
41


# Task 2: Create a program that takes user input and writes it to a 
# file. When the user hits enter, it should start a new line in the 
# text file. Stop taking input when the user types in 'exit'.

print("enter lines to be written to a file. when done type 'quit'")
with open('output1.txt', 'w') as my_file:
    done = False 
    while not done:
        answer = input()
        if answer == 'quit':
            done = True
        else:
            my_file.write(answer + '\n')
        

# Task 3: Create a text file from the following lines. Then access
# that text file and read its contents. Capitalize every name from
# the text file and then write it to a separate output file. You
# will need to have two file objects ('with' statements) in this
# program. Nothing should be outputted to the terminal 

"""
joanna
josh
trina
bo
natalie
katrina
howard
"""

# your output file should look like:

"""
Joanna
Josh
Trina
Bo
Natalie
Katrina
Howard
"""

names = []

with open('data2.txt', 'r') as my_file:
    names = my_file.readlines()

with open('output2.txt', 'w') as my_file:
    for name in names:
        my_file.write(name.capitalize())