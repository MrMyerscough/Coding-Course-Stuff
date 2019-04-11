import random

print('1 - Final Grade Calculator')
print('2 - Number Wheel')
print('3 - What to Wear')

user_choice = input('choose an option: ')

if user_choice == '1':
    print('welcome to the final grade calculator!')
    print('1 - Calculate what I need!')
    print('2 - Calculate what I got!')
    user_sub_choice = input('choose an option: ')
    if user_sub_choice  == '1':
        current_grade = float(input('what do you have in the class? '))
        wanted_grade = float(input('what grade do you want to get? '))
        weight = float(input('what percent is your final worth? '))
        weight /= 100
        needed_grade = (wanted_grade - current_grade * (1 - weight)) / weight
        print('you need a ' + str(needed_grade)[:6] + '% to get ' + str(wanted_grade) + '%' + ' in the class!')
    elif user_sub_choice == '2':
        current_grade = float(input('what do you have in the class? '))
        exam_grade = float(input('what grade did you get on the final exam? '))
        weight = float(input('what percent is your final worth? '))
        weight /= 100
        final_grade = exam_grade * weight + current_grade * (1 - weight)
        print('you got a ' + str(final_grade)[:6] + '%' + ' in the class overall!')

elif user_choice == '2':
    print('Welcome to the number wheel!')
    start = int(input('lowest number? '))
    end = int(input('highest number? '))
    random_number = random.randint(start, end)
    print('the wheel landed on ' + str(random_number) + "!")

elif user_choice == '3':
    temperature = float(input('what is the temperature outside? (F) '))
    precipitation = float(input('what is the percent chance of precipitation right now? '))
    if temperature > 75 and precipitation <= 30:
        print('you should wear a t-shirt!')
    elif temperature > 75 and precipitation > 30:
        print('you should wear a poncho!')
    elif temperature > 65 and precipitation <= 30:
        print('you should wear a long sleeve!')
    elif temperature > 65 and precipitation > 30:
        print('you should wear a jacket!')
    elif temperature > 50 and precipitation <= 30:
        print('you should wear a hoodie!')
    elif temperature > 50 and precipitation > 30:
        print('you should wear a rain coat!')
    else: 
        print('you should wear a coat!')