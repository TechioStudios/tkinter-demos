from binascii import b2a_base64
from tkinter import *
window = Tk()#make tkinter window object
window.title('New Window')#set window title
window.geometry('800x600')#set window size

entry1 = Entry(window)
entry1.pack()

textShow = Text(window,height=2)
textShow.pack()

def insert_point():
    var = entry1.get()
    textShow.insert('insert',var)
def insert_end():
    var = entry1.get()
    textShow.insert('end',var)

b1 = Button(window,text="Insert at cursor",width=15,height=2,command=insert_point)
b1.pack()
b2 = Button(window,text="Insert at end",width=15,height=2,command=insert_end)
b2.pack()

window.mainloop()#start loop