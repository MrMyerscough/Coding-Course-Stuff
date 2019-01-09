import tkinter

# This function takes a percentage and turns it into a letter grade.
def grade_convert(grade: int):
    if grade >= 93:
        return ("A")
    elif grade >= 90:
        return ("A-")
    elif grade >= 87:
        return ("B+")
    elif grade >= 83:
        return ("B")
    elif grade >= 80:
        return ("B-")
    elif grade >= 77:
        return ("C+")
    elif grade >= 73:
        return ("C")
    elif grade >= 70:
        return ("C-")
    elif grade >= 67:
        return ("D+")
    elif grade >= 63:
        return ("D")
    elif grade >= 60:
        return ("D-")
    elif grade <= 59 and grade >= 0:
        return ("E")
    else:
        return ("That's not a valid grade!")

# This function runs the grade_convert function and then sets the value of letter into the StringVar letter_grade and returns it
def letter_set():
    letter.set(grade_convert(grade.get()))

# This creates the root window
root = tkinter.Tk()
root.title("Grade Calculator")

# This sets the type of our grade variable to type IntVar
grade = tkinter.IntVar(root)
letter = tkinter.StringVar(root)

# This creates the prompt to enter the percentage and packs it into the root window
label = tkinter.Label(root, text = "Enter your percentage and hit calculate to find out your letter grade.", font=("Papyrus", 12, "bold italic"))
label.pack()

# This creates the entry box for the percentage and packs it into the root window
box = tkinter.Entry(root, text = grade, font=("Comic Sans MS", 12))
box.pack()

# This creates the button to push to calculate the grade as a letter
button = tkinter.Button(root, text = "Calculate!", font=("Papyrus", 12), command = letter_set)
button.pack()

# This creates the label that displays the letter grade once it is calculated
label2 = tkinter.Label(root, textvariable = letter, font=("Papyrus", 12, "bold italic"))
label2.pack()

# This makes the root window appear
root.mainloop()