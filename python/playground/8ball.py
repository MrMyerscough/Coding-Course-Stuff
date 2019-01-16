import random

print("Welcome to the 8 ball!")
input("Please ask a question: ")

random_number = random.randint(0,5)

if random_number == 0:
    print("heck no. sweetie no.")
elif random_number == 1:
    print("maaaybeee ?")
elif random_number == 2:
    print("what kind of a question is that?? of course ??")
elif random_number == 3:
    print("yeah. sure.")
elif random_number == 4:
    print("*magic conch shell voice* no")
else:
    print("mmhm. totally. ")