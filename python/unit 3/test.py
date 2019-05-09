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

# outer_count = 1

# while outer_count <= 10:

#     inner_count = 1

#     while inner_count <= 10:
#         print(f'{outer_count} x {inner_count} = {outer_count * inner_count}')
#         inner_count += 1
    
#     outer_count += 1

# count = 0
# total = 100

# while count < 10:
#     total -= 5
#     count += 1

# print(total)
# key = ''

# while len(key) < 8:
#     key = key + 'jump'

# print(key)

# count = 20

# while count <= 50:
#     count += 2
#     print(count)

# import random

# user_wins = 0
# computer_wins = 0

# while user_wins < 5 and computer_wins < 5:
#     user_choice = input('heads or tails? ')
#     random_number = random.randint(1,2)
#     if random_number == 1:
#         computer_choice = 'heads'
#     else: 
#         computer_choice = 'tails'

#     if user_choice == 'heads' and computer_choice == 'heads'
# mod = []
# done = False

# while not done:
#     user_input = input()
#     if user_input == 'stop':
#         done = True
#     else:
#         mod.append(int(user_input) + 5)

# print(mod)

# things = []

# done = False

# while not done:
#     user_input = input('add an object, or enter stop: ')
#     if user_input == 'stop':
#         done = True
#     else:
#         things.append(user_input)

# print(things)


# count = 0
# total = 100

# while count < 10:
#     total -= 5
#     count += 1

# print(total)



# key = ''

# while len(key) < 8:
#     key = key + 'jump'

# print(key)




# mod = []
# done = False

# while not done:
#     user_input = input()
#     if user_input == 'stop':
#         done = True
#     else:
#         mod.append(int(user_input) + 5)

# print(mod)



# count = 0
# numbers = []

# while count <= 13:
#     numbers.append(count)
#     count += 2

# print(numbers)


# print('hello there!')

# user_number = input('pick a number')

# x = int(user_number)

# x *= 2

# print(user_number, 'x 2 =', x)


# test_scores = [96, 100, 82, 84, 93, 100]

# total = 0

# for score in test_scores:
#     total = total + score

# average = total / len(test_scores)

# print('the average is', average)

# x = ['green', 'yellow', 'red', 'blue', 'orange']
# y = ['apple', 'lemon', 'strawberry', 'raspberry', 'orange']

# for i in range( len(x) ):
#     color = x[i]
#     flavor = y[i]
#     print(color, 'is', flavor, 'flavored!')

# x = [True, False, True]

# for boo in x:
#     boo = not boo

# print(x)

# import random
# x = []
# y = []

# for i in range(10):
#     x.append(random.randint(1,100))
#     y.append(random.randint(1,100))

# print(x)
# print(y)


#  ----------------


# dividends = [58, 87, 93, 88, 73, 66, 65, 88, 58, 78]
# divisors = [22, 31, 55, 38, 36, 12, 19, 24, 33, 27]

# greatest_remainder = 0

# for dividend in dividends:
#     for divisor in divisors:

#         if dividend % divisor > greatest_remainder:
#             greatest_remainder = dividend % divisor
#             greatest_dividend = dividend
#             greatest_divisor = divisor

# print(f'the greatest remainder was {greatest_dividend} / {greatest_divisor} = {greatest_remainder}')


# --------------

# words = ['hypothesis', 'coffee', 'iteration', 'software', 'landscape', 'code', 'rainbow']

# vowels = 'aeiou'

# most_occurrences = 0
# frequent_word = ''

# for word in words:

#     # how many vowels are in the word
#     vowel_count = 0

#     # for every vowel, count how many are in the word, and add that to the count
#     for vowel in vowels:
#         vowel_count += word.count(vowel)
    
#     if vowel_count > most_occurrences: 
#         most_occurrences = vowel_count
#         frequent_word = word

# print(f"the word {frequent_word} had the most vowels in it!")


# x = [58, 87, 93, 88, 73, 66, 65, 88, 58, 78]
# y = [22, 31, 55, 38, 36, 12, 19, 24, 33, 27]

# greatest_difference = 0
# first_number = 0
# second_number = 0

# for number_1 in x:
#     for number_2 in y:

#         if abs(number_1 - number_2) > greatest_difference:
#             greatest_difference = abs(number_1 - number_2)
#             first_number = number_1
#             second_number = number_2

# print(f'the greatest difference was between {first_number} and {second_number} of {greatest_difference}')


# math_students = ['matt', 'barry', 'alyssa', 'aliza', 'carl', 'john', 'beth', 'nate', 'hannah', 'drew']

# art_students = ['molly', 'katie', 'carl', 'jake', 'hannah', 'lila', 'noah', 'barry', 'sean', 'carlos']

# students_in_both = []

# # for math_student in math_students:
# #     for art_student in art_students:
# #         if math_student == art_student:
# #             students_in_both.append(math_student)

# students_in_both = list(set(math_students).intersection(set(art_students)))

# print('the following students are in both math and art:')
# for student in students_in_both:
#     print(student)

outro = ['code', 'dog', 'out']

for word in outro:
    print(word)