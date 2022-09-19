from textwrap import fill
from tkinter import *
from tkinter import filedialog
    
def save_file() :
    
    save_files = filedialog.asksaveasfile(mode='w',defaultextension ='.txt')
    txt = text_area.get(1.0 ,END)
    save_files.write(txt)
    save_files.close()    

def open_file() :
     
    open_files = filedialog.askopenfile(mode="r")
    txt = open_files.read()
    text_area.insert(INSERT, txt)
    open_files.close()
    
def clear_file():
    
    text_area.delete(1.0 , END)

window = Tk()
window.title("notepad")
window.geometry('800x500')
window.resizable(0,0)

text_area = Text(window)
text_area.pack(fill='both', expand=True)

menubar = Menu(window)
filemenu =Menu(menubar, tearoff=0)
filemenu.add_command(label='save',command=save_file)
filemenu.add_command(label='open',command=open_file)
filemenu.add_command(label='exit',command=window.quit)
menubar.add_cascade(menu=filemenu,label='file')
editmenu = Menu(menubar , tearoff=0)
editmenu.add_command(label='clear',command=clear_file)
menubar.add_cascade(menu=editmenu ,label='edit')

window.config(menu=menubar)

window.mainloop()