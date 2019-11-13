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
                print(f'Thank you for adopting {name}!\n')
                return
        print('Could not find a dog with that name.\n')

    def introduce_all_dogs(self):
        """Print a description for all dogs."""
        print(f'There are {len(self.dogs)} animals in this shelter:')
        for dog in self.dogs:
            dog.introduce()
            print()

