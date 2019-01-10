print("You wake up in your bed. It's monday morning. What do you do?")
choice = input("Go to school (1) or Skip school (2)")
if choice == "1":
    print("You go to math class. Mr. Gill tells you you have a surprise test. What do you do?")
    choice = input("Fall asleep (1) or Show him whose boss (2)")
    if choice == "1":
         print("You fail your test since you fall asleep. Mr. Gill, in all his fury, expells you immediately. GAME OVER")
    elif choice == "2":
        print("You put every ounce of effort you have into that test, and you get 100%. Your parents are so proud of you they decide to buy you ice cream. CONGRATS!")
elif choice == "2":
    print("You decide to skip school. Where do you go on your day playing hookie?")
    choice = input("Go to the pool (1), the skatepark (2), or the arcade (3)")
    if choice == "1":
        print("You go to the pool. There is a waterslide, a lazy river, and a wave pool. Where do you want to go?")
        choice = input("Go to the waterslide (1), the lazy river(2), or the wave pool (3)")
        if choice == "1":
            print("You go down the waterslide. It's the largest one you have ever seen. You have so much fun, you go back over and over, and have a great day. CONGRATS!")
        elif choice == "2":
            print("You go into the lazy river. It's so relaxing you fall asleep on the tube, and you wake up hours later, burned to a crisp from the hot sun. You look like a lobster. GAME OVER")
        else:
            print("You go to the wavepool. The lifeguard tells you no diving at all, but you decide to dive into the pool to see how deep you can do. You go so deep you hit your head on the floor, and the lifeguard pulls you out and calls your mom, who is furious that you skipped school. GAME OVER")
    elif choice == "2":
        print("You're at the skatepark with some friends. You see some girls watching you and your friends. What do you do?")
        choice = input("Do a sick kickflip (1) or grind the rail (2)")
        if choice == "1":
            print("You nail that kickflip so hard that one of the girls comes over and asks if you want to go get dinner tonight. CONGRATS!")
        elif choice == "2":
            print("You try to grind the rail, and you fall off and break your leg. Everyone laughs at your pain as your mom shows up, furious at you, and takes you to the hospital. GAME OVER")
    else:
        print("You're at the arcade. What do you want to do?")
        choice = input("Play Pac-Man (1), play Polybius (2), or go eat arcade pizza (3)")
        if choice == "1":
            print("You start playing Pac-Man, and soon you have gathered a crowd watching as you break the high score that has been on the machine for 10 years. Everyone cheers you on like a hero. CONGRATS")
        elif choice == "2":
            print("You start to play Polybius, and realize that this is such a great game that you just can't stop playing. 8 hours and $55 later, your mom comes into the arcade and pulls you away from the machine, furious that you spent so much money and skipped school. GAME OVER")
        else:
            print("The cheese on the arcade pizza is so stringy that it just keeps coming off the pizza, and you can't swallow it all at once. You start to choke, and before someone gets over to help you, you collapse and die. GAME OVER")