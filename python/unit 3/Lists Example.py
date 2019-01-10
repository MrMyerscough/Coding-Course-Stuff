"""Mr. Myerscough's List Example
This program will show how to create and use lists in Python, and
the different uses that lists have in programming."""

# A list of strings and how to call a specific index
greetings = ["Hey", "Yo", "Hello", "Hi", "AY YO WAZZAP"]
print(greetings[4])

# Lists with multiple variable types
types_list = [1, 3.14, "String", True]
print(type(types_list[3]))

# Using a for loop to cycle through a list
octagon_sides = [5, 7, 11, 14, 3, 17, 18, 8]

def octagon_perimeter():
    perimeter = 0
    for i in range(8):
        perimeter = perimeter + octagon_sides[i]
    print("The octagon has a perimeter of", perimeter, "units.")

octagon_perimeter()


grid = [
    ["x", "o" ,"x"],
    ["o", "x", "x"],
    ["o", "o", "o"]
]

for i in range(3):
    print(grid[i])



# Adding to an already created list
my_list = ["Dogs", "Cats", "Birds"]
print(my_list)

my_list.append("Pigs")
print(my_list)

# Removing from a list
my_list.remove("Pigs")
print(my_list)

# Inserting an item into a list
my_list.insert(0, "Pigs")
print(my_list)

# Indexing a list
print(my_list.index("Dogs"))

# Counting in a list
a_list = ["Dogs", "Dogs", "Dogs", "Dogs", "Dogs", "Dogs", "Dogs", "Cats"]
print(a_list.count("Dogs"))

# Sorting a list alphabetically
my_list.sort()
print(my_list)

# Removes all items from a list
my_list.clear()

# Pop returns and removes an item from the list at a certain index
my_list = ["Dogs", "Cats", "Birds", "Pigs"]
print(my_list.pop(0))
print(my_list)

# Flips a list
my_list.reverse()
print(my_list)