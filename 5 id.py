import time as t
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=800, height=600)
canvas.pack()
print(canvas.create_polygon(510,10,510,120,600,60))#print ID of polygon
print(canvas.create_polygon(10,10,10,120,100,60))#print ID of polygon
while True:
    canvas.move(1,-1,1)
    canvas.move(2,1,1)
    tk.update()
    t.sleep(0.001)