from tkinter import *
window = Tk()#make tkinter window object
window.title('New Window')#set window title
window.geometry('800x800')#set window size

label1 = Label(window,text='Hi! This is TK!', bg='green',font=('KG Feeling 22',16),width=25,height=8)#add text label
label1.pack()#display label


showStr = StringVar()#vars and funcs for button
on_click = False
def click_me():
    global on_click
    if on_click == False:
        on_click = True
        showStr.set('You clicked me?')
    else:
        on_click = False
        showStr.set('')

label2 = Label(window,textvariable=showStr, bg='cyan',font=('KG Feeling 22',16),width=25, height=4)#label for button
label2.pack()
button1 = Button(window,text='Click me!', bg='red',font=('KG Feeling 22',16),width=25, height=4,command=click_me)#button
button1.pack()


#Entry--single line
#Text--multiple lines
entry1 = Entry(window)
entry1.pack()
textInput1=Text(window,height=5)
textInput1.pack()

#single select

var1 = StringVar()
var1.set(0)
def show_selection():
    showLabel.config(text='You chose '+var1.get())
showLabel = Label(window, bg='yellow',width=20,text='Make a selection:')
showLabel.pack()
r_Button_A = Radiobutton(window, text='Option A',variable=var1,value='A',command=show_selection)
r_Button_A.pack()
r_Button_B = Radiobutton(window, text='Option B',variable=var1,value='B',command=show_selection)
r_Button_B.pack()
r_Button_C = Radiobutton(window, text='Option C',variable=var1,value='C',command=show_selection)
r_Button_C.pack()

window.mainloop()#start loop