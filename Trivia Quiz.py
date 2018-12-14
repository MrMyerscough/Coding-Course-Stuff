"""This program is a trivia quiz game created for the functions
lab in Intro to Programming - Python. It will show a menu where
the user can select from different quizzes, and uses functions
to display the different quizzes."""

# This function is the Batman trivia game with 6 questions
def Batman():
    # This resets the number correct every time the function starts
    num_right = 0
    
    # This is where the questions start. The user input is compared
    # To the correct answer, and a running tally is kept.
    ans_1 = input("What is Batman's secret identity?")
    if ans_1 == "Bruce Wayne":
        print("Correct!")
        num_right = num_right+1
    else: 
        print("Wrong! It's Bruce Wayne")
    
    ans_2 = input("What is Batman's sidekick's superhero name?")
    if ans_2 == "Robin":
        print("Correct!")
        num_right = num_right+1
    else: 
        print("Wrong! It's Robin")
    
    ans_3 = input("Who is Batman's biggest villain?")
    if ans_3 == "Joker" or ans_3 == "The Joker":
        print("Correct!")
        num_right = num_right+1
    else: 
        print("Wrong! It's The Joker")

    ans_4 = input("Who is Batman's son?")
    if ans_4 == "Damian Wayne" or ans_4 == "Damian":
        print("Correct!")
        num_right = num_right+1
    else: 
        print("Wrong! It's Damian Wayne")

    ans_5 = input("Who played Batman in the 1960's Batman TV show?")
    if ans_5 == "Adam West":
        print("Correct!")
        num_right = num_right+1
    else: 
        print("Wrong! It's Adam West")

    ans_6 = input("Who is Batman's trusted butler?")
    if ans_6 == "Alfred" or ans_6 == "Alfred Pennyworth":
        print("Correct!")
        num_right = num_right+1
    else: 
        print("Wrong! It's Alfred")
    
    # The users score on the quiz is calculated here and displayed.
    score = (num_right/6)*100
    print("Thanks for playing the Batman trivia game!")
    print("You got " + str(num_right) + " correct, and got a " + str(score) + "%")
    if score >= 80:
        print("Great job! You really know your stuff!")
    else:
        print("You need to study more!")

# This function is the Green Lantern trivia game with 6 questions
def Lantern():
# This resets the number correct every time the function starts
    num_right = 0
    
    # This is where the questions start. The user input is compared
    # To the correct answer, and a running tally is kept.
    ans_1 = input("What is Green Lanterns's secret identity?")
    if ans_1 == "Hal Jordan":
        print("Correct!")
        num_right = num_right+1
    else: 
        print("Wrong! It's Hal Jordan")
    
    ans_2 = input("Who are the leaders of the Green Lantern Corps")
    if ans_2 == "Guardians" or ans_2 == "The Guardians":
        print("Correct!")
        num_right = num_right+1
    else: 
        print("Wrong! It's The Guardians")
    
    ans_3 = input("Who is Green Lantern's biggest villain?")
    if ans_3 == "Sinestro":
        print("Correct!")
        num_right = num_right+1
    else: 
        print("Wrong! It's Sinestro")

    ans_4 = input("Who is Hal Jordan's girlfriend?")
    if ans_4 == "Carol Ferris" or ans_4 == "Carol":
        print("Correct!")
        num_right = num_right+1
    else: 
        print("Wrong! It's Carol Ferris")

    ans_5 = input("Who played Green Lantern in the 2011 movie?")
    if ans_5 == "Ryan Reynolds":
        print("Correct!")
        num_right = num_right+1
    else: 
        print("Wrong! It's Ryan Reynolds")

    ans_6 = input("What is the emotion that the Red Lantern Corps is based on?")
    if ans_6 == "Rage" or ans_6 == "Anger":
        print("Correct!")
        num_right = num_right+1
    else: 
        print("Wrong! It's Rage or Anger")
    
    # The users score on the quiz is calculated here and displayed.
    score = (num_right/6)*100
    print("Thanks for playing the Green Lantern trivia game!")
    print("You got " + str(num_right) + " correct, and got a " + str(score) + "%")
    if score >= 80:
        print("Great job! You really know your stuff!")
    else:
        print("You need to study more!")

# This function is the Superman trivia game with 6 questions
def Superman():
# This resets the number correct every time the function starts
    num_right = 0
    
    # This is where the questions start. The user input is compared
    # To the correct answer, and a running tally is kept.
    ans_1 = input("What is Superman's secret identity?")
    if ans_1 == "Clark Kent":
        print("Correct!")
        num_right = num_right+1
    else: 
        print("Wrong! It's Clark Kent")
    
    ans_2 = input("What is the name of Superman's crime fighting dog?")
    if ans_2 == "Krypto":
        print("Correct!")
        num_right = num_right+1
    else: 
        print("Wrong! It's Krypto the Superdog")
    
    ans_3 = input("Who is Superman's girlfriend?")
    if ans_3 == "Lois Lane":
        print("Correct!")
        num_right = num_right+1
    else: 
        print("Wrong! It's Lois Lane")

    ans_4 = input("What newspaper company does Superman work for?")
    if ans_4 == "Daily Planet":
        print("Correct!")
        num_right = num_right+1
    else: 
        print("Wrong! It's the Daily Planet")

    ans_5 = input("Who is the current actor who plays Superman?")
    if ans_5 == "Henry Cavill":
        print("Correct!")
        num_right = num_right+1
    else: 
        print("Wrong! It's Henry Cavill")

    ans_6 = input("What planet is Superman from?")
    if ans_6 == "Krypton":
        print("Correct!")
        num_right = num_right+1
    else: 
        print("Wrong! It's Krypton")
    
    # The users score on the quiz is calculated here and displayed.
    score = (num_right/6)*100
    print("Thanks for playing the Superman trivia game!")
    print("You got " + str(num_right) + " correct, and got a " + str(score) + "%")
    if score >= 80:
        print("Great job! You really know your stuff!")
    else:
        print("You need to study more!")

# This is the menu when the program starts. The while loop makes
# the menu run until exit is selected.
while True:
    print("Welcome to Mr. Myerscough's trivia game! Select your quiz")
    print("Batman Trivia - B")
    print("Green Lantern Trivia - G")
    print("Superman Trivia - S")
    print("Exit - E")
    choice = input()

    # This checks what the user entered and runs the appropriate
    # function.
    if choice == "B" or choice == "b":
        Batman()
    elif choice == "G" or choice == "g":
        Lantern()
    elif choice == "S" or choice == "s":
        Superman()
    elif choice == "E" or choice == "e":
        break
    else:
        print("That's not a valid response.")

print("Thanks for playing!")

