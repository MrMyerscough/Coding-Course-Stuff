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

dog1 = Dog('buddy', 6, 'black') 
dog2 = Dog('scooby', 7, 'brown') 

dog1.learn_trick('speak')
dog1.learn_trick('sit')
dog2.learn_trick('shake')
dog2.learn_trick('roll over')

dog1.introduce()
dog2.introduce()


