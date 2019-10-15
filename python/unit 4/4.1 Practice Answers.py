# 4.1 - Functions
# In this practice there will be 4 different tasks to complete using 
# functions. Make sure to run your code in between each task 
# to make sure that the program is working correctly before moving on.

# Task 1: Create a function that prints out some ASCII art. (You can find
# an art generator online.) Call the function twice. 

def print_art():
    print('                  _            _                          _           ')
    print('                 | |          | |                        | |          ')
    print('     ___ ___   __| | ___    __| | ___   __ _   _ __ _   _| | ___  ___ ')
    print("    / __/ _ \ / _` |/ _ \  / _` |/ _ \ / _` | | '__| | | | |/ _ \/ __|")
    print("   | (_| (_) | (_| |  __/ | (_| | (_) | (_| | | |  | |_| | |  __/\__ \\")
    print('    \___\___/ \__,_|\___|  \__,_|\___/ \__, | |_|   \__,_|_|\___||___/')
    print('                                        __/ |                         ')
    print('                                       |___/                          ')

print_art()
print_art()

# Task 2: Create a function that takes in a number as a parameter and 
# prints out that number to the fifth power. Call the function given
# the numbers 3 and 28. (This function should not return, just print 
# on its own.)

def fifth_power(num):
    print(num ** 5)

fifth_power(3)
fifth_power(28)

# Task 3: Create a function that takes in a list as a parameter and 
# randomly returns an item from that list. Call the function given
# ['cat', 'dog', 'bird', 'hamster'] and print out the returned value. 

import random

def random_item(items):
    last_index = len(items) - 1
    rand_index = random.randint(0,last_index)
    return items[rand_index]

x = random_item(['cat', 'dog', 'bird', 'hamster'])
print(x)

# Task 4: Create a function that takes in an age as a parameter. If
# the entered value is less than 18 return 'minor'. Else, if the entered
# value is less than 65 return 'adult'. Else, return 'senior'. Test out
# the function by calling it with different ages and printing the output.

def age_class(age):
    """
    returns the class of a person given their age
    Parameters:
        age (int): the age of the person
    """
    if age < 18:
        return 'minor'
    elif age < 65:
        return 'adult'
    else:
        return 'senior'

print( age_class(7) )
print( age_class(27) )
print( age_class(70) )