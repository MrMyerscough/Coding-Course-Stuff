# data = open('data2.txt', 'a')

# lines = data.readlines()

# for line in lines: 
#     print( line.capitalize() )

# data.write('hi')
# data.write('hello')
# data.close()



# for line in data:
#     line = line.strip()

#     print(line)

# import random 

# with open('python/unit 3/data.txt', 'w') as my_file:
#     for i in range(100):
#         random_number = random.randint(1, 5000)
#         my_file.write( str(random_number) + '\n')

# names = []

# with open('python/unit 3/data.txt', 'r+') as my_file:
#     for line in my_file:
#         names.append( line.strip() )
#     my_file.seek(0)
#     my_file.write('hjewfklds')

# print(names)

# def my_function():
#     # code goes here
#     print('hi there!')
#     print('you just called my function!')

# my_function()

# numbers = []
# total = 0

# with open('data.txt', 'r') as my_file:
#     for line in my_file:
#         number = int(line)
#         numbers.append(number)
#         total += number

# average = total / len(numbers)
# largest = max(numbers)
# smallest = min(numbers)

# print('The total of all numbers is', total)
# print('The average of all numbers is', average)
# print('The largest number is', largest)
# print('The smallest number is', smallest)

# import random

# # open text file in write mode
# with open('data.txt', 'w') as my_file:
#     # generate and write random numbers
#     for i in range(100):
#         random_number = random.randint(1,5000)
#         my_file.write( str(random_number) + '\n' )

# reference = "abcdefghijklmnopqrstuvwxyz1234567890.,:!? "
# key       = "5w7m ktjvu@fd2hi#910.rg3*y8nso{!b?4+6zclxe"

# x = 'hello'
# encrypted = ''

# for letter in x:
#     if letter in reference:
#         position = reference.index(letter)
#         encrypted = encrypted + key[position]

# print(encrypted)



with open('output.txt', 'u+') as my_file:
    my_file.write('55')
    my_file.write('20')
    my_file.write('99')






result = ''

with open('data.txt', 'r') as my_file:
    for line in my_file:
        number = int(line)
        if number > 15:
            result += 'H'
        else:
            result += 'L'

print(result)