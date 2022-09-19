
from ast import Pass
from tkinter import *


def show():
    #print('joon! che khub click mikoni!')
    #Label(Window1,text='sum is :').pack()
    #M = (int(First_number.get())+int(second_number.get()))
    #Label(Window1,text = M).pack()
    #print(choice.get())
    
    #LB.config(text="j.o.j.e you have clicked"+ str(counter)  +'times!')
    #print(Scl.get())
    with open('out','w') as f:
        f.write(Text.get(1.0,END))

def load_error():
    print('already loaded!')
    Btn2.config(command=load)
def load():
    with open('out') as f:
        x = f.read()
        if len(Text.get(1.0,END))== 1 :
            Text.insert(INSERT,x)
              
        
            
        
        
        
    

Window1 = Tk()

Window1.title('mamad melody')
Window1.geometry('500x600')
Window1.minsize(300,400)
Window1.maxsize(700,800)
#Modes = [('male','M'),('female','F')]
#choice = StringVar()
#choice.set('M')

#for a,b in Modes:
#    Radiobutton(Window1,text=a ,value=b,variable=choice).pack()
#Label(Window1,text='first number').pack()
#First_number = Entry(Window1)
#First_number.pack()
#Label(Window1,text = "second number").pack()
#second_number = Entry(Window1)
#second_number.pack()
#window.resizable
#vase botton sabet!
#LB = Label(window,text='hello j.o.j.e!')
#LB.pack()
#LB.config(font=('Tahoma',25),fg='pink',bg='black')
#Checkbutton(Window1,text='male').pack()
#Scl = Scale(Window1,from_=0,to=100)
#Scl.pack()
Text = Text(Window1)
Text.pack()
Btn = Button(Window1,text='click')
Btn.pack()
Btn.config(bg='blue',command=show)
Btn2 = Button(Window1,text="load")
Btn2.pack()
Btn2.config(bg='blue',command=load)

Window1.mainloop()

