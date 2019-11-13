from dogs import Dog, AnimalShelter 

pound = AnimalShelter()

done = False

print('Welcome to the animal shelter!')

while not done:
    print('1 - view dogs')
    print('2 - adopt a dog')
    print('3 - drop off a found dog')
    print('4 - exit')
    choice = input('Choose an option: ')

    if choice == '1':
        # view dogs
        pound.introduce_all_dogs()         
    elif choice == '2':
        # adopt a dog
        name = input('Which dog would you like to adopt? (name) ')
        pound.adopt_dog(name)
    elif choice == '3':
        # drop off dog
        name = input("what is the dog's name?")
        age = int(input("what is the dog's age?"))
        color = input("what is the dog's color?")
        dog = Dog(name, age, color)
        pound.add_dog(dog) 
    elif choice == '4':
        done = True
    else:
        print('Not a valid option.')