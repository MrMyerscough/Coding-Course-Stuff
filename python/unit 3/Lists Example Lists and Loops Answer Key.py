"""Unit 3 - Lists - Loops and Lists
In this example there will be 6 different tasks to complete using methods that can be performed on lists.
Make sure to run your code in between each task to make sure that program is working correctly before moving on.
"""

# Task 1: Use a for loop that checks the greetings list for "Bonjour" and prints "Bonjour is at index " and then prints the index number.
# Then, run the program again after the list has been sorted to tell the new index.
# This should print index 4 with the original list, and index 0 after the list is sorted.

greetings = ["Hello", "Hi", "Hey", "Yo", "Bonjour", "Salut", "Hola"]
index = 0
for i in greetings:
    if i == "Bonjour":
        print("Bonjour is at index", index)
    index = index + 1

greetings.sort()
index = 0
for i in greetings:
    if i == "Bonjour":
        print("Bonjour is at index", index)
    index = index + 1


# Task 2: Write a program to take all of the values in the list whales, add 1 to them, and then store them
# in a new list called more_whales.
# When printed, new_whales should output "6, 5, 8, 4, 3, 4, 3, 7, 5, 3, 2, 8, 2, 4"

whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]

new_whales = []

for i in whales:
    num = i + 1
    new_whales.append(num)

print(new_whales)


# Task 3: Create a nested list where each element of the outer list contains the atomic number and atomic weight for an 
# alkaline earth metal. The values are beryllium (4 and 9.012), magnesium (12 and 24.305), calcium (20 and 40.078), 
# strontium (38 and 87.62), barium (56 and 137.327), and radium (88 and 226). Assign the list to variable alkaline_earth_metals.
# Then, write a for loop to print all the values in alkaline_earth_metals, with the atomic number and atomic weight for each 
# alkaline earth metal on a different line.

alkaline_earth_metals = [[4, 9.012], [12, 24.305], [20, 40.078], [38, 87.62], [56, 137.327], [88, 226]]

for i in alkaline_earth_metals:
    print(i[0])
    print(i[1])

# Task 4: Write a for loop to create a new list called number_and_weight that contains the elements of alkaline_earth_metals 
# in the same order but not nested.

number_and_weight = []
for i in alkaline_earth_metals:
    number_and_weight.append(i[0])
    number_and_weight.append(i[1])
print(number_and_weight)