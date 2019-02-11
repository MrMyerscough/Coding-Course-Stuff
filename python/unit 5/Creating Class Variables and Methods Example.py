"""Unit 5 - Creating Class Variables and Methods
In this example there will be __ different tasks to complete by creating class variables and methods.
Make sure to run your code in between each task to make sure that program is working correctly before moving on."""

# Task 1: Create a class called "Dogs". Create an __init__ funciton that has parameter "name". Inside the __init__ function, 
# create an empty list called "tricks". Create a class variable called "species" that tells the scientific name for dogs. 
# Then, create a method called "add_tricks" that adds a new trick to the tricks list.

class Dogs:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_tricks(self, trick):
        self.tricks.append(trick)

    species = "Canis Lupus Familiaris"

class DogManager:
    @staticmethod
    def compareTricks(dog1: Dogs, dog2: Dogs):
        common_tricks = []
        for trick in dog1.tricks:
            for trick2 in dog2.tricks:
                if trick == trick2:
                    common_tricks.append(trick)
        return common_tricks

# Task 2: Create a dog object of your own dog (or if you don't have a dog make one up). Then, use the add_tricks method to
# add tricks to your dog object. Then print the list of tricks, as well as the species of your dog.

dro = Dogs("Dro")
astra = Dogs("Astra")

dro.add_tricks("Sit")
dro.add_tricks("High Five")
dro.add_tricks("Shake")
dro.add_tricks("Lay Down")

astra.add_tricks("Sit")
astra.add_tricks("Sit Pretty")
astra.add_tricks("Lay Down")

print("Dro's Tricks:", dro.tricks)
print("Astra's Tricks:", astra.tricks)
print("Both dog's species:", dro.species)

# Task 3: Create a second dog object, and add tricks to that object as well. Then, create a static method to compare the 
# list of tricks between two different objects of type Dogs. The method should print the list of tricks that the two dogs share only.

print(DogManager.compareTricks(dro, astra))

# Task 4: 


