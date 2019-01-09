"""Python trivia quiz - Bryan Myerscough
This program will create a practice quiz using the tkinter GUI."""

# This imports the tkinter library into Python.
import tkinter

# This function packs the next frame
def frame_pack(x):
    if x == frame1:
        frame2.pack()
    elif x == frame2:
        frame3.pack()
    elif x == frame3:
        frame4.pack
    elif x == frame4:
        frame5.pack()
    elif x == frame5:
        frame6.pack()

# This function destroys the current frame
def destruction(x):
    x.destroy()
    frame_pack(x)

# This is the function that runs the Batman Quiz
def batman():
    # This clears the screen from the menu to bring up the quiz
    root.destroy()

    root2.title("Batman Quiz")
    root2.mainloop()

    # This creates all of the local variables for the quiz answers
    ans1 = tkinter.StringVar()
    ans2 = tkinter.StringVar() 
    ans3 = tkinter.StringVar() 
    ans4 = tkinter.StringVar() 
    ans5 = tkinter.StringVar() 
    ans6 = tkinter.StringVar() 

    # This creates the questions and entry boxes for the quiz questions
    frame1.pack()
    q1 = tkinter.Label(frame1, text = "What is Batman's secret identity?", font = ("Times", 12, "bold"))
    q1e = tkinter.Entry(frame1, text = ans1, font = ("Times", 12))
    q1b = tkinter.Button(frame1, text = "Submit", font = ("Times", 12), command = destruction(frame1))
    q1.pack(side = "top")
    q1e.pack(side = "left")
    q1b.pack(side = "left")

    q2 = tkinter.Label(frame2, text = "What is Batman's sidekick's superhero name?", font = ("Times", 12, "bold"))
    q2e = tkinter.Entry(frame2, text = ans2, font = ("Times", 12))
    q2b = tkinter.Button(frame2, text = "Submit", font = ("Times", 12), command = destruction(frame2))
    q2.pack(side = "top")
    q2e.pack(side = "left")
    q2b.pack(side = "left")

    q3 = tkinter.Label(frame3, text = "Who is Batman's biggest villain?", font = ("Times", 12, "bold"))
    q3e = tkinter.Entry(frame3, text = ans3, font = ("Times", 12))
    q3b = tkinter.Button(frame3, text = "Submit", font = ("Times", 12), command = destruction(frame3))
    q3.pack(side = "top")
    q3e.pack(side = "left")
    q3b.pack(side = "left")

    q4 = tkinter.Label(frame4, text = "Who is Batman's son?", font = ("Times", 12, "bold"))
    q4e = tkinter.Entry(frame4, text = ans4, font = ("Times", 12))
    q4b = tkinter.Button(frame4, text = "Submit", font = ("Times", 12), command = destruction(frame4))
    q4.pack(side = "top")
    q4e.pack(side = "left")
    q4b.pack(side = "left")

    q5 = tkinter.Label(frame5, text = "Who played Batman in the 1960's Batman TV show?", font = ("Times", 12, "bold"))
    q5e = tkinter.Entry(frame5, text = ans5, font = ("Times", 12))
    q5b = tkinter.Button(frame5, text = "Submit", font = ("Times", 12), command = destruction(frame5))
    q5.pack(side = "top")
    q5e.pack(side = "left")
    q5b.pack(side = "left")

    q6 = tkinter.Label(frame6, text = "Who is Batman's trusted butler?", font = ("Times", 12, "bold"))
    q6e = tkinter.Entry(frame6, text = ans6, font = ("Times", 12))
    q6b = tkinter.Button(frame6, text = "Submit", font = ("Times", 12), command = frame6.destroy())
    q6.pack(side = "top")
    q6e.pack(side = "left")
    q6b.pack(side = "left")

    # This calculates the score by comparing all of the answers to the correct answers
    if ans1.get().lower().strip() == "bruce wayne":
        score = score.get() + 1
    if ans2.get().lower().strip() == "robin":
        score = score.get() + 1
    if ans3.get().lower().strip() == "joker" or ans3.get().lower().strip() == "the joker":
        score = score.get() + 1
    if ans4.get().lower().strip() == "damian" or ans4.get().lower().strip() == "damian wayne":
        score = score.get() + 1
    if ans5.get().lower().strip() == "adam west":
        score = score.get() + 1
    if ans6.get().lower().strip() == "alfred":
        score = score.get() + 1

    # This creates the screen that shows the score
    score = score.get() / 6 * 100
    
    score_screen = tkinter.Frame(root)
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

# This is the function that runs the Green Lantern Quiz
def lantern():
    # This clears the screen from the menu to bring up the quiz
    root.destroy()

    root2.title("Green Lantern Quiz")
    root2.mainloop()

    # This creates all of the local variables for the quiz answers
    ans1 = tkinter.StringVar()
    ans2 = tkinter.StringVar() 
    ans3 = tkinter.StringVar() 
    ans4 = tkinter.StringVar() 
    ans5 = tkinter.StringVar() 
    ans6 = tkinter.StringVar() 

    # This creates the questions and entry boxes for the quiz questions
    frame1.pack()
    q1 = tkinter.Label(frame1, text = "What is Green Lanterns's secret identity?", font = ("Times", 12, "bold"))
    q1e = tkinter.Entry(frame1, text = ans1, font = ("Times", 12))
    q1b = tkinter.Button(frame1, text = "Submit", font = ("Times", 12), command = destruction(frame1))
    q1.pack(side = "top")
    q1e.pack(side = "left")
    q1b.pack(side = "left")

    q2 = tkinter.Label(frame2, text = "Who are the leaders of the Green Lantern Corps", font = ("Times", 12, "bold"))
    q2e = tkinter.Entry(frame2, text = ans2, font = ("Times", 12))
    q2b = tkinter.Button(frame2, text = "Submit", font = ("Times", 12), command = destruction(frame2))
    q2.pack(side = "top")
    q2e.pack(side = "left")
    q2b.pack(side = "left")

    q3 = tkinter.Label(frame3, text = "Who is Green Lantern's biggest villain?", font = ("Times", 12, "bold"))
    q3e = tkinter.Entry(frame3, text = ans3, font = ("Times", 12))
    q3b = tkinter.Button(frame3, text = "Submit", font = ("Times", 12), command = destruction(frame3))
    q3.pack(side = "top")
    q3e.pack(side = "left")
    q3b.pack(side = "left")

    q4 = tkinter.Label(frame4, text = "Who is Hal Jordan's girlfriend?", font = ("Times", 12, "bold"))
    q4e = tkinter.Entry(frame4, text = ans4, font = ("Times", 12))
    q4b = tkinter.Button(frame4, text = "Submit", font = ("Times", 12), command = destruction(frame4))
    q4.pack(side = "top")
    q4e.pack(side = "left")
    q4b.pack(side = "left")

    q5 = tkinter.Label(frame5, text = "Who played Green Lantern in the 2011 movie?", font = ("Times", 12, "bold"))
    q5e = tkinter.Entry(frame5, text = ans5, font = ("Times", 12))
    q5b = tkinter.Button(frame5, text = "Submit", font = ("Times", 12), command = destruction(frame5))
    q5.pack(side = "top")
    q5e.pack(side = "left")
    q5b.pack(side = "left")

    q6 = tkinter.Label(frame6, text = "What is the emotion that the Red Lantern Corps is based on?", font = ("Times", 12, "bold"))
    q6e = tkinter.Entry(frame6, text = ans6, font = ("Times", 12))
    q6b = tkinter.Button(frame6, text = "Submit", font = ("Times", 12), command = frame6.destroy())
    q6.pack(side = "top")
    q6e.pack(side = "left")
    q6b.pack(side = "left")

    # This calculates the score by comparing all of the answers to the correct answers
    if ans1.get().lower().strip() == "hal jordan":
        score = score.get() + 1
    if ans2.get().lower().strip() == "guardians" or ans2.get().lower().strip() == "the guardians":
        score = score.get() + 1
    if ans3.get().lower().strip() == "sinestro":
        score = score.get() + 1
    if ans4.get().lower().strip() == "carol" or ans4.get().lower().strip() == "carol ferris":
        score = score.get() + 1
    if ans5.get().lower().strip() == "ryan reynolds":
        score = score.get() + 1
    if ans6.get().lower().strip() == "rage" or ans6.get().lower().strip() == "anger":
        score = score.get() + 1

    # This creates the screen that shows the score
    score = score.get() / 6 * 100
    
    score_screen = tkinter.Frame(root)
    score_screen.pack()

    s_screen = tkinter.Label(score_screen, text = "Thanks for playing! Your score is: ", font = ("Times", 12, "bold"))
    s_screen.pack()

    percent = tkinter.Label(score_screen, textvariable = score.get(), font = ("Times", 12))
    percent.pack()

    if score.get() == 0:
        message = tkinter.Label(score_screen, text = "You don't know anything about Green Lantern! What's wrong with you??", font = ("Times", 12, "bold"))
        message.pack()
    elif score.get() > 85:
        message = tkinter.Label(score_screen, text = "Wow! You really know your Green Lantern facts!", font = ("Times", 12, "bold"))
        message.pack()
    else:
        message = tkinter.Label(score_screen, text = "You need to study your Green Lantern facts!", font = ("Times", 12, "bold"))
        message.pack()

# This is the function that runs the Superman Quiz
def superman():
    # This clears the screen from the menu to bring up the quiz
    root.destroy()

    root2.title("Superman Quiz")
    root2.mainloop()

    # This creates all of the local variables for the quiz answers
    ans1 = tkinter.StringVar()
    ans2 = tkinter.StringVar() 
    ans3 = tkinter.StringVar() 
    ans4 = tkinter.StringVar() 
    ans5 = tkinter.StringVar() 
    ans6 = tkinter.StringVar() 

    # This creates the questions and entry boxes for the quiz questions
    frame1.pack()
    q1 = tkinter.Label(frame1, text = "What is Superman's secret identity?", font = ("Times", 12, "bold"))
    q1e = tkinter.Entry(frame1, text = ans1, font = ("Times", 12))
    q1b = tkinter.Button(frame1, text = "Submit", font = ("Times", 12), command = destruction(frame1))
    q1.pack(side = "top")
    q1e.pack(side = "left")
    q1b.pack(side = "left")

    q2 = tkinter.Label(frame2, text = "What is the name of Superman's crime fighting dog?", font = ("Times", 12, "bold"))
    q2e = tkinter.Entry(frame2, text = ans2, font = ("Times", 12))
    q2b = tkinter.Button(frame2, text = "Submit", font = ("Times", 12), command = destruction(frame2))
    q2.pack(side = "top")
    q2e.pack(side = "left")
    q2b.pack(side = "left")

    q3 = tkinter.Label(frame3, text = "Who is Superman's girlfriend?", font = ("Times", 12, "bold"))
    q3e = tkinter.Entry(frame3, text = ans3, font = ("Times", 12))
    q3b = tkinter.Button(frame3, text = "Submit", font = ("Times", 12), command = destruction(frame3))
    q3.pack(side = "top")
    q3e.pack(side = "left")
    q3b.pack(side = "left")

    q4 = tkinter.Label(frame4, text = "What newspaper company does Superman work for?", font = ("Times", 12, "bold"))
    q4e = tkinter.Entry(frame4, text = ans4, font = ("Times", 12))
    q4b = tkinter.Button(frame4, text = "Submit", font = ("Times", 12), command = destruction(frame4))
    q4.pack(side = "top")
    q4e.pack(side = "left")
    q4b.pack(side = "left")

    q5 = tkinter.Label(frame5, text = "Who is the current actor who plays Superman?", font = ("Times", 12, "bold"))
    q5e = tkinter.Entry(frame5, text = ans5, font = ("Times", 12))
    q5b = tkinter.Button(frame5, text = "Submit", font = ("Times", 12), command = destruction(frame5))
    q5.pack(side = "top")
    q5e.pack(side = "left")
    q5b.pack(side = "left")

    q6 = tkinter.Label(frame6, text = "What planet is Superman from?", font = ("Times", 12, "bold"))
    q6e = tkinter.Entry(frame6, text = ans6, font = ("Times", 12))
    q6b = tkinter.Button(frame6, text = "Submit", font = ("Times", 12), command = frame6.destroy())
    q6.pack(side = "top")
    q6e.pack(side = "left")
    q6b.pack(side = "left")

    # This calculates the score by comparing all of the answers to the correct answers
    if ans1.get().lower().strip() == "clark kent":
        score = score.get() + 1
    if ans2.get().lower().strip() == "krypto" or ans2.get().lower().strip() == "krypto the superdog":
        score = score.get() + 1
    if ans3.get().lower().strip() == "lois lane" or ans3.get().lower().strip() == "lois":
        score = score.get() + 1
    if ans4.get().lower().strip() == "daily planet":
        score = score.get() + 1
    if ans5.get().lower().strip() == "henry cavill":
        score = score.get() + 1
    if ans6.get().lower().strip() == "krypton":
        score = score.get() + 1

    # This creates the screen that shows the score
    score = score.get() / 6 * 100
    
    score_screen = tkinter.Frame(root)
    score_screen.pack()

    s_screen = tkinter.Label(score_screen, text = "Thanks for playing! Your score is: ", font = ("Times", 12, "bold"))
    s_screen.pack()

    percent = tkinter.Label(score_screen, textvariable = score.get(), font = ("Times", 12))
    percent.pack()

    if score.get() == 0:
        message = tkinter.Label(score_screen, text = "You don't know anything about Superman! What's wrong with you??", font = ("Times", 12, "bold"))
        message.pack()
    elif score.get() > 85:
        message = tkinter.Label(score_screen, text = "Wow! You really know your Superman facts!", font = ("Times", 12, "bold"))
        message.pack()
    else:
        message = tkinter.Label(score_screen, text = "You need to study your Superman facts!", font = ("Times", 12, "bold"))
        message.pack()

# This creates the root window of the GUI and gives it a name
root = tkinter.Tk()
root.title("Trivia Quiz")

root2 = tkinter.Tk()

# This creates the variable that is used to keep track of the score
score = tkinter.IntVar()

# This creates the frame that the menu exists in
frame = tkinter.Frame(root)
frame.pack()

# This creates the frames for this quiz
frame1 = tkinter.Frame(root2)
frame2 = tkinter.Frame(root2)
frame3 = tkinter.Frame(root2)
frame4 = tkinter.Frame(root2)
frame5 = tkinter.Frame(root2)
frame6 = tkinter.Frame(root2)

# This creates the menu for the trivia game
menu = tkinter.Label(frame, text = "Welcome to the Superhero Trivia game! Choose one of the quizzes below.", font = ("Times", 12, "bold"))
menu.grid(column = 1, row = 0)

# This helps space the buttons from the menu
space = tkinter.Label(frame, text = "")
space.grid(row = 1)

# This creates all of the buttons to select the quizzes with their function calls
batman = tkinter.Button(frame, text = "Batman Quiz", font = ("Times", 12), command = batman)
lantern = tkinter.Button(frame, text = "Green Lantern Quiz", font = ("Times", 12), command = lantern)
superman = tkinter.Button(frame, text = "Superman Quiz", font = ("Times", 12), command = superman)
batman.grid(column = 0, row = 2)
lantern.grid(column = 1, row = 2)
superman.grid(column = 2, row = 2)

# This loads the root window and makes it run
root.mainloop()