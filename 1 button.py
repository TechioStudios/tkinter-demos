from tkinter import *
def printStr():
    print("Hello world!")
windows1 = Tk()
button1 = Button(windows1, text='Click me!', command=printStr)
button1.pack()#display button
windows1.mainloop()#loop