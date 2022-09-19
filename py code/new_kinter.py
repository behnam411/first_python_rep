
from tkinter import *
import requests

global_text = requests.get('https://api.coinlore.net/api/tickers/')
x = global_text.json()

symbol = dict()

for i in x['data'] :
    symbol[i['symbol']] = i['price_usd']

all_symbol = list(symbol.keys())


usdt = requests.get('http://api.navasan.tech/latest/?api_key=freeH1njcMsLTHCJFd9haMcGI1ZdNK3g&item=usdt')
usdt = usdt.json()
usdt = usdt['usdt']['value']

def price(e):
    data_from = list_from.get(ACTIVE)
    price_entry.delete(0,END)
    price_entry.insert(END,symbol[data_from])
    
def price_rial(e):
    data_from = list_from.get(ACTIVE)
    price_entry.delete(0, END)
    price_entry.insert(END, float(symbol[data_from]) * float(usdt))

def update(data):
    list_from.delete(0,END)
    for i in data:
        list_from.insert(END,i)

def symbolout(e):
    searching.delete(0,END)
    searching.insert(0,list_from.get(ACTIVE))
    
def check_symbol(e):
    typed = searching.get()
    if typed == '' :
        data = all_symbol
    else:
        data = []
        for i in all_symbol:
            if typed.upper() in i :
                data.append(i)
                
    update(data)

window = Tk()

window.title('exchange')
window.geometry('500x400')
my_font = ('Arial_rounded',11)

Label(window,text='search', font=my_font).pack(fill='both',expand=True)

searching = Entry(window , font=my_font)
searching.pack(fill='both',expand=True)
searching.bind('<KeyRelease>',check_symbol)

list_from = Listbox(window, font=my_font, exportselection=False)
list_from.pack(fill='both' , expand=True)
update(all_symbol)
list_from.bind('<<ListboxSelect>>', symbolout)

Label(window, text='price', font=my_font).pack(fill='both',expand=True)

price_entry = Entry(window, font=my_font)
price_entry.pack(fill='both',expand=True)

btn = Button(window, text='get the price', font=my_font)
btn.pack(fill='both' , expand=True)

btn.bind('<ButtonPress-1>',price)
btn.bind('<ButtonPress-3>',price_rial)

window.mainloop()