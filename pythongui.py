from tkinter import *

def clearChat():
    h=open("chatfile2.txt",'w')
    h.write('')


root=Tk()
root.geometry('100x100')
btn=Button(root, text='Clear',bd='5',command=clearChat)
btn.pack(side='top')
root.mainloop()
