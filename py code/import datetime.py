import datetime


dt = datetime.datetime.now()

date = datetime.datetime(2022,11,12,18,35)
delta = datetime.timedelta(20)

x = dt.strftime('%a')
print(x)

