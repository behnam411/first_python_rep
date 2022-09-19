import requests, time, schedule ,datetime 
import mysql.connector

def get_price():
    global_test = requests.get('https://api.coinlore.net/api/tickers/')
    x = global_test.json()
    price_list = dict()
    for i in x['data'][0:6]:
        price_list[i['symbol']] = i['price_usd']
    return price_list

print(get_price)