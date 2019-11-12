# 5.1 - Classes
# In this practice there will be 5 different tasks to complete using 
# advanced functions. Make sure to run your code in between each task 
# to make sure that the program is working correctly before moving on.

# Task 1: Create a videogame class that takes in a name, year released,
# and price for a videogame. The function where you pass these values
# in should store them inside of the object as properties.

class Videogame:
    def __init__(self, name, year, price):
        self.name = name
        self.year = year 
        self.price = price

    def information(self):
        print(f'{self.name}, released {self.year} - ${self.price}')

    def change_price(self, new_price):
        self.price = new_price


# Task 2: Using that class, create 4 videogame objects of some of your
# favorite games. Store them in four separate variables.

game1 = Videogame('Pokemon Blue', 1996, 30)
game2 = Videogame('Super Smash Bros.', 1999, 70)
game3 = Videogame('Half-Life 2', 2004, 10)
game4 = Videogame('Minecraft', 2009, 30)


# Task 3: Create a method that prints the object information in a formatted
# string. For example 'Wii Sports, released 2006 - $20'


# see above


# Task 4: Create a method inside of the class that changes the value of 
# the price property. This method should take in a new price value 
# and then change the price property of the object. To verify everything 
# works, change the price of the second and fourth videogames, and then
# call the method you wrote in task #3. 

# see above 

game2.change_price(100)
game4.change_price(10)

game1.information()
game2.information()
game3.information()
game4.information()
