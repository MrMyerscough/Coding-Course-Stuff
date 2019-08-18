# print('Welcome to the Trivia Quiz!')
# print('Here are 10 questions. Answer them to the best of your knowledge!')

# questions = []
# answers = []
# user_answers = []
# correct = 0

# with open('quiz_questions.txt', 'r') as my_file:
#     for line in my_file:
#         questions.append(line.strip())

# with open('quiz_answers.txt', 'r') as my_file:
#     for line in my_file:
#         answers.append(line.strip())

# done = False

# option = '1'

# while not done:

#     if option == '1':
#         user_answers.clear()
#         for i in range(len(questions)):
#             print(f'Question {i + 1}:')
#             answer = input(questions[i] + ' ')
#             user_answers.append(answer)
#         for i in range(len(questions)):
#             if answers[i].lower().strip() == user_answers[i].lower().strip():
#                 correct += 1
#         print('Your results:')
#         print(f'You got {correct} out of {len(questions)}, or {correct / len(questions) * 100}%')
#     if option == '2':
#         for i in range(len(questions)):
#             print(f'Question {i + 1}:')
#             print(questions[i])
#             print('Correct Answer:')
#             print(answers[i])
#             print()
#     elif option == '3':
#         with open('quiz_results.txt', 'w') as my_file:
#             for i in range(len(questions)):
#                 my_file.write(f'Question {i + 1}:\n')
#                 my_file.write(questions[i] + '\n')
#                 my_file.write('User Answer:\n')
#                 my_file.write(user_answers[i] + '\n\n')
#         for i in range(len(questions)):
#             if answers[i].lower().strip() == user_answers[i].lower().strip():
#                 correct += 1
#         my_file.write('Results:\n')
#         my_file.write(f'{correct} out of {len(questions)}, or {correct / len(questions) * 100}%')
#     elif option == '4':
#         done = True 
#     else:
#         print('Not a valid menu option')

#     print('1 - Retake the quiz')
#     print('2 - See correct answers')
#     print('3 - Save your results to quiz_results.txt')
#     print('4 - Quit the program')
#     option = input()

transactions = []

with open('account.txt', 'r') as my_file:
    for line in my_file:
        transactions.append(float(line))

print('Welcome to the ATM!')

done = False 

while not done:
    print('1 - Account Summary')
    print('2 - Make a Deposit')
    print('3 - Make a Withdrawal')
    print('4 - Quit the program')
    choice = input('Pick an option.')
    print()

    if choice == "1":
        for transaction in transactions:
            if transaction > 0:
                print(f'Deposit:    {transaction}')
            else:
                print(f'Withdrawal: {transaction}')
        balance = 0
        for transaction in transactions:
            balance += transaction
        print()
        print(f'The total balance for the account is ${balance}')
        print()
    elif choice == "2":
        amount = float(input('Deposit amount? '))
        transactions.append(amount)
        with open('account.txt', 'w') as my_file:
            for transaction in transactions:
                my_file.write(str(transaction) + '\n')
        balance = 0
        for transaction in transactions:
            balance += transaction
        print()
        print(f'The total balance for the account is now ${balance}')
        print()
    elif choice == "3":
        amount = -float(input('Withdrawal amount?'))
        transactions.append(amount)
        with open('account.txt', 'w') as my_file:
            for transaction in transactions:
                my_file.write(str(transaction) + '\n')
        balance = 0
        for transaction in transactions:
            balance += transaction
        print()
        print(f'The total balance for the account is now ${balance}')
        print()
    elif choice == "4":
        print('Thank you for using this ATM!')
        done = True 
    else:
        print('Not a valid option!')