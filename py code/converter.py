
from cProfile import label
from distutils.cmd import Command
from multiprocessing.sharedctypes import Value
from tkinter import*
from convert_class import *


def send_data():
    data_from = List_from.get(ACTIVE)
    data_to = List_to.get(ACTIVE)
    Value = int(EN_from.get())
    obj = converter(data_from,data_to,Value)
    EN_to.delete(0,END)
    EN_to.insert(END,obj.convert())
    

window = Tk()
window.title('converter')
#window.geometry('260x270')
window.resizable(0,0)


my_font =('Arial_rounded',11)

Label(window,text='From',font=my_font).grid(row=0,column=0,sticky=W,padx=5)
EN_from = Entry(window,font=my_font)
EN_from.grid(row=1,column=0,sticky=W,pady=2,padx=5)
List_from = Listbox(window,font=my_font,exportselection=False)
List_from.grid(row=2,column=0,sticky=W,pady=5,padx=5)
List_from.insert(END,'gr')
List_from.insert(END,'kg')
List_from.insert(END,'ton')

Label(window,text='to',font=my_font).grid(row=0,column=1,sticky=W,padx=5)
EN_to = Entry(window,font=my_font)
EN_to.grid(row=1,column=1,sticky=E,pady=2,padx=5)
List_to = Listbox(window,font=my_font,exportselection=False)
List_to.grid(row=2,column=1,sticky=E,pady=5,padx=5)
List_to.insert(END,'gr')
List_to.insert(END,'kg')
List_to.insert(END,'ton')


btn = Button(window,text='convert',font=my_font,command=send_data)
btn.grid(row=3,column=0,padx=5,pady=5,columnspan=2,sticky=W+E)


window.mainloop()