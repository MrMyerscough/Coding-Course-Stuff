def fibonacci(number: int):
   if number <= 1:
       return number
   else:
       return fibonacci(number-1) + fibonacci(number-2)

print(fibonacci(10))

def un_fibonacci(number: int, count: int = 1):
    if number == 1:
        return count+1
    else:
        return un_fibonacci(number - fibonacci(count), count = count + 1)

print(un_fibonacci(55))

def factorial(number: int):
    if number == 1:
        return number
    else:
        return number * factorial(number-1)

print(factorial(5))

def un_factorial(number: int, count: int = 1):
    if number == 1:
        return count-1
    else:
        return un_factorial(number = number/count, count = count + 1)

print(un_factorial(720))