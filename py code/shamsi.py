from khayyam import JalaliDatetime,JalaliDate

dt = JalaliDate.today()
dorta = JalaliDatetime.now().strftime('%A')
print(dorta)