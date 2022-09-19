

import requests, time, schedule,datetime
import mysql.connector
from matplotlib import pyplot as plt
from matplotlib import dates as plt_dates

mydb = mysql.connector.connect(host='127.0.0.1', port='3306', user='root',  database= 'adak' , password='1234' )

mycs = mydb.cursor()

def get_price():
    global_test = requests.get('https://api.coinlore.net/api/tickers/')
    x = global_test.json()
    price_list = dict()
    for i in x['data'][0:6]:
        price_list[i['symbol']] = i['price_usd']
    return price_list

def save_price():
    price_list = get_price()
    time_req = time.time()
    for item in price_list:
        sql = 'INSERT INTO price (coin_name,cion_price,time_price) VALUES(%s,%s,%s)'
        value_insert = (item,price_list[item],time_req)
        mycs.execute(sql,value_insert)
    mydb.commit()
    print('OK')

x = schedule.every(10).seconds.do(save_price)

#while True:
    #schedule.run_pending()
    #time.sleep(1)
   
COIN_NAME = "ETH"
sql = f"select * from price where coin_name = '{COIN_NAME}' "
mycs.execute(sql)
sql_res = mycs.fetchall()
#print (sql_res)

price = []
time_price = []

for i in sql_res:
    price.append(float(i[2]))
    mytime = datetime.datetime.fromtimestamp(int(float(i[3])))
    time_price.append(mytime)
    
plt.figure(figsize=(30,15))
plt.title(COIN_NAME,fontsize = 20)
plt.plot_date(time_price,price,ms = 10, mfc='yellow',linestyle= 'solid')
plt.gcf().autofmt_xdate
date_format= plt_dates.DateFormatter('%d %b %H :%M')
plt.gca().xaxis.set_major_formatter(date_format)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel('price' , fontsize=10, labelpad=10)
plt.xlabel('time' ,  fontsize=10, labelpad=10)
plt.grid(axis='both')
plt.show()

#print(price,time_price)
    