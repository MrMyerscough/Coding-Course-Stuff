divisor = int(input('what do you want to divide?'))
dividend = int(input('what do you want to divide by?'))

quotient = divisor // dividend
remainder = divisor % dividend

print('the answer is', quotient, 'and', str(remainder) + "/" + str(dividend))