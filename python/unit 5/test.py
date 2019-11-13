class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        self.tricks = [] 

    def introduce(self):
        print(f'Hello! My name is {self.name}. I am {self.age} years old. My fur is {self.color}.') 
        print(f'I know {len(self.tricks)} trick(s):')
        for trick in self.tricks:
            print(trick)

    def learn_trick(self, trick):
        self.tricks.append(trick)

class AnimalShelter:
    """Holds found dogs for adoption."""
    def __init__(self):
        self.dogs = []
    
    def add_dog(self, dog):
        """Add dog to animal shelter."""
        self.dogs.append(dog)
    
    def adopt_dog(self, name):
        """Removes dog from animal shelter given name, if dog exists in shelter."""
        for dog in self.dogs:
            if dog.name == name:
                self.dogs.remove(dog)
                print(f'Thank you for adopting {name}!')
                return 
        print('Could not find a dog with that name')
    
    def introduce_all_dogs(self):
        """Print a description for all dogs."""
        print(f'There are {len(self.dogs)} in this shelter:')
        for dog in self.dogs:
            dog.introduce()
            print()
    
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
        pound.introduce_all_dogs()
    elif choice == '2':
        name = input('Which dog would you like to adopt? (name) ')
        pound.adopt_dog(name)
    elif choice == '3':
        name = input("what is the dog's name?")
        age = int(input("what is the dog's age?"))
        color = input("what is the dog's color?")
        dog = Dog(name, age, color)
        pound.add_dog(dog) 
    elif choice == '4':
        done = True
    else:
        print('Not a valid option.')