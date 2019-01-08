# Add tkinter to file
import tkinter

# Creating a graphics window and making it appear
root = tkinter.Tk()
root.title("Graphics Window")
#root.mainloop()

# Changing the size of the graphics window
root.geometry("500x500")
#root.mainloop()

# Adding widgets to the main window
label = tkinter.Label(root, text = "This is a label")
label.pack()

button = tkinter.Button(root, text = "This is a button")
button.pack()

#root.mainloop()

# Frames in tkinter
root2 = tkinter.Tk()
root2.title("Graphics Window")
root2.geometry("500x500")

frame1 = tkinter.Frame(root2)
frame2 = tkinter.Frame(root2)

label = tkinter.Label(frame1, text = "This is a label in frame 1")
label.pack()

button = tkinter.Button(frame2, text = "This is a button in frame 2")
button.pack()

frame1.pack()
frame2.pack()

root2.mainloop()