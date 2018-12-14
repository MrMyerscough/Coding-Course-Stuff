import tkinter

def submit_quiz(score: tkinter.IntVar):
    root.destroy()
    root2 = tkinter.Tk()
    root2.title("Scores")
    root2.mainloop()

    score_screen = tkinter.Frame(root2)
    score_screen.pack()

    s_screen = tkinter.Label(score_screen, text = "Thanks for playing! Your score is: ", font = ("Times", 12, "bold"))
    s_screen.pack()

    percent = tkinter.Label(score_screen, textvariable = score.get(), font = ("Times", 12))
    percent.pack()

    if score.get() == 0:
        message = tkinter.Label(score_screen, text = "You don't know anything about Batman! What's wrong with you??", font = ("Times", 12, "bold"))
        message.pack()
    elif score.get() > 85:
        message = tkinter.Label(score_screen, text = "Holy superfan Batman! You really know your stuff!", font = ("Times", 12, "bold"))
        message.pack()
    else:
        message = tkinter.Label(score_screen, text = "You need to study your Batman facts!", font = ("Times", 12, "bold"))
        message.pack()

# This is the function that runs the Batman Quiz
def batman():
    # This creates all of the local variables for the quiz answers
    ans1 = tkinter.StringVar()
    ans2 = tkinter.StringVar() 
    ans3 = tkinter.StringVar() 
    ans4 = tkinter.StringVar() 
    ans5 = tkinter.StringVar() 
    ans6 = tkinter.StringVar() 
    score = tkinter.IntVar()
    score.set(0)

    # This creates the questions and entry boxes for the quiz questions
    q1 = tkinter.Label(root, text = "What is Batman's secret identity?", font = ("Times", 12, "bold"))
    q1e = tkinter.Entry(root, text = ans1, font = ("Times", 12))
    q1.pack()
    q1e.pack()

    q2 = tkinter.Label(root, text = "What is Batman's sidekick's superhero name?", font = ("Times", 12, "bold"))
    q2e = tkinter.Entry(root, text = ans2, font = ("Times", 12))
    q2.pack()
    q2e.pack()

    q3 = tkinter.Label(root, text = "Who is Batman's biggest villain?", font = ("Times", 12, "bold"))
    q3e = tkinter.Entry(root, text = ans3, font = ("Times", 12))
    q3.pack()
    q3e.pack()

    q4 = tkinter.Label(root, text = "Who is Batman's son?", font = ("Times", 12, "bold"))
    q4e = tkinter.Entry(root, text = ans4, font = ("Times", 12))
    q4.pack()
    q4e.pack()

    q5 = tkinter.Label(root, text = "Who played Batman in the 1960's Batman TV show?", font = ("Times", 12, "bold"))
    q5e = tkinter.Entry(root, text = ans5, font = ("Times", 12))
    q5.pack()
    q5e.pack()

    q6 = tkinter.Label(root, text = "Who is Batman's trusted butler?", font = ("Times", 12, "bold"))
    q6e = tkinter.Entry(root, text = ans6, font = ("Times", 12))
    q6.pack()
    q6e.pack()

    submit = tkinter.Button(root, text = "Submit", command = submit_quiz(score))
    submit.pack(side = "bottom")

    if ans1.get().lower().strip() == "bruce wayne":
        score.set(score.get() + 1)
    if ans2.get().lower().strip() == "robin":
        score.set(score.get() + 1) 
    if ans3.get().lower().strip() == "joker" or ans3.get().lower().strip() == "the joker":
        score.set(score.get() + 1)
    if ans4.get().lower().strip() == "damian" or ans4.get().lower().strip() == "damian wayne":
        score.set(score.get() + 1)
    if ans5.get().lower().strip() == "adam west":
        score.set(score.get() + 1)
    if ans6.get().lower().strip() == "alfred":
        score.set(score.get() + 1)

    # This creates the screen that shows the score
    score.set(score.get() / 6 * 100)
    
# # This is the function that runs the Green Lantern Quiz
# def lantern():
# # This creates all of the local variables for the quiz answers
#     ans1 = tkinter.StringVar()
#     ans2 = tkinter.StringVar() 
#     ans3 = tkinter.StringVar() 
#     ans4 = tkinter.StringVar() 
#     ans5 = tkinter.StringVar() 
#     ans6 = tkinter.StringVar() 

#     # This creates the questions and entry boxes for the quiz questions
#     frame1.pack()
#     q1 = tkinter.Label(frame1, text = "What is Green Lanterns's secret identity?", font = ("Times", 12, "bold"))
#     q1e = tkinter.Entry(frame1, text = ans1, font = ("Times", 12))
#     q1b = tkinter.Button(frame1, text = "Submit", font = ("Times", 12), command = destruction(frame1))
#     q1.pack(side = "top")
#     q1e.pack(side = "left")
#     q1b.pack(side = "left")

#     q2 = tkinter.Label(frame2, text = "Who are the leaders of the Green Lantern Corps", font = ("Times", 12, "bold"))
#     q2e = tkinter.Entry(frame2, text = ans2, font = ("Times", 12))
#     q2b = tkinter.Button(frame2, text = "Submit", font = ("Times", 12), command = destruction(frame2))
#     q2.pack(side = "top")
#     q2e.pack(side = "left")
#     q2b.pack(side = "left")

#     q3 = tkinter.Label(frame3, text = "Who is Green Lantern's biggest villain?", font = ("Times", 12, "bold"))
#     q3e = tkinter.Entry(frame3, text = ans3, font = ("Times", 12))
#     q3b = tkinter.Button(frame3, text = "Submit", font = ("Times", 12), command = destruction(frame3))
#     q3.pack(side = "top")
#     q3e.pack(side = "left")
#     q3b.pack(side = "left")

#     q4 = tkinter.Label(frame4, text = "Who is Hal Jordan's girlfriend?", font = ("Times", 12, "bold"))
#     q4e = tkinter.Entry(frame4, text = ans4, font = ("Times", 12))
#     q4b = tkinter.Button(frame4, text = "Submit", font = ("Times", 12), command = destruction(frame4))
#     q4.pack(side = "top")
#     q4e.pack(side = "left")
#     q4b.pack(side = "left")

#     q5 = tkinter.Label(frame5, text = "Who played Green Lantern in the 2011 movie?", font = ("Times", 12, "bold"))
#     q5e = tkinter.Entry(frame5, text = ans5, font = ("Times", 12))
#     q5b = tkinter.Button(frame5, text = "Submit", font = ("Times", 12), command = destruction(frame5))
#     q5.pack(side = "top")
#     q5e.pack(side = "left")
#     q5b.pack(side = "left")

#     q6 = tkinter.Label(frame6, text = "What is the emotion that the Red Lantern Corps is based on?", font = ("Times", 12, "bold"))
#     q6e = tkinter.Entry(frame6, text = ans6, font = ("Times", 12))
#     q6b = tkinter.Button(frame6, text = "Submit", font = ("Times", 12), command = frame6.destroy())
#     q6.pack(side = "top")
#     q6e.pack(side = "left")
#     q6b.pack(side = "left")

#     # This calculates the score by comparing all of the answers to the correct answers
#     if ans1.get().lower().strip() == "hal jordan":
#         score = score.get() + 1
#     if ans2.get().lower().strip() == "guardians" or ans2.get().lower().strip() == "the guardians":
#         score = score.get() + 1
#     if ans3.get().lower().strip() == "sinestro":
#         score = score.get() + 1
#     if ans4.get().lower().strip() == "carol" or ans4.get().lower().strip() == "carol ferris":
#         score = score.get() + 1
#     if ans5.get().lower().strip() == "ryan reynolds":
#         score = score.get() + 1
#     if ans6.get().lower().strip() == "rage" or ans6.get().lower().strip() == "anger":
#         score = score.get() + 1

#     # This creates the screen that shows the score
#     score = score.get() / 6 * 100
    
#     score_screen = tkinter.Frame(root)
#     score_screen.pack()

#     s_screen = tkinter.Label(score_screen, text = "Thanks for playing! Your score is: ", font = ("Times", 12, "bold"))
#     s_screen.pack()

#     percent = tkinter.Label(score_screen, textvariable = score.get(), font = ("Times", 12))
#     percent.pack()

#     if score.get() == 0:
#         message = tkinter.Label(score_screen, text = "You don't know anything about Green Lantern! What's wrong with you??", font = ("Times", 12, "bold"))
#         message.pack()
#     elif score.get() > 85:
#         message = tkinter.Label(score_screen, text = "Wow! You really know your Green Lantern facts!", font = ("Times", 12, "bold"))
#         message.pack()
#     else:
#         message = tkinter.Label(score_screen, text = "You need to study your Green Lantern facts!", font = ("Times", 12, "bold"))
#         message.pack()

# # This is the function that runs the Superman Quiz
# def superman():
#     # This creates all of the local variables for the quiz answers
#     ans1 = tkinter.StringVar()
#     ans2 = tkinter.StringVar() 
#     ans3 = tkinter.StringVar() 
#     ans4 = tkinter.StringVar() 
#     ans5 = tkinter.StringVar() 
#     ans6 = tkinter.StringVar() 

#     # This creates the questions and entry boxes for the quiz questions
#     frame1.pack()
#     q1 = tkinter.Label(frame1, text = "What is Superman's secret identity?", font = ("Times", 12, "bold"))
#     q1e = tkinter.Entry(frame1, text = ans1, font = ("Times", 12))
#     q1b = tkinter.Button(frame1, text = "Submit", font = ("Times", 12), command = destruction(frame1))
#     q1.pack(side = "top")
#     q1e.pack(side = "left")
#     q1b.pack(side = "left")

#     q2 = tkinter.Label(frame2, text = "What is the name of Superman's crime fighting dog?", font = ("Times", 12, "bold"))
#     q2e = tkinter.Entry(frame2, text = ans2, font = ("Times", 12))
#     q2b = tkinter.Button(frame2, text = "Submit", font = ("Times", 12), command = destruction(frame2))
#     q2.pack(side = "top")
#     q2e.pack(side = "left")
#     q2b.pack(side = "left")

#     q3 = tkinter.Label(frame3, text = "Who is Superman's girlfriend?", font = ("Times", 12, "bold"))
#     q3e = tkinter.Entry(frame3, text = ans3, font = ("Times", 12))
#     q3b = tkinter.Button(frame3, text = "Submit", font = ("Times", 12), command = destruction(frame3))
#     q3.pack(side = "top")
#     q3e.pack(side = "left")
#     q3b.pack(side = "left")

#     q4 = tkinter.Label(frame4, text = "What newspaper company does Superman work for?", font = ("Times", 12, "bold"))
#     q4e = tkinter.Entry(frame4, text = ans4, font = ("Times", 12))
#     q4b = tkinter.Button(frame4, text = "Submit", font = ("Times", 12), command = destruction(frame4))
#     q4.pack(side = "top")
#     q4e.pack(side = "left")
#     q4b.pack(side = "left")

#     q5 = tkinter.Label(frame5, text = "Who is the current actor who plays Superman?", font = ("Times", 12, "bold"))
#     q5e = tkinter.Entry(frame5, text = ans5, font = ("Times", 12))
#     q5b = tkinter.Button(frame5, text = "Submit", font = ("Times", 12), command = destruction(frame5))
#     q5.pack(side = "top")
#     q5e.pack(side = "left")
#     q5b.pack(side = "left")

#     q6 = tkinter.Label(frame6, text = "What planet is Superman from?", font = ("Times", 12, "bold"))
#     q6e = tkinter.Entry(frame6, text = ans6, font = ("Times", 12))
#     q6b = tkinter.Button(frame6, text = "Submit", font = ("Times", 12), command = frame6.destroy())
#     q6.pack(side = "top")
#     q6e.pack(side = "left")
#     q6b.pack(side = "left")

#     # This calculates the score by comparing all of the answers to the correct answers
#     if ans1.get().lower().strip() == "clark kent":
#         score = score.get() + 1
#     if ans2.get().lower().strip() == "krypto" or ans2.get().lower().strip() == "krypto the superdog":
#         score = score.get() + 1
#     if ans3.get().lower().strip() == "lois lane" or ans3.get().lower().strip() == "lois":
#         score = score.get() + 1
#     if ans4.get().lower().strip() == "daily planet":
#         score = score.get() + 1
#     if ans5.get().lower().strip() == "henry cavill":
#         score = score.get() + 1
#     if ans6.get().lower().strip() == "krypton":
#         score = score.get() + 1

#     # This creates the screen that shows the score
#     score = score.get() / 6 * 100
    
#     score_screen = tkinter.Frame(root)
#     score_screen.pack()

#     s_screen = tkinter.Label(score_screen, text = "Thanks for playing! Your score is: ", font = ("Times", 12, "bold"))
#     s_screen.pack()

#     percent = tkinter.Label(score_screen, textvariable = score.get(), font = ("Times", 12))
#     percent.pack()

#     if score.get() == 0:
#         message = tkinter.Label(score_screen, text = "You don't know anything about Superman! What's wrong with you??", font = ("Times", 12, "bold"))
#         message.pack()
#     elif score.get() > 85:
#         message = tkinter.Label(score_screen, text = "Wow! You really know your Superman facts!", font = ("Times", 12, "bold"))
#         message.pack()
#     else:
#         message = tkinter.Label(score_screen, text = "You need to study your Superman facts!", font = ("Times", 12, "bold"))
#         message.pack()

def end():
    root.destroy()

root = tkinter.Tk()
root.title("Quiz Program")
root2 = None

menubar = tkinter.Menu(root)

gamemenu = tkinter.Menu(menubar, tearoff = 0)

gamemenu.add_command(label = "Batman Quiz", command = batman)
#gamemenu.add_command(label = "Green Lantern Quiz", command = lantern)
#gamemenu.add_command(label = "Superman Quiz", command = superman)
gamemenu.add_separator()
gamemenu.add_command(label = "Quit", command = end)
menubar.add_cascade(label = "Games", menu = gamemenu)

root.config(menu = menubar)
root.mainloop()