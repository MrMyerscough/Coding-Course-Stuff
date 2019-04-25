# print('hello there!')
# user_number = input('pick a number')
# x = int(user_number)
# x *= 2
# print(user_number, 'x 2 =', x)

# user_choice = ''

# while user_choice != 'yes':
#     user_choice = input('do you want to stop yet? ')

# print('okay.')

# outer_count = 0

# while outer_count < 5:

#     inner_count = 0

#     while inner_count < 3:
#         print(outer_count, inner_count)
#         inner_count += 1
    
#     outer_count += 1

outer_count = 1

while outer_count <= 10:

    inner_count = 1

    while inner_count <= 10:
        print(f'{outer_count} x {inner_count} = {outer_count * inner_count}')
        inner_count += 1
    
    outer_count += 1