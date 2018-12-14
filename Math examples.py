"""Mr. Myerscough's math example:
This program will show you how to do mathematics in python."""

# All basic math operators should be pretty self explanitory.
print(9+3)
print(8-3)
print(8*3)
# Note when you do division, python defaults to an answer as type 
# float. If you want type int, make sure to cast it. 
print(4/2)

# To use exponents, you use ** as the operator. This raises 2 to
# the 3 power.
print(2**3)

"""There is also a modulo operator. This shows you what the
remainder is when dividing one number by another. To write a
modulo, use the % sign. If two numbers divide evenly, the program
will return 0. When 5 is divided by 2, there will be a
remainder of one, so the program will return 1."""
print(4%2)
print(5%2)

"""Python automatically follows the order of operations: PEMDAS.
It does parenthesis, exponents, multiplication and division from
left to right, then addition and subtraction from left to right.
If you want math done in a different order, make sure to use 
parenthesis to show what you want done first."""
print(2*2+8)
print(2*(2+8))

# If you want to round an answer to the nearest whole number,
# you can just cast the answer as an int.
print(9/7)
print(int(9/7))

"""You can also do math using variables. Instead of just entering
the numbers as we have above, you can use the value of a variable
that either you set or a user enters to do operations."""
x = 2
y = int(input("Enter a number to be doubled: "))
print(x*y)

s = int(input("What is the side length of your square? "))
perimeter = 4*s
area = s**2
print("The perimeter of your square is " + str(perimeter) + " and the area of your square is " + str(area))