"""Mr. Myerscough's math example:
This program will show you how to do mathematics in python."""

# Math operators

print(9+3)

print(8-3)

print(8*3)

print(4/2)

print(2**3)

print(4%2)
print(5%2)

# Order of operations

print(2*2+8)

print(2*(2+8))

# Casting an answer

print(9/7)
print(int(9/7))
print(round(13/7))

# Operations with variables

x = 2
y = 5
print(x*y)

s = 6
perimeter = 4*s
area = s**2
print("The perimeter of your square is", perimeter, "and the area of your square is", area)

# Logical Operators
age = 60
isOld = age > 50
print(isOld)

age = 12
isOld = age > 50
print(isOld)

isYoung = not isOld
print(isYoung)

name = "Mr. Myerscough"
isMrMyerscough = name == "Mr. Myerscough"
print(isMrMyerscough)

isMrMyerscough = name != "Mr. Myerscough"
print(isMrMyerscough)

number = 5
isFive = number == 5
print(isFive)

print(isMrMyerscough and isOld)
print(isMrMyerscough or isOld)
print(isMrMyerscough and isOld and isFive)
print(isOld or not isFive)

print(False or not True and True or False and not True)

""" Video points

- Intro

- Explanation of operations (+, -, *, /, **, %)
Division defaults to type float

- Order of operations

- Rounding answers from an operation

- Operations with variables

- Make sure to SMASH that thumbs up button, leave a comment down below and subscribe for more coding content. Roboman out.

"""