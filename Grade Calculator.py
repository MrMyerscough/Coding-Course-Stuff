"""This program will ask the user how many classes they want to 
calculate their grades in, and how many tests they have taken in 
each of their classes. It will then ask for the user to enter their
scores, and then find the average of their test scores to give
them a grade for each class."""

print("Thanks for using the grade calculator!")

# This allows the user to designate how many classes they want to calculate grades for.
classes = int(input("How many classes do you want to calculate grades for? "))

# This runs the average calculator for the number of classes indicated above.
for i in range(classes):
    name = input("What is the name of the class? ")
    
    # This allows the user to tell the program how many tests they are averaging.
    tests = int(input("How many tests have you taken in " + name + "? "))
    
    # This resets the average on every subsequent run of the loop on line 16.
    average=0
    
    # This loop compiles the scores for all of the tests into one variable.
    for j in range(tests):
        score = int(input("What is the grade of test " + str(j+1) + "? "))
        average = average+score
    
    # This calculates the average and outputs it for the specific class.
    average = average/tests
    print("Your average for " + name + " is " + str(average))

print("Thanks for using the grade calculator!")