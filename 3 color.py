from tkinter import *
from tkinter import colorchooser
def colorChoose():
    colorTuple = colorchooser.askcolor()
    print("Selected RGB color is ",colorTuple[0])
    print("Selected color hexadecimal is ",colorTuple[1])

window1 = Tk()
button1 = Button(window1,text="Pick a color", command=colorChoose)
button1.pack()
window1.mainloop()