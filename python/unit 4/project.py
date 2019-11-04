# import random

# def create_list_from_file(filename='data.txt'):
#     collection = []
#     with open(filename, 'r') as my_file:
#         lines = my_file.readlines()
#         for line in lines:
#             collection.append(line.strip())
#     return collection


# def random_item(collection):
#     return random.choice(collection)

# def phrase_to_blanks(phrase):
#     blanks = ''
#     for letter in phrase:
#         if letter == ' ':
#             blanks += ' '
#         else:
#             blanks += '_'
#     return blanks

# def check_letter(letter, phrase):
#     for char in phrase:
#         if letter == char:
#             return True
#     # this will ONLY run if none of the letters are in the phrase
#     return False

# def replace_letters(letter, phrase, dashes):
#     for char in phrase:
#         if char == letter:


# phrases = create_list_from_file('phrases.txt')

# random_phrase = random_item(phrases)

# blanks = phrase_to_blanks(random_phrase)

# health = 5

# done = False

# while not done:
#     print(blanks)
#     guess = input('guess a letter or guess the phrase:')
#     if len(guess) == 1:
#         if check_letter(guess, random_phrase):
