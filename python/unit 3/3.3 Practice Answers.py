# 3.3 - While Loops
# In this example there will be 5 different tasks to complete using 
# For Loops. Make sure to run your code in between each task 
# to make sure that program is working correctly before moving on.


# Task 1: Print each item in the given list 'materials'.
# Your program should use a simple for loop. It's good practice to name
# your variables something that makes sense, instead of just 'x' or 'item'.

materials = ['wool', 'cotton', 'silk', 'polyester', 'felt']

for material in materials: 
    print(material)

# Task 2: Create a program that finds the largest string out of the given
# list 'messages'. You'll need to keep track of the longest string and 
# print it after you've found it. This works just like finding the largest 
# number in a list. Your program should output 'hey there'.

messages = ['hi', 'hey there', 'hello', "what's up", 'hey']

longest = ''

for message in messages: 
    if len(message) > len(longest):
        longest = message

print(longest)


# Task 3: Create a program that counts down from 20 to -10 by threes 
# using the range() command. What do you do to include the '-10' in the
# sequence? 

for i in range(20, -11, -3):
    print(i)


# Task 4: Given is a two-dimensional list of names. Each item in the list
# is a pair of first and last names. Using a for loop, print each pair of
# names and capitalize each. 

names = [
    ['melissa', 'doren'],
    ['jake', 'garney'],
    ['chen', 'quill'],
    ['brooke', 'mena'],
    ['patrick', 'fenwell']
]

for pair in names:
    first_name = pair[0]
    last_name = pair[1]
    print(first_name.capitalize(), last_name.capitalize())



# Challenge: Create a program that finds which items are NOT shared between
# the two given lists 'in_stock' and 'in_transit'. Then print out those items. 

in_stock = ['RJ-295', '34WH-9', 'PL-443', 'PJ-332', '37WH-13', 'GW-44']

in_transit = ['CR20', 'PL-443', 'GW-44', 'JJ5', 'RJ-295', '34WH-9']

not_shared = []

# search items in stock
for item_in_stock in in_stock:

    # is item in transit?
    found = False

    for item_in_transit in in_transit:
        if item_in_stock == item_in_transit:
            found = True
    # if item not found, then not shared
    if found == False:
        not_shared.append(item_in_stock)

# search items in transit
for item_in_transit in in_transit:

    # is item in stock?
    found = False

    for item_in_stock in in_stock:
        if item_in_transit == item_in_stock:
            found = True
    # if item not found, then not shared
    if found == False:
        not_shared.append(item_in_transit)

# print
print('items not shared:')
for item in not_shared:
    print(item)