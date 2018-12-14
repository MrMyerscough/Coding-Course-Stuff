import tkinter

def click():
    counter.set(counter.get() + 1)

window = tkinter.Tk()
window.title("The Magic Button!")

counter = tkinter.IntVar()
counter.set(0)

label = tkinter.Label(window, text = "You have pressed the button this many times:", font = ("Comic Sans MS", 12, "bold italic"))
label.pack()

label2 = tkinter.Label(window, textvariable = counter)
label2.pack()

button = tkinter.Button(window, text = "Press me!", command = click, font = ("Comic Sans MS", 8, "bold"))
button.pack()

window.mainloop()