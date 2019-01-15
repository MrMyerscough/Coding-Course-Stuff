""" Unit 2 - Conditionals - Population
In this example there will be 4 different tasks to complete using if/elif/else statements.
Make sure to run your code in between each task to make sure that program is working correctly before moving on."""


# Task 1: Create a program that will print the population if it is less than 10,000,000
# population_1 should print, and population_2 and population_3 shouldn't print

population = 5000000
if population < 10000000:
    print(population)

population = 20000000
if population < 10000000:
    print(population)

population = 30000000
if population < 10000000:
    print(population)

# Task 2: Create a program that will print the population if it is between 10,000,000 and 25,000,000
# population_2 should print, and population_1 and population_3 shouldn't print

population = 5000000
if population > 10000000 and population < 25000000:
    print(population)

population = 20000000
if population > 10000000 and population < 25000000:
    print(population)

population = 30000000
if population > 10000000 and population < 25000000:
    print(population)

# Task 3: Create a program that will print "Densely populated" if the land area (number of people per unit area) is greater than 100
# You should get 1 print of densely populated for land_area_2 and no output for land_area_1

land_area = 50
if land_area > 100:
    print("Densely populated")

land_area = 105
if land_area > 100:
    print("Densely populated")

# Task 4: Create a program that will print "Densely populated" if the land area is greater than 100, and "Sparsely populated" otherwise
# You should get 1 print of sparsely populated for land_area_1, followed by 1 print of densely populated for land_area_2

land_area = 50
if land_area > 100:
    print("Densely populated")
else:
    print("Sparsely populated")

land_area = 105
if land_area > 100:
    print("Densely populated")
else:
    print("Sparsely populated")
