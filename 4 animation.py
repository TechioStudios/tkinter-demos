import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=800, height=600)
canvas.pack()
canvas.create_polygon(510,10,510,120,600,60)#draw triangle
for x in range(0,670):
    canvas.move(1,-1,1)#move triangle  atributtes: (target id(see "5 id.py"),moveX(-1/0/1) by one px,moveY(-1/0/1) by one px)
    tk.update()
    time.sleep(0.01)