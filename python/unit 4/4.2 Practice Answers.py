# 4.2 - Advanced Functions
# In this practice there will be 5 different tasks to complete using 
# advanced functions. Make sure to run your code in between each task 
# to make sure that the program is working correctly before moving on.

# Task 1: Create a function that takes in three numbers and returns
# the product of the three. Call the function using keyword arguments,
# and then print out the result.

def multiply(a, b, c):
    return a * b * c

x = multiply(c=6, b=2, a=12)
print(x)

# Task 2: Create a function that calculates the total cost of an item
# including sales tax. The function will need the subtotal and a tax rate.
# If a tax rate is not provided, default to using a tax of 6%. Remember 
# that you calculate a total by multiplying a subtotal by (1 + (tax rate / 100)). 
# Test the function by providing the subtotal and the rate, and again with only
# the subtotal.

def total_cost(subtotal, tax=6):
    return subtotal * (1 + tax/100)

print( total_cost(100, 12) )
print( total_cost(100) )

# Task 3: Create a function that will take an unlimited amount of 
# arguments and returns all of the string arguments in a list. Then
# test the function by printing out the returned list.
# hint: use the type() command

def get_strings(*args):
    strings = []
    for arg in args:
        if type(arg) == str:
            strings.append(arg)
    return strings

x = get_strings(12, 'hello', [True, False], False, 'dog', 'words', 2, 'by')

print(x)


# Task 4: Create a function that solves ratio problems. For example
# 12/3 = 9/x. To find the answer, cross multiply the numbers and
# then solve for X. You can use the equation a/b = c/x where 
# x = (b * c) / a. Add proper documentation explaining the parameters 
# for this function using a docstring.

def ratio(a, b, c):
    """Return X in the equation a/b = c/x"""
    return (b * c) / a


# Task 5: Create a function that takes in a list of numbers, adds 12 to
# each number, and then returns it in a new list. Your function should 
# leave the old list unmodified. Test your function by printing out
# the original list along with the new one. 


def add_twelve(collection):
    new_collection = collection.copy()
    for index in range(len(new_collection)):
        new_collection[index] = new_collection[index] + 12
    return new_collection

original_list = [1, 7, 3, 94, 23, -12]

new_list = add_twelve(original_list)

print(original_list)
print(new_list)