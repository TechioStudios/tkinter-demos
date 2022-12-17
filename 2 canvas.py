from tkinter import *
object1 = Tk()
canvas = Canvas(object1, width=800, height=500)#set canvas size
canvas.pack()
canvas.create_line(0,0,800,500)#draw a line
canvas.create_rectangle(30,30,150,150)#draw a rectangle
object1.mainloop()