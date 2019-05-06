# 3.2 - While Loops
# In this example there will be 4 different tasks to complete using 
# While Loops. Make sure to run your code in between each task 
# to make sure that program is working correctly before moving on.


# Task 1: Create a program that counts to 27
# Your program should use a while loop, and keep increasing the variable 
# each time the loop runs

count = 0

while count <= 27:
    print(count)
    count += 1


# Task 2: Create a program that counts backwards from 20 to -10 by twos
# Your program should print 20, 18, 16, 14 ... -6, -8, -10 using a while loop.

count = 20

while count >= -10:
    print(count)
    count -= 2


# Task 3: Create a menu that lets the user pick from 3 options, and only ends 
# when the user selects the end option. Write this using a boolean variable
# to stop the program.

done = False

print('pick an option')

while not done:
    print('1 - option one')
    print('2 - option two')
    print('3 - option three')
    print('4 - quit')
    choice = input()

    if choice == '1':
        print('you chose option one!')
    elif choice == '2':
        print('you chose option two!')
    elif choice == '3':
        print('you chose option three!')
    elif choice == '4':
        done = True
    else:
        print('invalid option')


# Task 4: Create an empty list variable called 'things'. Ask the user to 
# enter in an object, and add it to the list. Keep asking the user and
# adding to the list until the user types in 'stop'. Then print out the list. 

things = []

done = False

while not done:
    user_input = input('add an object, or enter stop: ')
    if user_input == 'stop':
        done = True
    else:
        things.append(user_input)

print(things)