
# say_hi()

def say_hi(name):
    print(f'hi there, {name}!')
    print('hello!')

def pathagorean(a, b):
    total = a ** 2 + b ** 2
    c = total ** 0.5
    return c

# print( pathagorean(3,4) )


def vehicle(number_people):
    if number_people <= 5:
        return 'car'
    elif number_people <= 7:
        return 'van'
    elif number_people <= 30:
        return 'bus'
    
    x = 12
    y = x ** 3
    print(y, x)

def what():
    return 1
    return 2
    return 3
    print('what')

# print(what())

def get():
    print('before')
    return 
    print('after')


# get()

def add_time(hours, minutes, meridiem, added_hours, added_minutes):
    new_hours = hours + added_hours
    new_minutes = minutes + added_minutes
    new_meridiem = meridiem
    if new_minutes >= 60:
        new_minutes -= 60
        added_hours += 1
    if new_hours >= 12:
        new_hours -= 12
        if new_meridiem == 'am':
            new_meridiem = 'pm'
        else:
            new_meridiem = 'am'
    return f'{new_hours}:{new_minutes} {new_meridiem}'




# my_age = 30
# my_age = my_age + 10
# print("i will be", my_age, "after 10 years")
# my_age = my_age + 20
# print("i will be", my_age, "after 30 years")


# print('hi') 

# music list
# game or sum
# 


drinks = [
    'Coffee',
    'Iced Coffee',
    'Frozen Coffee',
    'Macchiato',
    'Cappuccino',
    'Latte'
]

flavors = [
    'Vanilla',
    'Mocha',
    'Caramel',
    'No Flavor'
]

milks = [
    '2% Milk',
    'Skim Milk',
    'Whole Milk',
    'Nonfat Milk',
    'Almond Milk',
]

additions = [
    'Sugar',
    'Espresso',
    'Whipped Cream',
]

sizes = [
    'Small',
    'Medium',
    'Large',
    'Extra Large'
]



# def menu(menu_list):
#     index = 1
#     for item in menu_list:
#         print(f'{index} - {item}')
#         index += 1
#     choice = input('choose an option:')
#     return menu_list[int(choice) - 1]
        


# print('welcome to the coffee shop')

# drink = menu(drinks)

# flavor = menu(flavors)

# milk = menu(milks)

# addition = menu(additions)

# size = menu(sizes)

# print()
# print("Here's your order: ")
# print(drink)
# print(flavor)
# print(milk)
# print(addition)
# print(size)


# def find_average(num_list):
#     average = 0
#     for num in num_list:
#         average += num
#     average /= len(num_list)
#     return average

# x = find_average([1, 6, 44])

# print(x)

# def scan(text, key):
#     occurrences = 0
#     for character in text:
#         if character == key:
#             occurrences += 1
#     return occurrences 

# print( scan('spooky skeletons', 's') )


def days_to_seconds(num_days):
    return num_days * 24 * 60 * 60

days_to_seconds(2)



# ?????? TEXT QUESTION

# def my_command():
#     print('blue')
#     return 'purple'
#     print('red')

# color = my_command()

# print('yellow')

# print(color)
 


"""
a) 
yellow
blue
purple
red

b)
yellow
blue
purple 

c)
blue 
purple
yellow 
red

d)
blue
yellow
purple


def my_function():
    return 5
    print('five')
    return 50

x = my_function()


what will be the value of x?

a) 5

b) 'five'

c) 50

d) the program will error

"""


# v = vehicle(500)

# print('you will need a ' + v)

# x = say_hi('dog')

# print(x)



def function(name_list):
    for name in name_list:
        print(name.capitalize())


def find_average(num_list):
    average = 0
    for num in num_list:
        average += num
    average /= len(num_list)
    return average

x = find_average([1, 6, 44])
print(x)



def scan(text, key):
    occurrences = 0
    for character in text:
        if character == key:
            occurrences += 1
    return occurrences 

print( scan('spooky skeletons', 's') )


