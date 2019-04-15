# import random
# exit = False 
# print('welcome to math practice! pick an option.')

# while exit != True:
#     print('1 - practice addition')
#     print('2 - practice subtraction')
#     print('3 - practice multiplication')
#     print('4 - practice division')
#     print('5 - exit')

#     choice = input()

#     if choice == '1':
#         one = random.randint(1, 100)
#         two = random.randint(1,100)
#         answer = int(input(f'what is {one} + {two}? '))
#         if answer == one + two:
#             print('correct!')
#         else:
#             print(f'incorrect! the correct answer was {one + two}.')
#     elif choice == '2':
#         one = random.randint(1, 100)
#         two = random.randint(1,100)
#         answer = int(input(f'what is {one} - {two}? '))
#         if answer == one - two:
#             print('correct!')
#         else:
#             print(f'incorrect! the correct answer was {one - two}.')
#     elif choice == '3':
#         one = random.randint(1, 12)
#         two = random.randint(1, 12)
#         answer = int(input(f'what is {one} x {two}? '))
#         if answer == one * two:
#             print('correct!')
#         else:
#             print(f'incorrect! the correct answer is {one * two}.')
#     elif choice == '4':
#         one = random.randint(1, 12)
#         two = random.randint(1, 12)
#         product = one * two
#         answer = int(input(f'what is {product} ÷ {one}? '))
#         if answer == two:
#             print('correct!')
#         else:
#             print(f'incorrect! the correct answer is {two}.')
#     elif choice == '5':
#         exit = True
#     else: 
#         print('not a valid menu option!')


# count = 0
# while True:
#     print(count)
#     count += 1
#     if count == 10:
#         break

# stop = False
# print('pick an option')

# while not stop:
#     print('1 - option one')
#     print('2 - option two')
#     print('3 - option three')
#     print('4 - quit')

#     choice = input()

#     if choice == '1':
#         print('you chose option one!')
#     elif choice == '2':
#         print('you chose option two!')
#     elif choice == '3':
#         print('you chose option three!')
#     elif choice == '4':
#         stop = True 
#     else:
#         print('not a menu option!')

# first_names = ['james', 'john', 'jack', 'jerry', 'julian']
# last_names = ['cross', 'doe', 'harrison', 'beck', 'poole' ]
# count = 0

# while count < len(first_names):
#     print(first_names[count], last_names[count])
#     count += 1