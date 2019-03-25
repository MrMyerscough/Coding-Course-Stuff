dollars = float(input('Enter an amount of US dollars: '))
euros = dollars / 1.13
print(f'${dollars} is equivalent to €{str(euros)[0:5]}')

sentence = input('enter a sentence: ')
a = sentence.count('a')
e = sentence.count('e')
i = sentence.count('i')
o = sentence.count('o')
u = sentence.count('u')

vowels = a + e + i + o + u
print('there are', vowels, 'vowels in your sentence')
print(f"{a} A's - {str(a/len(sentence))[0:5]}%")
print(f"{e} E's - {str(e/len(sentence))[0:5]}%")
print(f"{i} I's - {str(i/len(sentence))[0:5]}%")
print(f"{o} O's - {str(o/len(sentence))[0:5]}%")
print(f"{u} U's - {str(u/len(sentence))[0:5]}%")

one = float(input('enter a number: '))
two = float(input('enter another number: '))
three = float(input('enter a third number: '))

is_one_largest = one > two and one > three
is_two_largest = two > one and two > three
is_three_largest = three > one and three > two

print(f'{one} is the largest: {is_one_largest}')
print(f'{two} is the largest: {is_two_largest}')
print(f'{three} is the largest: {is_three_largest}')