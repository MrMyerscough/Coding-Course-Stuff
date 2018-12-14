import tkinter

class Window:
    def __init__(self):
        self.root = tkinter.Tk()

    def closeWindow(self):
        self.root.destroy()

    def openWindow(self):
        self.root.mainloop()

    def addLabel(self, text = None, font = None):
        tkinter.Label(mater = self.root, text = text, font = font)
    
window = Window()
# windowTwo = Window()



window.openWindow()
# windowTwo.openWindow()


window.addLabel(text = "hi there")
