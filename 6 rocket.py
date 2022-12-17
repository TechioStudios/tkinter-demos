from tkinter import *
import time as t
tk = Tk()
canvas = Canvas(tk, width = 800, height=800)
canvas.pack()

canvas.create_polygon(350,350,400,350,375,300)#draw nose
canvas.create_polygon(300,600,350,600,350,500)#draw fin
canvas.create_polygon(450,600,400,600,400,500)#draw another fin
canvas.create_rectangle(350,350,400,600, fill='white')#rocket body
canvas.create_text(375, 400, text='N', fill='blue', font=('Times', 30))#text
canvas.create_text(375, 450, text='A', fill='blue', font=('Times',30))#more text
canvas.create_text(375, 500, text='S', fill='blue', font=('Times', 30))#even more text
canvas.create_text(375, 550, text='A', fill='blue', font=('Times', 30))#even even more text
canvas.create_polygon(350, 600, 370, 600, 360, 620, fill='red')#draw flame
canvas.create_polygon(380, 600, 400, 600, 390, 620, fill='red')#draw another flame

while True:
    for i in range(1,11):
        canvas.move(i,0,-10)
    tk.update()
    t.sleep(0.01)

tk.mainloop()