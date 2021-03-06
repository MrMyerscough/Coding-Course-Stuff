"""Unit 3 - Lists - Intro to methods
In this example there will be 6 different tasks to complete using methods that can be performed on lists.
Make sure to run your code in between each task to make sure that program is working correctly before moving on.
"""

ids = [4353, 2314, 2956, 3382, 9362, 3900]

# Task 1: Remove 3382 from your list.
# When printed, the list should no longer have 3382 in it

ids.remove(3382)
print(ids)

# Task 2: Get the index of 9362.
# When printed, you should have the index number of 9362

print(ids.index(9362))

# Task 3: Insert 4499 in the list after 9362.
# When printed, the list should have 4499 directly after 9362

ids.insert(ids.index(9362)+1, 4499)
print(ids)

# Task 4: Extend the list by adding [5566, 1830] to it
# When printed, the list should have 5566 and 1830 added to the end of it

ids = ids + [5566, 1830]
print(ids)

# Task 5: Reverse the list.
# When printed, the list should be backwards from the list in task 4

ids.reverse()
print(ids)

# Task 6: Sort the list.
# When printed, the list should be sorted numerically (Smallest number first)

ids.sort()
print(ids)
