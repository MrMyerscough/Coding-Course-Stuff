import math

# number_one = int(input("pick a number "))
# number_two = int(input("pick a second number "))

# print(number_one + number_two)
# print(number_one - number_two)
# print(number_one * number_two)
# print(number_one / number_two)


# divisor = int(input('what do you want to divide?'))
# dividend = int(input('what do you want to divide by?'))

# quotient = divisor // dividend
# remainder = divisor % dividend

# print('the answer is', quotient, 'and', str(remainder) + "/" + str(dividend))

# print("pythagorean theorem")
# a = int(input('a? ') )
# b = int(input('b? ') )
# c = math.sqrt(a ** 2 + b ** 2)
# print("the hypotenuse is", c)

first_name = input('first name: ')
last_name = input('last name: ')
phone_number = input('phone number (##########): ')
street = input('address: ')
city = input('city: ')
state = input('state: ')
zip = input('zip: ')

first_name = first_name.capitalize()
last_name = last_name.capitalize()
phone_number = f"({phone_number[0:3]})-{phone_number[3:6]}-{phone_number[6:]}"
street = street[0:street.index(' ')+1] + street[street.index(' ')+1:street.index(' ')+2].upper() + street[street.index(' ')+2:]
# street = street.capitalize()
city = city.capitalize()
state = state.upper()

print(f"{first_name} {last_name}")
print(phone_number)
print(f"{street} {city} {state} {zip}")


